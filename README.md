# Rule-Based Cyber Incident Triage Assistant

## Project Overview

This project implements a lightweight, rule-based cybersecurity log analysis tool designed to assist analysts during the initial incident triage phase.

The system processes authentication log files, identifies suspicious behavioral patterns, assigns weighted risk scores, and generates prioritized investigation insights along with a risk score visualization.

This project is intended for academic demonstration purposes.

---

## Project Structure

```
sp301/
│
├── logs/
│   └── auth.log
├── output/              (can be empty before run)
├── src/
│   ├── main.py
│   ├── parser.py
│   └── detector.py
├── .gitignore
└── README.md
```
---

## Features

- Authentication log parsing
- Detection of multiple failed login attempts
- Detection of failures followed by successful login
- Detection of odd-hour login activity (00:00–05:00)
- Weighted risk scoring system
- Priority classification (LOW / MEDIUM / HIGH)
- Explainable rule-based output
- Risk score visualization (bar chart)

---

## System Architecture

```

Authentication Logs
↓
Log Parser
↓
Behavior Aggregation
↓
Rule-Based Scoring Engine
↓
Priority Mapping
↓
Console Report + Risk Score Graph

```

---

## Scoring Model

| Condition | Score |
|-----------|--------|
| ≥ 3 failed attempts | +1 |
| Failures followed by success | +2 |
| Login during unusual hours | +1 |

Priority Mapping:
- 1 → LOW
- 2 → MEDIUM
- ≥3 → HIGH

---

## Technology Stack

- Python
- re
- datetime
- collections
- matplotlib

---

## How to Run

From project root:

```
python src/main.py
```

Outputs:
- Console triage report
- Risk score graph saved in `output/` directory

---

## Limitations

- Works on static log files
- Rule-based detection (no machine learning)
- May generate false positives
- No real-time monitoring
- Designed for academic demonstration

---

## Future Scope

- Time-window based correlation
- Real-time log ingestion
- Integration with SIEM platforms
- Advanced anomaly detection techniques

---
