## Overview
The Case Management Service provides a secure web interface for fraud analysts to review suspicious payment authorizations, manage queues, and inspect audit trails. It integrates strict compliance controls and high-performance components to meet PCI-DSS Level 1 mandates within a fixed infrastructure budget.

## Key Elements
- Fraud Analysts & Risk Managers: End-users interacting with the system.
- Case Management Service: Core container hosted on AWS ECS Fargate.
- AWS Cognito: OIDC/OAuth2 identity provider managing user authentication and RBAC.
- Amazon S3 with Object Lock: Tamper-evident 7-year audit storage using S3 Glacier Instant Retrieval.
- Amazon Redis: In-memory datastore for low-latency priority queue management.
- AWS X-Ray: Distributed tracing tool for observability.

## Relationships
- Fraud Analysts -> Case Management Service: Reviews suspicious payments and manages queues via HTTPS (OIDC/OAuth2 via AWS Cognito).
- Case Management Service -> Amazon S3: Stores audit trails and case history via AWS SDK.
- Case Management Service -> Amazon Redis: Reads and writes priority queue states via TCP.

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for low operational overhead with a three-engineer team.
- AWS Cognito: Authentication provider ensuring PCI-DSS compliant session security and RBAC.
- Amazon S3 with Object Lock: Compliant WORM storage ensuring 7-year tamper-evident auditability cost-effectively.
- Amazon Redis: Sorted sets used for high-performance priority queue management without database locks.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational burden for a three-engineer team while strictly enforcing PCI-DSS compliance. The selected tech stack ensures secure, low-latency case investigations and tamper-evident auditing within the 25,000 EUR monthly budget constraint.