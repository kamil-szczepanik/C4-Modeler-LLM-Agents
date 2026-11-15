## Overview
The Audit Logging Container is a compliance-focused component of the Library Management System that securely ingests, buffers, cryptographically chains, and stores immutable audit trails. It provides secure export endpoints for compliance officers while strictly adhering to EU data residency requirements.

## Key Elements
- **Compliance Officers & System Administrators**: Primary human actors accessing logs and compliance reports.
- **API Gateway**: Upstream router submitting logs.
- **Observability Platform**: External sink for metrics and traces.
- **Audit Ingestion API**: Express/gRPC handler with mTLS authentication.
- **Event Normalizer**: TypeScript component enforcing cryptographic hash-chaining.
- **Local Buffer Manager**: SQLite with Write-Ahead Logging (WAL) on encrypted storage.
- **Compliance Storage Writer**: PostgreSQL/TimescaleDB with write-only roles and TDE.
- **Compliance Query Service**: REST/GraphQL API protected by JWT/OAuth2 RBAC.
- **Telemetry Exporter**: OpenTelemetry SDK.

## Relationships
- API Gateway -> Audit Ingestion API: Ingests audit logs [gRPC over mTLS]
- Audit Ingestion API -> Event Normalizer: Passes raw events [In-memory]
- Event Normalizer -> Local Buffer Manager: Buffers hash-chained events [Local Disk / SQLite WAL over dm-crypt]
- Local Buffer Manager -> Compliance Storage Writer: Flushes batched records [SQL over TLS]
- Compliance Storage Writer -> PostgreSQL/TimescaleDB: Persists immutable records [SQL over TLS with TDE]
- Compliance Officers -> Compliance Query Service: Exports audit trails [HTTPS]
- Compliance Query Service -> Compliance Storage Writer: Reads immutable logs [SQL over TLS]
- Telemetry Exporter -> Observability Platform: Streams traces and metrics [OTLP over TLS]

## Technology Stack
- **Node.js**: Core runtime chosen for asynchronous processing efficiency.
- **Express / gRPC**: Protocols for high-performance internal ingestion and REST/GraphQL querying.
- **SQLite with WAL**: Local durable buffer preventing log loss during database latency.
- **PostgreSQL / TimescaleDB**: Append-only storage utilizing Transparent Data Encryption (TDE) for EU data residency compliance.
- **OpenTelemetry SDK**: Standardized protocol for exporting system metrics and traces.
- **LUKS / dm-crypt**: Encrypted volumes securing transient local buffer files.

## Rationale
This architecture ensures tamper-evident audit logging and strict EU data residency compliance through encrypted local buffering, cryptographic hash-chaining, and write-only database constraints. It simultaneously guarantees high performance and operational resilience during peak database latency.