# lastframe - Complete Beginner's Guide for Mac 🍎

**Easy guide for extracting the last sharp frame from your videos - No coding experience needed!**

---

## 📥 Step 1: Download lastframe

1. Go to: https://github.com/tahabahrami/lastframe/releases
2. Find the **latest release** (it will be at the top)
3. Download the file called: **`lastframe-mac`**
4. The file will download to your **Downloads** folder

---

## 🔓 Step 2: Allow the App to Run

Mac will block the app at first because it's not from the App Store. Here's how to fix it:

### Method 1: Using Finder (Easiest)
1. Open **Finder**
2. Go to your **Downloads** folder
3. Find the **lastframe-mac** file
4. **Right-click** (or Control+Click) on it
5. Select **"Open"** from the menu
6. Click **"Open"** again when the warning appears
7. The app will run once and quit - that's normal!

### Method 2: Using System Settings
1. Try to open **lastframe-mac** by double-clicking
2. Mac will show a security warning
3. Open **System Settings** → **Privacy & Security**
4. Scroll down and click **"Open Anyway"**
5. Click **"Open"** when asked

**You only need to do this ONCE!** After this, lastframe will work normally.

---

## 📁 Step 3: Put lastframe in an Easy Location

Let's make it easy to use:

1. Open **Finder**
2. Go to your **Home folder** (click your username in the sidebar)
3. **Drag** the **lastframe-mac** file from Downloads to your Home folder
4. You can now delete it from Downloads

---

## 🎬 Step 4: Use lastframe

### Open Terminal
1. Press **Command (⌘) + Space** to open Spotlight
2. Type: **Terminal**
3. Press **Enter**
4. A black or white window will open - this is Terminal!

---

## 💻 How to Use lastframe

### Extract Last Frame from ONE Video

**Step 1:** In Terminal, type:
```bash
cd ~/Desktop
```
Press **Enter** (this goes to your Desktop)

**Step 2:** Type:
```bash
~/lastframe-mac movie.mp4
```
(Replace `movie.mp4` with your actual video filename)

Press **Enter**

**Done!** You'll find **movie_lastframe.jpg** on your Desktop! 🎉

---

### Extract Frames from MANY Videos (Batch Mode)

**Step 1:** Create a folder on your Desktop called **videos**

**Step 2:** Put all your video files in that folder

**Step 3:** In Terminal, type:
```bash
cd ~/Desktop
```
Press **Enter**

**Step 4:** Type:
```bash
~/lastframe-mac videos
```
Press **Enter**

**Done!** All extracted frames will be in the **videos** folder! 🎉

---

## 🎯 Common Examples

### Example 1: Video on Desktop
```bash
cd ~/Desktop
~/lastframe-mac my-video.mp4
```

### Example 2: Video in Downloads
```bash
cd ~/Downloads
~/lastframe-mac clip.mov
```

### Example 3: Custom Output Name
```bash
cd ~/Desktop
~/lastframe-mac video.mp4 thumbnail.jpg
```

### Example 4: Batch Process All Videos in a Folder
```bash
cd ~/Desktop
~/lastframe-mac my-videos-folder
```

### Example 5: Batch Process to Different Folder
```bash
cd ~/Desktop
~/lastframe-mac input-videos output-frames
```

---

## 🆘 Troubleshooting

### "Permission denied"
The file isn't executable. Fix it:
```bash
chmod +x ~/lastframe-mac
```

### "File not found"
Make sure you're in the right folder:
```bash
ls
```
This shows all files in your current location.

### "No such file or directory"
Your video name might have spaces. Use quotes:
```bash
~/lastframe-mac "my vacation video.mp4"
```

### Can't find Terminal?
- Press **Command (⌘) + Space**
- Type: **Terminal**
- Press **Enter**

Or:
- Open **Finder**
- Go to **Applications** → **Utilities** → **Terminal**

---

## 💡 Pro Tips

### Make it Even Easier
Add lastframe to your Applications:

1. Open **Finder**
2. Go to **Applications**
3. **Drag** lastframe-mac into Applications
4. Now you can use it from anywhere:
```bash
/Applications/lastframe-mac movie.mp4
```

### Process Videos Faster
Right-click on a video folder and select:
**Services** → **New Terminal at Folder**

Then just type:
```bash
~/lastframe-mac .
```
(The dot means "current folder")

---

## 📝 What File Types Work?

lastframe works with all common video formats:
- MP4
- MOV
- AVI
- MKV
- WebM
- And more!

---

## ❓ Frequently Asked Questions

**Q: Do I need to install anything?**
A: No! lastframe-mac works by itself. No Python, no other software needed.

**Q: Is it safe?**
A: Yes! The code is open source on GitHub. Mac blocks it because I'm not an Apple registered developer.

**Q: How do I update?**
A: Download the new version from GitHub and replace the old file.

**Q: Can I use it on multiple videos at once?**
A: Yes! Put all videos in a folder and use: `~/lastframe-mac foldername`

**Q: Where does the image save?**
A: In the same folder as your video, with `_lastframe.jpg` added to the name.

**Q: What if the video has spaces in the name?**
A: Use quotes: `~/lastframe-mac "my vacation.mp4"`

---

## 🎓 Complete Example Walkthrough

Let's say you have videos on your Desktop called:
- vacation.mp4
- birthday.mov
- concert.mp4

**Here's what to do:**

1. **Open Terminal**
   - Press Command+Space
   - Type: Terminal
   - Press Enter

2. **Go to Desktop**
   ```bash
   cd ~/Desktop
   ```

3. **Extract first video**
   ```bash
   ~/lastframe-mac vacation.mp4
   ```
   Result: `vacation_lastframe.jpg` appears on Desktop

4. **Extract second video with custom name**
   ```bash
   ~/lastframe-mac birthday.mov bday-thumbnail.jpg
   ```
   Result: `bday-thumbnail.jpg` appears on Desktop

5. **Extract third video**
   ```bash
   ~/lastframe-mac concert.mp4
   ```
   Result: `concert_lastframe.jpg` appears on Desktop

**That's it!** You now have 3 beautiful images extracted from your videos! 🎉

---

## 📞 Need More Help?

- **Issues/Bugs**: https://github.com/tahabahrami/lastframe/issues
- **Questions**: Open an issue on GitHub with the tag "question"

---

**Made with ❤️ for people who just want it to work!**

**No coding experience needed. No terminal expertise required. Just simple, working software.** ✨
