# Security Tools Labs

Hands-on labs (ITEC 340) with four tools that sit on both sides of the security line — offensive password cracking and reconnaissance-adjacent anonymity, plus defensive secure-deletion and forensic recovery. Understanding how each works is what lets an analyst reason about the artifacts they leave behind.

## Labs

### Tor Browser — Anonymity & IP Exposure
Compared my real public IP (Google Fiber, Kansas City) as seen in Chrome/Edge against the Tor Browser's exit-node IP (which surfaced in Norway). Demonstrated that HTTPS alone does not provide anonymity — the origin IP is still visible without an anonymizing layer.

### John the Ripper — Password Cracking
Ran a dictionary attack against a `hackme.txt` hash file (DES-based crypt hashes, 584 hashes with 127 salts). The dictionary run cracked common passwords quickly; combined with brute-force observations, the lab drives home why length + character-class variety matters and why weak passwords fall in seconds. **Takeaway I wrote up:** letters-only or numbers-only passwords are never safe, which is exactly why complexity + MFA are enforced in the real world.

### Eraser — Secure Deletion
Used Eraser to overwrite free space and files beyond recovery (not just recycle-bin deletion). Notably, the scheduled free-space wipe "completed with errors" due to insufficient permissions — a useful reminder that secure-deletion tooling needs the right privileges to actually do its job.

### Recuva — File Recovery
The counterpart to Eraser: recovered deleted files from disk, illustrating why "deleted" doesn't mean "gone" until the sectors are overwritten. This is the forensic principle behind data-remanence risk.

## Why group these together

Eraser and Recuva are two sides of the same coin (data remanence), and John the Ripper plus the Tor exercise show attacker techniques from the defender's seat. Knowing what each tool leaves in logs and on disk is what makes an analyst able to interpret evidence rather than just collect it.

## Files

- `Tor Browser Anonymity Project.pdf`
- `John the Ripper Password Cracking.pdf`
- `Eraser Secure Deletion.pdf`
- `Recuva File Recovery.pdf`
