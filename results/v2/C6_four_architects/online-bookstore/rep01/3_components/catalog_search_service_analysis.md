## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books with integrated search, recommendations, and reviews. It provides a multi-region cloud architecture supporting high availability, global compliance, and low-latency performance.

## Key Elements
- **Customers & Admins**: End-users browsing/purchasing books and staff managing operations.
- **Client Tier**: Customer SPA and Admin SPA built with React, hosted on Amazon S3 and distributed via CloudFront.
- **API & Gateway**: AWS API Gateway secured with AWS WAF.
- **Backend Services**: Catalog & Search Service (Spring Boot), Order & Checkout Service (Node.js), Recommendation Service (Python FastAPI), Digital Asset Delivery (Go), and Async Worker.
- **Data & Caching Tier**: Amazon Aurora PostgreSQL Global Tables, Amazon DynamoDB, and Redis ElastiCache.
- **Integration & Messaging**: Amazon EventBridge, AWS SQS, Payment Gateway, Shipping Provider APIs, Identity Provider, Notification Service, and Tax Calculation Service.

## Relationships
- **Customer SPA -> AWS API Gateway**: Routes frontend requests using HTTPS / gRPC over TLS.
- **AWS API Gateway -> Catalog & Search Service**: Forwards internal traffic using gRPC over TLS.
- **Catalog & Search Service -> Amazon Aurora PostgreSQL**: Manages relational records via Native Database Protocol over VPC.
- **Catalog & Search Service -> OpenSearch**: Executes full-text queries via REST over HTTP/S within VPC.
- **Catalog & Search Service -> Redis ElastiCache**: Caches frequent queries via in-process calls.
- **Backend Services -> Amazon EventBridge / SQS**: Publishes and consumes domain events asynchronously.
- **Amazon S3 -> Customers**: Delivers digital assets via CloudFront Signed URLs.

## Technology Stack
- **Frontend**: React hosted on Amazon S3 and Amazon CloudFront for static asset delivery.
- **Compute & API**: AWS API Gateway, AWS WAF, Spring Boot, Node.js, Python FastAPI, Go.
- **Databases**: Amazon Aurora PostgreSQL Global Tables for relational data; Amazon DynamoDB for NoSQL storage.
- **Caching & Search**: Redis ElastiCache for low-latency queries; OpenSearch for catalog indexing.
- **Messaging & Observability**: Amazon EventBridge, AWS SQS, and AWS Distro for OpenTelemetry (ADOT).

## Rationale
This microservices-based architecture on AWS ensures horizontal scalability to handle 1 million monthly active users while maintaining 99.95% uptime. Decoupling search, ordering, and asset delivery guarantees sub-2-second page loads even under peak global traffic.