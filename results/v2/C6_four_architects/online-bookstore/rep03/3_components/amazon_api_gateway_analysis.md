## Overview
[The Online Bookstore is an e-commerce platform designed for selling physical and electronic books with integrated reviews and recommendations. The architecture leverages AWS-native services to support 1 million monthly active users (MAU) while ensuring GDPR and OWASP compliance.]

## Key Elements
* Edge Router & Reverse Proxy (AWS API Gateway V2 / HTTP APIs)
* WAF & Threat Mitigation Filter (AWS WAF)
* Authentication & Authorization Filter (AWS Lambda Authorizer)
* Rate Limiting & Throttling Engine (API Gateway Usage Plans & Amazon ElastiCache Redis)
* Request/Response Transformation Engine (API Gateway Mapping Templates)
* API Logging & Telemetry Publisher (Amazon CloudWatch & AWS X-Ray)

## Relationships
* React Single Page Application -> Edge Router & Reverse Proxy: Submits client requests [HTTPS / HTTP/2 over TLS 1.3]
* Edge Router -> WAF & Threat Mitigation Filter: Inspects incoming payloads [AWS WAF WebACL]
* Edge Router -> Authentication & Authorization Filter: Validates JWT tokens [AWS Lambda]
* Rate Limiting Engine -> Amazon ElastiCache (Redis): Tracks token-bucket sliding windows [TCP / Redis Protocol]
* Transformation Engine -> Backend Microservices: Proxies sanitized payloads [gRPC over HTTP/2]

## Technology Stack
* AWS API Gateway V2 (HTTP APIs): Selected for cost-efficiency, native gRPC proxying, and performance.
* AWS WAF: Integrated for native edge inspection against SQLi, XSS, and bot traffic.
* AWS Lambda: Used for stateless, scalable JWT validation.
* Amazon ElastiCache (Redis): Provides sub-millisecond state tracking for rate limiting.
* Amazon CloudWatch & AWS X-Ray: Ensures native distributed tracing and observability.

## Rationale
[This architecture utilizes managed AWS edge services to meet strict performance and availability SLAs under high scale. The component-level separation of security, routing, and telemetry ensures robust OWASP mitigation and GDPR compliance without introducing latency bottlenecks.]