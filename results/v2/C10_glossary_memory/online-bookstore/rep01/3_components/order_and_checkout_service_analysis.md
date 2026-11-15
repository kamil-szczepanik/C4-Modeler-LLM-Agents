## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. The Order and Checkout Service handles transactional safety, multi-currency support (USD, EUR, GBP), and order processing.

## Key Elements
- Book Shopper [person, container]
- Web Frontend (React SPA) [container]
- Amazon API Gateway (Amazon API Gateway) [container]
- Order and Checkout Service (Go) [container]
- Cart Component (Go / In-Memory) [component]
- Checkout Orchestrator (Go) [component]
- Order Processing Component (Go) [component]
- Notification Component (Go) [component]
- Payment Gateway (Stripe or PayPal) [externalSystem]
- Third-Party Shipping APIs [externalSystem]
- Email Service (Amazon SES) [externalSystem]
- Amazon Aurora PostgreSQL [container]
- Amazon DynamoDB [container]

## Relationships
- Web Frontend -> Amazon API Gateway [HTTPS/REST with JWT validation]
- Amazon API Gateway -> Order and Checkout Service [HTTPS/REST with JWT validation]
- Checkout Orchestrator -> Cart Component [In-Memory / Function Call]
- Checkout Orchestrator -> Payment Gateway [HTTPS/REST]
- Checkout Orchestrator -> Third-Party Shipping APIs [HTTPS/REST]
- Order Processing Component -> Amazon Aurora PostgreSQL [TCP with TLS 1.3]
- Cart Component -> Amazon DynamoDB [TCP with TLS 1.3]
- Notification Component -> Email Service [Amazon SES]

## Technology Stack
- Go: Chosen for the Order and Checkout Service to ensure high performance and concurrency during transactions.
- Amazon DynamoDB: Selected for low-latency shopping cart persistence to minimize cart abandonment.
- Amazon Aurora PostgreSQL: Utilized for ACID-compliant order finalization and multi-region replication.
- Amazon SES: Used for asynchronous transactional email notifications without blocking checkout.

## Rationale
This architecture ensures 99.95% uptime and sub-second performance by decoupling low-latency cart operations from ACID-compliant order processing. Security controls like PCI-DSS tokenization and mTLS meet strict compliance and resilience requirements across global regions.