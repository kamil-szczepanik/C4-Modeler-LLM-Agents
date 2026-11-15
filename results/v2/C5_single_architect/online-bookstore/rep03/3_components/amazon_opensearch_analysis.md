## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with recommendations and reviews. It provides a secure, high-performance retail experience handling 1M MAU across global AWS regions.

## Key Elements
- **Customers & Administrators**: End-users browsing the catalogue and staff managing operations.
- **Single-Page App (SPA)**: React frontend hosted on AWS S3 and distributed via Amazon CloudFront.
- **Backend Services**: Node.js and NestJS microservices running on Amazon ECS/Fargate (Catalog, Order & Checkout, Recommendation, Email).
- **Amazon OpenSearch**: Managed search engine containing Catalog Search Index, OpenSearch REST API Engine, Index Management & Ingestion Service, and Search Analytics & Suggestions Engine.
- **Data Stores**: Amazon RDS (PostgreSQL), Amazon DynamoDB, and Amazon ElastiCache (Redis).
- **External Systems**: Payment Gateway, Shipping Provider APIs, Email Service, Identity Provider, Tax Calculation Service.

## Relationships
- **Customer -> Single-Page App**: Accesses store UI via HTTPS/TLS.
- **Single-Page App -> API Gateway**: Sends client requests via REST/HTTPS.
- **Catalog Service -> OpenSearch REST API Engine**: Synchronizes product data and queries products via HTTPS (Bulk API).
- **Catalog Service -> Search Analytics & Suggestions Engine**: Fetches search auto-complete suggestions via HTTPS.
- **Order Service -> Payment Gateway**: Processes secure transactions via REST/HTTPS.

## Technology Stack
- **AWS S3 & CloudFront**: Delivers static SPA assets with low latency globally.
- **Node.js with NestJS**: Provides a modular framework for backend microservices.
- **Amazon ECS/Fargate**: Runs containerized services without server management.
- **Amazon OpenSearch**: Powers full-text catalog search, auto-complete, and relevance ranking.
- **PostgreSQL & DynamoDB**: Handles relational transactional data and high-speed NoSQL data.

## Rationale
This architecture uses serverless and managed AWS services to scale dynamically to 1M MAU while ensuring 99.95% uptime and OWASP compliance. Decoupling storage and search via Amazon OpenSearch meets performance goals (<2s page load) for global users.