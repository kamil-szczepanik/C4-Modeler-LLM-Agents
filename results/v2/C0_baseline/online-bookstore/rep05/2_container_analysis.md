## Overview
[An Amazon-style e-commerce site for physical and electronic books with recommendations, reviews, and multi-currency support.]
[Designed to handle 1M MAU across multi-regions while enforcing strict GDPR/CCPA compliance and 99.95% uptime.]

## Key Elements
* **Users:** Customer (Shopper), Book Reviewer, Store Administrator
* **Frontend Containers:** Single-Page Application (SPA) (React), Admin Back-Office App (React)
* **Backend Containers:** API Gateway (Amazon API Gateway), Core Services (Node.js/NestJS), Recommendation Engine (Python/FastAPI), Notification Worker, Analytics Ingestion Container
* **Data & Storage:** Aurora PostgreSQL (Multi-AZ), Amazon DynamoDB, Amazon S3
* **Infrastructure & Integration:** Amazon ECS (Fargate), Amazon EventBridge, Amazon SQS, AWS Service Connect, Amazon CloudFront, AWS Route 53
* **External Systems:** Payment Gateway, Third-Party Shipping Provider, Tax & Compliance Service, Email/Notification Service

## Relationships
* **SPA to API Gateway:** HTTPS/JSON via Amazon CloudFront
* **API Gateway to Core Services, Admin App, & Recommendation Engine:** HTTPS/gRPC with mTLS via AWS Service Connect
* **Core Services to Aurora PostgreSQL:** TCP/TLS
* **Core Services to Amazon EventBridge:** Async Event Publishing (JSON)
* **EventBridge to Notification Worker & Shipping APIs:** HTTPS/SQS
* **Users to Route 53:** Latency-based DNS routing

## Technology Stack
* **Frontend:** React hosted on Amazon S3 / CloudFront for edge performance
* **Backend:** Node.js/NestJS and Python/FastAPI running on Amazon ECS (Fargate) for scalable microservices
* **Database:** Amazon Aurora PostgreSQL (Multi-AZ) and Amazon DynamoDB for transactional and recommendation data
* **Messaging:** Amazon EventBridge and Amazon SQS for asynchronous decoupling
* **Security & Ops:** AWS KMS, Secrets Manager, AWS Service Connect (mTLS), OpenTelemetry, and AWS X-Ray

## Rationale
[This architecture uses serverless containers and multi-region AWS services to guarantee 99.95% uptime, sub-2-second page loads, and seamless scalability for 1M MAU.]
[Robust security controls, regional data residency configurations, and decoupled async messaging ensure strict GDPR/CCPA compliance and resilience against third-party outages.]