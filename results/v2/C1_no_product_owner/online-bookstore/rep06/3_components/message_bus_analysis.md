## Overview
An online bookstore supporting physical and electronic book sales with recommendations and reviews. The architecture utilizes an AWS-based message bus for asynchronous communication.

## Key Elements
- **Event Publisher (AWS SNS Topics):** Fan-out messaging and broadcast of domain events.
- **Event Queue (AWS SQS Queues):** Reliable, durable queuing with SQS Long Polling.
- **Schema Validator:** Application-level validation enforcing JSON schema contracts.
- **Dead-Letter Queues (AWS SQS DLQ):** Failed message isolation and storage.
- **Monitoring & Security Controls:** AWS KMS, IAM least-privilege, AWS CloudWatch, and AWS CloudTrail.

## Relationships
- Order & Checkout -> Schema Validator [HTTPS]: Validates payload structure before publishing.
- Schema Validator -> Event Publisher [AWS Internal]: Forwards validated domain events.
- Event Publisher -> Event Queue [AWS Internal]: Fans out messages.
- Event Queue -> Engagement Service [SQS Long Polling]: Consumes events asynchronously.

## Technology Stack
- **AWS SNS/SQS:** Native AWS managed messaging for scalability and 99.95% availability.
- **TLS 1.3 & AWS KMS CMK:** Encrypts data in transit and at rest for GDPR/CCPA compliance.
- **AWS IAM & SigV4:** Secures service-to-service authentication and authorization.
- **AWS CloudWatch:** Tracks queue depth and message age for performance SLAs.

## Rationale
This architecture ensures 99.95% availability and 1M MAU scalability by using decoupled, native AWS services. Strict security, validation, and monitoring protocols protect sensitive data and prevent message processing failures.