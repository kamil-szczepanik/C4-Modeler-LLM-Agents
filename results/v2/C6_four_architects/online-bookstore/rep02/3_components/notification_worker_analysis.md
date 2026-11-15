## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for physical and electronic books, supporting browsing, secure checkout, reviews, and recommendations. It is designed to handle 1 million Monthly Active Users (MAU) with high availability and global compliance.

## Key Elements
- **Users**: Customer, Admin/Content Manager
- **External Systems**: Payment Gateway, Third-Party Shipping API, Email/Notification Service, External Identity Provider, Tax Calculation Service
- **Containers**: AWS Route 53 & Amazon CloudFront, Frontend SPA (React), BFF Container (Next.js/ECS), AWS API Gateway, Compliance/Audit Lambda, Core E-Commerce Service (Spring Boot/ECS), Recommendation Engine (FastAPI), Search & Discovery (Amazon OpenSearch), Notification Worker (ECS), Amazon Aurora Global Database, Amazon DynamoDB, Amazon ElastiCache, Amazon MSK, AWS Glue & Athena
- **Notification Worker Components**: Kafka Consumer, Preference & Compliance Filter, Template Renderer, Template Cache Manager, Dispatch Adapter, DLQ Handler
- **Core E-Commerce Service Components**: API Controllers, Order Domain Service, Catalog Domain Service, Payment Integration Adapter, Outbox Pattern Processor, Database Repository Layer

## Relationships
- *Frontend SPA -> BFF Container*: Communicates via HTTPS/REST
- *BFF Container -> Core E-Commerce Service*: Invokes business logic via gRPC/REST over TLS
- *Notification Worker -> Amazon MSK*: Consumes event streams via Kafka protocol over TLS
- *Notification Worker -> Email/Notification Service*: Sends notifications via secure REST/HTTPS
- *Order Domain Service -> Payment Integration Adapter*: Processes secure transactions via HTTPS
- *Payment Integration Adapter -> Payment Gateway*: Authorizes charges via HTTPS
- *Order Domain Service -> Database Repository*: Persists orders via JDBC over TLS

## Technology Stack
- **Compute**: AWS Lambda, Amazon ECS with AWS Fargate for serverless and containerized microservices
- **Databases**: Amazon Aurora Global Database (PostgreSQL) for transactional data; Amazon DynamoDB for NoSQL storage
- **Caching**: Amazon ElastiCache (Redis) and Caffeine local LRU for low-latency template and data caching
- **Messaging & Streaming**: Amazon MSK (Apache Kafka) for event-driven architecture and asynchronous workflows
- **Backend Frameworks**: Spring Boot (Java) for core services; FastAPI (Python) for recommendations
- **Resilience & Integration**: Resilience4j for circuit breaking and fault tolerance; Spring Cloud for microservice coordination

## Rationale
This architecture leverages managed AWS services to guarantee 99.95% availability, sub-2-second page loads on 3G, and seamless global scalability for 1M MAU. Event-driven decoupling via Apache Kafka and strict component boundaries ensure GDPR/CCPA compliance and fault-tolerant e-commerce operations.