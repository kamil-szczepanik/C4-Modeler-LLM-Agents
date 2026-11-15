## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Media Relay & Signaling Service container handles resilient real-time video consultations with adaptive bitrate control for unstable connections.

## Key Elements
* Patients and Licensed Clinicians (Users)
* Media Relay & Signaling Service (Container)
* Signaling Controller (Component: Node.js / Go)
* SFU Media Router (Component: LiveKit / WebRTC SFU)
* TURN/STUN Relay Module (Component: Coturn / LiveKit Egress)
* Bandwidth Adaptation Monitor (Component: Go)
* Third-party Video Infrastructure (External System)

## Relationships
* Patients / Clinicians -> Signaling Controller: Session signaling [WSS]
* Patients / Clinicians -> SFU Media Router & TURN Module: Encrypted media streams [WebRTC over UDP/TCP]
* Signaling Controller -> SFU Media Router: Orchestrate tracks [gRPC]
* SFU Media Router -> Bandwidth Adaptation Monitor: Track packet metrics [Goroutines/Channels]
* Bandwidth Adaptation Monitor -> SFU Media Router: Adjust Simulcast/SVC layers [In-memory Go calls]
* Media Relay & Signaling Service -> Third-party Video Infrastructure: Relays real-time video supporting degraded connections [WebRTC]

## Technology Stack
* Go / Node.js: High-performance, concurrent execution for signaling and bandwidth monitoring
* LiveKit / WebRTC SFU: Selective Forwarding Unit for multi-party video routing and congestion control
* Coturn / LiveKit Egress: NAT traversal and media relay fallback for restricted networks
* WebSockets (WSS) and gRPC: Low-latency session signaling and internal IPC

## Rationale
This component architecture separates control and media planes while using adaptive bitrate controls to maintain video availability for rural connections below 300 kbit/s. It meets GCP cloud constraints and supports cross-border telemedicine availability requirements.