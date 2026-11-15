## Overview
A public and academic library management system that catalogues physical and digital items, manages circulation, and provides self-service patron portals. It enforces strict EU-only data residency and high-performance search SLAs.

## Key Elements
- **Users**: Library Patrons, Librarians, Administrators
- **External Systems**: External Identity Provider (IdP), Payment Gateway, Notification Service
- **Containers**: Web App / SPA (React/TypeScript), API Gateway (Envoy/Kong), Core Services Container (Java/Spring Boot), Search Container (Elasticsearch), Audit Container (Go), Message Broker (Apache Kafka/RabbitMQ), Database (PostgreSQL)
- **Infrastructure**: Kubernetes cluster with EU node affinity, HashiCorp Vault / Cloud KMS

## Relationships
- Patrons and Librarians interact with Web App / SPA via HTTPS
- Web App communicates with API Gateway via HTTPS
- API Gateway routes traffic to Core Services via gRPC/REST over mTLS
- Core Services queries Search Container (Elasticsearch) and PostgreSQL via mTLS
- Core Services publishes events to Message Broker; Audit Container consumes security events via Message Broker
- System integrates with external IdP, Payment Gateway, and Notification Service

## Technology Stack
- **Frontend**: React/TypeScript served via CDN for patron and librarian portals
- **Gateway & Routing**: Envoy/Kong API Gateway enforcing OAuth2/OIDC
- **Core Logic**: Java/Spring Boot modular monolith implementing RBAC
- **Search Engine**: Elasticsearch for low-latency queries meeting the <800ms SLA (R-05)
- **Data & Messaging**: PostgreSQL with EU hosting and encryption at rest; Apache Kafka/RabbitMQ for asynchronous events
- **Security & Infrastructure**: Kubernetes with EU-only node affinity, mTLS service mesh, HashiCorp Vault, and Cosign/Sigstore image signing

## Rationale
This architecture decouples heavy search and auditing loads from transactional paths to consistently achieve sub-800ms search responses. Furthermore, strict Kubernetes placement, mTLS, and localized message retention enforce EU-only data residency and compliance requirements.