## Overview
[The system is a real-time payment fraud screening platform that screens card-not-present transactions for fraud and provides case management for human analysts. Its core purpose is to block fraudulent authorizations with sub-50ms latency while ensuring PCI-DSS compliance and 7-year auditability.]

## Key Elements
- Fraud Analysts, ML Engineers
- Real-Time Payment Fraud Screening System (AWS eu-west-1)
- Real-Time Scoring Engine (Go on AWS ECS Fargate)
- ML Inference Service (Python with ONNX Runtime on AWS ECS Fargate)
- Case Management Backend (Go on AWS ECS Fargate)
- Fraud Analyst Frontend (Amazon CloudFront and S3)
- Amazon ElastiCache (Redis), Amazon DynamoDB, Amazon S3 Object Lock, Amazon EventBridge

## Relationships
- Fraud Analyst Frontend -> Case Management Backend: Sends API requests for case management [HTTPS]
- Case Management Backend -> Amazon DynamoDB: Reads and writes case data [HTTPS (AWS SDK)]
- Amazon EventBridge -> Case Management Backend: Routes events asynchronously [HTTPS / Webhook]
- Decision Dispatcher -> Amazon EventBridge: Publishes analyst decision events [HTTPS / AWS SDK]
- Audit Logger -> Amazon S3 Object Lock: Writes immutable audit trails [HTTPS / AWS SDK]

## Technology Stack
- Go: Chosen for backend services to maintain architectural consistency and support a 3-engineer team
- Python with ONNX Runtime: Powers ML inference to meet sub-50ms P99 latency requirements
- Amazon DynamoDB: Provides low-latency NoSQL storage for case data and indexes
- Amazon S3 Object Lock: Ensures tamper-evident, 7-year retention for audit compliance
- Amazon EventBridge: Handles asynchronous event routing without heavy broker overhead

## Rationale
[This architecture satisfies strict PCI-DSS Level 1 compliance and sub-50ms latency constraints while operating within a 25,000 EUR monthly AWS budget. Using Go and managed AWS services minimizes operational overhead for the three-engineer team.]