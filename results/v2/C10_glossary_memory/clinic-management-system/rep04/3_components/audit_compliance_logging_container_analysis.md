## Overview
The Audit & Compliance Logging Container provides immutable, tamper-proof security event logging and regulatory reporting for the Clinic Management System. It ensures strict HIPAA and GDPR compliance with a mandatory 10-year data retention lifecycle.

## Key Elements
- Compliance Officer [person]
- Audit Collector Component [container component] (Spring Integration)
- Compliance Query Service Component [container component] (Spring MVC)
- Audit Indexing & Tokenization Service Component [container component]
- WORM Storage Adapter Component [container component] (AWS S3 Compliance Mode / Object Lock)
- Message Broker [container] (RabbitMQ/Kafka)

## Relationships
- Compliance Officer -> Compliance Query Service Component: HTTPS (TLS 1.3, OAuth2/OIDC, MFA)
- Message Broker -> Audit Collector Component: AMQP
- Audit Collector Component -> Audit Indexing & Tokenization Service Component: gRPC over mTLS
- Audit Indexing & Tokenization Service Component -> WORM Storage Adapter Component: S3 API / TLS 1.3 (AES-256 at rest)

## Technology Stack
- Java/Spring Boot: Foundation for reliable, enterprise-grade log processing and microservice integration
- Spring Integration / Spring MVC: Efficient message consumption and secure REST query endpoints
- AWS S3 Object Lock (WORM): Enforces tamper-proof, ≥ 10-year data retention compliance
- AWS KMS: Envelope encryption with AES-256 at rest and automated key rotation

## Rationale
This architecture guarantees strict adherence to HIPAA and GDPR mandates through immutable WORM storage, cryptographic log chaining, and strict least-privilege trust boundaries. It balances regulatory accountability with data minimization by tokenizing PHI while providing rapid access-log reporting for compliance audits.