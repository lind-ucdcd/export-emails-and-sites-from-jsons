# JSON Email & Website Extractor

This Python app is designed to extract emails and websites from JSON files exported from Telegram groups. It scans through multiple JSON files, pulls out unique emails and websites, and saves them into text files. The app is ideal for those who need to gather and analyze data across multiple files.

## Key Features

- Extract emails and websites from JSON files.
- Handles multiple JSON files at once.
- Ensures no duplicate emails or websites in the output.
- Supports domain filtering for websites (.ca, .com, .org, .co, .net).
- Simple command-line interface for easy use.

## How It Works

1. Place all JSON files in a folder.
2. Run the Python script to extract emails and websites from all files.
3. The output will be saved into two text files: `all_unique_emails.txt` and `all_unique_websites.txt`, ensuring no duplicates.

## Setup

### Prerequisites

- Python 3.x
- Basic understanding of command-line interface

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/repo-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd repo-name
    ```

3. Make sure all JSON files are in the `json_directory` folder, and update the `json_directory` variable in the script.

4. Run the script:
    ```bash
    python3 find_emails_websites.py
    ```

## Output

- `all_unique_emails.txt`: Contains all unique emails from the JSON files.
- `all_unique_websites.txt`: Contains all unique websites matching the criteria.

## Author

This project was created and is maintained by **Mehdi Azizi**. Feel free to reach out if you have any questions or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
