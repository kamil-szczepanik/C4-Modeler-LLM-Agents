## Overview
The Case Management API & UI system provides real-time fraud case review capabilities, audit logging, and queue management for fraud analysts. It ensures PCI-DSS compliance and long-term regulatory auditability within budget constraints.

## Key Elements
* API Gateway / Router (Go)
* Case Handler Service (Go)
* Audit & Compliance Logger (Go)
* Fraud Analyst SPA (React on AWS S3/CloudFront)
* Amazon SQS
* AWS ECS Fargate
* AWS S3 Object Lock

## Relationships
* Fraud Analyst / Operations Manager -> API Gateway / Router: Reviews cases and monitors queues [HTTPS / WebSockets]
* API Gateway / Router -> Case Handler Service: Routes API requests and WebSocket streams [Internal gRPC/REST]
* Case Handler Service -> Amazon SQS: Consumes review queues [SQS Message Polling]
* Audit & Compliance Logger -> AWS S3 Object Lock: Writes HMAC-SHA256 signed audit logs [HTTPS / S3 API]

## Technology Stack
* Go: Backend services for low memory footprint and single binary deployment
* React: Frontend SPA hosted on Amazon S3 and CloudFront for fast analyst access
* AWS ECS Fargate: Serverless container execution minimizing operational overhead
* Amazon SQS: Reliable asynchronous message queuing for review cases
* S3 Object Lock: Tamper-evident 7-year retention storage for compliance audits

## Rationale
A unified Go backend running on ECS Fargate minimizes maintenance overhead for a three-engineer team. Client-side data masking and secure AWS integrations ensure strict PCI-DSS compliance and tamper-evident auditability within the €25,000 monthly budget.