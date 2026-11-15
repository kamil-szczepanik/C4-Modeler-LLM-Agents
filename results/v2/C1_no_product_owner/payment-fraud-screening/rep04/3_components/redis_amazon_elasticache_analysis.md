## Overview
[A real-time payment fraud screening system that evaluates card-not-present authorizations and manages fraud analyst reviews for a mid-size payment processor in AWS (eu-west-1).]

## Key Elements
- Fraud Analyst
- Payment Gateway / Core Ledger
- Card Schemes / Identity Providers
- Compliance / Auditor
- API Gateway (AWS API Gateway / ALB)
- Scoring Engine (Go)
- Case Management (Node.js / Spring Boot)
- Model Registry (Python / MLflow / Amazon S3)
- Envoy Sidecar Proxy (Envoy)
- Redis / Amazon ElastiCache (Redis / Amazon ElastiCache)
- Aurora PostgreSQL (Amazon Aurora PostgreSQL)
- Amazon MSK / Kafka (Amazon MSK / Kafka)

## Relationships
- Scoring Engine -> Redis / Amazon ElastiCache: Executes feature lookups over RESP via TLS 1.3 with AWS IAM Authentication [TCP/6379]
- AWS IAM / KMS -> In-Memory Data Store: Enforces identity and encryption policies over HTTPS/TLS [TCP/443]

## Technology Stack
- AWS (eu-west-1): Target cloud provider for infrastructure within the 25,000 EUR monthly budget constraint.
- Amazon ElastiCache (Provisioned cache.m6g.large): Dedicated provisioned Redis cluster chosen over serverless for deterministic network boundaries and PCI-DSS compliance control.
- Go: Used for the Scoring Engine to achieve sub-50ms P99 latency at 3,000 TPS.
- Amazon Aurora PostgreSQL: Relational database for persistent storage and audit logs.
- Amazon MSK / Kafka: Event streaming for asynchronous processing and decoupling.

## Rationale
- The architecture utilizes provisioned AWS services and optimized runtimes like Go to meet sub-50ms latency SLAs and strict PCI-DSS Level 1 security requirements.
- Managed database and caching components reduce operational toil, enabling a lean three-person engineering team to maintain high availability within a fixed budget.