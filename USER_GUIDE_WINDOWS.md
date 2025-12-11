# lastframe - Complete Beginner's Guide for Windows 🪟

**Easy guide for extracting the last sharp frame from your videos - No coding experience needed!**

---

## 📥 Step 1: Download lastframe

1. Go to: https://github.com/tahabahrami/lastframe/releases
2. Find the **latest release** (it will be at the top)
3. Download the file called: **`lastframe-windows.exe`**
4. The file will download to your **Downloads** folder

---

## 🔓 Step 2: Allow the App to Run

Windows might show a security warning. Here's how to handle it:

### If Windows Defender SmartScreen appears:

1. Click **"More info"**
2. Click **"Run anyway"**

### If your antivirus blocks it:

1. Open your antivirus software
2. Add **lastframe-windows.exe** to the **exceptions** or **whitelist**
3. The app is safe - it's open source on GitHub!

**You only need to do this ONCE!**

---

## 📁 Step 3: Put lastframe in an Easy Location

Let's make it easy to use:

**Option 1: Desktop (Easiest)**
1. Open **File Explorer**
2. Go to **Downloads**
3. **Drag** lastframe-windows.exe to your **Desktop**

**Option 2: Documents**
1. Open **File Explorer**
2. Go to **Downloads**
3. **Drag** lastframe-windows.exe to **Documents**

---

## 🎬 Step 4: Use lastframe

### Open Command Prompt

**Method 1: Search**
1. Press **Windows key** (or click Start)
2. Type: **cmd**
3. Press **Enter**
4. A black window will open - this is Command Prompt!

**Method 2: Right-click**
1. Go to the folder with your videos
2. Hold **Shift** and **right-click** in empty space
3. Select **"Open PowerShell window here"** or **"Open command window here"**

---

## 💻 How to Use lastframe

### Extract Last Frame from ONE Video

**Step 1:** Open Command Prompt

**Step 2:** Go to your Desktop (or wherever your video is):
```cmd
cd Desktop
```
Press **Enter**

**Step 3:** Type:
```cmd
lastframe-windows.exe movie.mp4
```
(Replace `movie.mp4` with your actual video filename)

Press **Enter**

**Done!** You'll find **movie_lastframe.jpg** on your Desktop! 🎉

---

### Extract Frames from MANY Videos (Batch Mode)

**Step 1:** Create a folder on your Desktop called **videos**

**Step 2:** Put all your video files in that folder

**Step 3:** Open Command Prompt

**Step 4:** Type:
```cmd
cd Desktop
```
Press **Enter**

**Step 5:** Type:
```cmd
lastframe-windows.exe videos
```
Press **Enter**

**Done!** All extracted frames will be in the **videos** folder! 🎉

---

## 🎯 Common Examples

### Example 1: Video on Desktop
```cmd
cd Desktop
lastframe-windows.exe my-video.mp4
```

### Example 2: Video in Downloads
```cmd
cd Downloads
lastframe-windows.exe clip.mov
```

### Example 3: Custom Output Name
```cmd
cd Desktop
lastframe-windows.exe video.mp4 thumbnail.jpg
```

### Example 4: Batch Process All Videos in a Folder
```cmd
cd Desktop
lastframe-windows.exe my-videos-folder
```

### Example 5: Batch Process to Different Folder
```cmd
cd Desktop
lastframe-windows.exe input-videos output-frames
```

### Example 6: Using Full Paths
```cmd
C:\Users\YourName\Desktop\lastframe-windows.exe C:\Users\YourName\Videos\movie.mp4
```

---

## 🚀 Even Easier Way - Drag and Drop Script

Create a file called **extract-frame.bat** on your Desktop with this:

```batch
@echo off
echo Drag your video file here and press Enter
set /p video="Video file: "
lastframe-windows.exe "%video%"
pause
```

**How to use:**
1. Double-click **extract-frame.bat**
2. Drag your video into the window
3. Press **Enter**
4. Done!

---

## 📂 Add to Windows PATH (Optional - Advanced)

This lets you use `lastframe` from anywhere without typing the full path.

1. **Right-click** "This PC" or "My Computer"
2. Click **Properties**
3. Click **Advanced system settings**
4. Click **Environment Variables**
5. Under "User variables", find **Path**, click **Edit**
6. Click **New**
7. Add: `C:\Users\YourName\Desktop` (or wherever you put lastframe-windows.exe)
8. Click **OK** on everything
9. **Restart Command Prompt**

Now you can just type:
```cmd
lastframe-windows.exe movie.mp4
```
From ANY folder!

---

## 🆘 Troubleshooting

### "File not found" or "Cannot find path"
Make sure you're in the right folder:
```cmd
dir
```
This shows all files in your current location.

### Video name has spaces
Use quotes:
```cmd
lastframe-windows.exe "my vacation video.mp4"
```

### "Access denied"
Right-click Command Prompt and select **"Run as administrator"**

