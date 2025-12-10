# Contributing to lastframe 🤝

First off, thanks for taking the time to contribute! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates.

**When reporting a bug, include:**
- A clear and descriptive title
- Steps to reproduce the behavior
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, Python version, lastframe version)
- Sample video file (if possible and not too large)

### 💡 Suggesting Features

Feature requests are welcome! Please provide:
- A clear and descriptive title
- Detailed description of the proposed feature
- Use cases and why it would be useful
- Any examples or mockups if applicable

### 🔧 Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes:**
   - Write clear, commented code
   - Follow existing code style
   - Add tests if applicable
3. **Test your changes:**
   - Test on multiple video formats
   - Test edge cases
   - Ensure existing functionality still works
4. **Update documentation:**
   - Update README if needed
   - Add docstrings to new functions
   - Update CHANGELOG if we have one
5. **Commit your changes:**
   - Use clear commit messages
   - Reference issues if applicable
6. **Push to your fork** and submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small
- Use type hints where helpful

### Testing

Before submitting:
```bash
# Test basic functionality
lastframe test_video.mp4

# Test error handling
lastframe nonexistent.mp4
lastframe --help

# Test with different formats
lastframe video.mov
lastframe video.mkv
```

### Commit Messages

Use clear, descriptive commit messages:
- ✅ "Add batch processing feature"
- ✅ "Fix blur detection on low-res videos"
- ✅ "Update README with new examples"
- ❌ "fix stuff"
- ❌ "update"

## Development Setup

1. **Clone your fork:**
```bash
git clone https://github.com/YOUR_USERNAME/lastframe.git
cd lastframe
```

2. **Install in development mode:**
```bash
pip install -e .
```

3. **Make your changes**

4. **Test thoroughly**

5. **Submit PR**

## Project Structure

```
lastframe_app/
├── lastframe/
│   ├── __init__.py
│   └── cli.py          # Main CLI logic
├── README.md           # Main documentation
├── INSTALL_WINDOWS.md  # Windows-specific docs
├── setup.py            # Package configuration
└── requirements.txt    # Dependencies
```

## Areas to Contribute

### Easy Issues (Good for beginners)
- Documentation improvements
- Adding more examples
- Writing tests
- Fixing typos

### Medium Issues
- Adding support for more video formats
- Improving error messages
- Performance optimizations
- Adding new CLI options

### Advanced Issues
- Batch processing multiple videos
- Custom output paths and naming
- Video metadata preservation
- GPU acceleration support
- Video format conversion

## Questions?

- 💬 Open an issue with the `question` label
- 📧 Contact the maintainer
- 💡 Check existing issues and discussions

## Code of Conduct

### Our Standards

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers
- ✅ Accept constructive criticism
- ✅ Focus on what's best for the community
- ❌ No harassment or trolling
- ❌ No spam or off-topic content

### Attribution

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct.

## Recognition

Contributors will be:
- Listed in the README (coming soon)
- Credited in release notes
- Appreciated in the community! 🎉

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing! 🙏**

Every contribution, no matter how small, makes a difference. ✨
