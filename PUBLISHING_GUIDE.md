# Publishing to PyPI - Complete Guide

## Prerequisites ✅ (Already Completed)

Your package is ready with all necessary files:
- ✅ `pyproject.toml` - Package configuration
- ✅ `LICENSE` - MIT license
- ✅ `MANIFEST.in` - Include documentation files
- ✅ `README.md` - Project description
- ✅ `.gitignore` - Clean repository
- ✅ GitHub Actions workflow for automated testing

## Step 1: Update Package Metadata

Edit `pyproject.toml` and update these fields with your information:

```toml
[project]
name = "di-done-right"  # This name must be unique on PyPI
authors = [{name = "Your Real Name", email = "your.real.email@example.com"}]
homepage = "https://github.com/yourusername/di-done-right"
repository = "https://github.com/yourusername/di-done-right"
documentation = "https://github.com/yourusername/di-done-right#documentation"
```

## Step 2: Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Create an account
3. Verify your email address
4. Enable 2FA (recommended)

## Step 3: Create API Token

1. Go to https://pypi.org/manage/account/
2. Scroll down to "API tokens"
3. Click "Add API token"
4. Name it (e.g., "di-done-right-upload")
5. Select scope: "Entire account" or specific project
6. Copy the token (starts with `pypi-`)

## Step 4: Test Build Locally

```bash
# Install build tools (already done)
pip install build twine

# Build the package
python -m build

# Check the built package
twine check dist/*
```

This creates:
- `dist/di_done_right-1.0.0-py3-none-any.whl` (wheel)
- `dist/di-done-right-1.0.0.tar.gz` (source distribution)

## Step 5: Test Upload to Test PyPI (Recommended)

1. Create account at https://test.pypi.org/account/register/
2. Get API token from test PyPI
3. Upload to test PyPI:

```bash
twine upload --repository testpypi dist/*
# Enter username: __token__
# Enter password: pypi-AgEIcHl... (your test PyPI token)
```

4. Test install from test PyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ di-done-right
```

## Step 6: Upload to Production PyPI

```bash
twine upload dist/*
# Enter username: __token__
# Enter password: pypi-AgEIcHl... (your production PyPI token)
```

## Step 7: Verify Upload

1. Check your package at: https://pypi.org/project/di-done-right/
2. Test installation: `pip install di-done-right`

## Step 8: Set Up GitHub Repository (Optional but Recommended)

1. Create repository on GitHub
2. Push your code:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/di-done-right.git
git push -u origin main
```

3. Add PyPI API token to GitHub Secrets:
   - Go to repository Settings → Secrets and variables → Actions
   - Add secret: `PYPI_API_TOKEN` with your PyPI token
   - The GitHub Action will automatically publish on releases

## Step 9: Create a Release

After pushing to GitHub:

1. Go to your repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. Describe the release
6. Click "Publish release"

The GitHub Action will automatically:
- Run tests
- Build the package
- Upload to PyPI

## Common Issues and Solutions

### Issue: Package name already exists
**Solution:** Change the name in `pyproject.toml`. Try variations like:
- `di-done-right-framework`
- `python-di-done-right` 
- `di-framework-done-right`

### Issue: Build fails
**Solution:** Check these files exist and are properly formatted:
- `di_container/__init__.py` ✅
- `pyproject.toml` ✅
- `LICENSE` ✅

### Issue: Import errors after install
**Solution:** Ensure `di_container/__init__.py` exports the main classes:

```python
from .container import DIContainer
from .service_provider import ServiceProvider
from .enums import ServiceLifetime
# etc.
```

### Issue: Documentation not included
**Solution:** Check `MANIFEST.in` includes all documentation files ✅

## Package Structure Check ✅

Your package structure is correct:

```
di-done-right/
├── di_container/           # Main package
│   ├── __init__.py        ✅
│   ├── container.py       ✅
│   ├── service_provider.py ✅
│   └── ...
├── examples/              # Example code
├── tests/                 # Test suite
├── pyproject.toml         ✅ Properly configured
├── LICENSE               ✅ MIT license
├── README.md             ✅ Documentation
├── MANIFEST.in           ✅ Include additional files
└── .gitignore            ✅ Clean repository
```

## Final Checklist

Before publishing:

- [ ] Update author information in `pyproject.toml`
- [ ] Choose unique package name
- [ ] Test package builds locally (`python -m build`)
- [ ] Test import works (`python -c "import di_container"`)
- [ ] Run test suite (`pytest tests/`)
- [ ] Create PyPI account and get API token
- [ ] Upload to test PyPI first
- [ ] Upload to production PyPI
- [ ] Create GitHub repository (optional)
- [ ] Set up automated releases (optional)

## Success! 🎉

Once published, users can install your package with:

```bash
pip install di-done-right
```

And use it like:

```python
from di_container import ServiceProvider, ServiceLifetime

# Your DI framework is now available to the Python community!
```

## Marketing Your Package

- Add topics/tags to your GitHub repo
- Write a blog post about your .NET-inspired DI framework
- Share on Python communities (Reddit r/Python, Python Discord, etc.)
- Consider adding to awesome-python lists
- Add badges to README (build status, PyPI version, downloads)

Your package is well-documented and production-ready! 🚀
