## Overview
[The system provides cross-border telehealth services including video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Core architecture enforces regional data residency while ensuring low-latency, resilient media streaming for unstable networks.]

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- WebRTC SFU Video Streaming Containers (GCP Kubernetes)
- OpenTelemetry Observability Sidecar Agents
- Regional GCP Load Balancers and API Gateways
- Regional Distributed Cache / Redis for Session Handover
- Regional GCP Secret Manager

## Relationships
- Patients and Clinicians -> WebRTC SFU Video Streaming Containers: Streams video consultations [WebRTC/UDP]
- WebRTC SFU Containers -> Regional API Gateways: Manages session routing and signaling [gRPC/REST]
- WebRTC SFU Containers -> Redis: Stores stateless session handover tokens [TCP]
- OpenTelemetry Sidecar -> WebRTC SFU Containers: Captures real-time packet loss, jitter, and bitrate metrics

## Technology Stack
- WebRTC SFU: Powers selective forwarding unit video streaming for low-latency multi-party consultations
- OpenTelemetry: Captures real-time container metrics and telemetry for automated scaling and health checks
- Redis: Manages low-latency distributed caching for stateless SFU session tokenization and resumption
- GCP Kubernetes (GKE): Provides container orchestration with optimized CNI networking and explicit UDP ephemeral port ranges
- GCP Secret Manager: Injects immutable configuration and secrets securely into container runtimes

## Rationale
[This architecture fits requirements by isolating workloads into region-specific GCP environments to strictly satisfy GDPR and HIPAA data residency rules. Furthermore, implementing adaptive bitrate controls, stateless session handovers, and automated RTP packet shedding ensures robust video availability in unstable rural environments.]