## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals. It utilizes a hybrid architecture combining an on-premise Kubernetes cluster with AWS (`eu-central-1`) to ensure high availability, disaster recovery, and strict regulatory compliance.

## Key Elements
- **AWS (`eu-central-1`)**: Cloud infrastructure serving as a warm-standby disaster recovery site.
- **Amazon EKS**: Pre-provisioned container compute fleets for stateless services.
- **Amazon Route 53**: DNS traffic management and automated health-check failover.
- **AWS KMS**: Customer-Managed Keys (CMKs) with annual rotation for data encryption.
- **AWS CloudTrail & Amazon GuardDuty**: Immutable audit logging and runtime threat detection.
- **HashiCorp Vault**: Dynamic secrets manager for ephemeral injection via mTLS sidecars.

## Relationships
- **`on-prem-k8s` -> AWS (`eu-central-1`)**: Asynchronous database replication and cross-boundary traffic over TLS 1.3 / mTLS (SPIFFE/SPIRE).
- **Amazon Route 53 -> On-Prem / AWS EKS**: Automated health-check based traffic routing during failover events.
- **AWS EKS -> AWS KMS**: Cryptographic operations using AES-256 for data at rest.
- **AWS CloudTrail -> WORM Audit Sidecars**: Immutable security and access log synchronization.

## Technology Stack
- **Cloud Provider**: Hybrid (On-premise Kubernetes and AWS `eu-central-1`) for active-passive disaster recovery.
- **Container Orchestration**: Amazon EKS with pre-warmed node fleets to guarantee an RTO under 60 seconds.
- **Security & Encryption**: TLS 1.3, mTLS via SPIFFE/SPIRE, and AWS KMS (AES-256) for data protection.
- **Identity & Compliance**: AWS IAM with Attribute-Based Access Control (ABAC), Organizations SCPs, and CloudTrail.

## Rationale
This hybrid warm-standby architecture mitigates the split-brain risks and latency spikes of multi-master sync while guaranteeing a 60-second RTO and sub-second EMR performance. Utilizing AWS `eu-central-1` with KMS, CloudTrail, and EKS satisfies stringent HIPAA, GDPR, and 10-year data retention mandates.