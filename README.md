# **CyberGuard Keylogger**

**CyberGuard Keylogger** is a comprehensive Python application designed for monitoring keystrokes and mouse actions. It efficiently captures and logs user activity, sending the logs via email at specified intervals. Ideal for cybersecurity enthusiasts and developers, this tool provides a practical approach to understanding keylogging and data monitoring.


## **Features**

- **Keystroke Logging:** Captures all keyboard inputs.
- **Mouse Activity Logging:** Records mouse movements and clicks.
- **Automated Email Reports:** Sends log files to your email at regular intervals.
- **Startup Integration:** Configurable to start automatically with your computer.

## **Project Structure**

- **`Python_scripts/`**
  - `key_logger.py`: Script to capture keystrokes.
  - `mouse_logger.py`: Script to capture mouse actions.
- **`key_log.txt`**: File storing keystroke logs.
- **`m_log.txt`**: File storing mouse activity logs.
- **`run.py`**: Main script that initiates logging and handles email notifications.

## **How It Works**

1. **Run the Application:**
   - Execute `run.py` to start both the keylogger and mouse logger.
   - Logs are collected and sent via email based on your configuration.

2. **Setup Instructions:**
   - Update the `run.py` script with your email credentials and recipient details.
   - Add the script to your startup applications to ensure it runs automatically on system boot.

## **Adding to Startup Apps**

To have CyberGuard Keylogger start automatically with your computer:

1. **Create a Shortcut:**
   - Create a shortcut to `run.py` in your Startup folder.

2. **Locate Startup Folder:**
   - For Windows, the Startup folder path is: 
     ```
     C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
     ```

3. **Add Shortcut:**
   - Drag and drop the shortcut into the Startup folder.

## **Requirements**

- **Python 3.x**
- **Python Libraries:** Listed in `requirements.txt`

## **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/adnaanzshah/CyberGuard-Keylogger.git
