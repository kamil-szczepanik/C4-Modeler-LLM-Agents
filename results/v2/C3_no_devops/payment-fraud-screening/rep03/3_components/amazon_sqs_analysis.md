## Overview
Real-time payment fraud screening system for card-not-present transactions, designed to score authorization requests under 50ms while maintaining strict PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Fraud Analysts, Risk & Compliance Officers, Fraud Engineers
- AWS API Gateway / ALB, Scoring Engine (Rust, AWS ECS Fargate), Case Management App (Node.js/Python + React, AWS ECS Fargate), Model & Rule Management Service (AWS ECS Fargate)
- Amazon Aurora PostgreSQL, Amazon SQS FIFO, AWS Lambda
- External Systems: Payment Gateway, IdP, Notification Service, Audit Ledger

## Relationships
- Scoring Engine -> Amazon SQS FIFO: Publishes raw decision payloads asynchronously [HTTPS / SigV4, TLS 1.2+]
- Amazon SQS FIFO -> AWS Lambda: Batch invokes processing function [AWS SDK / Event Source Mapping]
- AWS Lambda -> Amazon SQS DLQ: Automatically routes unprocessable messages on failure [AWS SDK]
- Scoring Engine -> Amazon Aurora PostgreSQL: Reads rules and writes decision data [SQL / TLS]

## Technology Stack
- AWS ECS Fargate: Container orchestration for microservices within 25,000 EUR monthly budget and 3-person team
- Rust: High-performance backend for Scoring Engine to meet <50ms P99 latency at 3,000 TPS
- Amazon SQS FIFO: Decouples latency-critical scoring from audit logging with guaranteed per-transaction ordering
- Amazon Aurora PostgreSQL: Relational persistence with encryption for transactional and case data
- AWS KMS: Customer-managed keys (CMK) ensuring data encryption at rest for PCI-DSS compliance

## Rationale
Decoupling the scoring path via Amazon SQS FIFO protects low-latency payment authorization requirements while ensuring reliable, tamper-evident asynchronous audit logging. Managed AWS services minimize operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 and 7-year auditability constraints within budget.