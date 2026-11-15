## Overview
The Catalog & Search Service is a core e-commerce engine designed to provide instant book discovery and inventory management for shoppers and publishers. It guarantees high availability and sub-2-second performance for 1 million monthly active users globally.

## Key Elements
- Customer (Shopper): Primary user browsing categories and searching catalogs.
- Book Author/Publisher: Contributes and updates book inventory metadata.
- API Gateway & Load Balancer: AWS API Gateway and ALB routing inbound traffic.
- Catalog & Search Service: Node.js application running on Amazon ECS on Fargate.
- Search Facade Component: Amazon OpenSearch query builder with fuzzy matching, synonyms, and ranking boosts.
- Inventory Manager Component: Express.js service handling stock mutations.
- Catalog Event Publisher & Stock Event Notifier: Amazon SNS/SQS event integration.
- Database Cluster: Amazon Aurora (PostgreSQL) for persistence.

## Relationships
- Customer -> API Gateway & Load Balancer: Browses catalog and executes keyword searches [HTTPS / REST]
- API Gateway & Load Balancer -> Catalog & Search Service: Routes catalog and search requests [gRPC / REST]
- Search Facade Component -> Amazon OpenSearch: Queries keyword, facet, and fuzzy data [TCP / HTTPS]
- Inventory Manager Component -> Amazon Aurora: Reads and writes stock/catalog mutations [PostgreSQL Wire Protocol]
- Catalog Event Publisher -> Amazon SNS/SQS: Emits state-change and low-stock events [AMQP / JSON]

## Technology Stack
- Node.js & Express.js: Powers the core application and controllers for rapid API request handling.
- Amazon ECS on Fargate: Provides serverless container orchestration with multi-AZ auto-scaling.
- Amazon OpenSearch: Acts as the dedicated read replica providing typo tolerance, fuzzy matching, and ranking.
- Amazon Aurora (PostgreSQL): Delivers robust transactional persistence for inventory mutations.
- Amazon SNS / SQS: Enables asynchronous event publishing for recommendations and alerts.

## Rationale
Decoupling the search read path (OpenSearch) from the transactional write path (Aurora PostgreSQL) ensures high read performance and protects availability under heavy traffic. Serverless containerization (ECS Fargate) and multi-region AWS deployments fulfill stringent scalability, latency, and uptime requirements.