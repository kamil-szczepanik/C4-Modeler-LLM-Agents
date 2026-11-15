## Overview
The system is a hybrid-cloud Clinic Management System designed to handle patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It leverages an Istio service mesh to enforce strict zero-trust security, mTLS encryption, and high availability across on-premise Kubernetes clusters and AWS (`eu-central-1`).

## Key Elements
- **Istiod (Control Plane)**: Manages configuration, cert issuance, and xDS policy pushes (Tech: *Go*).
- **Istio CNI Plugin**: Manages pod network redirection without privileged init containers (Tech: *Kubernetes CNI*).
- **Envoy Sidecar Proxies**: Injected alongside microservices for traffic management and telemetry (Tech: *Envoy C++*).
- **East-West Gateway**: Handles cross-network mTLS and service discovery between hybrid clusters (Tech: *Envoy Gateway*).
- **Telemetry Provider**: Aggregates metrics and distributed traces (Tech: *Prometheus, OpenTelemetry Collector*).

## Relationships
- `Istiod` configures `Envoy Sidecar Proxies` via **gRPC (xDS API)**.
- `Envoy Sidecar Proxies` enforce mTLS between internal microservices via **Mutual TLS over TCP**.
- `Envoy Sidecar Proxies` route cross-cluster traffic through the **East-West Gateway** via **mTLS over TCP**.
- `Envoy Sidecar Proxies` export metrics and traces to the **Telemetry Provider** via **OTLP / gRPC (TLS encrypted)**.

## Technology Stack
- **Istiod**: Selected for reliable multi-replica control plane management and automated cert distribution.
- **Istio CNI**: Chosen to eliminate privileged init containers and reduce the Kubernetes attack surface.
- **HashiCorp Vault**: Integrated as an external CA for secure enterprise PKI and leaf certificate rotation.
- **OpenTelemetry / Prometheus**: Deployed to ensure secure, encrypted telemetry collection for HIPAA compliance.

## Rationale
This architecture uses an enterprise service mesh to fulfill strict HIPAA/GDPR security mandates through enforced strict mTLS and external HashiCorp Vault PKI integration. Furthermore, multi-replica control planes, East-West gateways, and circuit breaking guarantee the 99.99% availability and low-latency performance required for clinical operations across hybrid environments.