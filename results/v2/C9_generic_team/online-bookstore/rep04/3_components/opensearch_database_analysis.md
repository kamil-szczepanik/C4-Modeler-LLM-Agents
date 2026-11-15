## Overview
The Online Bookstore is an Amazon-style e-commerce platform providing catalog browsing, secure checkout, recommendations, and reviews. The architecture utilizes AWS-hosted containers and managed services to meet strict scalability and performance requirements.

## Key Elements
- Customers and Administrators/Content Moderators
- Single Page Application / Server-Side Rendered Frontend (AWS S3 / CloudFront)
- API Gateway (AWS API Gateway)
- Catalog & Search Container (AWS ECS/EKS with OpenSearch Database)
- Checkout & Order Container (AWS ECS/EKS with PostgreSQL Database)
- Recommendations and User & Reviews Containers (AWS ECS/EKS)
- Async Event Bus (AWS EventBridge / Kafka)
- Redis Cache, AWS Secrets Manager, and OpenTelemetry sidecars

## Relationships
- Frontend -> API Gateway: HTTPS/REST
- API Gateway -> Catalog & Search: HTTP/REST
- Catalog & Search -> OpenSearch Database: Native database protocols (NoSQL drivers)
- Containers -> Async Event Bus: Publish/Subscribe events (Kafka protocols)

## Technology Stack
- AWS ECS/EKS: Container orchestration for microservices, ensuring elastic scalability (R-05).
- PostgreSQL: Relational database for transactional checkout and order data integrity.
- OpenSearch: Search and indexing engine for sub-2-second keyword catalogue searches (R-01, R-06).
- Redis: In-memory caching layer to optimize read performance and page load speeds.
- AWS S3 / CloudFront: CDN and object storage for frontend hosting and OpenSearch snapshot backups.

## Rationale
The microservices architecture deployed across multiple AWS regions ensures high availability (99.95% uptime) and fault tolerance under heavy traffic. Decoupling the search and catalogue tiers using OpenSearch and event-driven synchronization guarantees rapid page loads and robust performance.