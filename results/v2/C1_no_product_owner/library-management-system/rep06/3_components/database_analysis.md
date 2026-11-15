## Overview
[Library Management System] provides cataloging, circulation, and self-service portals for public and academic libraries. It meets strict EU-only data residency and high-performance requirements.

## Key Elements
- **Core Domain Service** (Spring Boot / Java)
- **Database Container** (PostgreSQL 15)
- **Connection Pooler** (PgBouncer)
- **Relational Tables** (PostgreSQL SQL)
- **Security & Access Policy Engine** (PostgreSQL RLS / pgcrypto)
- **Audit Logging Module** (pgAudit extension)
- **Secrets Management** (HashiCorp Vault)

## Relationships
- **Core Domain Service -> Connection Pooler:** Routes queries via [JDBC over mTLS / TLS 1.3]
- **Connection Pooler -> Relational Tables:** Forwards pooled connections [PostgreSQL Native Protocol over TLS 1.3]
- **Relational Tables -> Audit Logging Module:** Captures security events [Internal PostgreSQL Hook]
- **Core Domain Service -> Secrets Management:** Injects dynamic tokens [OIDC / IAM]

## Technology Stack
- **PostgreSQL 15:** ACID-compliant relational persistence for structured operational data
- **PgBouncer:** Enterprise connection pooler to prevent backend worker exhaustion
- **pgAudit:** Database event tracking for EU regulatory compliance
- **pgcrypto & RLS:** Column-level encryption and row-level security for patron isolation
- **HashiCorp Vault:** Dynamic credential generation and secret rotation

## Rationale
This architecture uses PostgreSQL with RLS, pgcrypto, and pgAudit to enforce EU data residency and strict privacy mandates. PgBouncer and statement timeouts ensure high performance and resilience under peak loads.