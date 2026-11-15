## Overview
The system is a real-time payment fraud screening platform built on AWS to screen card-not-present payment authorizations and manage fraud cases securely. It ensures PCI-DSS Level 1 compliance, strict auditability, and sub-50ms decision latency within a fixed infrastructure budget.

## Key Elements
- Fraud Analysts (Users)
- Analyst UI (React SPA / AWS S3 / CloudFront)
- API Gateway / Envoy (Envoy)
- Fraud Scoring Engine (Go / gRPC)
- Case Management Backend (Java / Spring Boot)
- Model & Rule Registry Service (Python / FastAPI / S3)
- Asynchronous Audit Worker (Go / AWS Lambda)
- Redis Cluster / Amazon ElastiCache (Amazon ElastiCache Redis)
- PostgreSQL / Amazon Aurora (Amazon Aurora PostgreSQL)
- Compliance Archive (AWS S3 Object Lock)
- Identity Provider (AWS Cognito)

## Relationships
- Fraud Analysts -> Analyst UI: Accesses case management dashboard via HTTPS [CloudFront]
- Analyst UI -> API Gateway / Envoy: Routes API calls via REST/JSON over HTTPS [TLS 1.3, JWT Bearer]
- API Gateway / Envoy -> Fraud Scoring Engine: Evaluates payment authorizations via gRPC
- API Gateway / Envoy -> Case Management Backend: Manages fraud cases via REST/JSON over HTTPS
- API Gateway / Envoy -> Model & Rule Registry Service: Updates rules and models via REST/JSON over HTTPS
- Fraud Scoring Engine -> Redis Cluster: Fetches rules and caches state via Redis Protocol
- Case Management Backend -> PostgreSQL: Persists case data and decisions via JDBC over TLS
- Asynchronous Audit Worker -> Compliance Archive: Stores tamper-evident decision logs via AWS SDK / S3 API

## Technology Stack
- Cloud Provider: AWS (eu-west-1 region) for scalable, compliant infrastructure
- Frontend: React hosted on AWS S3 and distributed via Amazon CloudFront for cost-effective static asset delivery
- API Routing & Security: Envoy (API Gateway) for centralized authentication, TLS 1.3 termination, and rate limiting
- Real-Time Scoring: Go with gRPC for high-performance, low-latency transaction processing (<50ms P99)
- Case Management: Java with Spring Boot for robust enterprise backend workflows
- Model & Rule Management: Python with FastAPI for flexible data science integration
- Datastores: Amazon Aurora PostgreSQL for ACID case storage and Amazon ElastiCache (Redis) for low-latency rule caching
- Audit & Compliance: AWS S3 Object Lock for immutable 7-year audit logs

## Rationale
This AWS-based serverless and containerized architecture meets strict PCI-DSS Level 1 compliance and 7-year auditability constraints through immutable S3 storage and centralized Envoy security routing. It operates efficiently within a 25,000 EUR monthly budget and can be maintained by a small team of three engineers.