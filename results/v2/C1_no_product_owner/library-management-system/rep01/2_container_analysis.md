## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It is architected as a distributed containerized system prioritizing strict EU data residency and high-performance search capabilities.

## Key Elements
- **Library Patrons & Staff**: End-users interacting via self-service portals and staff interfaces.
- **Web Application**: Single Page Application built with React/TypeScript, served via AWS CloudFront Frankfurt.
- **API Gateway**: Kong / Node.js reverse proxy handling client entry.
- **Catalogue & Search Service**: Java / Spring Boot service backed by Elasticsearch.
- **Circulation & User Service**: Go / Spring Boot service managing loans and patrons.
- **Notification Worker Service**: Go background worker processing asynchronous alerts.
- **Apache Kafka (AWS MSK)**: Event-driven broker for decoupled domain events.
- **Database**: Managed PostgreSQL cluster.
- **External Systems**: External Payment Gateway, Digital Repository / DRM Provider, External Notification Service.

## Relationships
- **Web Application to API Gateway**: HTTPS / REST.
- **API Gateway to Internal Services**: gRPC with mTLS.
- **Services to Apache Kafka**: Asynchronous Avro/JSON over TLS.
- **Catalogue & Search Service to Elasticsearch**: Internal VPC TCP.
- **Notification Worker to External Notification Service**: Outbound HTTPS with strict egress filtering.

## Technology Stack
- **Frontend**: React and TypeScript for interactive client interfaces.
- **Routing**: Node.js / Kong API Gateway for secure traffic entry and token validation.
- **Backend Services**: Java / Spring Boot for high-throughput catalogue operations; Go for efficient circulation and notification workers.
- **Databases & Search**: PostgreSQL for relational data; Elasticsearch for rapid searching.
- **Messaging**: Apache Kafka (AWS MSK) for reliable event streaming.
- **Infrastructure & Security**: AWS Frankfurt region, EKS, AWS CloudFront, OAuth2/OIDC, mTLS, TLS 1.3, and AWS KMS for encryption.

## Rationale
This architecture uses co-located Frankfurt-based services and Elasticsearch to reliably achieve sub-800ms search latency (R-05). Strict regional deployment, mTLS, and encrypted Kafka streams guarantee compliance with EU-only data residency constraints.