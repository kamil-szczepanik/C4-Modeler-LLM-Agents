## Overview
[The Rule/Model Authoring Service manages, validates, and securely publishes fraud detection rules and ONNX scoring models for a real-time payment processor.]
[It provides zero-downtime updates, simulation sandboxes, and immutable audit trails while ensuring PCI-DSS Level 1 compliance.]

## Key Elements
- Risk Rule Author & Data Scientist (Users)
- Rule Authoring Controller (Spring Boot / Java REST API)
- Drools Rule Engine / DRL Compiler (Rule validation component)
- Model Validation Service (Security scanning and constraint validation worker)
- Simulation Worker (AWS Lambda for dry-run testing)
- Authoring Database (Amazon DynamoDB with Point-in-Time Recovery)
- Amazon SQS (Message broker for rule publishing and simulation triggers)
- AWS Backup Immutable Vaults (Compliance and audit storage)

## Relationships
- Rule Authoring Controller -> Authoring Database: Reads/Writes draft rules via AWS SDK (HTTPS)
- Rule Authoring Controller -> Simulation Worker: Triggers dry-runs via Amazon SQS
- Rule Authoring Controller -> Amazon SQS: Publishes cryptographically signed rule/model packages via AWS SDK (SQS)
- Simulation Worker -> Amazon S3: Accesses historical sample data via HTTPS

## Technology Stack
- Java / Spring Boot: Chosen for the authoring backend to maintain ecosystem consistency
- Amazon DynamoDB: Selected for low-latency storage of draft and historical versions within budget
- AWS Lambda: Used for serverless simulation workloads to minimize steady-state compute costs
- AWS KMS: Provides cryptographic keys for signing packages and encrypting data at rest

## Rationale
[This architecture uses serverless compute and managed AWS services to keep operational overhead manageable for a three-engineer team within a 25k EUR monthly budget.]
[Strict cryptographic signing, RBAC four-eyes approvals, and immutable backups satisfy PCI-DSS Level 1 and 7-year audit requirements without compromising real-time performance.]