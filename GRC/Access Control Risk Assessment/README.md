# Access Control Risk Assessment

**Type:** Hands-on lab report (Access Control & Identity Management, Lab 02) · **Standards:** PCI DSS, HIPAA

## Purpose

Conduct a risk assessment of an access-control environment against a recognized compliance standard, identify control gaps, and produce a prioritized remediation list.

## Key topics

- **Standards comparison** — PCI DSS vs. the HIPAA Security Rule for access control: PCI DSS is prescriptive (explicit MFA and password mandates), while HIPAA (§164.312) is more flexible with required vs. addressable controls.
- **Gap analysis** — documented five control gaps in a retail POS scenario using PCI DSS: generic cashier accounts, no MFA, weak password complexity, no audit-trail logging, and inadequate physical security for POS terminals.
- **Prioritized remediation** — ranked fixes by PCI DSS severity: unique accounts and MFA (high), audit logging (high), password complexity (medium), physical-access monitoring (low).
- **Challenge exercise** — applied HIPAA to RevolutionEHR (an optometry EHR system I use daily), recommending MFA and real-time audit-log monitoring to close identified gaps.

## File

- `Risk Assessment Lab Report.pdf`
