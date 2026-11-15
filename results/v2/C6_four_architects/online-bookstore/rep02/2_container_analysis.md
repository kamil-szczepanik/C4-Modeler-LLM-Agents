## Overview
An Amazon-style online bookstore designed for global scale, supporting physical and electronic book sales, recommendations, and reviews. Built on a multi-region AWS cloud infrastructure to guarantee high availability and performance.

## Key Elements
* **Clients**: Customers and Admin/Content Managers accessing via web browsers.
* **Global Routing**: AWS Route 53 and Amazon CloudFront CDN.
* **Presentation Layer**: React/TypeScript SPA (stored in AWS S3) and Next.js Node.js BFF container on Amazon ECS/Fargate.
* **Gateway & Security**: AWS API Gateway and Compliance/Audit Lambda container.
* **Business Logic Containers**: Core E-Commerce Service (Spring Boot), Recommendation Engine (FastAPI), Search & Discovery (OpenSearch), and Notification Worker.
* **Data & Messaging Containers**: Amazon Aurora Global Database (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon MSK (Kafka), and AWS Glue/Athena data lake.
* **External Systems**: Payment Gateway, Third-Party Shipping API, Notification Service, Identity Provider, and Tax Calculation Service.

## Relationships
* **Clients to Edge**: HTTPS via AWS Route 53 and CloudFront.
* **CloudFront to BFF**: HTTPS.
* **BFF to API Gateway**: gRPC over TLS (internal VPC).
* **API Gateway to Core Services**: gRPC over TLS (internal VPC peering).
* **Services to Data Layers**: TLS/JDBC to Aurora Global DB; RESP over TLS to ElastiCache; TLS to DynamoDB.
* **Services to Event Bus**: Kafka protocol over TLS to Amazon MSK.
* **External Integrations**: Secure REST/HTTPS APIs with payment, shipping, notification, and tax providers.

## Technology Stack
* **Cloud & Regions**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for global multi-region presence.
* **Frontend/BFF**: React, TypeScript, Next.js for Server-Side Rendering and <2s page loads.
* **Backend**: Spring Boot (Java) for transactional core logic; FastAPI (Python) for AI recommendations.
* **Search & Caching**: Amazon OpenSearch for catalog queries; Amazon ElastiCache (Redis) for low-latency read caching.
* **Databases**: Amazon Aurora Global Database (PostgreSQL) for ACID checkout; Amazon DynamoDB for reviews/caching.
* **Messaging & Analytics**: Amazon MSK (Kafka) for event streaming; AWS Glue/Athena for analytics.

## Rationale
* The multi-region active deployment via Route 53, CloudFront, and Aurora Global Database ensures 99.95% uptime and low-latency performance globally.
* Event-driven decoupling via Amazon MSK and containerized isolation on ECS/Fargate effortlessly handle 1M MAU scaling and OWASP security requirements.