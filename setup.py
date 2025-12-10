from setuptools import setup, find_packages

with open("README.md", "w") as f:
    f.write("""# lastframe

Extract the last non-blurry frame from videos with style ✨

## Usage

```bash
lastframe movie.mp4
```

This will extract the last sharp frame and save it as `movie_lastframe.jpg`
""")

setup(
    name="lastframe",
    version="1.0.0",
    description="Extract the last non-blurry frame from videos",
    author="lastframe",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "lastframe=lastframe.cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
