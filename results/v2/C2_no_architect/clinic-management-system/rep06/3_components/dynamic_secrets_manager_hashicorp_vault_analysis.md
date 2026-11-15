## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, high availability, and secure clinical data handling across a hybrid cloud infrastructure.

## Key Elements
- System Administrator / DevOps Engineer
- Security / Compliance Officer
- Dynamic Secrets Manager (HashiCorp Vault)
- EMR Service & Billing / Claims Service
- AWS KMS / On-prem HSM

## Relationships
- Workloads authenticate to Dynamic Secrets Manager via AppRole and Kubernetes Service Account JWT over mTLS (SPIFFE/SPIRE).
- Dynamic Secrets Manager connects to AWS KMS / On-prem HSM for automated unsealing via encrypted transport channels.
- Vault telemetry exports metrics to the OpenTelemetry pipeline for availability monitoring.
- Break-glass audit events write immutable logs to the WORM audit sidecar.

## Technology Stack
- HashiCorp Vault: Dynamic secret management with short-lived credentials to minimize leak blast radiuses.
- Distributed Raft Storage: Multi-region storage backend with encrypted inter-node traffic for high availability.
- AWS KMS / On-prem HSM: Automated cluster unsealing to prevent manual downtime during restarts.
- AES-256 and TLS 1.3: Data encryption at rest and in transit across hybrid boundaries.

## Rationale
This architecture ensures 99.99% uptime through active-active replication and automated unsealing while satisfying strict HIPAA and GDPR security mandates. Short-lived credentials, least-privilege scoping, and immutable audit logs comprehensively protect patient health information.