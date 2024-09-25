import os
import requests
import sys
from datetime import datetime

telegram_bot_token = 'xxxxx'
telegram_chat_id = 'xxxxx'
telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"

target_directory = "/home/user/"
archive_extensions = [".zip", ".tar", ".gz", ".bz2", ".7z", ".rar", ".xz"]
send_to_telegram = True

def print_help():
    help_message = """
Usage: python3 archive-file-finder.py [OPTIONS]

Options:
  -x          Display the output in the terminal instead of sending to Telegram.
  --help      Show this help message and exit.

Example:
  python3 archive-file-finder.py       # Send results to Telegram
  python3 archive-file-finder.py -x    # Display results in the terminal only
"""
    print(help_message)

if len(sys.argv) > 1:
    if sys.argv[1] == '-x':
        send_to_telegram = False
    elif sys.argv[1] == '--help':
        print_help()
        sys.exit(0)

def send_telegram_message(message):
    if send_to_telegram:
        try:
            payload = {
                'chat_id': telegram_chat_id,
                'text': message
            }
            response = requests.post(telegram_api_url, data=payload)
            if response.status_code == 200:
                print(f"Message sent to Telegram successfully.")
            else:
                print(f"Failed to send message: {response.text}")
        except Exception as e:
            print(f"Error sending message to Telegram: {e}")
    else:
        print(message)

def find_archive_files(directory):
    result_message = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in archive_extensions):
                file_path = os.path.join(root, file)
                result_message.append(file_path)
    return result_message

def send_long_message_by_lines(lines, header, max_lines=10):
    if len(lines) <= max_lines:
        send_telegram_message(f"{header}\n" + "\n".join(lines))
    else:
        send_telegram_message(f"{header}\n" + "\n".join(lines[:max_lines]))
        for i in range(max_lines, len(lines), max_lines):
            message = "\n".join(lines[i:i+max_lines])
            send_telegram_message(message)

if __name__ == "__main__":
    run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archive_files = find_archive_files(target_directory)
    header = f"{run_time}\n"
    if archive_files:
        send_long_message_by_lines(archive_files, header)
    else:
        send_telegram_message(f"No archive files found in {target_directory} at {run_time}.")
