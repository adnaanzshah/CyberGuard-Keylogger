# Key Logger

This is a simple keylogger application developed using Python. It logs keystrokes and mouse actions and sends the log files via email at regular intervals.

## Project Structure

- `Python_scripts/`
  - `key_logger.py`: Captures keystrokes.
  - `mouse_logger.py`: Captures mouse actions.
- `key_log.txt`: Logs keystrokes.
- `m_log.txt`: Logs mouse actions.
- `run.py`: Main script that runs the loggers and sends email.

## How It Works

1. **Run the Application:**
   - The `run.py` script executes the keylogger and mouse logger scripts.
   - It sends the log files via email every hour (or as configured).

2. **Setup:**
   - Update the `run.py` script with your email credentials and recipient details.

## Requirements

- Python 3.x
- Required Python libraries (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adnaanzshah/Key_logger.git
