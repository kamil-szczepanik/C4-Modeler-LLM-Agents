## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and resilient access for rural users.

## Key Elements
- Patients and Licensed Clinicians (External Users)
- GCP Cloud Load Balancing (Edge TLS Termination & HTTP/3 Edge)
- GCP Cloud Armor (Global WAF & Geo-Routing Engine)
- Envoy Proxy (Auth & Consent Inspection Proxy)
- Envoy Proxy (mTLS Upstream Dispatcher)
- Core Telehealth Backend, AI Symptom Checker Service, and Consent Service (Regional Backends)

## Relationships
- Patients and Licensed Clinicians -> GCP Cloud Load Balancing: Sends edge requests [HTTPS / HTTP/3 / WSS / WebRTC]
- GCP Cloud Load Balancing -> GCP Cloud Armor: Inspects inbound traffic [HTTPS / HTTP/3]
- GCP Cloud Armor -> Auth & Consent Inspection Proxy: Forwards valid regional traffic [HTTP/2]
- Auth & Consent Inspection Proxy -> mTLS Upstream Dispatcher: Forwards validated requests [gRPC]
- mTLS Upstream Dispatcher -> Regional Backends: Routes secure internal traffic [gRPC / mTLS]

## Technology Stack
- GCP Cloud Load Balancing & Cloud Armor: Selected for edge termination, geo-routing, and DDoS mitigation to enforce regional data residency.
- Envoy Proxy: Chosen for low-latency routing, OAuth2/OIDC validation, consent inspection, and W3C trace context injection.
- HTTP/3 (QUIC): Implemented at the edge to support rural patients with unstable connections below 300 kbit/s.
- GCP Secret Manager: Utilized with workload identity for dynamic mTLS certificate provisioning without static secrets.

## Rationale
This architecture enforces regional data separation between `europe-west3` and `us-central1` to meet GDPR and HIPAA mandates while ensuring traceability for EU MDR compliance. Edge-optimized protocols maintain high availability and video consultation continuity for users with degraded internet connections.