## Overview
The Messaging & Observability Infrastructure provides secure event streaming, service mesh telemetry, secrets management, and GitOps deployments for the Clinic Management System. It guarantees high availability, strict HIPAA/GDPR compliance, and zero data loss across hybrid cloud boundaries.

## Key Elements
* **Event Broker Component**: Apache Kafka (KRaft mode) for asynchronous event streaming.
* **Service Mesh**: Istio Envoy sidecars enforcing zero-trust networking.
* **Secrets Management Component**: HashiCorp Vault for dynamic secrets and encryption keys.
* **Telemetry Collector & Monitoring**: OpenTelemetry Collector, Prometheus, and Grafana.
* **GitOps Engine**: ArgoCD for declarative deployments.

## Relationships
* **Service-to-Service**: Istio mTLS (strict mode) for secure microservice communication.
* **Event Streaming**: TCP via SASL/SCRAM over TLS 1.3 with application-layer envelope encryption for Kafka.
* **Secrets & Identity**: HTTPS (REST/Transit API) with Kubernetes Service Account JWTs for Vault authentication.
* **Telemetry Pipeline**: OTLP/gRPC for metrics and traces routed through OpenTelemetry scrubbing filters to Prometheus and Grafana.
* **Deployments**: HTTPS via Kubernetes API for ArgoCD cluster synchronization.

## Technology Stack
* **Apache Kafka (KRaft)**: Chosen for distributed event streaming without ZooKeeper overhead, ensuring 99.99% availability.
* **Istio & Envoy**: Selected to provide strict mTLS and real-time service mesh telemetry.
* **HashiCorp Vault**: Implemented for dynamic secret injection and AES-256 key management.
* **OpenTelemetry, Prometheus & Grafana**: Deployed for observable, scrubbed, and sanitized system metrics.
* **ArgoCD**: Utilized for automated, auditable GitOps deployments with strict sync waves.

## Rationale
This architecture decouples core clinical services from billing and scheduling, protecting front-desk responsiveness and preventing localized outages. Comprehensive encryption, real-time log sanitization, and immutable WORM audit streaming satisfy stringent HIPAA and GDPR regulatory mandates.