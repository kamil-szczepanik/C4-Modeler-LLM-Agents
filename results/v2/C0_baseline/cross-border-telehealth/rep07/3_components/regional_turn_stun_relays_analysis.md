## Overview
This architecture summary defines the Regional TURN/STUN Relays container for the Cross-Border Telehealth Platform, ensuring reliable video consultations for rural and low-bandwidth users in the EU and US. It guarantees strict data residency and secure real-time media handling across GCP regions.

## Key Elements
* STUN/TURN Allocation Engine (Coturn / GCP Managed Service)
* Bandwidth Adaptation & Congestion Controller (WebRTC GCC / Simulcast/SVC Controller)
* Session Auth & Quota Validator (Go with SPIFFE/SPIRE mTLS)
* Regional GCP Compute Engine Managed Instance Groups (MIGs)
* GCP Regional VPC Networks (`europe-west3` and `us-central1`)

## Relationships
* Client Apps -> Session Auth & Quota Validator: Authenticate relay sessions [HTTPS/REST]
* Client Apps <-> STUN/TURN Allocation Engine: Relay encrypted media streams [DTLS-SRTP over UDP/TCP]
* Bandwidth Adaptation & Congestion Controller -> STUN/TURN Allocation Engine: Throttle and prioritize audio streams [Internal IPC]
* Session Auth & Quota Validator -> Consultation Service: Validate tokens and session quotas [gRPC via mTLS]

## Technology Stack
* Coturn / GCP Managed TURN/STUN: Handles media packet forwarding and UDP/TCP port allocation.
* WebRTC GCC / Simulcast/SVC: Manages dynamic bandwidth adaptation below 300 kbit/s to maintain audio integrity.
* GCP Managed Instance Groups (MIGs): Ensures scalable and resilient regional deployments.
* SPIFFE/SPIRE: Provides secure mTLS service-to-service authentication.
* DTLS-SRTP: Secures end-to-end media streams with zero payload retention.

## Rationale
This architecture satisfies stringent GDPR and HIPAA data residency mandates by completely isolating regional media processing. Additionally, it guarantees high availability and regulatory compliance for rural users under unstable network conditions.