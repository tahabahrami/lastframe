# lastframe ✨

> **extract the last sharp frame from your videos, no cap** 🎬

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)](https://github.com/tahabahrami/lastframe)

Smart CLI tool that automatically detects and extracts the sharpest frame from the end of your videos. Because blurry screenshots are not it. 💯

---

## 📥 Download (No Python Required!)

**For non-technical users - just download and use!**

### 🍎 macOS
[**Download lastframe for Mac**](https://github.com/tahabahrami/lastframe/releases/latest/download/lastframe-mac)

→ [Complete Mac Guide](USER_GUIDE_MAC.md)

### 🪟 Windows
[**Download lastframe for Windows**](https://github.com/tahabahrami/lastframe/releases/latest/download/lastframe-windows.exe)

→ [Complete Windows Guide](USER_GUIDE_WINDOWS.md)

### ⚡ Quick Start
Don't know where to begin? Check out the [Quick Start Guide](QUICK_START.md)!

---

## 🔥 Features

- **🧠 Smart Blur Detection** - Automatically checks last 3 frames and picks the sharpest one using Laplacian variance
- **📦 Batch Processing** - Process entire folders of videos at once (NEW in v1.1!)
- **🎯 Custom Output** - Specify custom output files or directories (NEW in v1.1!)
- **💎 Quality Preserved** - Saves as JPEG with 100% quality (zero compression, full flex)
- **🎥 Universal Format Support** - MP4, MOV, AVI, MKV, WebM, and more
- **✨ Beautiful UI** - Modern terminal output with colors, emojis, and vibes
- **🌍 Cross-Platform** - Works on macOS, Windows, and Linux
- **⚡ Lightning Fast** - Processes videos in seconds

---

## 🚀 Quick Start

```bash
# Install
pip install -e .

# Single video
lastframe movie.mp4

# Batch process
lastframe ./videos

# Profit 💰
```

---

## 📦 Installation

### Option 1: Standalone Executables (Recommended for Beginners) ⭐

**No Python installation required!**

#### macOS 🍎
1. [Download lastframe-mac](https://github.com/tahabahrami/lastframe/releases/latest)
2. Right-click → Open (first time only)
3. Use it: `./lastframe-mac movie.mp4`

📖 [Complete Mac Guide](USER_GUIDE_MAC.md)

#### Windows 🪟
1. [Download lastframe-windows.exe](https://github.com/tahabahrami/lastframe/releases/latest)
2. Click "More info" → "Run anyway" (first time only)
3. Use it: `lastframe-windows.exe movie.mp4`

📖 [Complete Windows Guide](USER_GUIDE_WINDOWS.md)

---

### Option 2: Python Install (For Developers)

#### macOS / Linux

```bash
cd lastframe_app
pip3 install -e .
```

#### Windows

**Method 1:** Double-click `install_windows.bat`

**Method 2:** Manual install
```cmd
pip install -e .
```

See [INSTALL_WINDOWS.md](INSTALL_WINDOWS.md) for detailed setup.

---

## 💻 Usage

### Single File Mode

```bash
# Default output (same directory)
lastframe video.mp4                    # → video_lastframe.jpg

# Custom output file
lastframe video.mp4 output.jpg         # → output.jpg
```

### Batch Mode (NEW! 🎉)

Process entire directories of videos at once:

```bash
# Process all videos in a directory
lastframe ./videos                     # → ./videos/*_lastframe.jpg

# Process to custom output directory
lastframe ./videos ./output            # → ./output/*_lastframe.jpg
```

---

## 🎨 Demo

### Single File Mode
```bash
$ lastframe shaky_video.mp4

lastframe v1.1.0

✓ extracted 2nd last frame (last was blurry 🔍 score: 892.1)
✓ saved to shaky_video_lastframe.jpg

╭──────────────────────────────────────────────╮
│   video: 1280x720 • 150 frames • 24.0 fps    │
│   frame: #149 of 150                         │
╰──────────────────────────────────────────────╯
```

### Batch Mode
```bash
$ lastframe ./videos

lastframe v1.1.0 • batch mode

📁 Input:  videos
📤 Output: videos
🎬 Videos: 15 found

  Processing clip_015.mp4... ━━━━━━━━━━━━━━━━━ 100%

✓ Batch processing complete!

┏━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Status       ┃ Count ┃
┡━━━━━━━━━━━━━━╇━━━━━━━┩
│ ✓ Success    │    15 │
│ Total        │    15 │
└──────────────┴───────┘
```

The tool intelligently tells you what it did:
- ✨ **"last frame (sharp)"** - when the last frame is crisp
- 🔍 **"2nd last frame (last was blurry)"** - when it skips a blurry one
- 🔍 **"3rd last frame (last 2 were blurry)"** - when it goes back further
- ⚠️ **"last frame (all frames blurry)"** - fallback to last frame

---

## 🧪 How It Works

1. **Analyzes** the video file (resolution, fps, frame count)
2. **Extracts** the last 3 frames
3. **Calculates** blur score for each frame using Laplacian variance
4. **Selects** the sharpest one (highest score wins)
5. **Saves** it as high-quality JPEG (100% quality, no losses)

**Algorithm:** Uses Laplacian variance to detect blur. Higher variance = sharper edges = better frame.

---

## 🎯 Use Cases

- 📹 **Video Editing** - Extract clean thumbnails
- 🎮 **Gaming** - Grab sharp screenshots from gameplay
- 📱 **Social Media** - Get crisp frames for posts
- 🎬 **Content Creation** - Quick frame extraction
- 📊 **Analysis** - Extract frames for CV/ML tasks
- 🗂️ **Batch Processing** - Process entire video libraries at once (NEW!)

---

## 📚 Examples

### Basic Usage

```bash
# Single video, default output
lastframe movie.mp4

# Single video, custom output
lastframe movie.mp4 thumbnail.jpg

# With spaces (use quotes)
lastframe "vacation video.mp4" "vacation thumbnail.jpg"
```

### Batch Processing

```bash
# Process all videos in current directory
lastframe .

# Process videos in specific directory
lastframe ~/Videos/recordings

# Process to different output directory
lastframe ./input ./output

# Process to organized output folder
lastframe ~/Downloads/videos ~/Pictures/thumbnails
```

### Advanced

```bash
# Full paths
lastframe /path/to/video.mp4 /path/to/output.jpg

# Batch with full paths
lastframe /Volumes/External/videos /Volumes/External/frames
```

---

## 🛠️ Tech Stack

- **Python** - Core language
- **OpenCV** - Video processing powerhouse
- **NumPy** - Mathematical operations
- **Rich** - Beautiful terminal UI

---

## 📋 Requirements

- Python 3.8+
- opencv-python >= 4.8.0
- numpy >= 1.24.0
- rich >= 13.0.0

Dependencies auto-install during setup.

---

## 🎮 Command Reference

```bash
# Help
lastframe --help
lastframe -h

# Single file mode
lastframe <video_file> [output_file]

# Batch mode
lastframe <input_directory> [output_directory]
```

---

## 🐛 Error Handling

Got you covered with helpful error messages:

- ❌ File/directory not found
- ❌ Unsupported formats
- ❌ Corrupted videos
- ❌ Permission issues
- ❌ Empty videos
- ❌ Invalid output paths

Each error includes suggestions to fix it. No more guessing! 💡

---

## 🌐 Supported Formats

All major video formats:
```
MP4 • MOV • AVI • MKV • WebM • FLV • WMV • M4V • MPG • MPEG • 3GP
```

Basically if your video player can open it, we can handle it. 💪

---

## 🤝 Contributing

Contributions are welcome! Got ideas? Found a bug? Want to add features?

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

MIT License - do whatever you want with it!

See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Built with [OpenCV](https://opencv.org/)
- UI powered by [Rich](https://github.com/Textualize/rich)
- Created with [Claude Code](https://claude.ai/claude-code)

---

## 💬 Community

- 🐛 **Bug reports:** [Open an issue](https://github.com/tahabahrami/lastframe/issues)
- 💡 **Feature requests:** [Open an issue](https://github.com/tahabahrami/lastframe/issues)
- ⭐ **Star this repo** if you find it useful!

---

## 📊 Stats

![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Code Style](https://img.shields.io/badge/code%20style-clean-brightgreen.svg)

---

## 🚦 Status

- ✅ Core functionality
- ✅ Blur detection
- ✅ Cross-platform support
- ✅ Error handling
- ✅ Documentation
- ✅ Batch processing (v1.1.0)
- ✅ Custom output paths (v1.1.0)
- 🚧 Video format conversion (coming soon)
- 🚧 GPU acceleration (coming soon)

---

## 📖 Changelog

### v1.1.0 (Latest)
- ✨ Added batch processing - process entire directories
- ✨ Added custom output support - specify output file/directory
- 🎨 Improved progress display with progress bars
- 🎨 Added summary table for batch operations
- 📝 Updated documentation and examples

### v1.0.0
- 🎉 Initial release
- 🧠 Smart blur detection
- 💎 Maximum quality output
- 🌍 Cross-platform support
- ✨ Beautiful terminal UI

---

## 📞 Contact

**Taha Bahrami**
- GitHub: [@tahabahrami](https://github.com/tahabahrami)

---

## ⭐ Show Your Support

If this project helped you, give it a ⭐! It helps others discover it too.

---

<div align="center">

**Made with ❤️ and Python**

[Report Bug](https://github.com/tahabahrami/lastframe/issues) • [Request Feature](https://github.com/tahabahrami/lastframe/issues)

</div>

---

### 💡 Pro Tips

```bash
# Get help anytime
lastframe --help

# Works with any video format
lastframe video.mkv
lastframe clip.avi
lastframe movie.mov

# Handles spaces in filenames
lastframe "my vacation 2024.mp4"

# Batch process your entire video library
lastframe ~/Movies/clips ~/Movies/thumbnails

# Organize your output
lastframe ./raw-footage ./extracted-frames
```

---

**Stay sharp! ✌️**
