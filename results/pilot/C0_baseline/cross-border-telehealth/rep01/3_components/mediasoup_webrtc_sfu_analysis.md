## Overview
The mediasoup WebRTC SFU provides low-latency, real-time video consultations for cross-border telehealth patients. It ensures regional data residency and connection resilience under low-bandwidth constraints.

## Key Elements
- Patients and Licensed Clinicians (Users)
- mediasoup WebRTC SFU (Container)
- Worker Pool Manager (Component)
- Signaling Event Handler (Component)
- Transport & Congestion Controller (Component)
- Media Router (Component)
- Go Clinical Workspace Service (External Container)

## Relationships
- Patients/Clinicians -> mediasoup WebRTC SFU: Streams audio/video [WebRTC, ICE, STUN, TURN via UDP/TCP]
- Go Clinical Workspace Service -> Signaling Event Handler: Orchestrates rooms [gRPC over mTLS]
- Worker Pool Manager -> Media Router: Manages C++ worker threads and packet forwarding [IPC]

## Technology Stack
- mediasoup / C++ worker modules: High-performance selective forwarding of video/audio packets
- Node.js: Runtime for container orchestration and worker management
- DTLS-SRTP: Ensures encryption of media payloads traversing public networks
- GCC / REMB: Congestion control algorithms for bandwidth adaptation below 300 kbit/s
- Prometheus: Scrapes internal SFU worker metrics for packet loss and RTT observability

## Rationale
Isolated regional SFU deployments in GCP enforce strict data residency mandates for EU and US health data. Simulcast and dynamic layer adaptation maintain essential clinical audio during unstable rural connections.