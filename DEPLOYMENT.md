# 🚀 Deployment Guide - Streamlit Community Cloud

This guide will help you deploy your Secure Hash Generator to Streamlit Community Cloud in just a few minutes!

## 📋 Prerequisites

1. **GitHub Account**: You need a GitHub account
2. **Git Repository**: Your code should be in a GitHub repository
3. **Python Files**: Ensure `main.py` and `requirements.txt` are in your repository

## 🎯 Quick Deployment Steps

### Step 1: Prepare Your Repository
Make sure your repository contains:
```
your-repo/
├── main.py              # Main Streamlit app
├── hasher.py            # Hashing functions
├── requirements.txt     # Dependencies
├── .streamlit/
│   └── config.toml     # Streamlit config
└── README.md           # Documentation
```

### Step 2: Deploy to Streamlit Cloud

1. **Visit Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Create New App**:
   - Click "New app"
   - Select your repository from the dropdown
   - Choose the branch (usually `main` or `master`)

3. **Configure App**:
   - **Main file path**: `main.py`
   - **App URL**: Choose a unique name for your app
   - Click "Deploy"

4. **Wait for Deployment**:
   - Streamlit will build and deploy your app
   - This usually takes 1-2 minutes
   - You'll see a success message when done

### Step 3: Access Your App
Your app will be live at:
```
https://your-app-name.streamlit.app
```

## 🔧 Configuration Options

### Custom Domain (Optional)
1. Go to your app settings in Streamlit Cloud
2. Click "Custom domain"
3. Enter your domain name
4. Update your DNS settings

### Environment Variables (If Needed)
1. In your app settings
2. Go to "Secrets"
3. Add any environment variables your app needs

## 🐛 Troubleshooting

### Common Issues

**App won't deploy:**
- Check that `main.py` exists in your repository root
- Verify `requirements.txt` is present and valid
- Ensure all imports in `main.py` are available

**App crashes on load:**
- Check the logs in Streamlit Cloud
- Verify all dependencies are in `requirements.txt`
- Test locally first with `streamlit run main.py`

**Styling issues:**
- Make sure custom CSS is properly formatted
- Check that all external resources are accessible

### Getting Help
- Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
- Visit Streamlit community: [discuss.streamlit.io](https://discuss.streamlit.io)
- Review your app logs in Streamlit Cloud dashboard

## 📈 Monitoring Your App

### View Analytics
- Go to your app in Streamlit Cloud
- Click "Analytics" to see usage statistics
- Monitor performance and user engagement

### Update Your App
1. Make changes to your code
2. Push to your GitHub repository
3. Streamlit Cloud will automatically redeploy

## 🎉 Success!

Your Secure Hash Generator is now live on the internet! Share the URL with others and start generating secure hashes.

---

**Need help?** Check the [Streamlit documentation](https://docs.streamlit.io) or ask in the [community forum](https://discuss.streamlit.io). 