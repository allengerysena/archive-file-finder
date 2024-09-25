# Archive File Finder

This Python script is used to search for archive files (such as `.zip`, `.tar`, `.gz`, etc.) in a specified directory recursively. The search results can be sent to a Telegram bot or displayed in the terminal based on the chosen option.

## Features
- Recursively searches for archive files in a specified directory.
- Sends search results to a Telegram bot or displays them in the terminal.
- Option to display the results directly in the terminal without sending to Telegram.
- Provides help information with the `--help` option.

## Requirements
- Python 3.x
- `requests` package to send messages to Telegram.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/allengerysena/archive-file-finder.git
    ```
2. Navigate to the project directory:
    ```bash
    cd archive-file-finder
    ```
3. Install the dependencies:
    ```bash
    pip install requests
    ```

## Send Results to Telegram
Send the search results of archive files to the configured Telegram bot.
```bash
python3 archive-file-finder.py
```

## Display Results in the Terminal Only
Use the `-x` option to display the results in the terminal without sending them to Telegram.
```bash
python3 archive-file-finder.py -x
```

## Display Help
To view the usage information, use the `--help` option.
```bash
python3 archive-file-finder.py --help
```
