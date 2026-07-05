# Ahmad Barakat — Cybersecurity Portfolio

Aspiring SOC Analyst · Overland Park, KS (Kansas City Metro) · Open to remote

---

## About

I'm a final-semester cybersecurity student working toward a SOC analyst role, with hands-on time in Microsoft Sentinel, Defender for Endpoint, KQL, Nessus, and cloud security architecture. This repository collects the labs, investigations, papers, and capstone work behind that goal — organized by discipline, with each project documented in its own README.

- **Role:** Aspiring SOC Analyst (entry-level)
- **Education:** B.S. Information Technology / Applied Cybersecurity — University of Kansas, Dec 2026
- **Currently:** IT Support Specialist @ VinCue
- **Certification:** CompTIA Security+ (SY0-701)

---

## Table of Contents

### [Security Operations](Security%20Operations/)
Detection engineering, threat hunting, and incident response in Microsoft Sentinel and Defender for Endpoint.
- [PowerShell Suspicious Web Request](Security%20Operations/PowerShell%20Suspicious%20Web%20Request/) — full incident lifecycle: Sentinel detection (T1059.001), MDE triage, containment, True Positive closure
- [Virtual Machine Brute Force Detection](Security%20Operations/Virtual%20Machine%20Brute%20Force%20Detection/) — scheduled analytics rule (T1110), investigation, and containment
- [Threat Hunting - Failed Logon Analysis](Security%20Operations/Threat%20Hunting%20-%20Failed%20Logon%20Analysis/) — proactive hunt in Defender Advanced Hunting
- [Wireshark Network Analysis Labs](Security%20Operations/Wireshark%20Network%20Analysis%20Labs/) — packet analysis of HTTP, TCP, DNS, NAT, ICMP, DHCP, 802.11, TLS
- [Security Tools Labs](Security%20Operations/Security%20Tools%20Labs/) — Tor, John the Ripper, Eraser, Recuva
- [BSidesKC 2025 Conference Reflection](Security%20Operations/BSidesKC%202025%20Conference%20Reflection/) — professional community engagement
- [Windows Server Lab Setup](Security%20Operations/Windows%20Server%20Lab%20Setup/) — foundational virtualization

### [Cloud Security](Cloud%20Security/)
Cloud and IoT security architecture.
- [KEVIN Smart Home Security Architecture](Cloud%20Security/KEVIN%20Smart%20Home%20Security%20Architecture/) — capstone security-architect role: defense-in-depth, Zero Trust, IAM, IoT compliance
- [AWS ALB and WAF Deployment](Cloud%20Security/AWS%20ALB%20and%20WAF%20Deployment/) — deployed an Application Load Balancer fronted by AWS WAF with managed rule groups (SQLi, XSS, malicious-IP filtering)

### [TryHackMe](TryHackMe/)
Blue-team room write-ups and the SAL1 path *(in progress)*.

### [GRC](GRC/)
Governance, risk, and compliance — grounded in NIST, PCI DSS, and HIPAA.
- [Business Impact Analysis - Initech](GRC/Business%20Impact%20Analysis%20-%20Initech/) · [Access Control Risk Assessment](GRC/Access%20Control%20Risk%20Assessment/) · [Security Policy Framework Evaluation](GRC/Security%20Policy%20Framework%20Evaluation/) · [Risk Management Plan](GRC/Risk%20Management%20Plan/) · [Remote Access and Physical Security Plan](GRC/Remote%20Access%20and%20Physical%20Security%20Plan/) · [IT Risk Success and Failure](GRC/IT%20Risk%20Success%20and%20Failure/) · [Risk Assessment Fundamentals](GRC/Risk%20Assessment%20Fundamentals/) · [Ethics Case Studies](GRC/Ethics%20Case%20Studies/)

### [Python Security Projects](Python%20Security%20Projects/)
Applied Python for AI and security.
- [Facial Recognition AI](Python%20Security%20Projects/Facial%20Recognition%20AI/) — ITEC 612 capstone: full ML pipeline reaching 100% test accuracy, with limitation and ethics analysis

### [Vulnerability Management](Vulnerability%20Management/)
Scanning, prioritization, and remediation.
- [AD Domain Controller Vulnerability Scan](Vulnerability%20Management/AD%20Domain%20Controller%20Vulnerability%20Scan/) — Nmap, Nessus, OpenVAS, SMBv1 remediation, CVSS analysis
- [Infrastructure Assessment](Vulnerability%20Management/Infrastructure%20Assessment/) — assessment scoping and methodology

---

## Featured Projects

- **PowerShell Suspicious Web Request** *(Security Operations)* — Built a Sentinel KQL detection for PowerShell download cradles, confirmed execution in Defender for Endpoint, isolated the host, and closed the incident as a True Positive with a full report. Mapped to ATT&CK T1059.001.
- **K.E.V.I.N. — Smart Home Security Architecture** *(Cloud Security)* — Capstone security architect: authored the defense-in-depth / Zero Trust compliance policy and AI-Zero-Trust research paper for an IoT smart-home app, mapped to NIST IR 8259, OWASP IoT Top 10, and NIST SP 800-207.
- **AWS ALB + WAF Edge Defense** *(Cloud Security)* — Deployed an Application Load Balancer fronted by AWS WAF with managed rule groups (SQL injection, XSS, bad inputs, malicious-IP filtering) as the hardened internet edge for the K.E.V.I.N. web app.
- **AD Domain Controller Vulnerability Scan** *(Vulnerability Management)* — Discovered and scanned a Windows Server target with Nmap/Nessus/OpenVAS, remediated SMBv1, and proved the fix with a before/after re-scan.
- **Facial Recognition AI** *(Python Security Projects)* — Four-model Python/OpenCV pipeline (SVM, KNN, Logistic Regression, Cosine Similarity) at 100% test accuracy, with candid limitation and ethics analysis.

---

## Skills

**SIEM / Detection:** Microsoft Sentinel · Defender for Endpoint · KQL · Defender Advanced Hunting · Wireshark
**Vulnerability Mgmt:** Nessus · OpenVAS · Nmap / Zenmap · CVSS
**Cloud / Identity:** AWS (ALB, WAF) · Zero Trust (NIST SP 800-207) · IAM / RBAC / MFA · Defense-in-Depth
**GRC / Frameworks:** NIST SP 800-30 / 800-34 / 800-63 · PCI DSS · HIPAA · MITRE ATT&CK
**Languages & Tools:** Python · PowerShell · Bash · Git · Linux · VirtualBox

---

## Certifications

| Credential | Issuer | Status |
|---|---|---|
| Security+ (SY0-701) | CompTIA | Active |
| SAL1 — Security Analyst Level 1 | TryHackMe | In progress |

---

## Contact

If you're hiring for a SOC Analyst role, open a channel.

[Email](mailto:ahmadbarakat914@gmail.com) · [LinkedIn](https://www.linkedin.com/in/ahmad-barakat-809b19b7/)
