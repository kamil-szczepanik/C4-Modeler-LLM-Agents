## Overview
The system is a hybrid cloud Clinic Management System that handles patient records, scheduling, and billing for healthcare facilities. It uses a zero-trust Istio service mesh to secure microservices across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- Sidecar Proxy (Envoy)
- Control Plane / Discovery (Istiod)
- Authorization Policy Engine (Envoy RBAC / SPIFFE/SPIRE)
- Cross-Network Gateway (Envoy Multi-Cluster Gateway)
- Telemetry Collector Adapter (Envoy OTel extension)
- Certificate Authority (CA) Controller (Istiod CA / Citadel with HashiCorp Vault)

## Relationships
- Sidecar Proxy to Microservices via mTLS (gRPC/HTTP/2)
- Control Plane to Sidecar Proxy via xDS API (gRPC)
- Sidecar Proxy to Cross-Network Gateway via Encrypted mTLS (TLS Passthrough/Termination over TCP)
- Sidecar Proxy to Telemetry Collector Adapter via gRPC/OTLP
- Control Plane/CA Controller to Sidecar Proxy via Secret Discovery Service (SDS / gRPC)

## Technology Stack
- Istio Service Mesh: Core framework for traffic management and security policies
- Envoy (C++): High-performance proxy for traffic interception and routing
- Istiod (Go): Central control plane for service discovery and configuration
- HashiCorp Vault: Secure key management for automated X.509 certificate generation
- OpenTelemetry / Prometheus / Loki: Observability stack for telemetry, metrics, and logs

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict zero-trust mTLS encryption and automated certificate rotation. The hybrid mesh configuration guarantees 99.99% availability across on-premises and cloud environments.