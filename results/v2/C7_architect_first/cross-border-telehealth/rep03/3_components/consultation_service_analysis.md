## Overview
The Consultation Service container provides real-time video consultations for a cross-border telehealth platform operating in the EU and US. It ensures low-bandwidth reliability and compliance with data residency and privacy regulations.

## Key Elements
* Signaling Component (Go, WebSockets): Manages WebRTC connection setup and room coordination.
* SFU Media Router (Go, Pion WebRTC): Handles media mixing and routing with adaptive bitrate control.
* Session Management Component (Go): Enforces access control, checks patient consent, and logs session metadata.
* Bandwidth Adaptator Component (Go): Dynamically monitors stream metrics and triggers downscaling for degraded mode.
* Google Kubernetes Engine (GKE): Compute-optimized (C2/C3) instance pools running in `europe-west3` and `us-central1`.
* Global TURN/STUN Relay Nodes: Managed via Google Cloud Load Balancers for NAT traversal.

## Relationships
* API Gateway -> Signaling Component: Routes consultation requests [gRPC over mTLS]
* Signaling Component -> SFU Media Router: Manages media tracks [In-process / Go function calls]
* Signaling Component -> Session Management Component: Validates auth tokens [In-process]
* Bandwidth Adaptator Component -> SFU Media Router: Adjusts track bitrates dynamically [In-process / Go channels]
* Session Management Component -> Data Storage Layer: Persists regional session states [SSL-enforced TCP/Postgres]
* SFU Media Router -> Client Applications: Relays encrypted video/audio [DTLS-SRTP]

## Technology Stack
* Go: Chosen for high concurrency and low-footprint in-process threading.
* Pion WebRTC: Enables pure-Go media routing and low-latency stream adaptation.
* PostgreSQL (Cloud SQL): Provides secure, region-bound relational storage.
* GKE & Google Cloud Load Balancers: Support auto-scaling and global traffic distribution.

## Rationale
This architecture uses in-process Go components and Pion WebRTC to minimize latency and meet the <300 kbit/s degraded mode requirement for rural users. Regional GKE clusters and token-based TURN relays enforce strict GDPR and HIPAA data residency constraints.