## Overview
[Component C4 architecture for the File Storage Container within the Library Management System, designed to securely manage digital asset cataloging while strictly enforcing EU data residency.]

## Key Elements
- File Controller / API Router (Spring WebFlux / Java)
- Presigned URL Generator
- Virus & Malware Scanner Service (ClamAV via FastAPI / Python)
- Storage Abstraction Manager (AWS SDK for Java)
- Audit Logging & Access Policy Enforcer (AWS IAM / CloudTrail)
- AWS S3 EU-Central (EU-Central-1 Region)

## Relationships
- Integration Service -> File Controller [HTTPS/REST]: Uploads/downloads digital assets and requests secure tokens
- File Controller -> Audit Logging & Access Policy Enforcer [In-Memory Java Call]: Validates IAM permissions and EU residency
- File Controller -> Presigned URL Generator [In-Memory]: Issues time-limited S3 upload/download tokens
- Presigned URL Generator -> AWS S3 EU-Central [HTTPS/SigV4]: Direct client data transfer
- File Controller -> Virus & Malware Scanner [Internal gRPC]: Triggers asynchronous security scan
- Virus & Malware Scanner -> Storage Abstraction Manager [Internal gRPC]: Signals clean scan status for quarantine-to-production promotion
- Storage Abstraction Manager -> AWS S3 EU-Central [HTTPS/SigV4]: Enforces AES-256 encryption-at-rest and bucket restrictions

## Technology Stack
- Spring WebFlux / Java: Non-blocking reactive streaming of metadata and API routing
- FastAPI / Python with ClamAV: Lightweight wrapper and daemon for secure virus/malware scanning
- AWS SDK for Java: Handles AWS S3 encryption-at-rest (AES-256) and IAM integration
- AWS S3 EU-Central-1: Ensures strict EU-only data residency and quarantine isolation

## Rationale
[This component architecture prevents network bottlenecks by offloading heavy binary transfers to direct S3 presigned URLs while ensuring robust security via ClamAV scanning and strict EU data residency enforcement.]