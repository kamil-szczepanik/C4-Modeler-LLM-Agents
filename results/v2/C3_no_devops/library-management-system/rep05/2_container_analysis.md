## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-second search performance constraints.

## Key Elements
- **Users:** Library Patrons, Librarians / Circulation Staff, Library Administrators
- **Client Container:** Web Application (React/TypeScript SPA hosted on Nginx)
- **Gateway Container:** API Gateway (Spring Cloud Gateway, Java)
- **Backend Container:** Core Services Container (Spring Boot, Java)
- **Search Container:** Elasticsearch / OpenSearch
- **Data & Messaging Containers:** PostgreSQL (AWS RDS EU), Message Broker (Apache Kafka/RabbitMQ)
- **External Services:** Stripe EU, Keycloak/Auth0 EU tenant, SendGrid EU

## Relationships
- *Web Application* -> *API Gateway* via HTTPS (REST/GraphQL, TLS 1.3)
- *API Gateway* -> *Core Services* & *Search Container* via internal gRPC/HTTPS using mTLS
- *Core Services* -> *PostgreSQL* & *Elasticsearch* via internal TCP/gRPC with mTLS
- *Core Services* -> *Message Broker* via AMQP/Kafka with mTLS and SASL/SCRAM
- *Core Services* -> *Stripe EU*, *SendGrid EU* via HTTPS (REST)
- *Core Services* -> *Keycloak EU* via OIDC/OAuth2

## Technology Stack
- **Frontend:** React, TypeScript, Nginx for fast SPA delivery
- **Backend/Gateway:** Java, Spring Boot, Spring Cloud Gateway for robust business logic and routing
- **Search:** Elasticsearch/OpenSearch to guarantee 99th-percentile search response < 800 ms
- **Database/Messaging:** PostgreSQL (AWS RDS) and Apache Kafka/RabbitMQ for resilient data persistence and event-driven architecture
- **Security:** Keycloak/Auth0 for OIDC/OAuth2 auth, HashiCorp Vault/AWS Secrets Manager for EU secret management, AES-256 and TLS 1.3/mTLS for data protection

## Rationale
This container decomposition isolates the search workload into a dedicated Elasticsearch instance to reliably achieve sub-800ms response times. Furthermore, restricting all hosting, databases, message brokers, and third-party integrations strictly to EU infrastructure fulfills the mandatory data residency constraints.