## Overview
[An Amazon-style online bookstore offering physical and electronic books with recommendations, reviews, and multi-currency support. Deployed across global AWS regions with high availability and strict security compliance.]

## Key Elements
- Shopper (User)
- Administrator (User)
- Frontend App (React SPA, Amazon S3, Amazon CloudFront, AWS Lambda@Edge)
- Amazon API Gateway (Amazon API Gateway)
- Catalog Service, Order & Checkout Service, Recommendation Service (Node.js, Java Spring Boot, Python FastAPI on AWS ECS Fargate)
- Amazon Aurora PostgreSQL & Amazon OpenSearch
- Third-Party Payment Gateway, Shipping Provider, Currency Exchange Service, Recommendation Engine

## Relationships
- Shopper -> Frontend App: Browses and interacts with store [HTTPS/JSON via browser]
- Administrator -> Frontend App: Administers platform [HTTPS/JSON via browser]
- Frontend App -> Amazon API Gateway: Sends API requests and localization headers [HTTPS/JSON]
- Amazon API Gateway -> ECS Fargate Services: Routes microservice requests [gRPC/HTTPS]
- ECS Fargate Services -> Amazon Aurora PostgreSQL & OpenSearch: Persists and indexes data [TCP]

## Technology Stack
- Frontend: React SPA, Tailwind/CSS-in-JS, `react-router`, `react-i18next`, `axios` for performance and localization.
- Hosting & CDN: Amazon S3 and Amazon CloudFront with AWS Lambda@Edge for SEO and static asset caching.
- Backend Compute: AWS ECS Fargate running Node.js, Java Spring Boot, and Python FastAPI containers.
- Databases: Amazon Aurora PostgreSQL and Amazon OpenSearch for scalable data storage and search.
- Security & DevOps: AWS CodePipeline, AWS CloudWatch RUM, TLS 1.3, strict CSP, HTTP-only SameSite cookies, and OWASP Top-10 mitigations.

## Rationale
[This cloud-native architecture leverages AWS global regions, CloudFront edge caching, and serverless containers to guarantee sub-2-second page loads on 3G, 99.95% uptime, and 1M MAU scalability. Decoupled microservices ensure robust security boundaries and compliance with GDPR, CCPA, and OWASP standards.]