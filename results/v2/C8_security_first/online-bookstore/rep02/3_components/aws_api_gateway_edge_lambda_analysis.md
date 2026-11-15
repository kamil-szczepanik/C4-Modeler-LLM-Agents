## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing books, providing catalogue browsing, secure checkout, reviews, and recommendations. The edge architecture utilizes AWS managed services to ensure low latency, high security, and global reach for 1M MAU.

## Key Elements
* Shoppers / Customers & Book Publishers / Administrators (Users)
* Payment Gateway & Third-Party Shipping APIs (External Systems)
* React Single Page Application (SPA) (Client Container)
* AWS API Gateway & Edge Lambda (Edge Container)
* Catalog & Search Service, Order & Checkout Service, Recommendation Service (Backend Containers)
* Edge WAF (`AWS WAF`)
* API Routing & Validation Layer (`Amazon API Gateway - HTTP API`)
* Edge Processing Function (`AWS Lambda@Edge`)

## Relationships
* React SPA -> AWS API Gateway & Edge Lambda: Sends API requests via [HTTPS/JSON]
* AWS API Gateway & Edge Lambda -> Catalog & Search Service: Routes search requests via [gRPC over mTLS with JWT]
* AWS API Gateway & Edge Lambda -> Order & Checkout Service: Routes checkout requests via [gRPC over mTLS with JWT]
* AWS API Gateway & Edge Lambda -> Recommendation Service: Routes recommendation requests via [gRPC over mTLS with JWT]
* AWS WAF -> Amazon API Gateway: Inspects and filters traffic for OWASP Top-10 threats

## Technology Stack
* AWS API Gateway & AWS Lambda@Edge: Entry routing, header injection, and localized currency handling with minimal latency.
* AWS WAF: Edge security, DDoS mitigation, and rate limiting.
* Terraform: Multi-region infrastructure management and drift detection across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
* Amazon Route 53: Latency-based routing and regional failover.
* AWS X-Ray & Datadog: Distributed tracing, metrics, and log aggregation with PII masking.

## Rationale
This architecture ensures sub-15ms edge overhead to meet the strict <2s page load performance SLA on 3G networks. It enforces zero-trust security and multi-region high availability to satisfy GDPR/CCPA compliance and 99.95% uptime requirements.