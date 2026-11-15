## Overview
The Online Bookstore is a globally distributed e-commerce platform built on AWS, designed to support 1 million monthly active users with high availability and stringent regulatory compliance. It provides a secure, multi-currency shopping experience with real-time catalog search, personalized recommendations, and isolated user privacy workflows.

## Key Elements
*   **Customers & Store Administrators:** End-users and back-office staff interacting via web/mobile interfaces.
*   **Single Page Application (SPA):** React and TypeScript frontend hosted on Amazon CloudFront and S3.
*   **API Gateway:** Amazon API Gateway providing entry routing, rate limiting, and JWT validation.
*   **Core Services (AWS ECS Fargate):** Catalog & Search Service (Spring Boot), Checkout & Order Service (Node.js/Express), Recommendation Service (FastAPI), and User Privacy & Compliance Service.
*   **Data Stores:** Amazon Aurora PostgreSQL (multi-region, multi-AZ) and Amazon DynamoDB.
*   **External Integrations:** Third-Party Payment Gateway, Shipping Provider, and Identity Provider (IdP).

## Relationships
*   **Client to API:** HTTPS/TLS between React SPA and Amazon API Gateway.
*   **Gateway to Services:** mTLS and AWS IAM-authenticated traffic from API Gateway to ECS Fargate containers.
*   **Service Messaging:** Asynchronous event handling and data export requests via Amazon SQS.
*   **External Payments/Shipping:** TLS-secured HTTPS integrations from Checkout & Order Service to external APIs.

## Technology Stack
*   **Frontend:** React (TypeScript) for high-performance client rendering (<2s 3G load time).
*   **Compute:** AWS ECS Fargate for scalable, serverless container orchestration.
*   **Databases:** Amazon Aurora PostgreSQL for transactional data and Amazon DynamoDB for session/compliance data.
*   **Caching & Search:** Redis for low-latency recommendation caching; Elasticsearch for fast catalog keyword search.
*   **Security:** AWS KMS for customer-managed encryption keys, AWS Secrets Manager for runtime credential injection, and Amazon Inspector for container image vulnerability scanning.

## Rationale
This containerized microservices architecture isolates high-throughput transactional paths from heavy recommendation and compliance workflows, ensuring optimal page performance and fault tolerance. Leveraging AWS multi-region infrastructure guarantees 99.95% uptime and strict adherence to global GDPR and CCPA data residency constraints.