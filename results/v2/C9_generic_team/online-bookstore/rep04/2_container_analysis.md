## Overview
An Amazon-style e-commerce platform built as a microservices architecture on AWS to support physical and electronic book sales. It ensures high scalability, strict compliance, and global availability across three regions.

## Key Elements
* **Clients:** Customers and Administrators/Content Moderators
* **Edge/Client-Side Container:** Single Page Application / Server-Side Rendered frontend hosted on AWS S3/CloudFront
* **API Gateway Container:** Entry point handling TLS termination, rate limiting, and JWT validation
* **Backend Containers:** Catalog & Search, Checkout & Order, Recommendations, and User & Reviews containers
* **Infrastructure Containers:** Async Event Bus (AWS EventBridge/Kafka), Configuration & Secrets Management (AWS Secrets Manager), Observability/Telemetry (OpenTelemetry sidecars)
* **Data Tier:** PostgreSQL (Checkout), OpenSearch (Catalog), Redis (Cart/Currency)
* **External Systems:** Payment Gateway, Third-Party Shipping APIs, Identity/Consent Management, Currency Exchange, Monitoring Provider

## Relationships
* **Client to API Gateway:** HTTPS / TLS
* **API Gateway to Microservices:** Internal TLS / REST / gRPC
* **Microservices to Event Bus:** Asynchronous pub/sub messaging
* **Microservices to Data Tier:** Native database protocols (SQL/NoSQL/Redis drivers)
* **Services to External Systems:** HTTPS / REST APIs with centralized secrets

## Technology Stack
* **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region redundancy
* **Orchestration & Packaging:** OCI-compliant Docker containers managed via AWS ECS/EKS
* **Communication & Protocols:** REST/OpenAPI contracts for internal/external APIs, Async Event Bus for decoupled events
* **Databases & Caching:** PostgreSQL for ACID transactions, OpenSearch for catalog indexing, Redis for session/cart caching
* **Security & Observability:** AWS Secrets Manager for credentials, OpenTelemetry sidecars for distributed tracing

## Rationale
Decoupled microservices with dedicated data stores isolate compute-heavy and transactional workloads to guarantee 99.95% uptime and prevent resource starvation. Global CDN caching and multi-region deployment ensure sub-2-second page loads on constrained networks while maintaining stringent security and GDPR/CCPA compliance.