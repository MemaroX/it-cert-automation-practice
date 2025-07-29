import re

def parse_log_entry(log_entry):
    """Parses a single log entry and extracts relevant information."""
    # Example log format: [TIMESTAMP] [LEVEL] MESSAGE
    match = re.match(r"[(.*?)] [(.*?)] (.*)", log_entry)
    if match:
        timestamp, level, message = match.groups()
        return {'timestamp': timestamp, 'level': level, 'message': message}
    return None

def analyze_log_file(filepath):
    """Reads a log file, parses each entry, and prints a summary."""
    error_count = 0
    with open(filepath, 'r') as f:
        for line in f:
            parsed_entry = parse_log_entry(line.strip())
            if parsed_entry:
                print(f"Timestamp: {parsed_entry['timestamp']}, Level: {parsed_entry['level']}, Message: {parsed_entry['message']}")
                if parsed_entry['level'].upper() == 'ERROR':
                    error_count += 1
            else:
                print(f"Could not parse: {line.strip()}")
    print(f"\nTotal errors found: {error_count}")

if __name__ == "__main__":
    # Create a dummy log file for testing
    dummy_log_content = """
[2023-07-28 10:00:00] INFO User logged in
[2023-07-28 10:01:05] WARNING Disk space low
[2023-07-28 10:02:10] ERROR Failed to connect to database
[2023-07-28 10:03:15] INFO Data processed
[2023-07-28 10:04:20] ERROR File not found
"""
    with open("dummy.log", "w") as f:
        f.write(dummy_log_content)

    print("Analyzing dummy.log...")
    analyze_log_file("dummy.log")
