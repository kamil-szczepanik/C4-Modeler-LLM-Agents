## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for mid-size payment processors to detect fraud. It provides sub-50ms automated decisions and case management tools for fraud analysts while ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
* Shopper / Cardholder and Merchant / Payment Gateway (External Actors)
* Fraud Analyst, Risk Operations Manager, and Fraud Model Data Scientist (Internal Users)
* AWS ALB / API Gateway (Ingress)
* Real-Time Scoring Engine (Stateless Go service on Amazon ECS Fargate with pre-warmed tasks)
* Amazon ElastiCache (Redis) (Feature Store and cache)
* Case Management & Analytics API (Backend service)
* Frontend Web App (React SPA for analysts and risk managers)
* Amazon RDS PostgreSQL (Case management and application database)
* Amazon S3 with Object Lock and AWS KMS (Tamper-evident audit log storage)
* AWS Kinesis Data Streams / Amazon SQS (Asynchronous event processing)

## Relationships
* Merchant Payment Gateway to AWS ALB via HTTPS
* AWS ALB to Real-Time Scoring Engine via HTTP/2
* Real-Time Scoring Engine to Amazon ElastiCache (Redis) via RESP
* Real-Time Scoring Engine to Amazon S3 via HTTPS for tamper-evident audit logging
* Frontend Web App to Case Management & Analytics API via HTTPS
* Case Management & Analytics API to Amazon RDS PostgreSQL via TCP/SQL

## Technology Stack
* AWS (Cloud Provider, region eu-west-1): Chosen to satisfy enterprise reliability and infrastructure constraints.
* Go: Selected for the Real-Time Scoring Engine to ensure high concurrency and sub-50ms P99 latency at 3,000 TPS.
* Amazon ECS (Fargate): Used with pre-warmed tasks to prevent cold-start latency spikes within budget.
* Amazon ElastiCache (Redis): Provides ultra-low latency access to feature vectors.
* Amazon RDS (PostgreSQL): Manages persistent relational data for case management.
* Amazon S3 with Object Lock and AWS KMS: Ensures immutable, tamper-evident 7-year audit logs for PCI-DSS compliance.
* Terraform: Enables infrastructure-as-code management operable by a 3-engineer team.

## Rationale
This architecture guarantees strict sub-50ms P99 decision latency at 3,000 TPS using pre-warmed Go containers and Redis while incorporating a circuit breaker for fail-safe availability. It maintains a 25,000 EUR monthly budget and operates within 3-engineer limits by relying on fully managed AWS serverless services.