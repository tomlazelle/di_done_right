# GitHub Environment Setup for PyPI Publishing

## What Is a GitHub Environment?

A GitHub environment is a **security layer** that protects your PyPI publishing workflow. It adds:

- ✅ Manual approval before publishing
- ✅ Restricted access (only certain people can approve)
- ✅ Separate secrets for production
- ✅ Audit trail of who published what

## Why You Need It

**Scenario without environment protection:**
```
Developer A commits code → Pushes to main → Creates release
   ↓
Workflow automatically publishes to PyPI (NO APPROVAL NEEDED)
   ↓
If code was malicious or buggy, it's already on PyPI!
```

**With environment protection:**
```
Developer A commits code → Pushes to main → Creates release
   ↓
Workflow starts → PAUSES and asks for approval
   ↓
You review the code → Approve if safe
   ↓
Workflow publishes to PyPI
```

## Step-by-Step Setup

### 1. Create PyPI Account and Get Token

**First time on PyPI:**
1. Go to https://pypi.org/account/register/
2. Verify your email
3. Enable 2FA (required for publishing)

**Get API Token:**
1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: `di-done-right-github-actions`
4. Scope: "Entire account" (for first publish) or "Project: di-done-right" (after first publish)
5. **COPY THE TOKEN** (starts with `pypi-AgEI...`) - you'll only see it once!

### 2. Push Code to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Production-ready DI framework"

# Create GitHub repository first, then:
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/di-done-right.git
git push -u origin main
```

### 3. Create GitHub Environment

**In your GitHub repository:**

1. Click **Settings** (top menu)
2. Click **Environments** (left sidebar, under "Code and automation")
3. Click **New environment** button
4. Enter environment name: `pypi-publish`
5. Click **Configure environment**

### 4. Add Protection Rules (RECOMMENDED)

**Require manual approval:**
- Check ☑️ "Required reviewers"
- Click "Add reviewers"
- Add yourself (or trusted maintainers)
- Set "Maximum of reviewers required": 1
- Now every publish will wait for your approval

**Restrict to main branch only:**
- Under "Deployment branches", select "Selected branches"
- Click "Add deployment branch rule"
- Enter: `main`
- This prevents accidental publishes from feature branches

**Optional - Wait timer:**
- Set "Wait timer": 5 (minutes)
- Gives you 5 minutes to cancel if needed

### 5. Add PyPI Token to Environment

**In the environment you just created:**

1. Scroll to **Environment secrets** section
2. Click **Add secret**
3. Name: `PYPI_API_TOKEN`
4. Value: Paste your PyPI token (the `pypi-AgEI...` string)
5. Click **Add secret**

✅ The token is now only available to workflows using the `pypi-publish` environment

### 6. Verify Workflow Configuration

Your workflow file (`.github/workflows/test-and-publish.yml`) should have:

```yaml
publish:
  needs: test
  runs-on: ubuntu-latest
  if: github.event_name == 'release' && github.event.action == 'published'
  environment:
    name: pypi-publish  # ← This links to the environment
    url: https://pypi.org/project/di-done-right/
```

✅ This is already configured in your workflow!

## How It Works

### Publishing Flow:

1. **You create a release on GitHub:**
   - Go to repository → Releases → Create new release
   - Tag: `v1.0.0`
   - Title: `v1.0.0 - Initial Release`
   - Click "Publish release"

2. **Workflow starts:**
   - Runs all tests ✅
   - Builds the package ✅
   - **PAUSES at publish step** ⏸️

3. **You get notified:**
   - GitHub sends you an email/notification
   - "Waiting for approval from reviewers"

4. **You review and approve:**
   - Go to Actions → Click the workflow run
   - Click "Review deployments"
   - Check the box next to `pypi-publish`
   - Click "Approve and deploy"

5. **Workflow completes:**
   - Publishes to PyPI ✅
   - Your package is live! 🎉

## Alternative: No Environment (Less Secure)

If you **don't** want the approval step (not recommended for public packages):

1. Don't create an environment
2. Add `PYPI_API_TOKEN` directly to repository secrets:
   - Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your token

**But this means:**
- ❌ No approval required
- ❌ Anyone with write access can publish
- ❌ Publishes happen automatically on release

## Recommended: Use TestPyPI First

**Before publishing to production PyPI:**

1. Create account at https://test.pypi.org/account/register/
2. Get token from test PyPI
3. Create second environment: `testpypi-publish`
4. Add test token as secret
5. Test your release process there first

Add to workflow:
```yaml
- name: Publish to Test PyPI
  env:
    TWINE_USERNAME: __token__
    TWINE_PASSWORD: ${{ secrets.TEST_PYPI_API_TOKEN }}
  run: twine upload --repository testpypi dist/*
```

## Security Best Practices

✅ **DO:**
- Use environment protection for production
- Require approval from trusted maintainers
- Use project-scoped tokens (after first publish)
- Enable 2FA on PyPI account
- Review code before approving deployments

❌ **DON'T:**
- Put tokens directly in workflow files
- Share tokens with others
- Use the same token for multiple projects
- Skip the approval step for public packages

## Troubleshooting

### "Environment not found"
**Solution:** Make sure the environment name matches exactly:
- Workflow: `environment: name: pypi-publish`
- GitHub: Settings → Environments → `pypi-publish`

### "Secret not found"
**Solution:** Check the secret is in the environment, not repository:
- ✅ Settings → Environments → pypi-publish → Environment secrets
- ❌ Settings → Secrets and variables → Actions (repository secrets)

### "Deployment waiting"
**Normal!** This means approval is required. Go to:
- Actions → Click the workflow run → Review deployments → Approve

### "403 Forbidden when publishing"
**Solutions:**
1. Token might be expired - generate a new one
2. Package name might be taken - check PyPI.org
3. First publish needs "Entire account" scope token
4. Subsequent publishes can use project-scoped token

## Summary

**What you need to do:**

1. ✅ Get PyPI token from pypi.org
2. ✅ Push code to GitHub
3. ✅ Create `pypi-publish` environment in repository settings
4. ✅ Add reviewers (yourself)
5. ✅ Add `PYPI_API_TOKEN` secret to environment
6. ✅ Create a release
7. ✅ Approve the deployment when prompted
8. 🎉 Your package is published!

The environment setup adds **one approval step** but significantly improves security for your PyPI package.