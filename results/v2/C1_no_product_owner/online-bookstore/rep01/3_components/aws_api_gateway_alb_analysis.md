## Overview
The Online Bookstore is a multi-region e-commerce platform built on AWS, designed to handle physical and electronic book sales, recommendations, and reviews. It delivers high scalability, security, and global availability.

## Key Elements
- **Users:** Customer & Admin Staff
- **External Systems:** Payment Gateway, Shipping Provider APIs, Identity Provider
- **Frontend Container:** Single Page Application (React, TypeScript, AWS S3, CloudFront)
- **API & Routing Container (AWS API Gateway & ALB):** Edge Router & WAF, API Management & Routing, Request Transformation & Caching, Service Mesh Proxy
- **Backend Containers:** Catalog Service, Order & Checkout Service, Recommendation Service (Go, Node.js, Python FastAPI on AWS ECS Fargate)
- **Data & Messaging:** Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), AWS SQS, AWS SNS

## Relationships
- **Single Page Application** -> **AWS API Gateway & ALB**: Sends API requests [HTTPS]
- **Edge Router & WAF** -> **API Management & Routing**: Forwards sanitized traffic [HTTPS]
- **API Management & Routing** -> **Request Transformation & Caching**: Validates schemas and checks cache [Internal API]
- **Request Transformation & Caching** -> **Service Mesh Proxy (Envoy)**: Forwards backend calls [gRPC over mTLS]
- **AWS API Gateway & ALB** -> **Catalog / Order / Recommendation Services**: Routes internal traffic [gRPC over mTLS via App Mesh]

## Technology Stack
- **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for global multi-region deployment.
- **Edge Security & Routing:** AWS WAF, Application Load Balancer, and Amazon API Gateway for traffic management and OWASP protections.
- **Service Mesh & Compute:** AWS App Mesh (Envoy proxy) and AWS ECS Fargate for containerized microservices.
- **Database & Caching:** Amazon Aurora PostgreSQL and Amazon ElastiCache (Redis) for low-latency persistence and caching.

## Rationale
This architecture leverages managed AWS services to guarantee 99.95% uptime and scale seamlessly to 1 Million Monthly Active Users. Utilizing edge security, regional isolation, and strict encryption meets GDPR, CCPA, and OWASP compliance requirements.