# AWS Application Load Balancer + WAF — Edge Defense Deployment

Hands-on AWS deployment of an **Application Load Balancer (ALB) fronted by AWS WAF**, built as the internet-facing edge-defense layer for the K.E.V.I.N. smart-home web application. This is the implementation counterpart to the [K.E.V.I.N. Security Architecture](../KEVIN%20Smart%20Home%20Security%20Architecture/) compliance documentation — the policy defined the controls, and this deployment enforced them at the network perimeter.

## Architecture

```
Internet
   │
   ▼
AWS WAF  (Web ACL — managed rule groups, action: BLOCK)
   │
   ▼
Application Load Balancer  (Layer 7 routing, TLS termination)
   │
   ▼
Target group  →  smart-home web application
```

The WAF Web ACL is associated directly with the ALB, so every request to the application is inspected and filtered at Layer 7 before it ever reaches the backend targets.

## What I built and configured

- **Application Load Balancer** as the single internet-facing entry point for the web app, handling Layer 7 routing and TLS termination.
- **AWS WAF Web ACL** attached to the ALB, using **AWS Managed Rule Groups** for broad, continuously-updated coverage:
  - **SQL injection (SQLi)** protection across the query string, body, and headers
  - **Common exploits / core rule set**, including cross-site scripting (XSS)
  - **Known bad inputs**
  - **Malicious / known-bad IP filtering** (IP reputation)
- Rules set to a **block** action, so matching requests are dropped rather than merely counted.

## Decisions and why

- **Why ALB + WAF instead of just a security group:** security groups filter by IP and port at Layers 3–4 — they can't see an HTTP payload. The web app's real risks (injection, XSS, malicious request patterns) live at Layer 7, which is exactly where WAF inspects. Attaching the Web ACL to an ALB puts that inspection inline with every request.
- **Why AWS Managed Rule Groups over all-custom rules:** the managed groups are maintained by AWS against evolving threats and cover the OWASP-style common attacks (SQLi, XSS, bad inputs) out of the box. For a dashboard that handles authentication and device commands, that's a stronger and lower-maintenance baseline than hand-writing every rule.
- **Why prioritize SQL injection and XSS:** the application is a web dashboard backed by a data store — injection and cross-site scripting are among the highest-impact web vulnerabilities (OWASP Top 10) and the ones most likely to be probed automatically by scanners and bots.
- **Why this fits a defense-in-depth story:** the WAF/ALB is the outermost layer. Behind it, the K.E.V.I.N. architecture adds MFA + RBAC, TLS 1.3, encrypted device communication, and audit logging — so a request has to survive edge filtering *and* application-level controls. No single layer is trusted to catch everything.

## Result

The deployment gives the smart-home application a hardened internet edge: malicious and known-bad traffic (SQL injection, XSS, bad inputs, flagged IPs) is filtered before it reaches the load balancer's targets. This directly implements the "AWS Web Application Firewall — filter bad requests and known malicious IPs, protect against SQL injection and cross-site scripting" control called for in the [security compliance policy](../KEVIN%20Smart%20Home%20Security%20Architecture/Security%20Compliance%20Policy.pdf).

## Related

- [K.E.V.I.N. Smart Home Security Architecture](../KEVIN%20Smart%20Home%20Security%20Architecture/) — the capstone application this edge defense protects, including the full compliance policy and Zero Trust research.

---

*This is a written architecture and configuration summary of the deployment.*
