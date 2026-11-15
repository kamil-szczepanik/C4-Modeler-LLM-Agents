## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It utilizes GCP infrastructure to ensure GDPR and HIPAA compliance while supporting low-bandwidth rural users.

## Key Elements
- Patients & Licensed Clinicians
- GCP Cloud Armor and Cloud CDN
- Istio API Gateway Container
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- WebRTC SFU Media Servers
- AI Symptom Checker Container
- Google Cloud Logging and Monitoring

## Relationships
- Patients & Licensed Clinicians -> GCP Cloud Armor and Cloud CDN: Accesses platform via [HTTPS (TLS 1.3), WebRTC]
- GCP Cloud Armor and Cloud CDN -> API Gateway Container: Routes inspected traffic via [HTTPS, Istio mTLS]
- Cloud Armor / CDN -> Google Cloud Monitoring: Streams security telemetry, WAF logs, and cache metrics via [OpenTelemetry, Google Cloud Logging API]

## Technology Stack
- GCP Cloud Armor: Provides edge WAF inspection, OWASP Top 10 rules, adaptive DDoS protection, and rate-limiting.
- Cloud CDN: Caches static frontend assets and WebRTC client shell to support low-bandwidth users (R-06), strictly excluding PHI.
- Terraform: Defines security policies and CDN rules as code for deployment parity across regions.
- Google Cloud Monitoring: Collects WAF block logs, cache-hit ratios, and trace contexts.

## Rationale
This architecture uses GCP edge services to enforce security and optimize performance without compromising data residency constraints. Edge caching and TLS 1.3 termination secure communications while maintaining resilience for unstable connections.