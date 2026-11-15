## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient records, scheduling, and billing while ensuring 99.99% uptime. It streamlines clinical workflows and financial operations while enforcing strict HIPAA and GDPR compliance mandates.

## Key Elements
- **Users**: Billing Specialist, Compliance Officer, Patient, Clinician
- **External Systems**: Insurance / Payer System, Lab & Imaging Systems
- **Containers**: Web Frontend, Patient Portal, API Gateway, EMR Service, Billing / Claims Service
- **Infrastructure**: on-prem-k8s cluster, AWS (eu-central-1), KEDA auto-scaling worker pools
- **Security & Support Tools**: HashiCorp Vault, OpenTelemetry sidecars, Audit Logging WORM sidecars

## Relationships
- **API Gateway -> Billing / Claims Service**: Forwards billing requests via gRPC/REST over mTLS
- **Billing / Claims Service -> Insurance / Payer System**: Submits insurance claims and real-time eligibility checks via Secure HTTPS with DLQ and TLS 1.3
- **Billing / Claims Service -> HashiCorp Vault**: Fetches dynamic encryption keys via mTLS
- **Billing / Claims Service -> Cold Object Storage**: Archives closed claims using immutable WORM policies

## Technology Stack
- **Compute & Orchestration**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) with KEDA for event-driven scaling
- **Security**: HashiCorp Vault for dynamic secrets and AES-256 field-level encryption
- **Protocols & Communication**: gRPC, REST, mTLS, SPIFFE/SPIRE, and TLS 1.3
- **Observability**: OpenTelemetry sidecars and synthetic monitoring for SLI tracking

## Rationale
This hybrid architecture pairs on-premises Kubernetes control with scalable AWS cloud workers to handle spiky batch workloads and external payer dependencies. Strict ABAC, WORM storage tiers, and AES-256 encryption ensure regulatory compliance and secure long-term data retention.