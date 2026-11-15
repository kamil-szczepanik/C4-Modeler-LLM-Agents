## Overview
The API Gateway / Edge Proxy acts as the secure entry point for the Clinic Management System, routing all external traffic to internal microservices. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and resilient hybrid cloud traffic management.

## Key Elements
- API Gateway / Edge Proxy (Envoy)
- TLS Termination & SSL Offloading Engine
- Authentication & Authorization Filter
- Rate Limiting & Threat Protection (with local token fallback)
- Routing & Load Balancing Core
- Priority & Traffic Shaping Filter
- Egress DLP & Sanitization Filter
- Telemetry & Distributed Tracing Sidecar

## Relationships
- Patient / Clinician / Receptionist / Billing Staff -> API Gateway / Edge Proxy [HTTPS / WSS]
- API Gateway / Edge Proxy -> Identity Provider [HTTPS]
- API Gateway / Edge Proxy -> Core Clinical & EMR Service [gRPC over Istio mTLS]
- API Gateway / Edge Proxy -> Scheduling & Billing Service [gRPC over Istio mTLS]
- Telemetry Sidecar -> Prometheus / Grafana [OpenTelemetry / Prometheus metrics]

## Technology Stack
- **Envoy:** Chosen as the edge proxy for native gRPC and Istio integration.
- **Istio Service Mesh:** Provides mTLS zero-trust encryption and xDS dynamic configuration.
- **Redis:** Used for distributed rate limiting, paired with local token-bucket fallbacks.
- **TLS 1.3:** Enforced for secure transport-layer encryption.
- **W3C Trace Context:** Used for distributed tracing and audit logging.

## Rationale
This architecture uses Envoy and Istio to meet high availability (99.99%) across hybrid environments (`on-prem-k8s` and `eu-central-1`). Built-in filtering, DLP, and token validation satisfy stringent HIPAA, GDPR, and latency requirements.