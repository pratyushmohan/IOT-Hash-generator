# 🔐 Secure Hash Generator

A modern, beautiful Streamlit application for generating SHA-256 hashes and managing passwords securely. Built with Python and Streamlit, this tool provides an enterprise-grade interface for cryptographic operations with a stunning UI.

## 🚀 Features

### 🔍 Hash Generator
- **SHA-256 Hashing**: Generate secure SHA-256 hashes from any text input
- **Salt Support**: Add random salt for enhanced security
- **Real-time Processing**: Instant hash generation with loading animations
- **Hash Information**: Display hash length, algorithm, and bit length
- **Quick Hash**: Pre-defined options for common inputs

### 🔑 Password Manager
- **Secure Storage**: Store password hashes in session state
- **Password Verification**: Verify passwords against stored hashes
- **Password Strength**: Visual indicators and security metrics
- **Hash Display**: View and analyze stored password hashes

### 🎨 Modern UI/UX
- **Responsive Design**: W[DEPLOYMENT.md](DEPLOYMENT.md)orks perfectly on all devices
- **Beautiful Interface**: Gradient backgrounds and modern styling
- **Tab Navigation**: Organized sections for different features
- **Visual Feedback**: Success/error messages with animations
- **Dark/Light Theme**: Automatic theme adaptation

## 🛠️ Technologies Used

- **Backend**: Python 3.8+
- **Framework**: Streamlit 1.28.0+
- **Styling**: Custom CSS with gradients and animations
- **Hashing**: SHA-256 cryptographic algorithm
- **Icons**: Streamlit native icons and emojis

## 📁 Project Structure

```
pythonProject5_Hashing/
├── main.py                 # Main Streamlit application
├── hasher.py              # Hashing utility functions
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── README.md             # This file
├── index.html            # Legacy web version
├── styles.css            # Legacy CSS
├── script.js             # Legacy JavaScript
└── notes.txt             # Project notes
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Installation
1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```
4. Open your browser and navigate to `http://localhost:8501`

### Streamlit Community Cloud Deployment

1. **Prepare your repository**:
   - Ensure all files are committed to your Git repository
   - Make sure `main.py` is in the root directory
   - Verify `requirements.txt` is present

2. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository and branch
   - Set the main file path to `main.py`
   - Click "Deploy"

3. **Your app will be live** at: `https://your-app-name.streamlit.app`

## 📖 Usage

### Hash Generator
1. Navigate to the "Hash Generator" tab
2. Enter your text in the text area
3. Choose options (add salt, hex format)
4. Click "Generate Hash" to create a SHA-256 hash
5. View hash information and copy the result

### Password Manager
1. Go to the "Password Manager" tab
2. **Set Password**:
   - Enter and confirm your password
   - Click "Store Password Hash"
3. **Verify Password**:
   - Enter the password to verify
   - Click "Verify Password" to check

## 🔒 Security Features

- **SHA-256 Algorithm**: Industry-standard cryptographic hashing
- **Client-side Processing**: All operations happen locally
- **No Data Transmission**: Your data never leaves your device
- **Secure Storage**: Passwords stored as hashes only
- **Salt Support**: Optional random salt for enhanced security
- **Session-based Storage**: Temporary storage during session

## 🎨 UI/UX Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Modern Interface**: Beautiful gradients and smooth animations
- **Tab Navigation**: Clean organization of features
- **Visual Feedback**: Clear success/error messages
- **Loading States**: Smooth user experience with spinners
- **Accessibility**: Proper labels and keyboard navigation

## 🔧 Customization

The application is highly customizable:

- **Styling**: Modify the CSS in `main.py` for custom themes
- **Functionality**: Extend the hashing functions in `hasher.py`
- **Configuration**: Adjust settings in `.streamlit/config.toml`
- **Features**: Add new tabs and functionality easily

## 📝 Configuration

### Streamlit Config (`.streamlit/config.toml`)
- Custom theme colors
- Server settings for deployment
- Browser configuration

### Requirements (`requirements.txt`)
- Streamlit framework
- Python standard libraries

## 🚀 Deployment Options

### Streamlit Community Cloud (Recommended)
- Free hosting
- Automatic deployments
- Custom domains
- Easy setup

### Local Development
- Run locally for testing
- Full control over environment
- Debug capabilities

### Other Platforms
- Heroku
- AWS
- Google Cloud
- Any platform supporting Python

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with `streamlit run main.py`
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- SHA-256 algorithm implementation
- Modern web design principles
- Open source community

---

**Built with ❤️ using Streamlit and SHA-256 hashing**

🔐 Secure • 🚀 Fast • 🎨 Beautiful • ☁️ Cloud-Ready 