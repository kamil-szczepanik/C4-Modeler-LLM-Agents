## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures regional data residency, strict regulatory compliance (GDPR/HIPAA), and reliable communication under unstable network conditions.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Web/Mobile Client (Flutter / React Native)
- Core Telehealth Backend (Node.js / Go)
- TURN/STUN Relay Tier (Coturn C++ Open Source)
- STUN/ICE Discovery Engine
- TURN Allocation & Relay Manager
- Geo-Routing & Health Agent (Go daemon with REST/JSON Credential Broker)
- Video Media Server (Janus / WebRTC on GCE)
- GCP Regional Infrastructure (`europe-west3` and `us-central1`)

## Relationships
- Web/Mobile Client connects to Geo-Routing & Health Agent via HTTPS (REST API) for time-limited HMAC-SHA1 TURN credentials.
- Core Telehealth Backend provisions static shared secrets to the Geo-Routing & Health Agent.
- Web/Mobile Client streams media to TURN Allocation & Relay Manager via TURN/UDP or TURN/TLS.
- TURN Allocation & Relay Manager routes media to Video Media Server (Janus) via RTP/SRTP over local GCP VPC networking.

## Technology Stack
- **Coturn (C++):** Lightweight open-source STUN/TURN implementation for NAT traversal and bandwidth throttling.
- **Go:** Used for the Geo-Routing & Health Agent daemon and REST/JSON Credential Broker.
- **WebRTC / RTP / SRTP:** Protocols for real-time video streaming and media encryption.
- **GCP Network Load Balancer & MIGs:** Managed TCP/UDP load balancing and ephemeral Compute Engine instances for regional scaling.
- **Linux `tc` (Traffic Control):** Enforces bandwidth shaping to support degraded mode (<300 kbit/s).

## Rationale
This architecture ensures strict data residency by isolating regional deployments in `europe-west3` and `us-central1`, satisfying GDPR and HIPAA requirements. The Coturn-based TURN/STUN Relay Tier guarantees high availability and compliance with R-06 through optimized P2P fallbacks, degraded mode traffic shaping, and robust NAT traversal for rural users.