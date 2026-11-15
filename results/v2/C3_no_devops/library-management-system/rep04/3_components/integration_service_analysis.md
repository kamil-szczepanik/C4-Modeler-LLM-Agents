## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It achieves a 99th-percentile search response time under 800 ms.

## Key Elements
- Library Patron (Member), Librarian / Circulation Staff, Library Administrator
- API Gateway (Nginx/Kong), Patron Portal (React SPA), Staff Dashboard (Angular SPA)
- Core Circulation & Cataloguing Service (Spring Boot), Search Service (Elasticsearch)
- Integration Service (Node.js/TypeScript)
- Notification Worker (Python/Celery), Reporting Service (Python/FastAPI)
- PostgreSQL, PostgreSQL Read Replica, RabbitMQ
- External Systems: Identity Provider (IdP), Payment Gateway, Notification Service, Inter-Library Loan (ILL) Network

## Relationships
- Patron Portal & Staff Dashboard -> API Gateway [HTTPS/REST]
- API Gateway -> Core Circulation & Cataloguing Service [gRPC]
- API Gateway -> Integration Service [HTTPS/REST with OAuth2/JWT]
- Core Circulation & Cataloguing Service -> Search Service [Elasticsearch Protocol]
- Core Circulation & Cataloguing Service -> PostgreSQL / PostgreSQL Read Replica [SQL over TLS]
- Integration Service -> External Systems [REST/Webhooks over mTLS with HMAC-SHA256 signature verification]
- Integration Service -> RabbitMQ [AMQP]

## Technology Stack
- **Frontend**: React SPA (Patron Portal), Angular SPA (Staff Dashboard)
- **Backend**: Spring Boot (Core Service), Node.js/TypeScript (Integration Service), Python/FastAPI & Python/Celery (Reporting and Notifications)
- **Database & Messaging**: PostgreSQL (Primary data store), Elasticsearch (Search), RabbitMQ (Message broker)
- **Integration Service Components**: Express.js (Webhook Ingress & Reconciliation Controller), BullMQ (Outbound Sync Worker), Axios with `opossum` (External Adapter Layer), Prisma/Knex (Transaction State Repository), HashiCorp Vault (Secrets Management)

## Rationale
This architecture isolates external third-party integrations into a dedicated Node.js container using circuit breakers and retry queues to ensure operational resilience and prevent external outages from blocking core library circulation. Security controls such as mTLS, HMAC verification, and PII-scrubbed audit logs enforce strict EU data residency and financial compliance.