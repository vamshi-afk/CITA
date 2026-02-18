import os
import matplotlib.pyplot as plt
from parser import parse_file
from detector import analyze_events

LOG_FILE = "logs/auth.log"
OUTPUT_DIR = "output"
GRAPH_PATH = os.path.join(OUTPUT_DIR, "risk_scores.png")


def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Parse logs
    events = parse_file(LOG_FILE)

    print("\nParsed Events:\n")
    for e in events:
        print(f"{e['timestamp']} | {e['user']} | {e['ip']} | {e['status']}")

    # Run triage analysis
    analysis = analyze_events(events)

    print("\n" + "=" * 60)
    print("TRIAGE ANALYSIS REPORT")
    print("=" * 60)

    for item in analysis:
        print(f"\nIP Address: {item['ip']}")
        print(f"Risk Score: {item['score']}")
        print(f"Priority Level: {item['priority']}")
        print("Triggered Rules:")

        for r in item["reasons"]:
            print(f"  - {r}")

    print("\n" + "=" * 60)
    print("End of Report")
    print("=" * 60)

    # Visualization: Risk Score per IP
    ips = [item["ip"] for item in analysis]
    scores = [item["score"] for item in analysis]

    if ips:
        plt.figure(figsize=(8, 5))

        bars = plt.bar(ips, scores)

        plt.xlabel("IP Address")
        plt.ylabel("Risk Score")
        plt.title("Risk Score per IP")
        plt.xticks(rotation=45)

        max_score = max(scores)
        plt.ylim(0, max_score + 1)

        # Add score values above bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.1,
                f"{scores[i]}",
                ha="center",
            )

        plt.tight_layout()
        plt.savefig(GRAPH_PATH, dpi=300)
        print(f"\nGraph saved to {GRAPH_PATH}")

    else:
        print("\nNo suspicious activity detected. No graph generated.")


if __name__ == "__main__":
    main()
