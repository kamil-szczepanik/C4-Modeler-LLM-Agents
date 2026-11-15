## Overview
The Online Bookstore system uses a microservices architecture on AWS to handle high-volume e-commerce operations. It provides a secure, scalable platform for browsing, purchasing, and reviewing books globally.

## Key Elements
- **API Gateway / BFF Container**: AWS API Gateway / Envoy
- **Checkout & Order Container**: Java / Spring Boot
- **Cart Component**: Spring Data Redis / Amazon Aurora PostgreSQL
- **Order Orchestrator Component**: Spring State Machine / Saga
- **Payment Integration Component**: Spring Cloud OpenFeign
- **Fulfillment Integration Component**: Spring Cloud OpenFeign
- **Database Containers**: Amazon Aurora Global PostgreSQL
- **Payment Gateway**: External secure payment processor
- **Shipping / Fulfillment Provider**: External logistics API

## Relationships
- API Gateway / BFF Container -> Order Orchestrator Component [Internal mTLS / REST]
- Order Orchestrator Component -> Cart Component [JDBC / Lettuce Redis Client]
- Order Orchestrator Component -> Payment Integration Component [Internal Method Call]
- Payment Integration Component -> Payment Gateway [HTTPS / REST, TLS 1.3, PCI-DSS]
- Fulfillment Integration Component -> Shipping / Fulfillment Provider [HTTPS / REST Webhooks]

## Technology Stack
- Java / Spring Boot: Chosen for enterprise-grade transaction management and robustness in the Checkout & Order Container.
- Amazon Aurora Global PostgreSQL: Provides multi-region relational data durability and cross-region replication.
- Amazon ElastiCache Redis: Delivers low-latency active cart state management with global datastores.
- TLS 1.3 & AWS KMS: Ensures secure transit and at-rest encryption for PCI-DSS, GDPR, and CCPA compliance.

## Rationale
This architecture guarantees 99.95% uptime and low-latency performance (<2s page load) across three AWS regions through resilient caching, Saga-based distributed transactions, and strict database connection pooling. It isolates the cardholder data environment to satisfy stringent PCI-DSS compliance requirements while supporting multi-currency transactions.