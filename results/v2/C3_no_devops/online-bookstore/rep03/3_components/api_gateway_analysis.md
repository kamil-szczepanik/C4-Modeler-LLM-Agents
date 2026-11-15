## Overview
The Online Bookstore is a secure, high-performance, multi-region e-commerce platform designed to support 1 million monthly active users with 99.95% uptime. It enables customers and administrators to browse catalogues, securely checkout, write reviews, and receive recommendations while complying with GDPR and CCPA.

## Key Elements
- **Users**: Customer, Admin / Content Manager
- **External Systems**: Payment Gateway, Shipping Provider APIs, Tax & Compliance Service, Recommendation Engine
- **Containers**: React SPA & Admin Portal, Amazon API Gateway, Core Microservices (Spring Boot, Python/FastAPI on AWS ECS Fargate), Amazon Aurora PostgreSQL, Amazon DynamoDB
- **API Gateway Components**: AWS WAF, Authentication & Authorization Component, Rate Limiting & Throttling Component, Geographic Routing & Compliance Component, Routing & Protocol Translation Component
- **Security & Infrastructure**: AWS Secrets Manager, AWS CloudWatch, AWS X-Ray

## Relationships
- **React SPA** -> **AWS WAF**: Sends ingress HTTP/HTTPS traffic [HTTPS]
- **AWS WAF** -> **Authentication & Authorization Component**: Inspects traffic for OWASP Top-10 threats [HTTPS]
- **Authentication & Authorization** -> **Geographic Routing Component**: Forwards authenticated requests with validated JWTs [Internal]
- **Geographic Routing Component** -> **Core Microservices**: Routes traffic across regional VPC Links [mTLS, gRPC]
- **API Gateway** -> **AWS CloudWatch & AWS X-Ray**: Emits telemetry, metrics, and distributed traces [Internal]

## Technology Stack
- **Amazon API Gateway**: Acts as the scalable entry point for routing, rate limiting, and analytics.
- **AWS WAF**: Provides edge-level OWASP Top-10 mitigations, SQL injection, and XSS protection.
- **Amazon ECS Fargate**: Hosts containerized core microservices built with Spring Boot and Python/FastAPI.
- **AWS Secrets Manager**: Dynamically injects and rotates mTLS certificates, API keys, and signing secrets.
- **Amazon Aurora PostgreSQL & DynamoDB**: Manages persistent transactional data and scalable NoSQL storage.

## Rationale
This architecture uses Amazon API Gateway combined with AWS WAF and edge-level authentication to instantly drop unauthorized traffic, ensuring high availability (99.95%) and strict security (OWASP Top-10) for 1M MAU. Multi-region deployments (`us-east-1`, `eu-west-1`, `ap-southeast-1`) with geographic routing guarantee low-latency page loads (<2s) and full GDPR and CCPA compliance.