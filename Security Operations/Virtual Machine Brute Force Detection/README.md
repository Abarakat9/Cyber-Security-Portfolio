# Virtual Machine Brute Force Detection — Sentinel + Defender for Endpoint

Detection and investigation of brute-force logon activity against lab virtual machines, worked end-to-end in Microsoft Sentinel: analytics rule creation, incident triage, host containment, and ticket closure as a **True Positive**.

**MITRE ATT&CK:** T1110 (Brute Force).

## The detection

I built a scheduled analytics rule in Sentinel over Defender for Endpoint logon telemetry:

```kql
DeviceLogonEvents
| where TimeGenerated >= ago(5h)
| where ActionType == "LogonFailed"
| summarize NumberOfFailures = count() by DeviceName, RemoteIP
| where NumberOfFailures >= 50
```

The rule runs every 4 hours over a 5-hour lookback and generates an alert whenever any single remote IP racks up 50+ failed logons against one device.

## The investigation

Working the incident like a SOC ticket:

1. **Alert triage** — the rule fired and Sentinel created an incident with the offending `RemoteIP` / `DeviceName` pairs mapped as entities.
2. **Scope check** — queried whether any of the brute-forcing IPs ever produced a *successful* logon on the targets (`ActionType == "LogonSuccess"`). None had — the attack was unsuccessful, but the volume confirmed it was a genuine attack rather than user error.
3. **Containment** — isolated the targeted machine (`Linux-Target-1`) in Defender for Endpoint and ran an antivirus scan as a precaution.
4. **Documentation & closure** — recorded findings in the incident activity log and closed the ticket as True Positive with notes.

## Decisions and why

- **Threshold of 50 failures over the window** — high enough to avoid paging on normal typo-and-retry behavior, low enough to catch scripted password guessing early.
- **Summarize by `DeviceName` + `RemoteIP`** — attributes the attack to a source, which makes the follow-up question ("did this IP ever get in?") a one-line pivot.
- **Check for successful logons before closing** — the difference between "attempted brute force" and "compromised host" is that pivot; skipping it is how real intrusions get closed as noise.
- **Isolate even though no success was found** — cheap insurance while the AV scan confirmed the host was clean.

## Files

Nine screenshots covering the full lifecycle: rule configuration (`General Rules`, `KQL Query Specifications`), alert firing and incident creation, entity mapping, the successful-logon check, device isolation and AV scan on Linux-Target-1, the annotated activity log, and the closed True Positive ticket.
