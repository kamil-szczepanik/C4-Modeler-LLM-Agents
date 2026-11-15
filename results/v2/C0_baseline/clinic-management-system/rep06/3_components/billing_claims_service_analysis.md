## Overview
- Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
- Operates in a hybrid cloud infrastructure ensuring HIPAA and GDPR compliance with 99.99% availability.

## Key Elements
- Billing & Claims Service (Java Spring Boot container)
- Claim Scrubbing Component (Drools / Spring Component)
- Claim Management Component (Spring MVC/Data)
- Payment Processing Component
- Dispute Management Component (Spring REST)
- Billing Archive Component
- Third-Party Payment & Insurance Gateway
- AWS S3 Object Lock
- HashiCorp Vault
- Patient Portal Frontend (React)
- Audit & Compliance Service

## Relationships
- Claim Scrubbing Component -> Claim Management Component: Passes validated claims [In-memory Java Method Call]
- Claim Management Component -> Third-Party Payment & Insurance Gateway: Real-time eligibility & submission [REST/JSON, mTLS, Async Message Broker]
- Dispute Management Component -> Audit & Compliance Service: Logs dispute actions [gRPC, mTLS]
- Patient Portal Frontend -> Dispute Management Component: Submits billing disputes [REST/JSON, OAuth2, mTLS]
- Billing Archive Component -> AWS S3 Object Lock: Encrypted long-term retention [HTTPS, AWS SDK]

## Technology Stack
- Java Spring Boot: Core framework for microservices providing robust enterprise capabilities.
- Drools / Spring Component: Local rules engine for offline claim scrubbing and error prevention.
- AWS S3 Object Lock: WORM storage ensuring immutable 10-year data retention.
- HashiCorp Vault: Secret management for envelope encryption and PHI data protection.
- PostgreSQL: Relational database for active transactional clinical and billing data.

## Rationale
- The hybrid architecture isolates sensitive billing workflows while leveraging cloud object storage for cost-effective, long-term regulatory compliance. Component decomposition ensures high performance, strict zero-trust security, and 99.99% uptime.