![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0B0C10,50:1F2833,100:0B0C10&height=220&section=header&text=AHMAD%20BARAKAT&fontSize=70&fontColor=66FCF1&animation=fadeIn&desc=//%20CYBER%20DEFENDER%20//%20SOC%20ANALYST%20IN%20TRAINING&descSize=18&descAlignY=72&descAlign=50)

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=Fira+Code&size=22&duration=2800&pause=900&color=66FCF1&center=true&vCenter=true&width=720&lines=Detecting+threats+before+they+become+incidents.;SIEM+%E2%80%A2+EDR+%E2%80%A2+KQL+%E2%80%A2+MITRE+ATT%26CK;Building+the+next+SOC+analyst+from+the+ground+up.)](#)

[![Status](https://img.shields.io/badge/STATUS-OPEN_TO_WORK-22C55E?style=for-the-badge&labelColor=0B0C10)](#)
[![Location](https://img.shields.io/badge/LOCATION-KC_METRO-66FCF1?style=for-the-badge&labelColor=0B0C10)](#)

</div>

---

## About

I'm a final-semester IT student working toward a SOC analyst role, with hands-on time in Microsoft Sentinel, Defender for Endpoint, KQL, Tenable, and AWS security services. This repository holds the labs, write-ups, and capstone work behind that goal.

- **Role:** Aspiring SOC Analyst (entry-level)
- **Education:** B.S. Information Technology / Applied Cybersecurity — University of Kansas, Dec 2026
- **Currently:** IT Support Specialist @ VinCue
- **Location:** Overland Park, KS (Kansas City Metro) · open to remote
- **Certification:** CompTIA Security+ (SY0-701)

---

## Portfolio

| Folder | What's there |
|---|---|
| [`soc/`](soc/) | SIEM detection rules, EDR investigations, ATT&CK-mapped analytics |
| [`tryhackme/`](tryhackme/) | Write-ups and notes from TryHackMe rooms, including the SAL1 path |
| [`vulnerability-management/`](vulnerability-management/) | Scanning, prioritization, and remediation tracking |
| [`cloud-security/`](cloud-security/) | AWS/Azure hardening, edge defense, and identity configuration |

---

## Detection Pipeline

```mermaid
flowchart LR
    A[Endpoints<br/>Network<br/>Cloud] -->|Ingest| B[(Microsoft<br/>Sentinel)]
    B -->|KQL Analytics| C{Alert<br/>Triage}
    C -->|True Positive| D[Incident<br/>Response]
    C -->|False Positive| E[Rule<br/>Tuning]
    D -->|ATT&CK Mapping| F[Containment<br/>+ Eradication]
    F --> G[Post-Mortem<br/>+ Hardening]
    E --> B
    G --> B
    style B fill:#0B0C10,stroke:#66FCF1,color:#66FCF1
    style C fill:#1F2833,stroke:#FBBF24,color:#FBBF24
    style D fill:#1F2833,stroke:#EF4444,color:#EF4444
    style F fill:#1F2833,stroke:#22C55E,color:#22C55E
```

---

## Skills & Tools

<table>
<tr>
<td valign="top" width="50%">

**SIEM / Detection**

![Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Defender](https://img.shields.io/badge/Defender_for_Endpoint-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![KQL](https://img.shields.io/badge/KQL-005A9E?style=flat-square&logo=microsoft&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![Tenable](https://img.shields.io/badge/Tenable-00A1E0?style=flat-square&logo=tenable&logoColor=white)

**Cloud / Identity**

![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonwebservices&logoColor=white)
![Entra](https://img.shields.io/badge/Entra_ID-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![WAF](https://img.shields.io/badge/AWS_WAF-FF4F00?style=flat-square&logo=amazonwebservices&logoColor=white)

</td>
<td valign="top" width="50%">

**Frameworks**

![MITRE](https://img.shields.io/badge/MITRE_ATT%26CK-BA0C2F?style=flat-square)
![NIST](https://img.shields.io/badge/NIST_CSF-005DAA?style=flat-square)
![RBAC](https://img.shields.io/badge/RBAC-1F2833?style=flat-square)
![MFA](https://img.shields.io/badge/MFA-1F2833?style=flat-square)

**Languages & Tools**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</td>
</tr>
</table>

---

## Projects

<table>
<tr><td>

### 🛡️ K.E.V.I.N. — Smart Home Defense Grid
**Role:** Security Architect &nbsp;·&nbsp; **Stack:** AWS · Python · ALB · WAF

End-to-end secure smart-home web application. Started life as a Python application-layer firewall, then re-architected onto a cloud-native edge stack — AWS ALB + WAF with managed rule groups including SQLi protection, defense-in-depth from edge to app.

`AWS WAF` `ALB` `Python` `Defense in Depth`

</td></tr>
<tr><td>

### 💻 Malicious PowerShell Executions — Detection Lab
**Role:** Solo build &nbsp;·&nbsp; **Stack:** Sentinel · KQL · Defender for Endpoint

Detection engineering lab targeting adversarial PowerShell — encoded commands, AMSI bypass attempts, download cradles, and suspicious cmdlet chains. Custom KQL analytics rules mapped to T1059.001, alert thresholds tuned for low false-positive rate.

```kql
// Sample: encoded PowerShell execution
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any ("-enc","-EncodedCommand","FromBase64String")
| project Timestamp, DeviceName, AccountName, ProcessCommandLine
| order by Timestamp desc
```

`Sentinel` `KQL` `Defender for Endpoint` `T1059.001`

</td></tr>
<tr><td>

### 🔍 Azure SIEM Threat Detection Lab
**Role:** Solo build &nbsp;·&nbsp; **Stack:** Sentinel · KQL · Log Analytics

Honeypot-style detection environment streaming Windows + network telemetry into Sentinel. Custom analytics rules mapped to T1110 (brute force) and T1071 (C2 over application-layer protocols). End-to-end: ingestion → analytics → workbook visualization.

`Sentinel` `KQL` `MITRE ATT&CK`

</td></tr>
<tr><td>

### 👁️ Facial Recognition AI — ITEC-612 Capstone
**Role:** Engineer & Debug Lead &nbsp;·&nbsp; **Stack:** Python · OpenCV · NumPy · Colab

Multi-model facial recognition pipeline on a 10-celebrity dataset. Debugged dataset URL handling, resolved missing `test_paths` keys in `.npz` artifacts, refined PIL/OpenCV preprocessing chain. Final result: 100% accuracy across all four models.

`Python` `OpenCV` `ML Ops` `Image Pipelines`

</td></tr>
</table>

---

## ATT&CK Coverage

```
┌─ TACTIC ─────────────────┬─ TECHNIQUE ─┬─ NAME ──────────────────────────┐
│  Initial Access          │  T1566.001  │  Spearphishing Attachment       │
│  Execution               │  T1204.002  │  User Execution: Malicious File │
│  Execution               │  T1059.001  │  PowerShell                     │
│  Credential Access       │  T1110      │  Brute Force                    │
│  Command & Control       │  T1071      │  Application Layer Protocol     │
└──────────────────────────┴─────────────┴─────────────────────────────────┘
```

---

## Certifications

| Credential | Issuer | Status |
|---|---|:---:|
| **Security+ (SY0-701)** | CompTIA | ![Active](https://img.shields.io/badge/-ACTIVE-22C55E?style=flat-square) |
| **SAL1 — Security Analyst Level 1** | TryHackMe | ![In Progress](https://img.shields.io/badge/-IN_PROGRESS-FBBF24?style=flat-square) |

---

## Current Focus

- Finishing my final semester at the University of Kansas (graduating 2026)
- Working through TryHackMe's SAL1 — Security Analyst Level 1 path
- Sharpening OSI model and port/protocol fluency for technical interviews
- Expanding my library of MITRE-mapped KQL detection rules

---

## Contact

<div align="center">

If you're hiring for a SOC Analyst role, open a channel.

[![Email](https://img.shields.io/badge/-ahmadbarakat914@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0B0C10)](mailto:ahmadbarakat914@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-Ahmad_Barakat-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0B0C10)](https://www.linkedin.com/in/ahmad-barakat-809b19b7/)

</div>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:1F2833,50:0B0C10,100:1F2833&height=120&section=footer)
