## Overview
An Amazon-style online bookstore providing secure multi-currency catalog browsing, checkout, and recommendations for 1M MAU.
The system is built on a scalable cloud architecture using AWS and React to meet strict performance and compliance requirements.

## Key Elements
- Customer (Shopper) & Book Reviewer
- Single-Page Application (SPA) (React, Amazon S3 / CloudFront)
- API Gateway (Amazon API Gateway)
- Core Services & Recommendation Engine (Node.js/Python, Amazon ECS Fargate)
- Database Tier (Amazon Aurora PostgreSQL, Amazon DynamoDB)

## Relationships
- Customer -> Single-Page Application (SPA): Browses and purchases books [HTTPS/JSON via Amazon CloudFront]
- Single-Page Application (SPA) -> API Gateway: Sends API requests and telemetry [HTTPS/JSON via Amazon CloudFront]
- API Gateway -> Core Services: Routes business logic requests [gRPC/HTTPS]
- Core Services -> Amazon Aurora PostgreSQL: Persists transactional data [SQL/TLS]

## Technology Stack
- Frontend: React hosted on Amazon S3 and distributed via Amazon CloudFront for global low latency.
- Backend Compute: Node.js (NestJS) and Python (FastAPI) running on Amazon ECS (Fargate) for scalable microservices.
- Database: Amazon Aurora PostgreSQL (Multi-AZ) for transactional data and Amazon DynamoDB for fast-access data.
- Security & Compliance: TLS 1.3, HttpOnly secure cookies, and strict GDPR/CCPA data handling.

## Rationale
This serverless and containerized AWS architecture guarantees 99.95% uptime and sub-2-second page loads on 3G networks.
Decoupled React containers on CloudFront scale seamlessly to handle 1M MAU while strictly enforcing OWASP security standards.