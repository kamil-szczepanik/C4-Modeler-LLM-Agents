## Overview
The Notification Service is an asynchronous, highly available microservice responsible for dispatching multi-channel transactional and promotional alerts for the Online Bookstore. It ensures secure, GDPR-compliant communication across global regions while meeting strict uptime and performance targets.

## Key Elements
- **Event Consumer Component**: Spring Boot (Java) service processing asynchronous domain events.
- **Notification Router Component**: Core logic handling user preferences via gRPC and routing decisions.
- **Template Engine Component**: Thymeleaf-based engine rendering localized messages using templates from Amazon S3.
- **Dispatch Adapter Component**: Integrates with external providers via HTTPS/SMTP, backed by AWS Secrets Manager.
- **Amazon SQS**: Buffers incoming domain events and includes Dead Letter Queues (DLQ).
- **Amazon DynamoDB**: Stores scalable, non-PII delivery audit trails.
- **External Providers**: SendGrid, Amazon SES, and Amazon SNS.

## Relationships
- Amazon SQS -> Event Consumer Component: Consumes domain events [Polling over AWS SDK]
- Notification Router Component -> Customer Privacy/Compliance Service: Validates opt-in preferences [gRPC over AWS App Mesh with mTLS]
- Template Engine Component -> Amazon S3: Fetches notification templates [HTTPS]
- Dispatch Adapter Component -> SendGrid / Amazon SES / Amazon SNS: Sends emails and SMS [HTTPS/SMTP]
- Dispatch Adapter Component -> AWS Secrets Manager: Fetches credentials [AWS SDK over HTTPS]
- Dispatch Adapter Component -> Amazon DynamoDB: Persists delivery logs [DynamoDB Wire Protocol]

## Technology Stack
- **Spring Boot (Java)**: Chosen for robust enterprise ecosystem and asynchronous processing capabilities.
- **Amazon SQS**: Provides traffic buffering and fault tolerance during high-volume sales.
- **Amazon DynamoDB**: Selected for write-heavy, highly scalable delivery audit logging.
- **Thymeleaf**: Enables rapid, localized HTML/text template rendering.
- **AWS App Mesh & mTLS**: Secures service-to-service communication with mutual TLS.

## Rationale
This architecture ensures 99.95% availability and high scalability by utilizing asynchronous event processing via SQS to absorb traffic spikes. Security and GDPR compliance are strictly enforced through IAM least privilege, data encryption, and PII masking.