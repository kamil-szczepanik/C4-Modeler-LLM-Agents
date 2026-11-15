## Overview
- Scaled-down Amazon-style e-commerce site for physical and electronic books with recommendations and reviews.
- Built on AWS across multiple regions to support 1M MAU with sub-2s page loads and GDPR/CCPA compliance.

## Key Elements
- **Users**: Customer, Admin / Content Manager.
- **Frontend**: Single Page Application (React) served via Amazon CloudFront (CDN) and S3.
- **Ingress**: Amazon API Gateway with JWT validation.
- **Backend Containers**: Core E-Commerce API (Node.js/Express) and Recommendation & Review Service (Python/FastAPI) running on Amazon ECS (Fargate).
- **Data & Caching**: Amazon Aurora (PostgreSQL) Global Database and Amazon ElastiCache (Redis).
- **External Systems**: Payment Gateway, Shipping Provider API, Notification Service, Tax Calculation Service, Third-Party Recommendation Engine, Identity Provider.

## Relationships
- **SPA to API Gateway**: HTTPS/JSON for client requests.
- **API Gateway to Core E-Commerce API**: HTTPS via AWS App Mesh/ECS Service Connect.
- **Core E-Commerce API to Recommendation Service**: gRPC over mTLS.
- **Services to Database/Cache**: TLS 1.3 with AES-256 encryption.
- **Global Routing**: AWS Route 53 latency-based routing with failover.

## Technology Stack
- **React/CloudFront/S3**: Client-side rendering and global CDN for sub-2s page load SLA.
- **Node.js/Express & Python/FastAPI**: Microservices handling business logic and async recommendations.
- **Amazon ECS (Fargate)**: Container orchestration minimizing server management.
- **Amazon Aurora PostgreSQL Global Database**: Transactional storage with cross-region replication for GDPR data residency.
- **Amazon ElastiCache (Redis)**: Write-through session and catalogue caching for persistent carts and low latency.
- **AWS App Mesh / Service Connect**: Automated mTLS and service discovery.
- **AWS KMS & Secrets Manager**: Regional encryption keys and secure credential rotation.

## Rationale
- Containerized microservices on AWS ECS with auto-scaling ensure scalable handling of 1M MAU and high availability.
- Multi-region Aurora databases, strict encryption, and mTLS satisfy GDPR/CCPA compliance and OWASP security constraints.