## Overview
[Real-Time Payment Fraud Screening screens card-not-present payment authorizations for a mid-size payment processor and enables fraud analysts to review suspicious transactions. It ensures sub-50ms P99 decision latency while maintaining strict PCI-DSS Level 1 compliance and 7-year audit retention within a 25,000 EUR monthly AWS budget.]

## Key Elements
- External Users: Fraud Analysts, Merchant Integration Systems
- External Services: Identity Provider
- Infrastructure: API Gateway / Network Load Balancer (NLB)
- Core Containers: Scoring Engine, Case Management Portal, Feature Store, Audit Queue, Audit Stream Processor, Audit Storage
- Audit Storage Components: Amazon S3, S3 Object Lock, AWS KMS, AWS VPC Gateway Endpoints

## Relationships
- Merchant Integration Systems -> API Gateway / NLB: Submit payment authorization requests [HTTPS / TLS 1.3]
- API Gateway / NLB -> Scoring Engine: Route authorization requests [gRPC / REST]
- Scoring Engine <-> Feature Store: Fetch user and transaction features [Redis Cluster Protocol / RESP]
- Scoring Engine -> Audit Queue: Publish decision events asynchronously [Amazon SQS]
- Audit Queue -> Audit Stream Processor: Stream decision payloads [Amazon Kinesis Firehose]
- Audit Stream Processor -> Audit Storage: Write immutable audit records [HTTPS / S3 PutObject]
- Case Management Portal <-> Scoring Engine: Fetch case details and update rules [REST / HTTPS]
- Fraud Analysts -> Case Management Portal: Review flagged payments [HTTPS / TLS 1.3]

## Technology Stack
- Cloud Provider: AWS (Region: eu-west-1) for managed scalability and compliance tooling
- Compute: AWS ECS Fargate for containerized scoring execution
- Backend & Datastores: Node.js/TypeScript and PostgreSQL for Case Management; Redis Cluster for ultra-low latency feature storage
- Audit & Compliance: Amazon S3 with Object Lock in Compliance Mode for WORM-compliant 7-year tamper-evident retention
- Security & Encryption: AWS KMS Customer Managed Keys (CMKs) for data at rest; TLS 1.3 enforced via bucket policies for data in transit; AWS VPC Gateway Endpoints for network isolation

## Rationale
[This AWS-native serverless and managed container architecture meets the strict 50ms P99 latency and 7-year tamper-evident audit requirements by leveraging in-memory Redis caching and immutable S3 Object Lock storage. Furthermore, it operates within the 25,000 EUR monthly budget and supports operation by a lean three-engineer team through fully managed services.]