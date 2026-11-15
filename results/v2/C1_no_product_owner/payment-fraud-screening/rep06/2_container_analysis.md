## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages analyst reviews for a mid-size payment processor on AWS. It ensures sub-50ms P99 decision latencies while maintaining strict PCI-DSS compliance, 7-year auditability, and fault tolerance within a fixed 25,000 EUR monthly budget.

## Key Elements
*   **Ingress Layer**: AWS API Gateway
*   **Compute Containers**: ECS Fargate running Go microservices
*   **In-Memory Cache**: Amazon ElastiCache (Redis)
*   **Database**: Amazon Aurora Serverless v2 with append-only tables
*   **Networking Security**: AWS VPC Lattice for mTLS
*   **Security & Secrets**: AWS Secrets Manager, AWS IAM, AWS Cognito, AWS Nitro Enclaves
*   **CI/CD & Supply Chain**: GitHub Actions, Trivy/AWS Inspector, Cosign

## Relationships
*   Payment Gateway to AWS API Gateway via HTTPS / HTTP/2
*   AWS API Gateway to Go Fraud Scoring Engine via gRPC over mTLS
*   Go Fraud Scoring Engine to Amazon ElastiCache (Redis) via TCP
*   Go Fraud Scoring Engine and Case Management to Amazon Aurora Serverless v2 via TLS
*   Fraud Analysts to Case Management Backend via HTTPS (OIDC/OAuth2 via AWS Cognito)

## Technology Stack
*   **AWS ECS Fargate**: Standardized container orchestration to minimize infrastructure management for a 3-person team.
*   **Go**: Standardized programming language for all backend services to ensure predictable memory footprints, static binaries, and sub-millisecond gRPC performance.
*   **Amazon ElastiCache (Redis)**: Low-latency in-memory data store for real-time velocity checks.
*   **Amazon Aurora Serverless v2**: Cost-effective, scalable relational database with append-only ledger tables for tamper-evident 7-year audit logs.
*   **AWS VPC Lattice**: Simplifies service-to-service connectivity and enforces mTLS without managing a custom service mesh.
*   **GitHub Actions & Cosign**: Automates GitOps deployments with zero-downtime rolling updates and cryptographic image signing for supply chain security.

## Rationale
This architecture uses a unified Go stack on AWS ECS Fargate to minimize cognitive load and operational complexity for a three-engineer team while easily meeting the <50ms P99 performance SLA at 3,000 TPS. Leveraging fully managed AWS services like Aurora Serverless v2, ElastiCache, and VPC Lattice ensures robust PCI-DSS compliance, tamper-evident auditability, and strict security controls well within the 25,000 EUR monthly budget.