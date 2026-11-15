## Overview
The Online Bookstore is a multi-region e-commerce platform built for high scalability, secure transactions, and global low-latency performance. It supports book sales, recommendations, reviews, and multi-currency processing while maintaining strict regulatory compliance.

## Key Elements
* **Clients:** Web and Mobile browsers accessing the storefront.
* **Edge & Delivery:** AWS CloudFront (CDN) and S3 for static assets.
* **API Gateway & BFF:** Handles client routing, rate limiting, and request aggregation.
* **Core Containers:** Catalog, Checkout, Recommendations, Reviews, and GDPR/CCPA Compliance Workers.
* **Data & Caching:** Amazon Aurora/RDS (database-per-service), Amazon ElastiCache (Redis) for caching and distributed sessions.
* **Messaging:** AWS SQS/SNS with Dead Letter Queues (DLQ).
* **Infrastructure & Security:** AWS ECS/EKS, AWS Secrets Manager, AWS Systems Manager Parameter Store, and CloudWatch.
* **External Systems:** Payment Gateways, Third-Party Shipping APIs, Forex/Currency Rate API, and Notification Service.

## Relationships
* Clients fetch static assets from **AWS CloudFront** via HTTPS.
* Clients interact with backend services through the **API Gateway / BFF** via HTTPS/REST.
* **API Gateway** queries **ElastiCache (Redis)** for session state and catalog caching via Redis Protocol.
* **Core Containers** communicate asynchronously via **AWS SQS/SNS** using AMQP/JSON protocols.
* **Checkout Container** integrates with external **Payment Gateways** and **Third-Party Shipping APIs** via HTTPS/REST.
* **Compliance Workers** interact with **Core Databases** for GDPR/CCPA data anonymization.

## Technology Stack
* **Cloud Infrastructure:** AWS (*us-east-1*, *eu-west-1*, *ap-southeast-1*) for global multi-region presence.
* **Orchestration & Packaging:** Docker containers managed via Amazon ECS/EKS.
* **Caching & Sessions:** Amazon ElastiCache (Redis) for low-latency reads and session persistence.
* **Messaging:** AWS SQS and SNS for decoupled asynchronous event-driven workflows and DLQ retry policies.
* **Observability & Security:** AWS CloudWatch, OpenTelemetry, AWS Secrets Manager, and Systems Manager Parameter Store.

## Rationale
This decoupled, containerized microservices architecture isolates hot paths like catalog search and checkout to easily handle 1M MAU and achieve 99.95% availability. Utilizing edge caching, regional AWS deployments, and asynchronous message brokers guarantees sub-2-second page loads on 3G networks while strictly enforcing GDPR/CCPA compliance.