## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient admissions, electronic medical records, scheduling, and billing for healthcare facilities while ensuring strict HIPAA and GDPR compliance. It provides 99.99% high availability and local data retention to support clinicians and administrators.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, and Compliance Officers
- Web Frontend, Patient Portal/Mobile App, and API Gateway (OAuth2/OIDC, ABAC)
- EMR Service and Billing/Claims Service (gRPC/REST over mTLS, SPIFFE/SPIRE)
- OpenTelemetry sidecars and Audit Logging sidecars (WORM)
- Dynamic Secrets Manager (HashiCorp Vault)
- On-premises Kubernetes cluster (on-prem-k8s) and AWS Cloud (eu-central-1)
- External Systems: Insurance/Payer System, Lab & Imaging Systems (HL7 FHIR)

## Relationships
- Patients and staff access services via Web/Mobile apps using HTTPS.
- Web and mobile clients communicate with internal microservices through the API Gateway using OAuth2/OIDC.
- Microservices communicate internally via gRPC/REST secured by mutual TLS (mTLS) with SPIFFE/SPIRE identities.
- EMR and billing services integrate with external Lab, Imaging, and Payer systems using HL7 FHIR APIs.
- The on-prem-k8s cluster synchronizes with AWS (eu-central-1) for disaster recovery using Anycast DNS and encrypted IPsec VPN/MACsec interconnects.

## Technology Stack
- **Orchestration:** Kubernetes (on-prem-k8s) for container management with GitOps (ArgoCD) for declarative deployments.
- **Security:** HashiCorp Vault for dynamic secrets and AES-256 encryption at rest; TLS 1.3 for ingress; SPIFFE/SPIRE for mTLS.
- **Observability:** OpenTelemetry sidecars with Prometheus and Grafana for SLO-based telemetry.
- **Storage & HA:** Synchronous multi-node replication (Ceph/Rook) with $N+2$ node buffering for strict RTO/RPO.
- **Interoperability:** HL7 FHIR standards for external clinical integrations.

## Rationale
This hybrid architecture keeps sensitive protected health information (PHI) under local institutional control on-premises to satisfy strict HIPAA and GDPR data residency mandates. Simultaneously, it leverages cloud elasticity in AWS (eu-central-1) and automated failover to guarantee 99.99% availability and high-performance EMR access.