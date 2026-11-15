## Overview
[The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals.]
[The architecture enforces strict EU-only data residency and meets high-performance search SLAs below 800 milliseconds.]

## Key Elements
- Library Patrons and Staff (Users)
- Self-Service Portals and Kiosks (Web/Mobile UI)
- API Gateway
- Core Domain Services (Microservices)
- Dedicated Search Tier (Search Infrastructure)
- Primary Transactional Datastore (Relational Database / SQL)
- Caching Layer (Redis)
- Asynchronous Event Bus (Message Broker / Kafka)
- EU-certified Secrets Management Vault

## Relationships
- Self-Service Portals and Kiosks -> API Gateway: HTTP/REST requests
- API Gateway -> Core Domain Services: HTTP/REST, OpenAPI, gRPC
- Core Domain Services -> Primary Transactional Datastore: queries and transactions [TCP/SQL]
- Core Domain Services -> Asynchronous Event Bus: publishes domain events [AMQP/Kafka]
- Asynchronous Event Bus -> Dedicated Search Tier: asynchronous data synchronization for search index

## Technology Stack
- Primary Transactional Datastore: Relational Database / SQL ensuring ACID compliance for circulation workflows
- Caching Layer: Redis for in-memory caching
- Asynchronous Event Bus: Kafka/AMQP for event-driven CQRS data synchronization
- Security: EU-certified Secrets Management Vault for dynamic credential rotation
- Deployment: EU-based cloud regions for strict data residency compliance

## Rationale
[Relational database storage combined with an asynchronous CQRS pattern protects transactional integrity while offloading heavy queries to a Dedicated Search Tier to satisfy performance SLAs.]
[Enforcing EU-only data residency, dynamic secret rotation, and automated backups ensures strict regulatory compliance and disaster recovery readiness.]