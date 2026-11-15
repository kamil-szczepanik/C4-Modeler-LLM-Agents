## Overview
[A real-time payment fraud screening system for a mid-size payment processor that evaluates card-not-present transactions for fraud and provides case management for analysts. It ensures PCI-DSS Level 1 compliance, maintains 7-year tamper-evident auditability, and operates within a 25,000 EUR monthly AWS budget.]

## Key Elements
- Fraud Analyst (Person)
- Shopper / Cardholder (External System)
- Merchant / Payment Gateway (External System)
- AWS ALB / API Gateway (Container)
- Real-Time Scoring Engine (Container - Go, Amazon ECS Fargate)
- Amazon ElastiCache (Redis) (Container)
- Case Management & Analytics API (Container - Backend service)
- Frontend Web App (Container - React SPA)
- Amazon RDS PostgreSQL (Container)
- Amazon S3 with Object Lock and AWS KMS (Container)
- AWS Kinesis Data Streams (Container - Real-Time Payment Event Stream)
- Amazon SQS (Container - Asynchronous Task Queue)

## Relationships
- Shopper / Cardholder interacts with Merchant / Payment Gateway via HTTPS/TLS
- Merchant / Payment Gateway sends authorization requests to AWS ALB / API Gateway via HTTPS/REST
- AWS ALB / API Gateway forwards requests to Real-Time Scoring Engine via HTTP/REST
- Real-Time Scoring Engine ingests streaming data from AWS Kinesis Data Streams via HTTPS (AWS SDK GetRecords)
- Real-Time Scoring Engine publishes audit logs and review cases to Amazon SQS via HTTPS (AWS SDK SendMessage)
- Case Management & Analytics API consumes tasks from Amazon SQS via HTTPS (AWS SDK ReceiveMessage/DeleteMessage)
- Frontend Web App communicates with Case Management & Analytics API via HTTPS/JSON

## Technology Stack
- AWS (Cloud Provider, eu-west-1 region): Chosen for robust compliance frameworks and managed services matching the 3-engineer team constraint.
- Go on Amazon ECS Fargate: Selected for the Real-Time Scoring Engine to meet the <50ms P99 latency requirement at high throughput.
- Amazon RDS PostgreSQL: Used for transactional case management data storage.
- Amazon S3 with Object Lock and AWS KMS: Chosen to meet strict 7-year tamper-evident auditability mandates (R-06).
- AWS Kinesis Data Streams (On-Demand) & Amazon SQS (Standard/FIFO): Used for scalable real-time ingestion and asynchronous task processing without manual operational overhead.
- React SPA: Provides a responsive user interface for fraud analysts.

## Rationale
[This AWS serverless and container-based architecture meets strict sub-50ms latency SLAs and PCI-DSS Level 1 compliance without exceeding the 25,000 EUR monthly budget. Utilizing managed services like ECS Fargate, SQS, and Kinesis On-Demand minimizes operational toil, enabling a three-engineer team to reliably operate, scale, and audit the system.]