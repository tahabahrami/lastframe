# lastframe ✨

> **extract the last sharp frame from your videos, no cap** 🎬

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)](https://github.com/tahabahrami/lastframe)

Smart CLI tool that automatically detects and extracts the sharpest frame from the end of your videos. Because blurry screenshots are not it. 💯

---

## 🔥 Features

- **🧠 Smart Blur Detection** - Automatically checks last 3 frames and picks the sharpest one using Laplacian variance
- **💎 Quality Preserved** - Saves as JPEG with 100% quality (zero compression, full flex)
- **🎥 Universal Format Support** - MP4, MOV, AVI, MKV, WebM, and more
- **✨ Beautiful UI** - Modern terminal output with colors, emojis, and vibes
- **🌍 Cross-Platform** - Works on macOS, Windows, and Linux
- **⚡ Lightning Fast** - Processes videos in seconds
- **🎯 Simple API** - One command, that's it

---

## 🚀 Quick Start

```bash
# Install
pip install -e .

# Use
lastframe movie.mp4

# Profit 💰
```

---

## 📦 Installation

### macOS / Linux

```bash
cd lastframe_app
pip3 install -e .
```

### Windows

**Option 1:** Double-click `install_windows.bat`

**Option 2:** Manual install
```cmd
pip install -e .
```

See [INSTALL_WINDOWS.md](INSTALL_WINDOWS.md) for detailed Windows setup.

---

## 💻 Usage

```bash
lastframe <video_file>
```

### Examples

```bash
# Basic usage
lastframe movie.mp4

# With spaces (use quotes)
lastframe "vacation video.mp4"

# Full path
lastframe /path/to/video.mp4
```

### Output

Creates `<filename>_lastframe.jpg` in the same directory as your video.

**Example:**
- Input: `movie.mp4`
- Output: `movie_lastframe.jpg` ✨

---

## 🎨 Demo

```bash
$ lastframe shaky_video.mp4

lastframe v1.0.0

✓ extracted 2nd last frame (last was blurry 🔍 score: 892.1)
✓ saved to shaky_video_lastframe.jpg

╭──────────────────────────────────────────────╮
│   video: 1280x720 • 150 frames • 24.0 fps    │
│   frame: #149 of 150                         │
╰──────────────────────────────────────────────╯
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

## 🎮 Options

```bash
-h, --help     Show help message
```

More options coming soon! 🚧

---

## 🐛 Error Handling

Got you covered with helpful error messages:

- ❌ File not found
- ❌ Unsupported formats
- ❌ Corrupted videos
- ❌ Permission issues
- ❌ Empty videos

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
- 🚧 Batch processing (coming soon)
- 🚧 Custom output paths (coming soon)
- 🚧 Video format conversion (coming soon)

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
```

---

**Stay sharp! ✌️**
