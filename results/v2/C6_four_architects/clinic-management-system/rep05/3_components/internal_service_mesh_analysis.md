## Overview
The Internal Service Mesh manages secure, reliable, and observable communication across the Clinic Management System microservices. It enforces zero-trust boundaries and regulatory compliance across hybrid Kubernetes clusters.

## Key Elements
- Control Plane (`istiod` with Go)
- Data Plane Sidecars (`Envoy Proxy`)
- Telemetry & Policy Enforcer (Telemetry v2)
- Ingress/Egress Gateway Proxies (`Envoy Gateway`)
- Authorization Policy Controller (embedded in `istiod`)
- East-West Gateways

## Relationships
- Microservices route traffic through local **Envoy Proxy** using standard TCP/HTTP.
- **Envoy Proxies** communicate via **mTLS over gRPC/HTTP2** for AES-256 encryption in transit.
- **Control Plane (`istiod`)** pushes policies via **xDS APIs over gRPC**.
- **Envoy Proxies** stream metrics to **Prometheus** via **OTLP/gRPC**.
- **API Gateway** routes external traffic via **HTTPS/gRPC** through **Ingress Gateways**.
- Hybrid clusters synchronize via **East-West Gateways** using **mTLS over gRPC**.

## Technology Stack
- Istiod & Envoy Proxy: Chosen for industry-standard service mesh capabilities and native Kubernetes integration.
- Prometheus & OTLP/gRPC: Selected for low-latency telemetry and compliance audit logging.
- mTLS & xDS: Implemented to satisfy strict HIPAA/GDPR encryption and dynamic policy enforcement.

## Rationale
This architecture ensures 99.99% availability and zero-trust security across a hybrid cloud topology without modifying application logic. It directly satisfies HIPAA and GDPR mandates for data protection and auditability.