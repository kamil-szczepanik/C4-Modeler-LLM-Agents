## Overview
[The Clinic Management System (CMS) manages patient records, scheduling, and billing for clinical environments. It leverages a hybrid-cloud architecture to ensure high availability and regulatory compliance.]

## Key Elements
- Temporal Frontend Service (Go)
- Temporal History Service (Go)
- Temporal Matching Service (Go)
- Temporal Worker Service (Go)
- Temporal Persistence Layer (PostgreSQL)
- Temporal Cluster Membership / Membership Service (Go/Ringpop)
- Temporal Crypt Interceptor (Go)

## Relationships
- Frontend Service -> History Service [gRPC]
- History Service -> Matching Service [gRPC]
- Matching Service -> Worker Service [gRPC]
- History Service -> Temporal Persistence Layer [SQL/CQL over TLS]
- Matching Service -> Temporal Persistence Layer [SQL/CQL over TLS]
- All Temporal Services <-> Membership Service [gRPC / Custom TCP]
- Frontend & History Services -> Temporal Crypt Interceptor [In-memory Go interface]
- Temporal Crypt Interceptor -> Key Management Service (KMS) [HTTPS/REST over mTLS]

## Technology Stack
- Go: Chosen for high concurrency, low latency, and robust memory management in distributed orchestration.
- PostgreSQL: Ensures ACID compliance and supports AES-256 encryption at rest for HIPAA/GDPR standards.
- Ringpop: Provides gossip-based node discovery and cluster health management for active-active high availability (99.99%).
- Crypt Interceptor with KMS: Secures Protected Health Information (PHI) via application-layer payload encryption.

## Rationale
[This component-based architecture ensures 99.99% uptime through active-active clustering and fault-tolerant state management. It strictly enforces HIPAA/GDPR compliance via application-layer payload encryption and secure hybrid-cloud persistence.]