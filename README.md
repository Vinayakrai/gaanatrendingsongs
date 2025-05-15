# gaanatrendingsongs

**gaanatrendingsongs** is a Python script that utilizes Selenium WebDriver to automate the process of playing trending songs on the [Gaana](https://gaana.com/) website. This tool is designed for music enthusiasts who wish to automatically play the latest trending tracks without manual intervention.

## 🎵 Features

- **Automated Playback**: Launches the Gaana website and plays trending songs automatically.
- **Web Automation**: Employs Selenium WebDriver for browser automation.
- **Customizable**: Easily adaptable to play different genres or playlists by modifying the script.

## 🛠️ Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Google Chrome**: The script is configured to work with the Chrome browser.
- **ChromeDriver**: Compatible version of ChromeDriver must be installed and added to your system's PATH.

## 📦 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Vinayakrai/gaanatrendingsongs.git
cd gaanatrendingsongs
```

2. **Install Required Packages**:

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install selenium
```

3. **Download ChromeDriver**:

- Find your Chrome browser version by navigating to `chrome://version/`.
- Download the corresponding ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Add the ChromeDriver executable to your system's PATH.

## 🚀 Usage

Run the script using Python:

```bash
python play_latest_songs.py
```

The script will:

1. Open a Chrome browser window.
2. Navigate to the Gaana website.
3. Automatically play the current trending songs.

## 🧩 Customization

To modify the playlist or target different songs:

- Open `play_latest_songs.py` in a text editor.
- Locate the section where the script identifies and interacts with the play button or playlist.
- Update the selectors or URLs to target your desired content.

## 🛡️ Disclaimer

This script is intended for educational and personal use only. Automating interactions with websites may violate their terms of service. Use responsibly and at your own risk.
