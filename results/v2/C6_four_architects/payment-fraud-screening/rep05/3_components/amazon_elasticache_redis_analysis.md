## Overview
Real-Time Payment Fraud Screening is a finance platform that screens card-not-present payment authorizations for fraud and manages analyst review cases. It uses AWS cloud infrastructure to deliver sub-50ms fraud scoring at 3,000 requests per second while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Core Ledger, Card Schemes / Tokenization Provider, Identity Provider (IdP), Notification Service (External Systems)
- AWS Application Load Balancer, Amazon API Gateway, Amazon CloudFront, React SPA (Containers)
- Fraud Scoring Service (Python, FastAPI, ONNX Runtime, Amazon ECS Fargate)
- Case Management API (Amazon ECS Fargate)
- Amazon ElastiCache (Redis) with internal components: In-Memory Feature Store Engine, Cluster Replication & Multi-AZ Manager, Encryption & Access Controller, Connection Pool & Command Batching Proxy, Memory & Eviction Policy Manager
- Amazon Aurora PostgreSQL, Amazon S3 Model Registry, Amazon S3 Object Lock, Amazon SQS, AWS Lambda, AWS Cloud Map, Amazon CloudWatch

## Relationships
- Fraud Scoring Service -> Amazon ElastiCache (Redis): Retrieves and stores features via TCP/RESP over TLS with command batching
- Case Management API -> Amazon Aurora PostgreSQL: Persists case and review data via PostgreSQL wire protocol
- Fraud Scoring Service -> Amazon S3 Model Registry: Loads scoring models via HTTPS
- Amazon CloudFront -> React SPA: Delivers frontend assets via HTTPS

## Technology Stack
- AWS ECS Fargate: Container execution for microservices without server management overhead
- Amazon ElastiCache (Redis): Low-latency in-memory feature store supporting high-throughput sliding window lookups
- Amazon Aurora PostgreSQL: Relational database providing transactional guarantees and ACID compliance
- Amazon S3 Object Lock: WORM storage ensuring tamper-evident, 7-year auditability
- Python with FastAPI and ONNX Runtime: High-performance machine learning inference framework

## Rationale
The AWS-native serverless and containerized architecture meets the strict P99 latency and high-availability requirements within a fixed budget of 25,000 EUR per month. Managed services minimize maintenance overhead, allowing a lean three-engineer team to operate the platform securely and reliably.