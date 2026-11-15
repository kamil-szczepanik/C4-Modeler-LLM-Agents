## Overview
The Core Clinical & EMR Container manages patient admissions, electronic medical records, and tamper-proof audit trails for the Clinic Management System. It ensures high-performance, secure clinical workflows across hybrid cloud environments.

## Key Elements
- Admission & Demographics Component
- EMR Clinical Core Component
- Audit Trail Manager
- Data Access Layer / Encryption Engine
- Redis L2 Cache Layer

## Relationships
- Admission & Demographics & EMR Clinical Core -> Data Access Layer: In-process method calls [Java]
- EMR Clinical Core -> Redis L2 Cache: Read/Write active clinical data [TCP/RESP over mTLS]
- EMR Clinical Core -> Audit Trail Manager: Async event publishing [Spring Application Events]
- Audit Trail Manager -> Audit Sidecar Container: Push batched cryptographic logs [gRPC]
- Core Clinical & EMR Container -> External PostgreSQL: Database transactions [mTLS and IAM authentication]

## Technology Stack
- Spring Boot 3 / Java 21: Framework providing robust dependency injection and enterprise readiness
- Hibernate with custom types: Enables field-level AES-256 encryption at rest
- Redis L2 Cache: Accelerates active EMR reads while maintaining encrypted PHI
- HashiCorp Vault: Manages dynamic secrets and cryptographic keys for zero-trust security

## Rationale
This architecture decouples stateful components to ensure 99.99% availability and compliance with HIPAA and GDPR regulations. Layered caching and asynchronous auditing successfully balance strict security mandates with sub-second EMR load time requirements.