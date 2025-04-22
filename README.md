# Python Ad Blocker

A simple ad blocker implementation that works by modifying the system's hosts file to block common advertising domains.

## Features

- Blocks common advertising domains
- Creates automatic backups of the hosts file before modifications
- Cross-platform support (Windows and Unix-based systems)
- Option to enable/disable ad blocking

## Requirements

- Python 3.x
- Administrative privileges (required to modify hosts file)

## Usage

1. Run the script with administrative privileges:
   - Windows: Run Command Prompt as Administrator
   - Linux/Mac: Use sudo

```bash
# Windows (in Admin Command Prompt)
python adblocker.py

# Linux/Mac
sudo python3 adblocker.py
```

2. Choose from the available options:
   - 1: Enable ad blocking
   - 2: Disable ad blocking
   - 3: Exit

## Important Notes

- This is a basic implementation for educational purposes
- Backup files are created automatically before any modifications
- The script requires administrative privileges to modify the hosts file
- Some changes might require a browser restart to take effect

## Disclaimer

This is a simple implementation and might not block all advertisements. For more comprehensive ad blocking, consider using established browser extensions or network-level solutions.