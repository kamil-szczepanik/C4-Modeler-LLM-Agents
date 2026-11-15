## Overview
The Claims Core Domain Service is a .NET 8 modular monolith container responsible for processing insurance claims within a hybrid Azure and on-premise legacy mainframe architecture. It implements core business logic, feature-flagged routing for gradual claim migration, and strict security controls to support the 3-year modernization program.

## Key Elements
- **Claim Management Controller**: Exposes REST/gRPC endpoints secured via mTLS for handling write and read operations.
- **Claim Domain Model & Engine**: Implements tactical Domain-Driven Design aggregates and value objects for insurance logic.
- **Claim Routing & Policy Engine**: Evaluates feature flags and rules per claim type to dynamically route execution paths.
- **Data Access Repository**: Abstracts persistence over Azure SQL Database using Entity Framework Core.
- **Telemetry & Domain Event Dispatcher**: Emits sanitized structured domain events and telemetry.

## Relationships
- **API Gateway -> Claims Core Domain Service**: Routes incoming validated JWT requests via gRPC/REST with mTLS.
- **Claims Core Domain Service -> Azure SQL Database**: Reads and writes transactional data using TCP/TLS 1.3 with TDE.
- **Claims Core Domain Service -> Azure Key Vault**: Retrieves encryption keys and secrets via Managed Identity and HTTPS.
- **Telemetry & Domain Event Dispatcher -> Azure Monitor**: Ships scrubbed operational metrics and audit logs via OpenTelemetry.

## Technology Stack
- **.NET 8 (C#)**: Chosen for the modular monolith implementation to match the team's cloud experience level while ensuring strict boundaries.
- **Entity Framework Core**: Provides robust object-relational mapping for Azure SQL persistence.
- **OpenTelemetry / .NET ILogger**: Native telemetry framework used to emit operational metrics without added complexity.
- **Azure Key Vault & Managed Identity**: Secures secrets and database credentials without hardcoded connection strings.

## Rationale
The modular monolith architecture directly enables the 24-hour rollback constraint and gradual claim type migration while keeping operational complexity low for a cloud-inexperienced team. Decoupled internal routing and dedicated security components protect sensitive data and provide the auditability required during the legacy modernization phase.