## Overview
The Hybrid VPN Gateway Container establishes secure, high-availability hybrid connectivity between on-premise Kubernetes clusters and AWS eu-central-1. It enforces strict HIPAA/GDPR compliance, traffic prioritization, and sub-second failover for clinical data transit.

## Key Elements
- WireGuard Core Tunneling Daemon (BoringTun)
- Route Agent (`Bird` BGP)
- Configuration Synchronizer
- IPsec/IKEv2 Fallback Manager
- Traffic Policer (`tc`)
- Network Flow Auditing Component
- Tunnel Termination Proxy
- State Synchronization Daemon
- Cryptographic Hardware Acceleration Module
- MTU Discovery and Fragmentation Manager
- Kernel Metrics Exporter (eBPF)
- Split-Tunnel Policy Enforcer
- Dead Peer Detection (DPD) Watchdog
- Packet Inspection and Anti-Replay Filter
- DNS Forwarding and Split-Resolver

## Relationships
- WireGuard Gateway to AWS VPC: Bidirectional UDP encrypted tunnels over port 51820
- Configuration Synchronizer to Data Encryption & Key Management Container: Encrypted gRPC for secret retrieval
- Network Flow Auditing to Audit & Compliance Sidecar Container: NetFlow/IPFIX telemetry export
- Kernel Metrics Exporter to Observability Collector Container: eBPF transport telemetry export
- DNS Forwarding to On-Premise DNS Servers: Encrypted DNS query resolution

## Technology Stack
- WireGuard & BoringTun: Memory-safe user-space tunneling daemon for high throughput
- `nftables`: Kernel-level packet filtering and policy routing
- `Bird`: Dynamic BGP route propagation and failover
- Linux `tc` (Traffic Control): QoS queues for traffic prioritization
- eBPF: Low-level transport telemetry and metric scraping
- gRPC: Secure inter-container configuration synchronization
- UDP Port 51820: Primary hybrid encapsulation protocol

## Rationale
This architecture ensures uninterrupted 99.99% availability and strict regulatory compliance for cross-environment clinical data transit. Redundant tunnels, automated failover mechanisms, and hardware-accelerated encryption protect sensitive patient information without degrading EMR system performance.