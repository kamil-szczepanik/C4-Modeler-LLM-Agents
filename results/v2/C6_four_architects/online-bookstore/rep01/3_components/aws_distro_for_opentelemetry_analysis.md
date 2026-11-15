## Overview
[A scaled-down Amazon-style e-commerce site utilizing a microservices architecture on AWS.
The system provides multi-currency book purchasing, recommendations, and reviews with high availability.]

## Key Elements
* **Users:** Customer, Admin/Support Staff
* **Frontend:** Customer SPA, Admin SPA (React, Amazon S3, CloudFront)
* **API Layer:** AWS API Gateway (AWS API Gateway, AWS WAF)
* **Backend Services:** Catalog & Search Service (Spring Boot, OpenSearch), Order & Checkout Service (Node.js), Recommendation Service (Python, FastAPI), Digital Asset Delivery Service (Go), Async Worker
* **Messaging & Events:** Amazon EventBridge, AWS SQS
* **Databases & Caching:** Amazon Aurora PostgreSQL, Amazon DynamoDB, Redis ElastiCache
* **Observability:** AWS Distro for OpenTelemetry (ADOT Sidecar)

## Relationships
* **Customer SPA** $\rightarrow$ **AWS API Gateway** via **HTTPS** for client requests
* **AWS API Gateway** $\rightarrow$ **Backend Services** via **REST/gRPC** for service routing
* **Application Containers** $\rightarrow$ **ADOT Sidecar** via **OTLP (gRPC/HTTP, port 4317/4318)** for local telemetry ingestion
* **ADOT Sidecar** $\rightarrow$ **AWS X-Ray** via **HTTPS** for trace persistence
* **ADOT Sidecar** $\rightarrow$ **Amazon Managed Service for Prometheus** via **HTTP Remote Write** for metric aggregation
* **ADOT Sidecar** $\rightarrow$ **AWS IMDSv2** via **HTTP (TCP port 80)** for runtime environment context

## Technology Stack
* **Cloud Provider:** AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability
* **Frontend & CDN:** React, Amazon S3, CloudFront for fast global static asset delivery
* **Backend Runtime:** Node.js, Spring Boot, Python FastAPI, Go for tailored service performance
* **Observability:** AWS Distro for OpenTelemetry (ADOT), AWS X-Ray, Amazon Managed Service for Prometheus for distributed tracing and metrics

## Rationale
[The microservices architecture deployed across multiple AWS regions ensures 99.95% uptime and scalability for 1 million monthly active users.
Native AWS integrations and robust observability components maintain strict performance and security standards.]