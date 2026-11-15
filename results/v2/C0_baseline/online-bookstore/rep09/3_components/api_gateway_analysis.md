## Overview
[The Online Bookstore system provides scalable e-commerce capabilities for physical and electronic books, supporting catalog browsing, secure multi-currency checkout, and recommendations.]
[The architecture utilizes an AWS-based microservices pattern designed to meet high availability, security, and global performance requirements.]

## Key Elements
* Single Page Application (SPA): React / TypeScript hosted on AWS S3 & CloudFront
* API Gateway: AWS API Gateway serving as the secure central entry point
* Catalogue Service: Node.js (Express) with Amazon OpenSearch
* Order & Checkout Service: Java (Spring Boot) with Amazon Aurora PostgreSQL
* Recommendation & Review Service: Python (FastAPI) with Amazon SQS/SNS
* Authentication & Authorization Filter: Component validating JWTs and scopes
* Rate Limiting & Throttling Engine: Component enforcing tiered WAF policies
* Routing & Protocol Translationer: Component converting REST to gRPC
* Context & Localization Injector: Component adding currency and geo-context

## Relationships
* SPA -> API Gateway: Sends user requests [HTTPS / REST]
* API Gateway -> Catalogue Service: Routes search and browse queries [mTLS / gRPC]
* API Gateway -> Order & Checkout Service: Routes transactions [mTLS / gRPC]
* API Gateway -> Recommendation & Review Service: Routes recommendations [mTLS / gRPC]

## Technology Stack
* AWS API Gateway & AWS WAF: Centralized routing, rate-limiting, and security enforcement
* Amazon CloudFront: Global edge termination and geo-DNS failover across regions
* gRPC over mTLS: Secure, high-performance internal service-to-service communication
* AWS X-Ray & CloudWatch: Distributed tracing and real-time observability

## Rationale
* The centralized AWS API Gateway architecture enforces strict GDPR compliance, rate-limiting, and security controls at the edge while scaling seamlessly for 1M MAU.
* Decoupling edge routing, localization injection, and protocol translation ensures high availability (99.95% uptime) and low latency (<2s page load) across multi-region AWS deployments.