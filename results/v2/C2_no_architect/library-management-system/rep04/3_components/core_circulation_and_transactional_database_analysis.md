## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture ensures strict EU data residency and high performance for patrons and staff.

## Key Elements
- Library Patrons (Members)
- Librarians / Library Staff
- Library Administrators
- Self-Service Web/Mobile Portal
- API Gateway
- Core Circulation and Transactional Database
- Read-optimized Search Index
- Admin/Reporting Container
- Inter-Library Loan (ILL) Partners
- Payment Gateways & Notification Services

## Relationships
- Self-Service Web/Mobile Portal -> API Gateway: Routes requests [HTTPS, OAuth2/OIDC]
- API Gateway -> Core Circulation and Transactional Database: Routes traffic and executes parameterized statements [mTLS]
- Core Circulation and Transactional Database -> Read-optimized Search Index: Queries search index [Internal Network]
- Core Circulation and Transactional Database -> Message Broker: Publishes domain events via Change Data Capture [Debezium, WAL, JWE]

## Technology Stack
- Kubernetes: Container orchestration for services with strict EU-region clustering
- PostgreSQL with Raft/Patroni: Core transactional database ensuring strong consistency and <200ms write-latency SLO
- Elasticsearch: Read-optimized search index for sub-800ms search response compliance
- HashiCorp Vault: Dynamic database credentials and secret rotation (max 24-hour TTL)
- Debezium: Change Data Capture (CDC) reading from database write-ahead log (WAL) for event-outbox pattern

## Rationale
This architecture guarantees strict EU data residency and robust security through zero-trust mTLS, AES-256 encryption, and JWE event payloads. It meets strict performance SLOs using Raft/Patroni synchronous replication and asynchronous event decoupling.