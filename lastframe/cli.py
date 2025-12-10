#!/usr/bin/env python3
"""
lastframe - Extract the last non-blurry frame from videos
"""
import sys
import os
import glob
from pathlib import Path
import cv2
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.text import Text
from rich.table import Table

console = Console()

VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv', '.wmv', '.m4v', '.mpg', '.mpeg', '.3gp'}

def calculate_blur_score(frame):
    """
    Calculate blur score using Laplacian variance.
    Higher score = sharper image. Lower score = more blurry.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def get_video_info(video_path):
    """Get basic video information."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        return None

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cap.release()

    return {
        'total_frames': total_frames,
        'fps': fps,
        'width': width,
        'height': height
    }

def extract_last_frame(video_path, blur_threshold=100):
    """
    Extract the last non-blurry frame from a video.

    Args:
        video_path: Path to the video file
        blur_threshold: Minimum blur score to consider a frame sharp

    Returns:
        tuple: (frame, frame_number, blur_score, status_message)
    """
    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        return None, None, None, "Failed to open video file"

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Check last 3 frames
    candidates = []
    frames_to_check = min(3, total_frames)

    for i in range(frames_to_check):
        frame_num = total_frames - 1 - i
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()

        if ret:
            blur_score = calculate_blur_score(frame)
            candidates.append((frame, frame_num, blur_score))

    cap.release()

    if not candidates:
        return None, None, None, "No frames could be extracted"

    # Sort by blur score (highest first)
    candidates.sort(key=lambda x: x[2], reverse=True)

    # Get the sharpest frame
    best_frame, best_frame_num, best_blur_score = candidates[0]

    # Determine which frame we used
    frame_position = total_frames - 1 - best_frame_num

    if frame_position == 0:
        status = f"last frame (sharp ✨ score: {best_blur_score:.1f})"
    elif best_blur_score < blur_threshold:
        # All frames are blurry, use last by default
        best_frame, best_frame_num, best_blur_score = candidates[-1]
        status = f"last frame (all frames blurry ⚠️  score: {best_blur_score:.1f})"
    elif frame_position == 1:
        status = f"2nd last frame (last was blurry 🔍 score: {best_blur_score:.1f})"
    elif frame_position == 2:
        status = f"3rd last frame (last 2 were blurry 🔍 score: {best_blur_score:.1f})"
    else:
        status = f"frame #{best_frame_num + 1} (score: {best_blur_score:.1f})"

    return best_frame, best_frame_num, best_blur_score, status

def find_videos_in_directory(directory_path):
    """Find all video files in a directory."""
    video_files = []
    directory = Path(directory_path)

    if not directory.exists():
        return []

    for ext in VIDEO_EXTENSIONS:
        video_files.extend(directory.glob(f"*{ext}"))
        video_files.extend(directory.glob(f"*{ext.upper()}"))

    return sorted(video_files)

def process_single_video(video_path, output_path=None):
    """Process a single video file."""
    video_path = Path(video_path)

    # Get video info
    try:
        video_info = get_video_info(video_path)
    except Exception as e:
        return False, f"Failed to analyze: {str(e)}"

    if not video_info:
        return False, "Cannot open video file"

    if video_info['total_frames'] == 0:
        return False, "Empty video file"

    # Extract frame
    try:
        frame, frame_num, blur_score, status = extract_last_frame(video_path)
    except Exception as e:
        return False, f"Frame extraction failed: {str(e)}"

    if frame is None:
        return False, status

    # Determine output path
    if output_path:
        output_file = Path(output_path)
    else:
        output_filename = video_path.stem + "_lastframe.jpg"
        output_file = video_path.parent / output_filename

    # Save frame
    try:
        success = cv2.imwrite(
            str(output_file),
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 100]
        )
        if not success:
            return False, "Failed to save image"
    except Exception as e:
        return False, f"Save failed: {str(e)}"

    return True, {
        'output_file': output_file,
        'status': status,
        'video_info': video_info,
        'frame_num': frame_num
    }

