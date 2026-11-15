## Overview
This system is an Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and recommendations. It is architected as a multi-region, scalable e-commerce platform deployed on AWS.

## Key Elements
- **Users**: Customers, Book Authors/Publishers, Customer Support Agents, Shipping Partners, Site Administrators
- **Frontend Container**: Single-Page Application (React)
- **Ingress & Security Containers**: AWS API Gateway, Envoy Service Mesh
- **Backend Containers (AWS ECS on Fargate)**: Catalog Service (Node.js/Express), Order & Checkout Service (Java/Spring Boot), Recommendation Service (Python/FastAPI), Customer Service (Go), Admin & Support Service (Node.js/GraphQL)
- **External Systems**: Payment Gateway, Shipping Provider APIs, Notification Service, Currency Exchange API
- **Databases & Caching**: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon S3, Amazon EventBridge, Amazon SQS

## Relationships
- **Client to Gateway**: HTTPS (TLS 1.3) via Amazon CloudFront and AWS Application Load Balancer
- **Internal Service Communication**: gRPC over mTLS using Envoy and SPIFFE/SPIRE
- **Asynchronous Messaging**: Amazon SQS and Amazon EventBridge with payload encryption via AWS KMS
- **External Integrations**: REST/JSON over HTTPS to third-party shipping APIs and payment gateways

## Technology Stack
- **Frontend Hosting**: Amazon S3 and Amazon CloudFront for low-latency global delivery
- **Compute**: AWS ECS on AWS Fargate with distroless base images for secure containerization
- **Backend Languages**: Node.js, Java (Spring Boot), Python (FastAPI), and Go for domain-specific services
- **Search & Caching**: Elasticsearch for keyword search; Amazon ElastiCache (Redis) for shopping cart state
- **Database**: Amazon Aurora PostgreSQL with multi-region replication and AWS KMS encryption-at-rest
- **Observability & Deployment**: OpenTelemetry, Prometheus, Grafana, AWS CloudWatch, and AWS CodeDeploy/ArgoCD

## Rationale
The microservices container architecture ensures strict isolation between the checkout and recommendation paths to protect core revenue streams. Multi-region AWS deployment combined with Redis caching and asynchronous queues guarantees high availability, sub-2-second performance, and scalability to support 1 million MAU.