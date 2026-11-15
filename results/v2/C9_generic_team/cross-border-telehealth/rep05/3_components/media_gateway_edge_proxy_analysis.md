## Overview
• Cross-border telehealth platform delivering video consultations, e-prescriptions, and an AI symptom checker across the EU and US.
• Enforces strict regional data residency and compliance using GCP regions `europe-west3` and `us-central1`.

## Key Elements
• Patients and Licensed Clinicians (End Users)
• Media Gateway / Edge Proxy (Coturn/Janus, WebRTC)
• Regional Distributed Cache (Memorystore for Redis)
• Load Balancer / DNS (Regional routing)
• Regional E-Prescription & AI Symptom Checker containers

## Relationships
• Patients / Clinicians -> Media Gateway: Real-time video consultations [WebRTC over UDP/TCP/TLS]
• Media Gateway -> Regional Distributed Cache: Session metadata offloading [Redis Protocol]
• Load Balancer -> Media Gateway: Regional traffic routing & health checks [HTTPS]

## Technology Stack
• Google Cloud Platform (`europe-west3`, `us-central1`): Core cloud infrastructure ensuring data residency compliance.
• WebRTC with Coturn/Janus: Media transport supporting NAT traversal and TURN-over-TCP/TLS fallback for rural networks.
• Google Congestion Control (GCC): Congestion control algorithm for unstable rural links and bandwidth adaptation.
• OpenTelemetry: Real-time telemetry export for media quality and connection tracing.

## Rationale
• Regional deployments and strict circuit-breaking guarantee adherence to GDPR and HIPAA data residency constraints.
• Stateless proxy design, adaptive bitrate control, and reconnection buffering ensure high availability and graceful degradation for unstable rural connections.