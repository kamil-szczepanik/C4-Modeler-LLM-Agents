## Overview
Real-Time Payment Fraud Screening system intercepts card-not-present payment authorizations in real-time to assess fraud risk, enforce compliance, and route suspicious transactions for analyst review. It balances sub-50ms latency SLAs with strict PCI-DSS Level 1 security constraints on AWS.

## Key Elements
- **API Gateway**: Nginx / AWS ALB
- **Fraud Scoring Engine**: Go service with embedded ONNX runtime
- **Case Management Backend**: Node.js / Express service
- **Model/Rule Manager**: Python / FastAPI service
- **Data & State Stores**: Amazon ElastiCache for Redis (Feature Store), Amazon Aurora Serverless v2 (Case DB), Amazon S3 (Audit WORM Archives)
- **Messaging & Ingestion**: Amazon MSK Serverless
- **Security & Infrastructure**: AWS IAM Roles for Tasks (IRSA), AWS KMS, AWS ECS Fargate

## Relationships
- Payment Gateway -> API Gateway: HTTPS/JSON
- API Gateway -> Fraud Scoring Engine: gRPC
- Fraud Scoring Engine <-> ElastiCache for Redis: TCP (Feature lookups)
- Fraud Scoring Engine -> Amazon MSK Serverless: TLS (Asynchronous audit log streaming)
- Amazon MSK Serverless -> Amazon S3 / Aurora: Native consumer connectors (Audit persistence)
- Case Management Backend <-> Aurora Serverless v2: SQL/TCP (Analyst data access)
- Model/Rule Manager -> Fraud Scoring Engine: HTTP/gRPC (Zero-downtime rules updates)

## Technology Stack
- **Go**: Chosen for Fraud Scoring Engine to guarantee <50ms P99 latency at 3000 TPS within budget.
- **Amazon ECS Fargate**: Container orchestration providing serverless scaling for a 3-engineer team.
- **Amazon MSK Serverless**: Decouples scoring from audit persistence to protect hot-path latency.
- **Amazon Aurora Serverless v2 & S3**: Scalable storage with WORM configurations for 7-year audit requirements.
- **AWS KMS & IRSA**: Secures data-in-transit/rest and implements zero-trust task isolation.

## Rationale
The architecture prioritizes a Go-based hot path with embedded ONNX models to meet demanding latency and throughput requirements while avoiding complex multi-container IPC. Utilizing AWS managed services and serverless components ensures compliance with the €25,000 monthly budget and strict PCI-DSS Level 1 mandates for a three-engineer operations team.