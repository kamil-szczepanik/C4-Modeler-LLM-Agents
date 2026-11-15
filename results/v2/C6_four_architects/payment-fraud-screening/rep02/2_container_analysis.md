## Overview
- Real-Time Payment Fraud Screening system evaluating card-not-present payment authorizations for mid-size payment processors while supporting manual analyst reviews.
- Designed to meet sub-50ms latency, strict PCI-DSS compliance, and 7-year tamper-evident auditability constraints within a fixed AWS infrastructure budget.

## Key Elements
- Fraud Analysts
- Payment Gateway / Acquirer
- Fraud Analyst UI (React SPA via Amazon S3 / CloudFront)
- API Gateway & Ingress (Java / Spring Cloud Gateway)
- Real-Time Scoring Engine (Java / Spring Boot + ONNX)
- Case Management Backend (Node.js / TypeScript)
- Model & Rule Management Service (Python / FastAPI)
- Audit Worker (Node.js / Python worker)
- Amazon Kinesis Data Streams
- Amazon Aurora PostgreSQL (Scoring DB / Audit Log)
- Amazon ElastiCache (Redis)

## Relationships
- Payment Gateway to API Gateway & Ingress via HTTPS (REST/gRPC)
- Fraud Analyst to Fraud Analyst UI via HTTPS
- Fraud Analyst UI to Case Management Backend via HTTPS
- API Gateway & Ingress to Real-Time Scoring Engine via gRPC over HTTP/2
- Real-Time Scoring Engine to Amazon ElastiCache via RESP over TCP
- Real-Time Scoring Engine to Amazon Kinesis Data Streams via HTTPS (AWS SDK)
- Audit Worker to Amazon Aurora PostgreSQL via TLS/TCP
- Case Management Backend to Amazon Aurora PostgreSQL via TLS/TCP
- Model & Rule Management Service to Real-Time Scoring Engine via internal REST API over HTTPS

## Technology Stack
- Java / Spring Cloud Gateway: Handles secure public ingress and enforces PCI-DSS boundaries
- Java / Spring Boot + ONNX: Provides sub-50ms P99 latency scoring with embedded machine learning models
- Node.js / TypeScript: Powers lightweight case management backend workflows
- Python / FastAPI: Manages zero-downtime model and rule updates
- Amazon Kinesis Data Streams: Decouples scoring latency from durable audit logging
- Amazon Aurora PostgreSQL: Provides tamper-evident append-only storage for 7-year audit requirements
- Amazon ElastiCache (Redis): Delivers microsecond-latency feature lookups
- React & Amazon S3/CloudFront: Hosts secure single-page analyst interface

## Rationale
- Container decomposition and technology choices align with the skills of a 3-engineer team while respecting the 25,000 EUR monthly AWS budget constraint in `eu-west-1`.
- Asynchronous Kinesis streaming and in-memory model hot-swapping guarantee high performance (<50ms P99 latency at 3,000 TPS) without compromising strict PCI-DSS and auditability mandates.