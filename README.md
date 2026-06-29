# SOC Flight Recorder

SOC Flight Recorder is an early proof of concept for recording, replaying, and auditing AI-assisted Security Operations Center decisions.

This project explores a simple idea: as AI agents become more involved in security operations, teams will need a clear record of what the agent saw, what it decided, which policy checks were applied, and whether a response action was allowed or required human approval.

## Why This Exists

Many security teams are starting to use generative AI for SOC workflows such as alert triage, investigation summaries, recommended response actions, and automated remediation.

That creates a new governance problem.

It is not enough to know that an action happened. Security teams also need to know why it happened, what evidence supported it, and whether the action followed policy.

SOC Flight Recorder is a small POC for that missing audit layer.

## What This POC Does

The current script:

- Creates a mock SOC case.
- Receives a sample security alert.
- Performs a simple investigation based on alert severity.
- Recommends a response action.
- Checks whether that action is allowed by policy.
- Records each step in a timeline.
- Prints the final case timeline for review.

## Example Flow

```text
Start SOC Case
   |
   v
Receive Alert
   |
   v
Investigate Alert
   |
   v
Recommend Action
   |
   v
Check Policy
   |
   +--> Allowed: execute action
   |
   +--> Restricted: require human approval
   |
   v
Record Timeline
   |
   v
Print Case Summary
```

## Current Status

This project is intentionally in its infancy.

It is a learning-oriented proof of concept, not a production security tool.

The script does not yet:

- Connect to a real SIEM, EDR, identity provider, ticketing system, or SOAR platform.
- Use a real AI model or agent framework.
- Store records in a database.
- Create tamper-evident logs.
- Enforce real access control.
- Execute real security response actions.
- Provide a user interface.

## How To Run

Run the script with Python:

```bash
python soc_flight_recorder.py
```

If your system uses the Python launcher:

```bash
py soc_flight_recorder.py
```

## Example Output

```text
SOC Flight Recorder Case: 498bb6d5-f33e-4a39-984b-0df6f757e28e

[2026-06-29T21:44:01.425870+00:00] case_created
  {'case_id': '498bb6d5-f33e-4a39-984b-0df6f757e28e'}

[2026-06-29T21:44:01.425870+00:00] alert_received
  {'source': 'identity_provider', 'title': 'Impossible travel login detected', 'severity': 'high', 'user': 'alex@example.com'}

[2026-06-29T21:44:01.425870+00:00] investigation_completed
  {'hypothesis': 'Potential account compromise', 'recommended_action': 'disable_user'}

[2026-06-29T21:44:01.425870+00:00] policy_checked
  {'allowed': False, 'reason': 'Action requires human approval before execution.'}

[2026-06-29T21:44:01.425870+00:00] final_action
  {'status': 'approval_required', 'action': 'disable_user'}
```

## Future Ideas

Possible next steps:

- Add JSON output.
- Load sample alerts from a file.
- Add configurable policy rules.
- Store case timelines in SQLite.
- Add cryptographic signing for event records.
- Build a simple web dashboard.
- Export timelines to a SIEM or data lake.
- Add approval workflows for restricted actions.
- Add support for multiple mock AI agents.

## Project Goal

The long-term concept is a decision-governance layer for autonomous or AI-assisted SOC workflows.

In short:

> Logs show what happened. SOC Flight Recorder shows why an AI-assisted security decision happened and whether it was allowed.
