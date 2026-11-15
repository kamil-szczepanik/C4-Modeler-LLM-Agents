## Overview
The system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It evaluates transactions under strict latency and compliance constraints.

## Key Elements
- Payment Gateway / Acquirer Systems
- API Gateway & Routing Layer (AWS ALB + AWS WAF)
- Real-Time Scoring Engine (AWS ECS Fargate, Go/Java, ONNX Runtime)
- Analyst & Rules Portal (AWS Amplify / S3 + CloudFront)
- Case Management Backend (AWS ECS Fargate)
- Audit & Event Stream (Amazon SQS / EventBridge + Kinesis Data Firehose)
- Decision Audit Store (AWS S3 Object Lock & AWS KMS)
- Identity Provider (AWS Cognito / Okta)

## Relationships
- Payment Gateway / Acquirer Systems -> API Gateway & Routing Layer: Sends payment authorization requests [HTTPS/JSON via mTLS]
- API Gateway & Routing Layer -> Real-Time Scoring Engine: Routes authorization payloads for scoring [gRPC / HTTP2 over AWS VPC private links]
- Real-Time Scoring Engine -> Decision Audit Store: Persists decisions, inputs, and model versions [AWS KMS / HTTPS]
- Analyst & Rules Portal -> Case Management Backend: Manages suspicious payment reviews [HTTPS/JSON via OAuth2/JWT]

## Technology Stack
- AWS ALB + AWS WAF: Edge routing, TLS 1.3 termination, rate-limiting, DDoS protection, and PCI-DSS PAN masking without per-request cost penalties.
- AWS ECS Fargate: Container orchestration for microservices, eliminating server management for a 3-engineer team.
- Amazon S3 Object Lock & AWS KMS: Tamper-evident storage ensuring 7-year auditability and compliance.
- gRPC / HTTP2: Internal communication protocol guaranteeing P99 latency below 50 ms at 3,000 TPS.

## Rationale
This architecture uses fully managed AWS services to minimize operational toil for a three-engineer team while respecting the 25,000 EUR monthly budget. It meets strict PCI-DSS Level 1 and 7-year auditability requirements via secure edge tokenization and tamper-evident storage.