"""
SOC Flight Recorder - Early Proof of Concept

Purpose
-------
This script is a very early proof of concept for a "SOC Flight Recorder":
an audit trail for AI-assisted or autonomous Security Operations Center
workflows.

The idea is inspired by an aircraft flight recorder. When an AI security
agent receives an alert, investigates it, recommends an action, checks policy,
and either executes or pauses for approval, every meaningful step should be
recorded in a clear timeline.

Why This Exists
---------------
Many new cybersecurity products are using generative AI to triage alerts,
summarize incidents, and recommend response actions. As these tools become
more autonomous, security teams will need a trustworthy way to answer:

- What did the AI agent see?
- What did it decide?
- What evidence or rule drove that decision?
- Was the action allowed by policy?
- Did the agent act, or did it require human approval?
- Can the organization replay the full decision path later?

This POC demonstrates the smallest possible version of that concept.

Current Scope
-------------
This script currently:

1. Creates a mock SOC case.
2. Receives a hard-coded security alert.
3. Performs a simple investigation based on alert severity.
4. Recommends a response action.
5. Checks whether that action is allowed by policy.
6. Records each step into a timeline.
7. Prints the timeline for review.

Important POC Limitations
-------------------------
This is intentionally simple and still in its infancy. It does not yet:

- Connect to real SIEM, EDR, identity, ticketing, or SOAR tools.
- Use a real AI model or agent framework.
- Store events in a database or tamper-evident ledger.
- Authenticate users or enforce real authorization.
- Support real approvals, notifications, or response execution.
- Perform real security analysis.

Flow Chart
----------

    +-------------------+
    | Start SOC Case    |
    +---------+---------+
              |
              v
    +-------------------+
    | Receive Alert     |
    +---------+---------+
              |
              v
    +-------------------+
    | Investigate Alert |
    +---------+---------+
              |
              v
    +----------------------+
    | Recommend Action     |
    +----------+-----------+
               |
               v
    +----------------------+
    | Check Policy         |
    +----------+-----------+
               |
        +------+------+
        |             |
        v             v
 +--------------+  +-------------------+
 | Execute      |  | Require Approval  |
 | Allowed      |  | Restricted Action |
 +------+-------+  +---------+---------+
        |                    |
        +---------+----------+
                  |
                  v
        +--------------------+
        | Record Timeline    |
        +---------+----------+
                  |
                  v
        +--------------------+
        | Print Case Summary |
        +--------------------+

Future Direction
----------------
The next versions could add structured JSON output, real alert ingestion,
policy files, approval workflows, cryptographic event signing, replay views,
and integrations with common SOC tools.
"""

from datetime import datetime, timezone
from uuid import uuid4


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def record_event(timeline, event_type, details):
    timeline.append(
        {
            "time": timestamp(),
            "event_type": event_type,
            "details": details,
        }
    )


def policy_check(action):
    restricted_actions = {"disable_user", "isolate_host"}

    if action in restricted_actions:
        return {
            "allowed": False,
            "reason": "Action requires human approval before execution.",
        }

    return {
        "allowed": True,
        "reason": "Action is allowed for autonomous execution.",
    }


def investigate_alert(alert):
    if alert["severity"] == "high":
        return {
            "hypothesis": "Potential account compromise",
            "recommended_action": "disable_user",
        }

    return {
        "hypothesis": "Suspicious activity needs monitoring",
        "recommended_action": "create_ticket",
    }


def main():
    case_id = str(uuid4())
    timeline = []

    alert = {
        "source": "identity_provider",
        "title": "Impossible travel login detected",
        "severity": "high",
        "user": "alex@example.com",
    }

    record_event(timeline, "case_created", {"case_id": case_id})
    record_event(timeline, "alert_received", alert)

    investigation = investigate_alert(alert)
    record_event(timeline, "investigation_completed", investigation)

    check = policy_check(investigation["recommended_action"])
    record_event(timeline, "policy_checked", check)

    if check["allowed"]:
        final_action = {
            "status": "executed",
            "action": investigation["recommended_action"],
        }
    else:
        final_action = {
            "status": "approval_required",
            "action": investigation["recommended_action"],
        }

    record_event(timeline, "final_action", final_action)

    print(f"SOC Flight Recorder Case: {case_id}")
    print()

    for event in timeline:
        print(f"[{event['time']}] {event['event_type']}")
        print(f"  {event['details']}")


if __name__ == "__main__":
    main()
