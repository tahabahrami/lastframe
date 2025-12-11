#!/usr/bin/env python3
"""
Build script for creating standalone executables
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

def build_executable():
    """Build standalone executable using PyInstaller."""

    print("🔨 Building lastframe standalone executable...")
    print()

    # Clean previous builds
    if Path("build").exists():
        shutil.rmtree("build")
    if Path("dist").exists():
        shutil.rmtree("dist")

    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--name=lastframe",
        "--onefile",
        "--clean",
        "--noconfirm",
        "lastframe/cli.py"
    ]

    print(f"Running: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, capture_output=False)

    if result.returncode == 0:
        print()
        print("✅ Build successful!")
        print(f"📦 Executable: dist/lastframe")
        print()

        # Test the executable
        print("🧪 Testing executable...")
        test_result = subprocess.run(["dist/lastframe", "--help"], capture_output=True)

        if test_result.returncode == 0:
            print("✅ Executable works!")
            return True
        else:
            print("❌ Executable test failed")
            return False
    else:
        print()
        print("❌ Build failed")
        return False

if __name__ == "__main__":
    success = build_executable()
    sys.exit(0 if success else 1)
