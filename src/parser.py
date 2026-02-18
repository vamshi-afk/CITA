import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r"(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+).*"
    r"(?P<status>Failed|Accepted) password for (?P<user>\w+) from (?P<ip>[\d\.]+)"
)


def parse_line(line):
    match = LOG_PATTERN.search(line)
    if not match:
        return None

    data = match.groupdict()

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
