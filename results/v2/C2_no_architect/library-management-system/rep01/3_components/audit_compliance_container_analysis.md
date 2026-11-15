## Overview
The Audit & Compliance Container is a secure backend component of the Library Management System that enforces strict EU data residency and GDPR compliance. It provides tamper-evident logging, cryptographic verification, and a read-only compliance dashboard for Data Protection Officers.

## Key Elements
- **Data Protection Officers (DPOs) / Compliance Auditors**: Primary compliance stakeholders accessing audit logs and reports.
- **System Administrators**: Operations stakeholders responsible for security forensics and system oversight.
- **Audit & Compliance Container**: Core Kubernetes-based container managing audit ingestion, storage, and reporting.
- **EU-localized HSM**: Hardware Security Module providing cryptographic log signing and envelope encryption.
- **WORM Storage**: Write-once-read-many storage for immutable, long-term log retention.
- **API Gateway**: Entry point mediating traffic via mTLS and OAuth2/OIDC.
- **Centralized Logging & SIEM Service**: External system receiving security and tamper alerts.

## Relationships
- **API Gateway -> Audit & Compliance Container**: Routes audit requests and compliance queries via mTLS using SPIFFE/SPIRE.
- **Audit & Compliance Container -> EU-localized HSM**: Performs cryptographic log signing and envelope encryption via local cloud region connectivity.
- **Audit & Compliance Container -> WORM Storage**: Streams encrypted, Merkle-tree-structured audit logs for immutable retention.
- **Audit & Compliance Container -> Centralized Logging & SIEM Service**: Sends automated alerts for tampering, queue saturation, or disk exhaustion.

## Technology Stack
- **Kubernetes**: Container orchestration platform ensuring scalable deployment of the audit service.
- **EU-localized HSM**: Secures cryptographic operations to satisfy strict EU data residency constraints.
- **LUKS**: Encrypts local spillover disks for secure asynchronous log buffering during outages.
- **Prometheus**: Collects metrics on HSM response times, log ingestion lag, and certificate rotation.
- **Merkle Tree Structure**: Cryptographically ensures log tamper-evidence prior to WORM storage streaming.

## Rationale
This architecture guarantees strict adherence to EU-only data residency and GDPR mandates by isolating cryptographic operations within an EU-localized HSM and writing to immutable WORM storage. Asynchronous buffering with LUKS-encrypted spillover disks and dedicated read replicas protect system availability and high-performance search SLAs while providing robust audit capabilities.