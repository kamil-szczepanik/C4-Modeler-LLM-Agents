## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It operates entirely within EU-compliant cloud regions to satisfy strict data residency mandates.

## Key Elements
- Library Patron (Person)
- Librarian (Person)
- Library Management System (Software System)
- Single-Page Application (Container)
- API Gateway / Kong (Container)
- Core Domain Services / Spring Boot (Container)
- PostgreSQL & OpenSearch (Containers)
- Apache Kafka / RabbitMQ (Container)
- Identity Provider (External System)
- Payment Gateway (External System)
- Digital Content Provider (External System)
- Notification Service (External System)
- National Library Registry (External System)
- Physical Access Control System (External System)

## Relationships
- Library Patron -> Single-Page Application: Accesses portals via HTTPS
- Single-Page Application -> API Gateway: Routes requests via HTTPS/WSS
- API Gateway -> Core Domain Services: Forwards validated requests via gRPC/REST
- Core Domain Services -> PostgreSQL & OpenSearch: Queries data via SQL/REST
- Core Domain Services -> Apache Kafka / RabbitMQ: Publishes events asynchronously
- Library Management System -> Identity Provider: Authenticates via OIDC/HTTPS
- Library Management System -> Payment Gateway: Processes fines via REST/TLS
- Library Management System -> Notification Service: Sends reminders via REST/TLS

## Technology Stack
- React/TypeScript: Powers the frontend SPA for high interactivity
- Kubernetes: Orchestrates backend container instances in EU regions
- PostgreSQL: Manages transactional circulation data reliably
- OpenSearch: Delivers high-performance search indexing meeting latency requirements
- Apache Kafka/RabbitMQ: Enables decoupled event-driven processing

## Rationale
This architecture utilizes containerized microservices orchestrated in EU regions to guarantee strict data residency compliance. Dedicated search infrastructure and decoupled messaging ensure rapid response times and system scalability.