def process_batch(input_dir, output_dir=None):
    """Process all videos in a directory."""
    input_path = Path(input_dir)

    if not input_path.exists():
        show_error(
            "Directory not found",
            f"The input directory doesn't exist: {input_dir}",
            "Check the path and try again."
        )
        sys.exit(1)

    if not input_path.is_dir():
        show_error(
            "Not a directory",
            f"The path is not a directory: {input_dir}",
            "For batch mode, provide a directory path."
        )
        sys.exit(1)

    # Find all videos
    video_files = find_videos_in_directory(input_path)

    if not video_files:
        show_error(
            "No videos found",
            f"No video files found in: {input_dir}",
            f"Supported formats: {', '.join(sorted(VIDEO_EXTENSIONS))}"
        )
        sys.exit(1)

    # Setup output directory
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = input_path

    # Show header
    console.print()
    console.print("[bold magenta]lastframe[/bold magenta] [dim]v1.1.0[/dim] [yellow]• batch mode[/yellow]")
    console.print()
    console.print(f"[cyan]📁 Input:[/cyan]  {input_path}")
    console.print(f"[cyan]📤 Output:[/cyan] {output_path}")
    console.print(f"[cyan]🎬 Videos:[/cyan] {len(video_files)} found")
    console.print()

    # Process videos
    results = {'success': 0, 'failed': 0, 'details': []}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Processing videos...", total=len(video_files))

        for video_file in video_files:
            progress.update(task, description=f"[cyan]Processing {video_file.name}...")

            # Determine output path
            if output_dir:
                output_file = output_path / f"{video_file.stem}_lastframe.jpg"
            else:
                output_file = None

            # Process video
            success, result = process_single_video(video_file, output_file)

            if success:
                results['success'] += 1
                results['details'].append({
                    'file': video_file.name,
                    'status': 'success',
                    'output': result['output_file'].name
                })
            else:
                results['failed'] += 1
                results['details'].append({
                    'file': video_file.name,
                    'status': 'failed',
                    'error': result
                })

            progress.advance(task)

    # Show results
    console.print()
    console.print("[bold green]✓[/bold green] Batch processing complete!")
    console.print()

    # Summary table
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Status", style="dim", width=12)
    table.add_column("Count", justify="right")

    table.add_row("[green]✓ Success[/green]", f"[bold]{results['success']}[/bold]")
    if results['failed'] > 0:
        table.add_row("[red]✗ Failed[/red]", f"[bold]{results['failed']}[/bold]")
    table.add_row("Total", f"{len(video_files)}")

    console.print(table)
    console.print()

    # Show failures if any
    if results['failed'] > 0:
        console.print("[yellow]Failed videos:[/yellow]")
        for detail in results['details']:
            if detail['status'] == 'failed':
                console.print(f"  [red]✗[/red] {detail['file']}: [dim]{detail['error']}[/dim]")
        console.print()

    return results['success'], results['failed']

def show_help():
    """Display help message."""
    help_text = Text()
    help_text.append("lastframe", style="bold magenta")
    help_text.append(" v1.1.0\n\n", style="dim")
    help_text.append("Extract the last non-blurry frame from videos\n\n", style="white")

    help_text.append("USAGE\n", style="bold cyan")
    help_text.append("  lastframe ", style="white")
    help_text.append("<input> ", style="yellow")
    help_text.append("[output]\n\n", style="green")

    help_text.append("MODES\n", style="bold cyan")
    help_text.append("  Single file mode:\n", style="white")
    help_text.append("    lastframe video.mp4              ", style="dim")
    help_text.append("→ video_lastframe.jpg\n", style="dim cyan")
    help_text.append("    lastframe video.mp4 output.jpg   ", style="dim")
    help_text.append("→ output.jpg\n\n", style="dim cyan")

    help_text.append("  Batch mode (directory):\n", style="white")
    help_text.append("    lastframe ./videos               ", style="dim")
    help_text.append("→ ./videos/*_lastframe.jpg\n", style="dim cyan")
    help_text.append("    lastframe ./videos ./output      ", style="dim")
    help_text.append("→ ./output/*_lastframe.jpg\n\n", style="dim cyan")

    help_text.append("FEATURES\n", style="bold cyan")
    help_text.append("  • Smart blur detection - automatically picks the sharpest frame\n", style="white")
    help_text.append("  • Batch processing - process entire folders\n", style="white")
    help_text.append("  • Custom output - specify output file or directory\n", style="white")
    help_text.append("  • Saves as JPEG with maximum quality (100%)\n", style="white")
    help_text.append("  • Supports all major video formats (MP4, MOV, AVI, MKV, WebM, etc.)\n\n", style="white")

    help_text.append("OPTIONS\n", style="bold cyan")
    help_text.append("  -h, --help     Show this help message\n", style="white")

    console.print(Panel(help_text, border_style="magenta", padding=(1, 2)))

def show_error(title, message, suggestion=None):
    """Display a formatted error message with optional suggestion."""
    error_text = Text()
    error_text.append(f"{title}\n\n", style="bold red")
    error_text.append(f"{message}\n", style="white")

    if suggestion:
        error_text.append("\n")
        error_text.append("💡 Suggestion\n", style="bold yellow")
        error_text.append(f"{suggestion}", style="dim")

    console.print()
    console.print(Panel(error_text, border_style="red", padding=(1, 2)))
    console.print()