### Can't find Command Prompt
- Press **Windows key**
- Type: **cmd**
- Press **Enter**

Or:
- Press **Windows + R**
- Type: **cmd**
- Press **Enter**

### PowerShell Instead of CMD
PowerShell works too! Just use:
```powershell
.\lastframe-windows.exe movie.mp4
```
(Note the `.\` at the beginning)

---

## 💡 Pro Tips

### Process Multiple Videos Quickly

1. Put all videos in one folder
2. Open that folder in File Explorer
3. Hold **Shift** + **Right-click** in empty space
4. Click **"Open PowerShell window here"**
5. Type:
```powershell
.\lastframe-windows.exe .
```
(The dot means "current folder")

### Create Desktop Shortcut

1. Right-click on **lastframe-windows.exe**
2. Select **"Create shortcut"**
3. Drag shortcut to Desktop
4. Right-click the shortcut → **Properties**
5. In "Start in" field, put: `C:\Users\YourName\Desktop`
6. Click **OK**

Now double-click the shortcut to use it!

---

## 📝 What File Types Work?

lastframe works with all common video formats:
- MP4
- MOV
- AVI
- MKV
- WebM
- WMV
- FLV
- And more!

---

## ❓ Frequently Asked Questions

**Q: Do I need to install anything?**
A: No! lastframe-windows.exe works by itself. No Python, no other software needed.

**Q: Is it safe? Windows says it's dangerous!**
A: Yes! The code is open source on GitHub. Windows blocks it because I'm not a verified Windows publisher. Just click "More info" → "Run anyway"

**Q: How do I update?**
A: Download the new version from GitHub and replace the old file.

**Q: Can I use it on multiple videos at once?**
A: Yes! Put all videos in a folder and use: `lastframe-windows.exe foldername`

**Q: Where does the image save?**
A: In the same folder as your video, with `_lastframe.jpg` added to the name.

**Q: What if the video has spaces in the name?**
A: Use quotes: `lastframe-windows.exe "my vacation.mp4"`

**Q: Can I add it to right-click menu?**
A: Yes! See the advanced section in INSTALL_WINDOWS.md

---

## 🎓 Complete Example Walkthrough

Let's say you have videos on your Desktop called:
- vacation.mp4
- birthday.mov
- concert.mp4

**Here's what to do:**

1. **Open Command Prompt**
   - Press Windows key
   - Type: cmd
   - Press Enter

2. **Go to Desktop**
   ```cmd
   cd Desktop
   ```

3. **Make sure lastframe-windows.exe is on Desktop**
   ```cmd
   dir lastframe-windows.exe
   ```
   You should see the file listed

4. **Extract first video**
   ```cmd
   lastframe-windows.exe vacation.mp4
   ```
   Result: `vacation_lastframe.jpg` appears on Desktop

5. **Extract second video with custom name**
   ```cmd
   lastframe-windows.exe birthday.mov bday-thumbnail.jpg
   ```
   Result: `bday-thumbnail.jpg` appears on Desktop

6. **Extract third video**
   ```cmd
   lastframe-windows.exe concert.mp4
   ```
   Result: `concert_lastframe.jpg` appears on Desktop

**That's it!** You now have 3 beautiful images extracted from your videos! 🎉

---

## 🎬 Batch Processing Example

Let's say you have 50 videos from a wedding in a folder called "wedding-videos":

1. **Put lastframe-windows.exe in the same place** (Desktop)

2. **Open Command Prompt**
   ```cmd
   cd Desktop
   ```

3. **Process all videos at once**
   ```cmd
   lastframe-windows.exe wedding-videos
   ```

4. **Wait** (it will show progress)

5. **Done!** All 50 frames are now in the wedding-videos folder!

You just processed 50 videos in one command! 🚀

---

## 🖱️ Super Easy Method - No Command Prompt Needed

**Create this batch file once:**

1. Right-click on Desktop → **New** → **Text Document**
2. Name it: **lastframe-helper.bat**
3. Right-click it → **Edit**
4. Paste this:

```batch
@echo off
title lastframe - Video Frame Extractor
color 0A
echo.
echo ========================================
echo    lastframe - Video Frame Extractor
echo ========================================
echo.
echo Drag and drop your video file here,
echo or type the full path, then press Enter
echo.
set /p input="Video file or folder: "
echo.
lastframe-windows.exe "%input%"
echo.
echo Done! Press any key to close...
pause >nul
```

5. Save and close

**Now whenever you want to extract a frame:**
1. Double-click **lastframe-helper.bat**
2. Drag your video file into the window
3. Press Enter
4. Done!

---

## 📞 Need More Help?

- **Issues/Bugs**: https://github.com/tahabahrami/lastframe/issues
- **Questions**: Open an issue on GitHub with the tag "question"

---

**Made with ❤️ for people who just want it to work!**

**No coding experience needed. No terminal expertise required. Just simple, working software.** ✨
