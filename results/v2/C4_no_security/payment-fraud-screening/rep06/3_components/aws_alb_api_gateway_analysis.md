## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS (eu-west-1) for a mid-size payment processor and provides case management for fraud analysts. It operates within a €25,000/month budget, satisfies PCI-DSS Level 1 compliance, and maintains sub-50ms P99 latency at 3,000 TPS.

## Key Elements
- Merchant / Payment Gateway (External System)
- Shopper / Cardholder (External User)
- Fraud Analyst (Internal User)
- AWS Application Load Balancer (ALB) with AWS WAF (Ingress Container)
- Real-Time Scoring Engine (Go, Amazon ECS Fargate Container)
- Amazon ElastiCache Redis (Cache Container)
- Case Management & Analytics API (Backend Container)
- Frontend Web App (React SPA Container)
- Amazon RDS PostgreSQL (Database Container)
- Amazon S3 with Object Lock and AWS KMS, Amazon S3 Glacier (Storage Containers)
- AWS Kinesis Data Streams / Amazon SQS (Messaging Containers)

## Relationships
- Merchant / Payment Gateway -> AWS ALB: Sends payment authorizations [HTTPS / HTTP/2]
- AWS ALB -> Real-Time Scoring Engine: Routes scoring requests [HTTP/2 / VPC Lattice]
- Real-Time Scoring Engine <-> Amazon ElastiCache Redis: Evaluates rules and models [Redis Protocol]
- Fraud Analyst -> AWS ALB: Accesses review workflows [HTTPS]
- AWS ALB -> Frontend Web App: Serves static SPA assets [HTTPS]
- AWS ALB -> Case Management & Analytics API: Routes management traffic [HTTPS]
- Case Management & Analytics API -> Amazon RDS PostgreSQL: Persists cases and audit trails [PostgreSQL Protocol / TLS]
- Real-Time Scoring Engine -> Amazon S3: Stores tamper-evident decision logs [HTTPS / AWS SDK]
- AWS ALB -> Amazon S3: Stores AWS WAF and ALB access logs [HTTPS]

## Technology Stack
- AWS Application Load Balancer (ALB) & AWS WAF: Provides high-throughput Layer 7 ingress, TLS 1.3 termination, and volumetric attack mitigation within budget.
- Go on Amazon ECS Fargate: Delivers sub-50ms P99 decision latency with minimal compute resource overhead.
- Amazon ElastiCache Redis: Enables low-latency in-memory feature caching for real-time scoring.
- Amazon RDS PostgreSQL: Relational storage for structured case management data and audit logs.
- Amazon S3 with Object Lock and AWS KMS: Tamper-evident, encrypted storage ensuring the 7-year audit retention requirement (R-06).
- Terraform: Infrastructure as Code tool managed by a 3-engineer team, validated via automated security checks (`tflint`, `checkov`).

## Rationale
The architecture pairs a high-throughput, single-ALB ingress with Go-based ECS Fargate services to hit the strict 50ms P99 latency SLA at 3,000 TPS. Consolidating components onto managed AWS services ensures PCI-DSS Level 1 compliance and 7-year auditability while respecting the €25,000 monthly budget and operational constraints of a three-engineer team.