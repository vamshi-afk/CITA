from collections import defaultdict


def analyze_events(events):

    ip_data = defaultdict(
        lambda: {"fail_count": 0, "success": False, "odd_hour_success": False}
    )

    # Collect behavior per IP
    for e in events:
        ip = e["ip"]

        if e["status"] == "FAIL":
            ip_data[ip]["fail_count"] += 1

        elif e["status"] == "SUCCESS":
            ip_data[ip]["success"] = True

            # Check for odd-hour login
            if 0 <= e["timestamp"].hour <= 5:
                ip_data[ip]["odd_hour_success"] = True

    results = []

    # Scoring phase
    for ip, data in ip_data.items():
        score = 0
        reasons = []

        # Rule 1: Multiple failures
        if data["fail_count"] >= 3:
            score += 1
            reasons.append("Multiple failed login attempts")

        # Rule 2: Success after failures
        if data["fail_count"] >= 3 and data["success"]:
            score += 2
            reasons.append("Failures followed by successful login")

        # Rule 3: Odd-hour login
        if data["odd_hour_success"]:
            score += 1
            reasons.append("Login during unusual hours (00:00–05:00)")

        # Ignore IPs with no suspicious behavior
        if score == 0:
            continue

        # Map score to priority
        if score >= 3:
            priority = "HIGH"
        elif score == 2:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        results.append(
            {
                "ip": ip,
                "fail_count": data["fail_count"],
                "success": data["success"],
                "odd_hour": data["odd_hour_success"],
                "score": score,
                "priority": priority,
                "reasons": reasons,
            }
        )

    return results
