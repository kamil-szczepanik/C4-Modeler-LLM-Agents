## Overview
The Online Bookstore is a scaled-down e-commerce system built to deliver physical and electronic books with recommendations, reviews, and multi-currency support. It provides global, highly available catalogue browsing, secure checkout, and third-party shipping integrations while adhering to strict GDPR/CCPA compliance and OWASP security standards.

## Key Elements
- **Storefront Frontend (SPA):** Hosted via AWS S3 and distributed globally via Amazon CloudFront.
- **Edge Security & WAF:** AWS WAF integrated with CloudFront and API Gateway.
- **API Gateway / BFF:** Handles routing, rate limiting, and protocol translation.
- **Core Domain Services:** Catalog/Search, Checkout/Cart, Recommendations, and User Management containers (AWS ECS/EKS).
- **Caching Layer:** Amazon ElastiCache (Redis) for currency rates, search results, and recommendations.
- **Asynchronous Message Broker:** AWS SQS/SNS with a Dead Letter Queue (DLQ).
- **Background Workers:** ECS/Lambda tasks handling shipping integrations, audits, and GDPR anonymization.
- **Persistence Layer:** Amazon RDS (relational) and Amazon OpenSearch.
- **Observability & Synthetic Monitoring:** AWS CloudWatch, X-Ray, and regional synthetic probes.

## Relationships
- **Customers ➔ Amazon CloudFront (HTTPS):** Accesses the SPA storefront.
- **Amazon CloudFront ➔ API Gateway (HTTPS):** Routes frontend API requests.
- **API Gateway ➔ Core Domain Services (gRPC/REST):** Invokes backend business logic.
- **Core Domain Services ➔ Amazon ElastiCache (TCP):** Retrieves cached catalogue and rate data.
- **Core Domain Services ➔ Amazon RDS & OpenSearch (TCP):** Reads and writes transactional and search data.
- **Core Domain Services ➔ AWS SQS/SNS (AMQP/HTTPS):** Publishes asynchronous events for orders and shipping.

## Technology Stack
- **Cloud Provider:** AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability.
- **Compute:** Amazon ECS / EKS for containerized microservices orchestration.
- **Frontend/Edge:** Amazon S3, CloudFront, and AWS WAF for fast, secure content delivery.
- **Databases:** Amazon RDS (transactional data) and OpenSearch (catalogue search).
- **Messaging:** AWS SQS/SNS with DLQ for fault-tolerant asynchronous event-driven processing.
- **Caching:** Amazon ElastiCache (Redis) to minimize database load and optimize performance.

## Rationale
This microservices-based, multi-region AWS architecture ensures 99.95% availability and sub-2-second page loads through edge caching, CDN distribution, and segregated data persistence layers. Decoupled asynchronous workers and robust security controls meet stringent global scalability, compliance (GDPR/CCPA), and OWASP mitigation requirements.