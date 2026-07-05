# Threat Hunting — Failed Logon Analysis

A proactive hunt in **Microsoft Defender Advanced Hunting** across a shared cyber-range workspace (`LAW-Cyber-Range`), looking for password-guessing activity before any alert fired.

## The hunt

```kql
DeviceLogonEvents
| where LogonType has_any ("Network", "Interactive", "RemoteInteractive", "Unlock")
| where ActionType == "LogonFailed"
| where isnotempty(RemoteIP)
| summarize Attempts = count() by ActionType, RemoteIP, DeviceName
| order by Attempts
```

The query returned 258 result rows, surfacing external IPs hammering internet-facing lab VMs — the top source (`187.136.164.101`) had 192 failed attempts against a single machine, with several other IPs in the 90–170 range across different targets.

## Thought process

- **Start from logon telemetry, not alerts** — hunting means asking the data a question ("who is failing to log on, from where, how often?") instead of waiting for a rule to fire.
- **Filter to remote-capable logon types** and non-empty `RemoteIP` to focus on network-based guessing rather than local lockouts.
- **Aggregate by source and target** so the output reads as an attacker-centric leaderboard — the natural next pivots are "did any of these IPs succeed?" and "should any be blocked or fed into a detection rule?"

This hunt is the exploratory counterpart to the [Virtual Machine Brute Force Detection](../Virtual%20Machine%20Brute%20Force%20Detection/) project, where the same telemetry pattern was turned into a scheduled Sentinel analytics rule.

## Files

- `KQL Query - Failed Logon Attempts.jpg` — the Advanced Hunting query and its results table
