## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud before approval and provides case management for human analysts. It operates on AWS to meet strict latency, security, and auditability requirements within a fixed budget.

## Key Elements
* Payment Gateway / Core Ledger (External System)
* Identity Provider (External System)
* Fraud Analyst (User)
* API Gateway / Ingestion Service (AWS API Gateway / ECS Fargate with Go)
* Scoring Engine (AWS ECS Fargate with Go and in-memory model caching)
* Case Management Backend (ECS Fargate with Node.js/Java)
* Audit & Event Bus (Amazon MSK / Kafka)
* Feature Store (Amazon DynamoDB)
* Transactional Data Store (Amazon Aurora PostgreSQL)
* Audit Archival Storage (Amazon S3 with WORM)

## Relationships
* Payment Gateway sends authorization requests to API Gateway via HTTPS/REST (TLS 1.3).
* API Gateway forwards requests to Scoring Engine using gRPC over mTLS.
* Scoring Engine queries Amazon DynamoDB for real-time feature lookups.
* Scoring Engine publishes decision events to Amazon MSK.
* Case Management Backend reads/writes transactional case data in Amazon Aurora PostgreSQL.
* Audit archival writes decision payloads to Amazon S3 in tamper-evident form.

## Technology Stack
* AWS ECS Fargate & Go: Chosen for Scoring Engine to eliminate Lambda cold starts and guarantee predictable sub-50ms P99 latency at 3,000 TPS.
* Amazon DynamoDB: Selected for the feature store to ensure predictable single-digit millisecond reads.
* Amazon Aurora PostgreSQL: Used for transactional case management.
* Amazon MSK (Kafka): Provides reliable asynchronous event streaming for audit logs.
* Amazon S3: Implements WORM storage for 7-year tamper-evident audit retention.
* mTLS & TLS 1.3: Enforces encryption across container boundaries for PCI-DSS Level 1 compliance.

## Rationale
This architecture uses stateless Go containers and managed AWS services to guarantee sub-50ms latencies at scale while staying within the 25,000 EUR monthly budget. It strictly fulfills PCI-DSS security constraints, data tokenization, and 7-year tamper-evident auditability via S3 WORM storage operated by a three-engineer team.