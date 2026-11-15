## Overview
The Online Bookstore is a scaled-down e-commerce platform designed to handle physical and electronic book sales, customer reviews, and personalized recommendations. Its core purpose is to provide a highly scalable, secure, and globally available shopping experience supporting 1 million monthly active users (MAU).

## Key Elements
- Single Page Application (SPA) / Mobile Client served via Global CDN and WAF
- API Gateway handling rate limiting, WAF integration, and routing
- Core Microservices: Catalog Service, Order & Checkout Service, Recommendation Service, and Review Service
- Asynchronous Message Broker (AWS SQS/SNS)
- Distributed Caching Container (Amazon ElastiCache)
- Compliance/User Data Container and Configuration/Secrets Management Container
- External Systems: Payment Gateway, Shipping Providers, Tax Calculation Service, Notification Service, SIEM Provider, and AWS ECR

## Relationships
- SPA interacts with API Gateway via HTTPS using OpenAPI/Swagger specifications
- API Gateway routes internal traffic to decoupled microservices using REST/gRPC
- Order & Checkout Service communicates with Payment Gateway and Shipping APIs via TLS and AWS SQS/SNS
- Microservices connect to segregated isolated data stores using the Database-per-Service pattern
- Containers export structured JSON logs to the SIEM Provider for GDPR/CCPA audit compliance

## Technology Stack
- Cloud Infrastructure: AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for multi-region redundancy
- Orchestration & Registry: AWS ECS/EKS with AWS ECR for automated vulnerability scanning
- Messaging & Caching: AWS SQS/SNS for asynchronous decoupling and Amazon ElastiCache for regional low-latency reads
- Security & Config: AWS Secrets Manager / Parameter Store for centralized credentials and WAF for perimeter defense

## Rationale
This decoupled microservices architecture ensures 99.95% availability by isolating third-party shipping and payment failures using circuit breakers and asynchronous messaging. Regional distributed caching and multi-region AWS deployment satisfy the sub-2-second page load requirement and scale seamlessly to 1 million MAU.