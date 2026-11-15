## Overview
The Online Bookstore system is a scalable e-commerce platform designed for purchasing physical and electronic books with integrated recommendations, reviews, and secure global checkout. The architecture utilizes an edge-optimized API Gateway to route client traffic securely while supporting multi-region scalability and regulatory compliance.

## Key Elements
- Single Page Application (SPA): React and TypeScript client hosted on Amazon S3 and CloudFront.
- API Gateway: AWS API Gateway serving as the primary trust boundary and entry point.
- Edge Router / Reverse Proxy: Amazon CloudFront handling TLS 1.3 termination, caching, and OpenAPI schema validation.
- Auth & Policy Enforcer: Component validating JWT tokens, managing rate limiting, and enforcing OWASP Top-10 security controls (R-08).
- Request Transformer / Geo-Resolver: Component extracting client geo-location and injecting multi-currency headers (USD, EUR, GBP).
- Resiliency & Fallback Orchestrator: Component handling circuit breaking, timeouts, and fallback payloads.
- Backend Containers: Catalog & Search, Order & Checkout, Recommendation Engine, and Customer Reviews & Ratings containers.
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Notification Service, and Supplier Feeds/ERP.

## Relationships
- SPA -> API Gateway: Sends client requests via HTTPS / JSON.
- API Gateway -> Catalog & Search Container: Routes catalogue and search requests via gRPC over mTLS.
- API Gateway -> Order & Checkout Container: Routes order and checkout requests via gRPC over mTLS.
- API Gateway -> Recommendation Engine: Routes recommendation queries via gRPC over mTLS.
- API Gateway -> Customer Reviews & Ratings Container: Routes review and rating requests via gRPC over mTLS.
- API Gateway -> External Systems: Integrates with payment gateways and third-party shipping APIs via secure REST/HTTPS protocols.

## Technology Stack
- Cloud Infrastructure: AWS deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` regions for global reach and 99.95% uptime (R-07).
- Edge & Routing: AWS API Gateway and Amazon CloudFront for regional endpoint routing and response caching.
- Security & Compliance: AWS Certificate Manager (ACM) for mTLS certificate rotation, AWS X-Ray for distributed tracing, and AWS CloudWatch Synthetix for canary monitoring.
- Infrastructure as Code: Terraform and AWS CDK managed via GitOps pipelines.

## Rationale
This multi-region serverless architecture meets the 1M MAU scalability requirement (R-05) and sub-2-second page load SLA on 3G networks (R-06) through edge caching and geo-routing. Centralizing security, rate limiting, and resiliency logic at the API Gateway ensures robust GDPR/CCPA compliance and protection against OWASP Top-10 vulnerabilities (R-08).