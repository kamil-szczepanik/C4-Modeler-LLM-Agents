## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site designed to provide scalable catalogue browsing, secure checkout, reviews, and personalized book recommendations. The architecture leverages a distributed AWS cloud deployment across three global regions to ensure high availability and performance.

## Key Elements
* Amazon CloudFront (CDN / Edge Router)
* Application Load Balancer (ALB)
* Amazon API Gateway / Authorizer
* AWS ECS Microservices (Catalogue, Checkout, Recommendations, Review Services)
* Amazon Route 53 (Global Traffic Management)
* AWS WAF and AWS Shield (Security & DDoS Mitigation)

## Relationships
* Client / SPA -> Amazon CloudFront: Sends client traffic with injected geo-location headers [HTTPS]
* Amazon CloudFront -> Amazon API Gateway / ALB: Forwards dynamic API calls [HTTPS]
* Amazon API Gateway -> AWS ECS Microservices: Routes validated requests signed with AWS IAM SigV4 [HTTPS / REST]
* Amazon Route 53 -> Amazon CloudFront: Provides latency-based global routing and failover health checks [DNS]

## Technology Stack
* Amazon CloudFront: Handles TLS termination, Geo-DNS routing, and static asset caching at the edge
* Amazon API Gateway & ALB: Manages API routing, JWT validation via cached JWKS, and rate-limiting
* AWS ECS Fargate: Runs containerized microservices without server management overhead
* AWS WAF & AWS Shield: Provides automated OWASP Top-10 mitigations, rate-based rules, and DDoS protection
* Terraform / AWS CDK: Manages infrastructure as code across multi-region deployments

## Rationale
This architecture ensures 99.95% uptime and supports 1 million MAU by decoupling edge routing, security enforcement, and backend microservices across multiple AWS regions. Furthermore, utilizing edge geo-header injection and local token validation maintains low latency and performance under 2 seconds even on constrained networks.