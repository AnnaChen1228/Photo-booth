# Photo Booth Project 📸

A modern photo booth application that captures the essence of social media sharing while respecting privacy concerns.

## 🎯 Motivation

The project is inspired by several contemporary trends:
- 📱 Rising popularity of photo booth culture
- 🎬 Growing prominence of short-form videos
- 🌐 Widespread adoption of social media platforms
- 🔒 Increasing awareness of privacy concerns

## 📁 Project Structure

```
.
├── main.py                 # Main program that orchestrates the photo booth functionality
│                          # Latest update includes UI improvements and bug fixes
│
├── filter.py              # Contains various image filter implementations 
│                          # for photo enhancement
│
├── conbine_ffmpeg_new.py  # Handles video creation and combination 
│                          # using FFmpeg library
│
├── share_new.py           # Implements social media sharing capabilities
│
├── transVideo_new.py      # Manages video transitions and transformations
│
└── requirements.txt       # Project dependencies
```

## 📝 Requirements

### Python Version
- Recommended: Python 3.7 - 3.9
- Not recommended: Python 3.10+ (may have compatibility issues)

### Dependencies
```txt
opencv-python>=4.5.0
selenium>=4.0.0
webdriver-manager>=3.8.0
tk>=0.1.0
```

### System Requirements
- Python 3.7-3.9
- OpenCV
- FFmpeg
- Selenium
- Chrome Browser (for Selenium)
- Webcam access
- Internet connection (for sharing features)

## 🚀 Getting Started

1. Clone the repository

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## 🛠 Technical Implementation

The application is built using several powerful technologies:
- **OpenCV (CV2)**: For image capture and processing
- **FFmpeg**: For video manipulation and processing
- **Selenium**: For automated sharing capabilities
- **Tkinter**: For GUI implementation

## 🌟 Core Features

### 1. Capture & Filter
- Real-time photo capture
- Various filter options for image enhancement
- Custom image processing capabilities

### 2. Video Creation
- Combines multiple photos into video sequences
- Supports different video formats
- Custom transition effects

### 3. Social Sharing
- Direct integration with social platforms
- Privacy-focused sharing options
- Customizable sharing settings

## 🔐 Privacy
This project prioritizes user privacy and data protection, implementing secure handling of user content and sharing preferences.

## 👥 Contributors
- [AnnaChen1228](https://github.com/AnnaChen1228)

## 📅 Latest Updates
- Updated main.py with improved functionality
- Enhanced video combination features
- Improved sharing capabilities
- Added requirements.txt with specific version requirements

## ⚠️ Important Notes
- It's recommended to use a virtual environment to avoid package conflicts
- Make sure Chrome browser is installed for Selenium functionality
- Ensure webcam permissions are properly set
- Check that all system requirements are met before running
