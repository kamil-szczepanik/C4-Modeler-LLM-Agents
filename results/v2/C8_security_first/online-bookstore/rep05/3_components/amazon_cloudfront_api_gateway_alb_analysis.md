## Overview
[The Online Bookstore edge architecture manages global traffic routing, TLS termination, and security enforcement. It serves as the secure entry point for 1M Monthly Active Users across three regions.]

## Key Elements
- Route 53 DNS & Geo-Resolver (AWS Route 53)
- CDN & Edge Caching (AWS CloudFront with Origin Shield)
- API Gateway & Edge Auth (AWS API Gateway, AWS Lambda Authorizer, AWS Cognito/Auth0)
- Internal Application Load Balancer (AWS ALB)
- Security & Traffic Controls (AWS WAF, AWS Shield Advanced)

## Relationships
- Single Page Application -> CDN & Edge Caching: Sends API requests and static asset fetches [HTTPS (REST/GraphQL)]
- CDN & Edge Caching -> API Gateway & Edge Auth: Routes validated and WAF-inspected traffic [HTTPS]
- API Gateway & Edge Auth -> Internal Application Load Balancer: Forwards authorized traffic with injected user context [HTTPS]
- Internal Application Load Balancer -> ECS Fargate Services: Routes internal traffic via service mesh [HTTP/2 via gRPC, mTLS]

## Technology Stack
- AWS Route 53: Latency-based global DNS routing and geo-resolution for multi-currency localization.
- AWS CloudFront: Global CDN with TLS 1.3 termination, Origin Shield, and regional caching policies.
- AWS WAF & Shield Advanced: OWASP Top-10 mitigation, rate-limiting, and bot control.
- AWS API Gateway & Lambda: JWT validation, OAuth scope checking (`checkout:write`), and edge authentication.
- AWS ALB: Internal traffic distribution to microservices using gRPC health checks.

## Rationale
[This edge-focused architecture offloads security, rate-limiting, and caching to AWS managed services to ensure a sub-2-second page load on 3G and 99.95% uptime. Multi-region deployment across us-east-1, eu-west-1, and ap-southeast-1 guarantees global scalability for 1M MAU.]