def main():
    """Main CLI entry point."""

    # Parse arguments
    if len(sys.argv) == 1:
        show_error(
            "No input specified",
            "You need to provide a video file or directory.",
            "Try: lastframe movie.mp4\nOr: lastframe ./videos\nOr use: lastframe --help"
        )
        sys.exit(1)

    if len(sys.argv) > 3:
        show_error(
            "Too many arguments",
            "lastframe accepts at most 2 arguments: <input> [output]",
            "Try: lastframe movie.mp4 output.jpg"
        )
        sys.exit(1)

    # Check for help flag
    if sys.argv[1] in ['-h', '--help', 'help']:
        show_help()
        sys.exit(0)

    input_arg = sys.argv[1]
    output_arg = sys.argv[2] if len(sys.argv) == 3 else None

    input_path = Path(input_arg)

    # Validate input exists
    if not input_path.exists():
        show_error(
            "Input not found",
            f"The specified path doesn't exist: {input_arg}",
            "Check the file/directory path and try again.\nMake sure you're in the right directory or use the full path."
        )
        sys.exit(1)

    # Determine mode: batch (directory) or single file
    if input_path.is_dir():
        # Batch mode
        if output_arg and Path(output_arg).exists() and Path(output_arg).is_file():
            show_error(
                "Invalid output for batch mode",
                f"In batch mode, output must be a directory, not a file: {output_arg}",
                "Provide a directory path for batch output, or omit to use the same directory."
            )
            sys.exit(1)

        process_batch(input_path, output_arg)

    elif input_path.is_file():
        # Single file mode
        if output_arg and Path(output_arg).is_dir():
            show_error(
                "Invalid output for single file",
                f"Output must be a filename, not a directory: {output_arg}",
                "Provide a filename like: output.jpg"
            )
            sys.exit(1)

        # Check file extension
        if input_path.suffix.lower() not in VIDEO_EXTENSIONS:
            console.print()
            console.print(f"[yellow]⚠️  Warning:[/yellow] '{input_path.suffix}' might not be a video file.")
            console.print(f"[dim]Supported formats: {', '.join(sorted(VIDEO_EXTENSIONS))}[/dim]")
            console.print("[dim]Will try to process anyway...[/dim]")
            console.print()

        # Show header
        console.print()
        console.print("[bold magenta]lastframe[/bold magenta] [dim]v1.1.0[/dim]")
        console.print()

        # Process with progress
        with Progress(
            SpinnerColumn(spinner_name="dots"),
            TextColumn("[cyan]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("analyzing video...", total=None)

            try:
                video_info = get_video_info(input_path)
            except Exception as e:
                console.print()
                show_error(
                    "Failed to analyze video",
                    f"An error occurred while reading the video file: {str(e)}",
                    "The file might be corrupted or in an unsupported format.\nTry converting it to MP4 using: ffmpeg -i input.mov output.mp4"
                )
                sys.exit(1)

            if not video_info:
                console.print()
                show_error(
                    "Cannot open video file",
                    "The file exists but couldn't be opened as a video.",
                    "Possible reasons:\n• File is corrupted\n• Unsupported codec\n• File is not actually a video\n\nTry opening the file in a video player to verify it works."
                )
                sys.exit(1)

            if video_info['total_frames'] == 0:
                console.print()
                show_error(
                    "Empty video",
                    "The video file contains no frames.",
                    "The file might be corrupted or incomplete."
                )
                sys.exit(1)

            progress.update(task, description="extracting frame...")

            try:
                frame, frame_num, blur_score, status = extract_last_frame(input_path)
            except Exception as e:
                console.print()
                show_error(
                    "Frame extraction failed",
                    f"An error occurred while extracting frames: {str(e)}",
                    "The video file might have issues. Try re-encoding it with ffmpeg."
                )
                sys.exit(1)

        if frame is None:
            console.print()
            show_error(
                "No frames extracted",
                status,
                "The video might be too short or corrupted."
            )
            sys.exit(1)

        # Determine output path
        if output_arg:
            output_path = Path(output_arg)
        else:
            output_filename = input_path.stem + "_lastframe.jpg"
            output_path = input_path.parent / output_filename

        # Check if we can write to the directory
        output_dir = output_path.parent
        if not os.access(output_dir, os.W_OK):
            show_error(
                "Permission denied",
                f"Cannot write to directory: {output_dir}",
                "Make sure you have write permissions for the directory.\nTry running with appropriate permissions or choose a different output location."
            )
            sys.exit(1)

        # Save frame with best quality
        try:
            success = cv2.imwrite(
                str(output_path),
                frame,
                [cv2.IMWRITE_JPEG_QUALITY, 100]  # Maximum quality
            )
            if not success:
                raise IOError("cv2.imwrite returned False")
        except Exception as e:
            show_error(
                "Failed to save image",
                f"Could not write the output file: {output_path}",
                f"Error: {str(e)}\n\nMake sure you have enough disk space and write permissions."
            )
            sys.exit(1)

        # Show success message
        console.print(f"[bold green]✓[/bold green] extracted {status}")
        console.print(f"[bold green]✓[/bold green] saved to [cyan]{output_path.name}[/cyan]")
        console.print()

        # Show details
        info_text = Text()
        info_text.append("  video: ", style="dim")
        info_text.append(f"{video_info['width']}x{video_info['height']} ", style="bold")
        info_text.append(f"• {video_info['total_frames']} frames ", style="dim")
        info_text.append(f"• {video_info['fps']:.1f} fps\n", style="dim")
        info_text.append("  frame: ", style="dim")
        info_text.append(f"#{frame_num + 1} of {video_info['total_frames']}", style="bold")

        console.print(Panel(
            info_text,
            border_style="dim",
            padding=(0, 1)
        ))
        console.print()

if __name__ == "__main__":
    main()
