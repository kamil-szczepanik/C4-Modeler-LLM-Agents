## Overview
The AWS Key Management Service (KMS) component provides cryptographic key management, envelope encryption, and access controls for the Real-Time Payment Fraud Screening system. It ensures PCI-DSS Level 1 compliance and meets sub-50ms latency requirements while protecting sensitive cardholder data.

## Key Elements
- **Key Management API Component**: Processes cryptographic requests from application containers via the AWS SDK.
- **Hardware Security Module (HSM) Interface Component**: Interfaces with FIPS 140-2 Level 3 validated dedicated HSMs for secure key storage and cryptographic operations.
- **Key Policy & Access Control Component**: Enforces IAM, SigV4 authentication, resource-based policies, and KMS Grant constraints.
- **Key Rotation & Lifecycle Manager Component**: Manages automated annual rotation of Customer Master Keys (CMKs) without downtime.

## Relationships
- **Fraud Scoring Engine and Case Management Service** -> **Key Management API**: Invokes via AWS SDK over `HTTPS/TLS 1.3` with `SigV4` authentication for envelope encryption and data key generation.
- **AWS KMS** -> **AWS CloudTrail & S3 Object Lock**: Exports tamper-evident audit logs via AWS CloudTrail for 7-year retention.

## Technology Stack
- **AWS KMS**: Managed cryptographic service to offload physical PCI-DSS audit burdens and enforce strict access controls.
- **FIPS 140-2 Level 3 Hardware Security Modules (HSMs)**: Hardware-backed security for storing and executing operations on Customer Master Keys.
- **AWS SDK (SigV4)**: Secure protocol for authenticating application requests to the KMS API.
- **AWS CloudTrail & S3 Object Lock**: Provides tamper-evident, long-term audit logging required for financial compliance.

## Rationale
This architecture uses envelope encryption with client-side data key caching to bypass high-frequency API throttling limits, ensuring the system achieves P99 latency below 50 ms. Additionally, managed HSMs and automated lifecycle controls reduce operational overhead, fitting the constraints of a 3-engineer team and a 25,000 EUR monthly budget.