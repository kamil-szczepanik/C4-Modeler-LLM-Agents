## Overview
The Online Bookstore system is a scalable e-commerce platform built to provide secure book purchasing, personalized recommendations, and reviews. It delivers high performance, global multi-currency support, and strict compliance with privacy regulations.

## Key Elements
- **Users**: Casual Browsers, Intentional Buyers, Authors/Publishers, Store Administrators
- **System Containers**: Web Frontend SPA/SSR, Catalogue Service, Secure Checkout & Payment Service, Recommendation Engine, Admin & Reporting Service
- **External Systems**: Payment Gateway, Third-Party Shipping Provider APIs
- **Infrastructure**: Amazon CloudFront, AWS ECS Fargate, AWS WAF, AWS Secrets Manager

## Relationships
- **Users -> Web Frontend SPA/SSR**: Accesses catalogue, cart, checkout, and dashboards via HTTPS (TLS 1.3)
- **Web Frontend SPA/SSR -> Catalogue Service**: Requests product data via REST and gRPC over mTLS
- **Web Frontend SPA/SSR -> Secure Checkout & Payment Service**: Submits checkout requests via REST and gRPC over mTLS
- **Web Frontend SPA/SSR -> Recommendation Engine**: Fetches recommendations via REST and gRPC over mTLS
- **Web Frontend SPA/SSR -> Admin & Reporting Service**: Sends administrative queries via REST and gRPC over mTLS

## Technology Stack
- **Frontend/SSR**: React and Node.js for hybrid rendering and fast performance
- **Cloud & Orchestration**: AWS ECS Fargate behind Application Load Balancers for container hosting
- **Edge & CDN**: Amazon CloudFront and CloudFront Edge Functions (Lambda@Edge) for localization and static asset caching
- **Security & Compliance**: AWS WAF for rate limiting, AWS Secrets Manager for secret injection, httpOnly cookies for session management

## Rationale
This architecture uses a hybrid SPA/SSR approach combined with a multi-region AWS deployment to achieve sub-2-second 3G page loads and 99.95% availability. Edge caching, circuit breakers, and strict security controls ensure high resilience, OWASP mitigation, and GDPR/CCPA compliance globally.