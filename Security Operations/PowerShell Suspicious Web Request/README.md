# PowerShell Suspicious Web Request — Detection & Incident Response

End-to-end SOC workflow: I built a Microsoft Sentinel detection for PowerShell-based remote file downloads, triaged the resulting incident, contained the host with Microsoft Defender for Endpoint (MDE), and closed the ticket as a **True Positive** with a full incident report.

**MITRE ATT&CK:** T1059.001 (Command and Scripting Interpreter: PowerShell), plus Command and Control and Exfiltration tactics mapped in the Sentinel incident.

## What happened

A user on `windows-target-` attempted to install "free software." Three PowerShell commands ran with `-ExecutionPolicy Bypass`, each using `Invoke-WebRequest` to pull scripts from a GitHub repo into `C:\programdata\`:

- `portscan.ps1` — scanned an internal range (10.0.0.155–10.0.0.200) probing common ports
- `pwncrypt.ps1` — simulated ransomware: created and encrypted files, dropped a ransom note
- `eicar.ps1` — dropped an EICAR test file to trigger AV detection

## What I did

1. **Detection engineering** — wrote the KQL analytics rule in Sentinel over `DeviceProcessEvents`, alerting when `powershell.exe` command lines contain `Invoke-WebRequest`. Configured it as a scheduled rule (runs every 4 hours over a 5-hour lookback) with entity mapping for Account, Host, and Process so incidents auto-populate with investigable entities.
2. **Triage & analysis** — confirmed via MDE that the scripts didn't just download, they *executed*:

   ```kql
   let TargetHostname = "windows-target-";
   let ScriptNames = dynamic(["eicar.ps1", "portscan.ps1", "pwncrypt.ps1"]);
   DeviceProcessEvents
   | where DeviceName == TargetHostname
   | where FileName == "powershell.exe"
   | where ProcessCommandLine contains "-File" and ProcessCommandLine has_any (ScriptNames)
   | order by TimeGenerated
   | project TimeGenerated, AccountName, DeviceName, FileName, ProcessCommandLine
   | summarize Count = count() by AccountName, DeviceName, FileName, ProcessCommandLine
   ```

3. **User interview** — the user reported a brief black screen then "nothing happened," consistent with hidden-window execution. This corroborated the telemetry rather than contradicting it.
4. **Containment & recovery** — isolated the host in MDE, ran an anti-malware scan (clean), released the host from isolation.
5. **Post-incident actions** — the user was assigned upgraded KnowBe4 security-awareness training, and a policy was implemented restricting PowerShell for non-essential users.

## Decisions and why

- **Alert on `Invoke-WebRequest` in the command line** rather than on file-creation events: it catches the download-cradle pattern at the source and generalizes across payload names.
- **Verify execution before containment claims** — downloading a script and running it are different findings; the second KQL query distinguishes them, which drives the True Positive verdict.
- **Isolate first, scan second** — cutting network access stops potential C2 and lateral movement while the AV scan runs.

## Files

- `Incident Report.pdf` — the full written incident report
- Screenshots `1`–`7` — each investigation stage: KQL detection, SIEM rule creation with ATT&CK mapping, scheduled rule logic, incident creation, execution-check query, EDR isolation, and the closed ticket with True Positive disposition
