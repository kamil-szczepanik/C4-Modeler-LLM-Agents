## Overview
The Online Bookstore system is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations for physical and electronic books. It delivers a fast, secure, and globally scalable retail experience handling up to 1 million monthly active users across multiple regions.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA (Amazon S3, Amazon CloudFront, AWS WAF)
- AWS API Gateway (AWS API Gateway, AWS App Mesh)
- Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service, Customer Review & Moderation Service, Notification & Engagement Worker (AWS ECS on Fargate)
- Amazon RDS, Redis on Amazon ElastiCache, Amazon SQS, AWS Secrets Manager

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA via HTTPS (TLS 1.3)
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway via HTTPS
- AWS API Gateway -> Catalog & Search Service via gRPC over TLS (with mutual TLS via AWS App Mesh)
- Order & Checkout Service -> Payment Gateway via REST over HTTPS with circuit breakers
- Order & Checkout Service -> Third-Party Shipping Providers via REST over HTTPS with circuit breakers

## Technology Stack
- Front-End: Single Page Applications built with React, TypeScript, and Vite hosted on Amazon S3 and delivered via Amazon CloudFront.
- Security & Edge: AWS WAF and CloudFront Functions/Lambda@Edge for DDoS mitigation, edge routing, and CSP injection.
- Compute: Microservices running on AWS ECS on Fargate using Node.js/Express, Java/Spring Boot, and Python/FastAPI.
- Data & Caching: Amazon RDS for persistent relational data and Redis on Amazon ElastiCache for in-memory caching.
- Messaging & Integration: Amazon SQS for asynchronous messaging and AWS Secrets Manager for secure credential storage.

## Rationale
This architecture uses a globally distributed CDN and edge security to meet strict performance targets under 3G constraints while maintaining high availability. Containerized microservices on AWS ensure independent scalability to support 1 million MAU and robust compliance with GDPR and CCPA.