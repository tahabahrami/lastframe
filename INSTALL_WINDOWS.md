# Installing lastframe on Windows

A step-by-step guide to install and use `lastframe` on Windows.

---

## Prerequisites

You need Python 3.8 or higher installed on your Windows machine.

### Check if Python is installed

Open **Command Prompt** (CMD) or **PowerShell** and run:

```cmd
python --version
```

If Python is installed, you should see something like `Python 3.11.x`.

If not installed, download Python from: https://www.python.org/downloads/

**Important:** During installation, check the box that says "Add Python to PATH"

---

## Installation Steps

### Step 1: Download the lastframe package

Download or clone the `lastframe_app` folder to your computer. For example:
```
C:\Users\YourName\Downloads\lastframe_app
```

### Step 2: Open Command Prompt or PowerShell

**For Command Prompt:**
- Press `Win + R`
- Type `cmd` and press Enter

**For PowerShell:**
- Press `Win + X`
- Select "Windows PowerShell" or "Terminal"

### Step 3: Navigate to the lastframe_app directory

```cmd
cd C:\Users\YourName\Downloads\lastframe_app
```

Replace `YourName` with your actual Windows username and adjust the path to where you downloaded the folder.

### Step 4: Install lastframe

Run the following command:

```cmd
pip install -e .
```

You should see output showing the installation of opencv-python, numpy, and rich libraries.

**Note:** If you get a "pip is not recognized" error, try:
```cmd
python -m pip install -e .
```

### Step 5: Verify installation

After installation completes, verify it works:

```cmd
lastframe --help
```

If you see the help message, congratulations! Installation is complete.

---

## Troubleshooting

### Issue: "lastframe is not recognized as an internal or external command"

This means Python's Scripts folder is not in your PATH.

**Solution 1:** Add Python Scripts to PATH
1. Find your Python Scripts folder, typically:
   ```
   C:\Users\YourName\AppData\Local\Programs\Python\Python311\Scripts
   ```
2. Add it to your PATH environment variable:
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Go to "Advanced" tab → "Environment Variables"
   - Under "User variables", find "Path", click "Edit"
   - Click "New" and add the Scripts folder path
   - Click "OK" on all windows
   - **Restart** Command Prompt/PowerShell

**Solution 2:** Use full path
```cmd
python -m lastframe.cli movie.mp4
```

**Solution 3:** Create a batch file
Create a file `lastframe.bat` in `C:\Windows\System32` with:
```batch
@echo off
python -m lastframe.cli %*
```

### Issue: "Microsoft Visual C++ 14.0 is required" (during opencv installation)

OpenCV requires Microsoft Visual C++ redistributables.

**Solution:**
Download and install "Microsoft C++ Build Tools" from:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

Or install the redistributables from:
https://aka.ms/vs/17/release/vc_redist.x64.exe

### Issue: Permission denied

**Solution:** Run Command Prompt or PowerShell as Administrator:
- Right-click on Command Prompt/PowerShell
- Select "Run as administrator"
- Retry the installation command

---

## Usage on Windows

Once installed, you can use `lastframe` from any directory:

### Command Prompt (CMD)

```cmd
# Navigate to your video folder
cd C:\Users\YourName\Videos

# Extract last frame
lastframe movie.mp4

# With full path
lastframe "C:\Users\YourName\Videos\my video.mp4"
```

**Note:** Use quotes around paths with spaces!

### PowerShell

```powershell
# Navigate to your video folder
cd C:\Users\YourName\Videos

# Extract last frame
lastframe movie.mp4

# With full path
lastframe "C:\Users\YourName\Videos\my video.mp4"
```

### Examples

```cmd
# Single file
lastframe vacation.mp4

# File with spaces in name
lastframe "birthday party.mov"

# Full path with spaces
lastframe "C:\Users\John\Desktop\Screen Recording 2024.mp4"

# Different formats
lastframe clip.avi
lastframe video.mkv
lastframe recording.webm
```

---

## Output

The extracted frame will be saved in the same directory as your video file with the name:
```
<original_filename>_lastframe.jpg
```

For example:
- Input: `movie.mp4`
- Output: `movie_lastframe.jpg`

---

## Uninstall

To uninstall lastframe:

```cmd
pip uninstall lastframe
```

---

## Video Format Support on Windows

The tool supports all major video formats that OpenCV can read, including:
- MP4, MOV, AVI, MKV, WebM, FLV, WMV, M4V, MPG, MPEG, 3GP

**Note:** Some codecs might require additional codec packs on Windows. If you encounter issues with specific files, try converting them to MP4 using:
- HandBrake (free): https://handbrake.fr/
- VLC Media Player (free): https://www.videolan.org/
- FFmpeg (advanced): https://ffmpeg.org/

---

## Tips for Windows Users

### 1. Use Tab Completion
Press `Tab` to auto-complete file and folder names in CMD/PowerShell.

### 2. Drag and Drop
You can drag a video file into the CMD/PowerShell window to automatically paste its full path.

### 3. Create a Desktop Shortcut
Create a `.bat` file on your desktop:
```batch
@echo off
echo Drag and drop your video file here, then press Enter.
set /p videofile="Video file: "
lastframe "%videofile%"
pause
```

Save as `Extract_LastFrame.bat` and double-click to use!

### 4. Right-Click Context Menu (Advanced)

You can add lastframe to Windows Explorer's right-click menu by creating a registry entry. Create a file `add_to_context_menu.reg`:

```reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\lastframe]
@="Extract Last Frame"

[HKEY_CLASSES_ROOT\*\shell\lastframe\command]
@="cmd.exe /k lastframe \"%1\""
```

Double-click to add, then right-click any video file → "Extract Last Frame"

---

## Need Help?

Run `lastframe --help` for usage information.

For issues, check: https://github.com/anthropics/claude-code/issues
