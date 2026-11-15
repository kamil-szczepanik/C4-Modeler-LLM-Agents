## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring low-latency communication and regulatory compliance.

## Key Elements
- **Patients (EU & US)**: End-users accessing services via mobile/web clients.
- **Licensed Clinicians**: Healthcare providers conducting remote video diagnoses.
- **Video Media Server**: Janus WebRTC engine on Google Compute Engine (GCE).
- **Core Telehealth Backend**: Node.js / Go services managing business logic and session authorization.
- **TURN/STUN Relay Tier**: Coturn on GCE handling NAT traversal for restrictive networks.
- **Global Load Balancer**: GCP Global External HTTPS/TCP Load Balancer enforcing regional routing.

## Relationships
- **Web/Mobile Client -> Global Load Balancer**: Routes traffic to regional clusters [HTTPS/TCP]
- **Web/Mobile Client -> Video Media Server**: Connects for media streaming [WebRTC/SRTP]
- **Video Media Server -> Core Telehealth Backend**: Manages session establishment and room authorization [WebSocket / WSS]
- **Web/Mobile Client -> TURN/STUN Relay Tier**: Provides NAT traversal for unstable connections [STUN/TURN]

## Technology Stack
- **Janus Gateway on GCE**: Selected for robust, low-latency real-time video streaming and simulcast management.
- **Coturn**: Deployed on GCP for reliable NAT traversal in unstable rural connections.
- **GCP Global External Load Balancer**: Automatically routes cross-border traffic while enforcing regional data residency.
- **GCP Managed Instance Groups (MIGs)**: Provides auto-scaling for video media and relay servers.

## Rationale
This architecture ensures strict data residency compliance by localizing media processing within GCP regions (*europe-west3* and *us-central1*). Furthermore, Janus WebRTC simulcast and Coturn relay tiers directly satisfy high-availability and degraded-mode requirements for rural users.