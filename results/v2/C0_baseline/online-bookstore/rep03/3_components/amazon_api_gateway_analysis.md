## Overview
The Online Bookstore system uses Amazon API Gateway as its primary routing and security container to handle traffic for a 1M MAU e-commerce platform. It provides rate limiting, SSL termination, and OAuth2/JWT authentication while meeting strict scalability, performance, and GDPR/CCPA compliance requirements.

## Key Elements
- **Edge Router & SSL Terminus**: Handles TLS termination and global traffic distribution via AWS Edge locations.
- **JWT Validator Authorizer**: Evaluates OAuth2/JWT tokens against Auth0/AWS Cognito with strict claim validation and guest session support.
- **WAF & Rate Limiter Component**: Enforces AWS WAF managed rules, OWASP Top-10 mitigations, and tier-based throttling with custom fallback responses.
- **API Route Dispatcher**: Forwards validated traffic to internal backend containers via private VPC links using mTLS.

## Relationships
- **Single Page App (SPA) -> Amazon API Gateway**: Client-to-backend communication via HTTPS / REST.
- **Store Administrators -> Amazon API Gateway**: Accesses management operations via HTTPS with mTLS.
- **Amazon API Gateway -> Node.js BFF**: Routes public and dynamic catalogue traffic via mTLS and internal VPC endpoints.
- **Amazon API Gateway -> Checkout Service**: Routes secure transaction requests via mTLS and internal VPC endpoints.
- **Amazon API Gateway -> Recommendations Service**: Routes recommendation requests via mTLS and internal VPC endpoints.
- **Amazon API Gateway -> Auth0/AWS Cognito**: Authenticates requests via OAuth2/OpenID Connect.

## Technology Stack
- **Amazon API Gateway (HTTP APIs v2)**: Chosen for cost-effectiveness, lower latency, and native support for JWT validation and rate limiting.
- **AWS WAF & AWS Shield**: Provides payload inspection, DDoS protection, and OWASP Top-10 mitigations.
- **AWS App Mesh & Private VPC Links**: Secures internal service-to-service communication using mTLS.
- **Amazon CloudWatch & AWS X-Ray**: Enables active tracing, access logging, and latency monitoring across multi-region deployments.

## Rationale
This architecture uses managed AWS services to guarantee 99.95% uptime and sub-2-second page loads for 1M MAU. Centralizing security and routing at the edge ensures GDPR/CCPA compliance and protects backend microservices from volumetric attacks.