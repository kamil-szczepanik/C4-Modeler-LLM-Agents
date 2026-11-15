## Overview
The Admin & Support Container provides internal tooling for Store Administrators and Support Agents to manage operations securely. It ensures compliance, dispute resolution, and catalogue moderation for the Online Bookstore.

## Key Elements
- Store Administrator & Support Agent: Internal users managing operations
- Admin & Support Container (Amazon ECS/EKS): Isolated tasks for support operations and admin/compliance workloads
- AWS API Gateway: Entry point routing requests via mTLS
- Amazon SQS: Asynchronous queue for GDPR/CCPA data processing
- AWS CloudWatch & Amazon S3 Object Lock: Immutable audit logging storage

## Relationships
- AWS API Gateway -> Admin & Support Container: Routes administration and support requests [mTLS]
- Admin & Support Container -> Amazon SQS: Offloads asynchronous GDPR/CCPA deletion requests [IAM]
- Admin & Support Container -> Amazon S3 Object Lock: Ships cryptographically signed immutable audit logs [HTTPS/TLS 1.3]

## Technology Stack
- Amazon ECS/EKS: Container orchestration ensuring blast radius isolation and dedicated resource quotas
- AWS API Gateway: Secure routing and ingress management
- Amazon SQS: Asynchronous decoupling for compliance batch jobs
- AWS CloudWatch & S3 Object Lock: Cryptographic audit logging and regulatory compliance enforcement

## Rationale
Isolating administrative and support workloads prevents heavy batch jobs from degrading real-time dispute resolution. Strict RBAC, JIT privileged access, and asynchronous SQS processing guarantee GDPR/CCPA compliance and platform security.