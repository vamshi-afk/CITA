import re
from datetime import datetime

# Regex pattern to extract key fields from auth log lines
LOG_PATTERN = re.compile(
    r"(?P<month>\w+)\s+"
    r"(?P<day>\d+)\s+"
    r"(?P<time>\d+:\d+:\d+).*"
    r"(?P<status>Failed|Accepted) password for "
    r"(?P<user>\w+) from "
    r"(?P<ip>[\d\.]+)"
)


def parse_line(line):

    match = LOG_PATTERN.search(line)
    if not match:
        return None

    data = match.groupdict()

    # Construct datetime object (year defaults to 1900)
    timestamp_str = f"{data['month']} {data['day']} {data['time']}"
    timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")

    return {
        "timestamp": timestamp,
        "user": data["user"],
        "ip": data["ip"],
        "status": "FAIL" if data["status"] == "Failed" else "SUCCESS",
    }


def parse_file(filepath):

    events = []

    with open(filepath, "r") as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                events.append(parsed)

    return events
