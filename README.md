# Google Drive Bulk Downloader

This script automates the process of creating direct download links from a list of Google Drive file URLs and then uses Selenium to download them automatically.
Used this to download Student's Assignenments (IPYNB/PDF)

## Features
- Parses a text file containing Google Drive links.
- Generates direct download links.
- Automates file downloads using Selenium and Chrome WebDriver.

## Install Dependencies
```
pip install selenium webdriver_manager
```
## Configurable Options
1. **File Links:** Create a text file named `links.txt` in the same directory as the script.
2. **Chrome User Data Directory:** This is the directory where Chrome stores user data. You can change this directory by modifying the following line in the script
  ```
  chrome_options.add_argument("user-data-dir=C:/Users/YourWindowsUserName/AppData/Local/Google/Chrome/User Data")
  ```
3. **Chrome Profile Directory:** I use GSuite as a different profile on Chrome, to make sure that's what we're using, configure accordingly
  ```
  chrome_options.add_argument("--profile-directory=Profile 1")
  ```
4. **Download Delay:** Modify According to your internet speed, pc config. `default=3`
