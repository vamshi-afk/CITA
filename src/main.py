from parser import parse_file

LOG_FILE = "../logs/auth.log"


def main():
    events = parse_file(LOG_FILE)

    print("\nParsed Events:\n")
    for e in events:
        print(f"{e['timestamp']} | {e['user']} | {e['ip']} | {e['status']}")


if __name__ == "__main__":
    main()
