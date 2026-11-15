## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to provide a secure, multi-currency shopping experience with robust catalogue browsing, reviews, and recommendations. It leverages a resilient cloud-native architecture on AWS to ensure high availability, scalability, and strict regulatory compliance.

## Key Elements
- **Users**: Customers, Book Authors/Publishers, Customer Support Agents, Shipping Partners, Site Administrators
- **Edge & Routing**: Amazon CloudFront, Amazon S3, AWS API Gateway, Envoy Service Mesh
- **Core Containers**: Order & Checkout Service (Java, Spring Boot, AWS ECS on Fargate), Catalog Service, Recommendation Service, Customer Service, Admin & Support Service
- **Data & Messaging**: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon EventBridge, Amazon SQS
- **External Systems**: Payment Gateway, Shipping Provider APIs, Notification Service, Currency Exchange API

## Relationships
- Customer -> Amazon CloudFront / S3: Accesses frontend SPA [HTTPS]
- Envoy Service Mesh -> Order & Checkout Service: Routes order requests [gRPC over mTLS]
- Order & Checkout Service -> Amazon Aurora PostgreSQL: Persists transactional data [PostgreSQL Wire Protocol over TLS]
- Order & Checkout Service -> Amazon ElastiCache (Redis): Manages shopping cart state and locks [Redis Protocol over TLS]
- Order & Checkout Service -> Payment Gateway: Processes tokenized payments [REST/JSON over HTTPS]
- Order & Checkout Service -> Shipping Provider APIs: Coordinates fulfillment [REST/JSON over HTTPS]
- Order & Checkout Service -> Amazon SQS & EventBridge: Publishes domain events [AWS SDK / HTTPS]

## Technology Stack
- **Compute**: AWS ECS on Fargate (Java/Spring Boot, Node.js, Python, Go) for scalable containerized microservices
- **Database & Caching**: Amazon Aurora PostgreSQL with AWS KMS encryption for secure storage; Amazon ElastiCache (Redis) for low-latency cart state and distributed locks
- **Messaging & Integration**: Amazon SQS and Amazon EventBridge for asynchronous event-driven communication
- **Security & Networking**: Envoy Service Mesh with SPIFFE/SPIRE for mTLS; AWS Secrets Manager for credential management
- **Resiliency & Observability**: Resilience4j for circuit breaking; AWS X-Ray and Prometheus/Grafana for monitoring

## Rationale
This architecture uses AWS ECS on Fargate and multi-region deployments to easily handle 1 million monthly active users while maintaining 99.95% uptime. Security controls like tokenized payments, IAM roles, and AWS KMS encryption ensure full GDPR, CCPA, and PCI-DSS scope reduction without sacrificing page performance.