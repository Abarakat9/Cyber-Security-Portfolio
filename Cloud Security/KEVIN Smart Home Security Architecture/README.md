# K.E.V.I.N. — Smart Home Security Architecture

**Key Environmental Virtual Intelligence Network** — my capstone project (ITEC 490), a smart-home dashboard that unifies IoT devices, cameras, sensors, and climate controls into one interface. I served as the **Security Architect** on a three-person team (with Hasanain AlSaid, lead UI/UX, and Damion Tsosie, UI solutions).

My contribution was the complete security design and compliance documentation for the application — defense-in-depth, Zero Trust, and IoT-specific controls mapped to industry frameworks.

## What I accomplished

I authored two deliverables that define how K.E.V.I.N. protects a home full of internet-connected devices and the sensitive data (video/audio streams, usage patterns) they generate.

### 1. Security Compliance Policy Documentation
A full policy document structured around the CIA triad and defense-in-depth:

- **Security objectives** — confidentiality (encrypted device data), integrity (cryptographic hashing and digital signatures on device commands), availability (24/7 access to cameras and alerts)
- **Security architecture** — user authentication layer, hardened API gateway (DoS protection), encrypted device communication, centralized access-control engine
- **IAM** — MFA for all admin actions and first logins; Role-Based Access Control (Owner / Family Member / Guest); 30-minute session expiry
- **Data protection** — AES-256 at rest, TLS 1.3 in transit, SRTP for live video feeds
- **IoT device security** — Zero-Trust onboarding with unique device secrets, firmware signature verification, network segmentation via VLANs
- **Logging & monitoring** — immutable audit logs of state changes, real-time push alerts on high-risk events (e.g., 3 failed logins, new device registration)
- **Incident response** — automated token revocation on suspicious device behavior, disaster-recovery backups
- **Compliance mapping** — **NIST IR 8259** (Foundational Cybersecurity Activities for IoT) and the **OWASP IoT Top 10**

### 2. AI and Zero Trust Security Architecture
A companion research paper making the case for pairing Zero Trust with AI in a modern enterprise, grounded in **NIST SP 800-207 (Zero Trust Architecture)**. It covers the five Zero Trust pillars (never trust/always verify, least privilege, continuous authentication, assume breach, microsegmentation), how ML-based behavioral analytics and predictive threat modeling make Zero Trust workable at scale, a real-world example (IBM QRadar Advisor with Watson), and the governance frameworks (NIST AI RMF, EU AI Act) that keep AI-driven security accountable.

## Thought process & decisions

- **Why defense-in-depth + Zero Trust for a *home* app:** IoT devices are notoriously the weakest link — hardcoded credentials, unsigned firmware, flat networks. Treating every device and request as untrusted (rather than trusting anything "inside the house") is what contains a single compromised gadget.
- **Why map to NIST IR 8259 and OWASP IoT Top 10 specifically:** these are the IoT-focused standards, not generic enterprise ones — they speak directly to device onboarding, update integrity, and the privacy/interface weaknesses that actually sink smart-home products.
- **Why SRTP for video and AES-256/TLS 1.3 for everything else:** camera feeds are the most privacy-sensitive data in the system and need transport security purpose-built for real-time media; the rest follows current encryption baselines.
- **Why RBAC with three tiers:** a household isn't one user — owners, family, and guests need genuinely different privilege levels, and modeling that explicitly is what makes least-privilege real instead of aspirational.

## Files

- `Security Compliance Policy.pdf` — the full compliance/policy document
- `AI and Zero Trust Architecture.pdf` — the supporting research paper
- `KEVIN Presentation.pptx` — the capstone presentation deck
- `Team Formation.docx` — team charter and project plan
- `App - *.jpg` — six UI screenshots of the working dashboard (Home, Network, Notifications, Power Usage, Settings, About)
