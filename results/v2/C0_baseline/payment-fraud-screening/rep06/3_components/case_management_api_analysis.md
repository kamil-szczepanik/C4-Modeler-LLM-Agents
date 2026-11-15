## Overview
[The system is a Real-Time Payment Fraud Screening engine for card-not-present transactions, paired with a Case Management API that empowers analysts to review suspicious payments. It ensures PCI-DSS compliance, 7-year tamper-evident auditability, and sub-50ms latency within a 25,000 EUR/month AWS budget.]

## Key Elements
* Fraud Analyst
* Case Management API (AWS ECS Fargate, Node.js/TypeScript)
* Case Controller, Case Workflow Service, Note & Tagging Service, Audit & Compliance Logger, Data Access Repository
* Amazon DynamoDB
* Amazon EventBridge
* WORM Compliance Storage (Amazon S3 with Object Lock Compliance mode)
* AWS Secrets Manager & AWS KMS

## Relationships
* Fraud Analyst -> Case Management API: Reviews cases and manages alerts [HTTPS/OAuth2/mTLS]
* Case Management API -> Amazon DynamoDB: Persists and retrieves active cases [TCP/AWS SDK]
* Case Management API -> Amazon EventBridge: Emits analyst tags and case annotations asynchronously [HTTPS/AWS SDK]
* Case Management API -> WORM Compliance Storage: Writes cryptographically signed audit payloads via AWS Lambda [HTTPS/AWS SDK]

## Technology Stack
* AWS ECS Fargate: Chosen for serverless container orchestration, minimizing operational overhead for a 3-person team.
* Node.js/TypeScript: Selected for rapid development of the Case Management API within the engineering team's expertise.
* Amazon DynamoDB: Provides low-latency, scalable NoSQL storage for active cases with strict PAN-masking.
* Amazon EventBridge: Enables decoupled, asynchronous event distribution for analyst tags and model feedback loops.
* AWS S3 WORM Storage: Utilizes S3 Object Lock in Compliance mode for tamper-evident, 7-year audit logging.
* AWS Secrets Manager & KMS: Enforces encryption at rest (AES-256) and dynamic credential rotation for PCI-DSS compliance.

## Rationale
[This architecture balances strict PCI-DSS security and 7-year auditability requirements with the operational constraints of a 3-person engineering team. By leveraging fully managed AWS services and asynchronous event-driven decoupling, it achieves high performance and reliability within the fixed 25,000 EUR monthly budget.]