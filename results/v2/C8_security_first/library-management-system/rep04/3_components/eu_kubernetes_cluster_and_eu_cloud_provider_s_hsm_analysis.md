## Overview
The EU Kubernetes Cluster and HSM container orchestrates resilient microservices and secures cryptographic keys exclusively within EU data centers. It guarantees strict EU-only data residency while maintaining the 99th-percentile search response time under 800 ms.

## Key Elements
- Kubernetes Control Plane & Worker Nodes
- Istio Service Mesh (Sidecars)
- HSM Crypto-Plugin / PKCS#11 Daemon & External Secrets Operator
- SPIRE Agent & Server DaemonSet
- OpenTelemetry Collector & KEDA
- EU Cloud Provider's Hardware Security Module (HSM)

## Relationships
- Microservices communicate internally using mTLS via gRPC over Istio service mesh.
- External Secrets Operator connects to the Cloud HSM using KMIP/PKCS#11 over TLS 1.3.
- SPIRE Agent provisions workload identities to pods using SPIFFE/SPIRE protocols.
- OpenTelemetry Collector gathers telemetry metrics and traces to feed KEDA autoscaling.

## Technology Stack
- Kubernetes (Containerd): Bare-metal instances hosted in EU region for strict data residency compliance.
- Istio & Cilium: Provides zero-trust mTLS and network policy enforcement.
- PKCS#11 / KMIP: Cryptographic interface for secure envelope encryption and key wrapping.
- External Secrets Operator & KEDA: Manages secrets injection and event-driven autoscaling.
- OpenTelemetry: Monitors cryptographic latency to protect the search SLA.

## Rationale
The architecture enforces rigorous EU data residency through localized bare-metal nodes and HSM integration. Cryptographic offloading, DEK caching, and KEDA autoscaling maintain the < 800 ms search SLA under peak academic library loads.