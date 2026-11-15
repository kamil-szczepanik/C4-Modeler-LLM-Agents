## Overview
[The Order & Checkout Container manages secure transactions, multi-currency pricing, and fulfillment for the Online Bookstore system. It ensures high availability, strict security, and fault-tolerant checkout workflows.]

## Key Elements
* Checkout Controller
* Cart & Pricing Engine
* Order Orchestrator
* Payment Gateway Client
* Shipping & Fulfillment Client
* Event Publisher
* Order Repository

## Relationships
* API Gateway -> Checkout Controller (gRPC over mTLS)
* Checkout Controller -> Cart & Pricing Engine & Order Orchestrator (In-process Java method calls)
* Order Orchestrator -> Payment Gateway Client & Shipping & Fulfillment Client (HTTPS / REST with Resilience4j Circuit Breakers)
* Order Orchestrator & Event Publisher -> Order Repository (JDBC / JPA over TLS 1.3)
* Event Publisher -> AWS EventBridge / Kafka (HTTPS)

## Technology Stack
* Java 21 / Spring Boot: Core runtime for enterprise-grade dependency injection and container logic
* Aurora PostgreSQL: ACID-compliant relational database for transactional data integrity
* HikariCP & AWS RDS Proxy: Database connection pooling and spike mitigation
* Resilience4j: Circuit breakers and fault tolerance for external API calls
* AWS Secrets Manager: Secure credential storage and automated secret rotation
* AWS EventBridge / Kafka: Asynchronous messaging with Dead Letter Queues (DLQ)

## Rationale
[This architecture uses the Saga pattern and Transactional Outbox to guarantee reliable distributed transactions and prevent dual-write failures. It decouples core checkout processes from external dependencies while enforcing strict security, PCI-DSS scope reduction, and 99.95% availability.]