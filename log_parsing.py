import re
import json # Used for pretty printing the output

def parse_log_file(file_path):
    """
    Parses a log file using a regex pattern and returns a list of dictionaries.
    """
    # Regex to capture timestamp, log level, source, and message
    log_pattern = re.compile(
        r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+' # Timestamp
        r'([A-Z]+)\s+'                                  # Log Level
        r'\[(.*?)\]\s+-\s+'                              # Source
        r'(.*)$'                                        # Message
    )

    parsed_logs = []
    print(f"Attempting to read log file: {file_path}")

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                match = log_pattern.match(line)
                if match:
                    # Extract data from the capture groups
                    timestamp, log_level, source, message = match.groups()
                    
                    log_entry = {
                        'timestamp': timestamp,
                        'level': log_level,
                        'source': source,
                        'message': message.strip()
                    }
                    parsed_logs.append(log_entry)
                else:
                    print(f"Skipping malformed line: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    return parsed_logs

# --- Main execution ---
if __name__ == "__main__":
    # Create a dummy log file for the example
    log_data = """2025-09-10 11:30:15,255 INFO [main] - Application starting up...
2025-09-10 11:30:16,301 DEBUG [database] - Establishing database connection.
2025-09-10 11:30:17,450 WARNING [auth] - Failed login attempt for user: guest
This is a malformed line and should be skipped.
2025-09-10 11:30:18,102 ERROR [main] - Critical error occurred: service unavailable.
"""
    with open("app.log", "w") as f:
        f.write(log_data)

    # Parse the log file
    parsed_data = parse_log_file('app.log')

    if parsed_data:
        # Pretty print the structured data
        print("\n--- Parsed Log Data ---")
        print(json.dumps(parsed_data, indent=4))