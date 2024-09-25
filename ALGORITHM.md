# Algorithm Explanation

This document explains the algorithm used in the `archive-file-finder.py` script. The script is designed to search for archive files in a specified directory and either send the results to a Telegram bot or display them in the terminal based on the provided options.

## Algorithm Steps

1. **Importing Modules:**
   - The script begins by importing necessary modules:
     - `os`: For file and directory operations.
     - `requests`: For sending HTTP requests to the Telegram API.
     - `sys`: For handling command-line arguments.
     - `datetime`: For generating timestamps.

2. **Configuration Variables:**
   - The script sets up several configuration variables:
     - `telegram_bot_token`: The token for the Telegram bot.
     - `telegram_chat_id`: The chat ID where messages will be sent.
     - `telegram_api_url`: The API endpoint for sending messages to the Telegram bot.
     - `target_directory`: The directory path to be searched for archive files.
     - `archive_extensions`: A list of file extensions for archive files (`.zip`, `.tar`, `.gz`, `.bz2`, `.7z`, `.rar`, `.xz`).
     - `send_to_telegram`: A boolean flag, set to `True` by default, indicating whether to send results to Telegram.

3. **Handling Command-Line Arguments:**
   - The script checks for command-line arguments:
     - If `-x` is provided, the `send_to_telegram` flag is set to `False` so that results are displayed in the terminal instead of being sent to Telegram.
     - If `--help` is provided, the script prints a help message explaining usage and options, then exits.

4. **Function Definitions:**
   - **`print_help()`:**
     - Prints a help message that describes the script's usage and options.
   - **`send_telegram_message(message)`:**
     - Sends the provided `message` to the specified Telegram chat using the `telegram_api_url`.
     - If `send_to_telegram` is `False`, the message is printed to the terminal instead.
   - **`find_archive_files(directory)`:**
     - Recursively searches the specified `directory` for files with extensions listed in `archive_extensions`.
     - Returns a list of file paths for all found archive files.
   - **`send_long_message_by_lines(lines, header, max_lines=10)`:**
     - Sends the search results in chunks, each containing up to `max_lines` lines.
     - The first message includes a `header` with the timestamp and the first set of results.
     - Subsequent messages contain the remaining lines in chunks of `max_lines` each.

5. **Main Execution:**
   - The script records the current timestamp using `datetime.now()` to generate a timestamp for the results.
   - It calls the `find_archive_files(target_directory)` function to search for archive files in the specified directory.
   - If archive files are found:
     - The script sends the results to Telegram or prints them in chunks of 10 lines, starting with a message that includes the timestamp.
   - If no archive files are found:
     - A message indicating that no archive files were found is sent or printed.

6. **Output Control:**
   - If the `-x` option is used, all messages are printed to the terminal instead of being sent to Telegram.
   - If there are more than 10 lines of results, they are sent in separate messages until all lines have been processed.

## Flow of the Algorithm
1. **Initialization**: Import modules and set configuration variables.
2. **Argument Handling**: Check for `-x` or `--help` arguments.
3. **Search Execution**: Call `find_archive_files()` to search the target directory.
4. **Message Sending**: Send or print results based on `send_to_telegram` flag.
5. **Completion**: End the script after processing all results.

This algorithm ensures flexible behavior, allowing the user to choose between sending results to Telegram or displaying them in the terminal, and provides clear guidance with a help option.
