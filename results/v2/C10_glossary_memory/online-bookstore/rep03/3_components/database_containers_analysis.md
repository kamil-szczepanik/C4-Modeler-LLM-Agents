## Overview
An Amazon-style online bookstore platform supporting 1M MAU across three global regions with high availability and strict regulatory compliance. The system enables users to browse, search, purchase, review, and receive recommendations for physical and electronic books.

## Key Elements
* Customer / Reviewer [person]
* Store Administrator [person]
* Single Page App / Mobile App [container, React / React Native]
* API Gateway / BFF Container [container, AWS API Gateway / Envoy]
* Catalog & Search Container [container, Node.js / Go]
* Checkout & Order Container [container, Java / Spring Boot]
* Notification & Review Container [container, Node.js / Express]
* Admin Dashboard Container [container, React]
* Database Containers [container, Amazon Aurora Global PostgreSQL]
* Database Connection Pooler [component, PgBouncer]
* Catalog Database Schema [component, PostgreSQL Schema]
* Order & Checkout Database Schema [component, PostgreSQL Schema]
* Review & Notification Database Schema [component, PostgreSQL Schema]
* Payment Gateway, Shipping / Fulfillment Provider, Identity Provider (AWS Cognito / Auth0), Notification Service (AWS SES / SendGrid) [external systems]

## Relationships
* Customer / Reviewer -> Single Page App / Mobile App (HTTPS)
* Single Page App / Mobile App -> API Gateway / BFF Container (HTTPS / REST)
* API Gateway / BFF Container -> Catalog & Search Container, Checkout & Order Container (Internal mTLS / REST)
* Checkout & Order Container -> Payment Gateway (HTTPS / REST, TLS 1.3, PCI-DSS)
* Checkout & Order Container -> Shipping / Fulfillment Provider (HTTPS / REST Webhooks)
* Checkout & Order Container -> Notification & Review Container (Amazon SQS / SNS)
* Microservices -> Database Connection Pooler (TCP / PostgreSQL wire protocol with TLS 1.3)
* Database Connection Pooler -> Database Schemas (TCP)

## Technology Stack
* AWS (us-east-1, eu-west-1, ap-southeast-1): Multi-region cloud infrastructure ensuring high availability and low latency.
* Amazon Aurora Global PostgreSQL: Transactional database with cross-region replication and ACID compliance.
* PgBouncer: Connection pooling for high concurrency and connection management.
* AWS Cognito / Auth0: OIDC/OAuth 2.0 and JWT identity management.
* AWS SES / SendGrid: Asynchronous transactional notifications.
* Java Spring Boot, Node.js, Go, React: Microservice and frontend runtimes.

## Rationale
This architecture uses multi-region server replication and connection pooling to meet global scalability and sub-second performance demands. Strict schema isolation, TLS encryption, and least-privilege IAM controls ensure GDPR, CCPA, and PCI-DSS compliance while guaranteeing system uptime.