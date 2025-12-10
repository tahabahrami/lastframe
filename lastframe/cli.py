#!/usr/bin/env python3
"""
lastframe - Extract the last non-blurry frame from videos
"""
import sys
import os
from pathlib import Path
import cv2
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text

console = Console()

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

def show_help():
    """Display help message."""
    help_text = Text()
    help_text.append("lastframe", style="bold magenta")
    help_text.append(" v1.0.0\n\n", style="dim")
    help_text.append("Extract the last non-blurry frame from videos\n\n", style="white")

    help_text.append("USAGE\n", style="bold cyan")
    help_text.append("  lastframe ", style="white")
    help_text.append("<video_file>", style="yellow")
    help_text.append("\n\n")

    help_text.append("EXAMPLES\n", style="bold cyan")
    help_text.append("  lastframe movie.mp4\n", style="dim")
    help_text.append("  lastframe ~/Videos/clip.mov\n", style="dim")
    help_text.append("  lastframe recording.mkv\n\n", style="dim")

    help_text.append("FEATURES\n", style="bold cyan")
    help_text.append("  • Smart blur detection - automatically picks the sharpest frame\n", style="white")
    help_text.append("  • Checks last 3 frames and selects the best one\n", style="white")
    help_text.append("  • Saves as JPEG with maximum quality (100%)\n", style="white")
    help_text.append("  • Supports all major video formats (MP4, MOV, AVI, MKV, WebM, etc.)\n\n", style="white")

    help_text.append("OUTPUT\n", style="bold cyan")
    help_text.append("  Creates ", style="white")
    help_text.append("<filename>_lastframe.jpg", style="yellow")
    help_text.append(" in the same directory\n\n", style="white")

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
            "No video file specified",
            "You need to provide a video file to extract the last frame from.",
            "Try: lastframe movie.mp4\nOr use: lastframe --help"
        )
        sys.exit(1)

    if len(sys.argv) != 2:
        show_error(
            "Too many arguments",
            "lastframe accepts only one video file at a time.",
            "Try: lastframe movie.mp4"
        )
        sys.exit(1)

    # Check for help flag
    if sys.argv[1] in ['-h', '--help', 'help']:
        show_help()
        sys.exit(0)

    video_path = Path(sys.argv[1])

    # Validate input
    if not video_path.exists():
        show_error(
            "File not found",
            f"The video file doesn't exist: {video_path}",
            "Check the file path and try again.\nMake sure you're in the right directory or use the full path."
        )
        sys.exit(1)

    if not video_path.is_file():
        show_error(
            "Not a file",
            f"The path points to a directory, not a file: {video_path}",
            "Provide a path to a video file, not a folder."
        )
        sys.exit(1)

    # Check file extension
    video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv', '.wmv', '.m4v', '.mpg', '.mpeg', '.3gp'}
    if video_path.suffix.lower() not in video_extensions:
        show_error(
            "Unsupported file type",
            f"'{video_path.suffix}' might not be a video file.",
            f"Supported formats: {', '.join(sorted(video_extensions))}\nThe tool will still try to process it..."
        )
        # Don't exit, let OpenCV try to handle it

    # Show header
    console.print()
    console.print("[bold magenta]lastframe[/bold magenta] [dim]v1.0.0[/dim]")
    console.print()

    # Get video info
    with Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[cyan]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("analyzing video...", total=None)

        try:
            video_info = get_video_info(video_path)
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
            frame, frame_num, blur_score, status = extract_last_frame(video_path)
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

    # Generate output filename
    output_filename = video_path.stem + "_lastframe.jpg"
    output_path = video_path.parent / output_filename

    # Check if we can write to the directory
    if not os.access(video_path.parent, os.W_OK):
        show_error(
            "Permission denied",
            f"Cannot write to directory: {video_path.parent}",
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
    console.print(f"[bold green]✓[/bold green] saved to [cyan]{output_filename}[/cyan]")
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
