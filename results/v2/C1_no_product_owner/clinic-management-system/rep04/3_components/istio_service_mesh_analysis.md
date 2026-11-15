## Overview
[The Clinic Management System utilizes an Istio Service Mesh to secure, observe, and manage microservices communication across hybrid Kubernetes environments.]
[It guarantees HIPAA/GDPR compliance, 99.99% uptime, and zero-trust security for clinical workflows.]

## Key Elements
- Istiod Control Plane: Replicated deployment managing xDS configuration, certificate authority duties, and SPIFFE/SPIRE workload identities.
- Envoy Sidecar Proxies: Injected into microservice pods to handle traffic management, TLS 1.3 termination, and `AuthorizationPolicies`.
- Istio Ingress/Egress Gateways: Envoy-based gateways managing traffic crossing the service mesh boundary.
- Telemetry & Audit Exporter: Sub-component streaming Envoy access logs and RBAC enforcement decisions to the WORM audit store.

## Relationships
- Istiod configures Envoy Sidecars and Gateways via xDS over gRPC.
- Microservices communicate inter-service via Envoy Sidecars using Mutual TLS (mTLS via TLS 1.3 over TCP).
- API Gateway routes traffic into the mesh via the Istio Ingress Gateway using HTTPS/gRPC.
- Telemetry & Audit Exporter streams audit logs asynchronously to the WORM Audit Log Store via OTLP over gRPC.

## Technology Stack
- Istio / Istiod Control Plane: Manages service discovery and proxy configuration with high availability (replica count ≥ 3).
- Envoy Proxy: Handles traffic routing, sidecar injection, and gateway operations.
- SPIFFE/SPIRE: Provides workload identity and zero-trust authentication.
- TLS 1.3: Enforces secure cryptographic cipher suites for data-in-transit.
- Fluentbit / OTLP: Transmits audit logs securely to backend storage.

## Rationale
[Independent cluster-local control planes eliminate WAN split-brain risks, ensuring high availability across on-premise and AWS eu-central-1 clusters.]
[Strict mTLS, SPIFFE identities, and automated OPA policy gating enforce zero-trust security to meet HIPAA and GDPR compliance mandates.]