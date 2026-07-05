# Wireshark Network Analysis Labs

A series of packet-analysis labs (ITEC 422) using Wireshark to dissect core protocols at the packet level — the foundational network-forensics skill set a SOC analyst uses to read traffic captures during an investigation.

## Labs completed

| Lab | Focus | Key takeaways |
|---|---|---|
| Lab 1 | HTTP, TCP, DNS | First capture and filtering (`ip.addr ==`), identifying protocol layers in a simple web fetch |
| Lab 3 | TCP | SYN / SYN-ACK handshake sequence numbers, RTT and EstimatedRTT calculation, throughput, slow-start vs. congestion avoidance on the time-sequence graph |
| Lab 4 | NAT | Comparing client-side and ISP-side captures to see how NAT rewrites source IP/port on the same HTTP GET |
| Lab 5 | ICMP | Why ICMP has no port numbers, echo request/reply type & code fields, `ping` vs. `traceroute`, IP protocol number 1 (ICMP) vs. 17 (UDP) |
| Lab 6 | DHCP | The DISCOVER/OFFER/REQUEST/ACK exchange over UDP ports 67/68, transaction IDs, lease fields |
| Lab 7 | 802.11 Wi-Fi | Beacon frames and SSIDs, beacon intervals, association/authentication frames, open-system auth, failed vs. successful AP association |
| Lab 8 | TLS | The TLS 1.2 handshake, record types, cipher-suite negotiation, nonces and session IDs, pre-master secret exchange |

## Why these matter

Reading raw packets is what lets an analyst answer questions a dashboard can't: *what exactly did this host send, to whom, and did the connection actually complete?* Each lab builds fluency in a protocol I'd need to recognize in a real capture — the TCP handshake for connection analysis, DHCP for host attribution, 802.11 management frames for wireless incidents, and the TLS handshake for spotting anomalies in encrypted sessions.

## Files

Seven lab write-ups (Labs 1, 3–8) plus `Lab 1 Capture.pcapng`, the raw packet capture from the first lab, openable directly in Wireshark.
