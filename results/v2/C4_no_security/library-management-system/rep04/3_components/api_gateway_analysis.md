## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue items, manage circulation, and provide self-service portals while maintaining EU-only data residency. The system uses a microservices architecture fronted by a reactive API Gateway to ensure high-performance search and secure multi-tenant operations.

## Key Elements
- **Users**: Library Patrons, Librarians and Circulation Staff, Library Administrators
- **Containers**: Patron Web App & Staff Portal (TypeScript/React), API Gateway (Spring Cloud Gateway), Catalog & Search Service (Java/Spring Boot + Elasticsearch), Circulation Service (Java/Spring Boot + PostgreSQL), Internal Event Bus (Apache Kafka)
- **External Systems**: Identity Provider, Payment Gateway, Notification Service, Digital Content Providers, EU-hosted Log & Metrics Aggregator
- **API Gateway Components**: Routing & Versioning Filter, Tenant Context Extractor, Security & Rate Limiting Filter, Resilience & Tracing Filter

## Relationships
- Patron Web App & Staff Portal -> API Gateway: Sends client requests [HTTPS/REST, WebSockets]
- API Gateway -> Identity Provider: Validates OAuth2/OIDC JWT tokens [HTTPS/REST]
- API Gateway -> Catalog & Search Service: Routes search and catalog requests [internal gRPC]
- API Gateway -> Circulation Service: Routes circulation requests [internal gRPC]
- API Gateway -> EU-hosted Log & Metrics Aggregator: Forwards access logs and tracing metrics [OTLP/gRPC]
- API Gateway -> Internal Event Bus: Publishes gateway audit events [Apache Kafka]

## Technology Stack
- Spring Cloud Gateway (Java/WebFlux): Non-blocking reactive routing, security integration, and filter execution
- Elasticsearch & PostgreSQL: Core data persistence for search and transactional circulation data
- Apache Kafka: Asynchronous event messaging and auditing
- Kubernetes (EKS/AKS in EU-central) & Helm/ArgoCD: Container orchestration and GitOps deployments
- Resilience4j: Circuit breaking and fault tolerance

## Rationale
This architecture uses Spring Cloud Gateway with reactive Netty worker pools to guarantee sub-800ms search performance and robust rate-limiting under high concurrency. All components are deployed within EU-central infrastructure to strictly satisfy EU data residency constraints.