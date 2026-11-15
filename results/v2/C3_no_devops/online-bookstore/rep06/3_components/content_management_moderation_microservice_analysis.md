## Overview
[The Content Management & Moderation Microservice manages user-generated reviews, ratings, and content moderation workflows for the Online Bookstore. It ensures strict GDPR/CCPA compliance, OWASP Top-10 security mitigations, and automated user feedback loops.]

## Key Elements
- **Review & Rating Controller**: Node.js/TypeScript REST/gRPC endpoints handling customer review submissions, updates, and GDPR erasure requests.
- **Moderation Workflow Engine**: Manages queue states and enforces RBAC/ABAC authorization for Site Administrators and Customers.
- **Content Sanitizer Component**: DOMPurify-based input validation layer mitigating XSS and injection vulnerabilities.
- **Data Access Repository**: Interfaces with AWS Aurora PostgreSQL for secure multi-tenant storage.
- **Notification Dispatcher Component**: Asynchronous integration layer publishing moderation events.

## Relationships
- **API Gateway -> Review & Rating Controller / Moderation Workflow Engine**: Routes moderation requests via gRPC over mTLS through AWS App Mesh.
- **Review & Rating Controller & Moderation Workflow Engine -> Data Access Repository**: Reads and writes data via secure TCP with AWS KMS encryption.
- **Notification Dispatcher Component -> Notification Microservice**: Publishes moderation events asynchronously via AWS EventBridge over HTTPS with IAM authentication.

## Technology Stack
- **Runtime**: Node.js with TypeScript for application logic and microservice containers.
- **Compute**: AWS ECS Fargate for scalable, serverless container orchestration.
- **Sanitization**: DOMPurify for robust input validation and XSS mitigation.
- **Messaging**: AWS EventBridge for decoupled asynchronous event publishing.
- **Security & Encryption**: AWS KMS for column-level and data-at-rest encryption, TLS 1.3 for transit security.

## Rationale
[This architecture uses containerized Node.js microservices on AWS ECS Fargate to scale effortlessly and meet strict 99.95% availability targets. Integrated compliance controls, including DOMPurify, AWS KMS encryption, and AWS EventBridge pseudonymization, ensure full GDPR/CCPA adherence without sacrificing system performance.]