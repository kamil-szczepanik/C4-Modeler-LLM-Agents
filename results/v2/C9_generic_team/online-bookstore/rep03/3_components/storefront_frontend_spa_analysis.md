## Overview
[The system is an online bookstore providing catalog browsing, shopping carts, secure checkout, reviews, and recommendations for 1 million monthly active users. Its core purpose is to deliver a scalable, performant, and secure e-commerce experience globally via AWS.]

## Key Elements
- Storefront Frontend (SPA)
- Edge Security & WAF
- API Gateway / BFF
- Core Domain Services
- Caching Layer (Amazon ElastiCache)
- Asynchronous Message Broker (AWS SQS/SNS)
- Persistence Layer (Amazon RDS, Amazon OpenSearch)

## Relationships
- Customers -> Storefront Frontend (SPA): Accesses SPA storefront via HTTPS
- Storefront Frontend (SPA) -> Edge Security & WAF: Protects requests via AWS WAF
- Storefront Frontend (SPA) -> API Gateway / BFF: Routes frontend API requests via HTTPS
- API Gateway / BFF -> Core Domain Services: Invokes services via gRPC and REST

## Technology Stack
- Hosting & Delivery: AWS S3 and Amazon CloudFront for global static asset distribution
- Client State & Data Fetching: React Query / RTK Query for caching and stale-while-revalidate strategies
- CI/CD & Performance: Automated bundle-size monitoring and contract testing via OpenAPI/Swagger
- Security & Compliance: Content Security Policies (CSP) and WCAG 2.1 AA accessibility standards

## Rationale
[This architecture utilizes global CDN caching and decoupled frontend services to guarantee sub-2-second page loads on 3G connections. It scales seamlessly to 1 million MAU while enforcing strict security, accessibility, and multi-region deployment capabilities.]