## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability, strict regulatory compliance, and seamless interoperability for clinical operations.

## Key Elements
- **Users**: Front Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Compliance Officer
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouse APIs, Identity Provider (IdP), SMS/Email Notification Gateway
- **Containers**: React SPA / Mobile Client, Kong/NGINX API Gateway, Istio Service Mesh, Spring Boot/Node.js Patient & Scheduling Service, Python/Go EMR Service, Spring Boot Billing Service, Apache Camel Integration Service, Spring Boot Audit Service, PostgreSQL Clusters, Redis Enterprise
- **Service Mesh Components**: Sidecar Proxy (Envoy), Control Plane (Istiod), Telemetry Collector (Prometheus/OpenTelemetry), Ingress/Egress Gateways, Resilience & Policy Engine

## Relationships
- **Client to API Gateway**: HTTPS / TLS 1.3
- **Services to Sidecar Proxies**: localhost via HTTP / gRPC
- **Sidecar Proxies across mesh**: mTLS / TCP / gRPC over TLS 1.3
- **Sidecar Proxies to Telemetry Collectors**: OpenTelemetry Protocol (OTLP)
- **Integration Service to External Systems**: HL7 FHIR APIs over HTTPS

## Technology Stack
- **Kubernetes / Hybrid Cloud**: Deployed across on-premise Kubernetes and AWS (`eu-central-1`) to meet availability and residency constraints.
- **Istio Service Mesh**: Provides mTLS, zero-trust security, distributed tracing, and traffic management.
- **Envoy**: Acts as sidecar proxies and hybrid boundary gateways for secure cross-network communication.
- **Prometheus / OpenTelemetry**: Gathers centralized metrics and trace spans for HIPAA/GDPR audit trails.
- **ArgoCD**: Implements GitOps-based declarative deployment for Istio control plane and gateway configurations.

## Rationale
This hybrid architecture uses an Istio service mesh and Envoy sidecars to enforce strict zero-trust security and end-to-end encryption (mTLS) required for HIPAA and GDPR compliance. Automated circuit-breaking and hybrid gateways guarantee 99.99% availability and low-latency EMR access by preventing cascading failures across distributed workloads.