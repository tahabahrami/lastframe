# lastframe - Quick Start Guide ⚡

**Get started in 2 minutes!**

---

## 🚀 For Beginners (No Python Needed)

### macOS Users 🍎

1. **Download**: Get `lastframe-mac` from [GitHub Releases](https://github.com/tahabahrami/lastframe/releases)
2. **Allow**: Right-click → Open (first time only)
3. **Use**:
   ```bash
   ~/lastframe-mac movie.mp4
   ```

📖 **[Full Mac Guide](USER_GUIDE_MAC.md)** - Complete step-by-step instructions

---

### Windows Users 🪟

1. **Download**: Get `lastframe-windows.exe` from [GitHub Releases](https://github.com/tahabahrami/lastframe/releases)
2. **Allow**: Click "More info" → "Run anyway" (first time only)
3. **Use**:
   ```cmd
   lastframe-windows.exe movie.mp4
   ```

📖 **[Full Windows Guide](USER_GUIDE_WINDOWS.md)** - Complete step-by-step instructions

---

## 💻 For Developers (Python Install)

### Install
```bash
pip install -e .
```

### Use
```bash
# Single file
lastframe movie.mp4

# Batch mode
lastframe ./videos

# Custom output
lastframe video.mp4 output.jpg
```

---

## 🎯 Common Use Cases

### Extract one frame
```bash
lastframe vacation.mp4
→ Creates: vacation_lastframe.jpg
```

### Extract with custom name
```bash
lastframe video.mp4 thumbnail.jpg
→ Creates: thumbnail.jpg
```

### Process entire folder
```bash
lastframe ./my-videos
→ Creates: *_lastframe.jpg for each video
```

### Process to different folder
```bash
lastframe ./input-videos ./output-frames
→ Creates all frames in output-frames/
```

---

## 📊 What You'll See

### Single File
```
lastframe v1.1.0

✓ extracted last frame (sharp ✨ score: 892.1)
✓ saved to video_lastframe.jpg

╭────────────────────────────────────────╮
│ video: 1920x1080 • 300 frames • 30 fps │
│ frame: #300 of 300                     │
╰────────────────────────────────────────╯
```

### Batch Mode
```
lastframe v1.1.0 • batch mode

📁 Input:  videos
📤 Output: videos
🎬 Videos: 15 found

Processing... ━━━━━━━━━━━━━━ 100%

✓ Batch processing complete!

┏━━━━━━━━━━┳━━━━━━━┓
┃ Status   ┃ Count ┃
┡━━━━━━━━━━╇━━━━━━━┩
│ Success  │    15 │
│ Total    │    15 │
└──────────┴───────┘
```

---

## 🆘 Need Help?

- 🍎 **Mac Users**: [Complete Mac Guide](USER_GUIDE_MAC.md)
- 🪟 **Windows Users**: [Complete Windows Guide](USER_GUIDE_WINDOWS.md)
- 💻 **Developers**: [README.md](README.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/tahabahrami/lastframe/issues)

---

## 📝 Supported Formats

✅ MP4, MOV, AVI, MKV, WebM, FLV, WMV, M4V, MPG, MPEG, 3GP

---

## ⚡ Quick Tips

- Use quotes for filenames with spaces: `lastframe "my video.mp4"`
- Check progress: The tool shows what it's doing in real-time
- Batch mode: Perfect for processing 10+ videos at once
- Custom output: Great for organizing your thumbnails

---

**Made simple. Made fast. Made to work.** ✨
