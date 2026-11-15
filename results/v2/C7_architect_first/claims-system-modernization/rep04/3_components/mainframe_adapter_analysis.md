## Overview
[Gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern hybrid platform while ensuring uninterrupted claim processing.]

## Key Elements
[
• API Controller (.NET Core Web API)
• Translation Service (.NET Core Business Logic)
• Mainframe Connector (.NET Core Infrastructure)
• Audit & Reconciliation Logger (.NET Core State/Log Component)
• Idempotency Manager (.NET Core with Local SQLite/PostgreSQL)
• Active Directory (Corporate Identity Provider)
]

## Relationships
[
• Claims Integration Service -> API Controller: REST/JSON over mTLS
• API Controller -> Translation Service: In-memory data mapping
• Translation Service -> Mainframe Connector: Processed domain models
• Mainframe Connector -> Legacy COBOL/DB2 Mainframe: Legacy Protocol / DB2 over TCP/Sockets/CICS/MQ
• Mainframe Connector -> Azure Key Vault: Dynamic credential sync via hybrid sync
]

## Technology Stack
[
• .NET Core: Selected for the Mainframe Adapter for high-performance on-premises execution
• SQLite / PostgreSQL: Local on-premise storage for idempotency tracking and state persistence
• mTLS & Azure Key Vault: Ensures secure communication and dynamic secret rotation
• OpenTelemetry & Prometheus/Grafana: Provides distributed tracing and batch-window operational metrics
]

## Rationale
[
• The hybrid on-premises Mainframe Adapter architecture bridges cloud services securely while guaranteeing low-latency proximity to the legacy mainframe.
• Component-level design patterns (like data abstraction and idempotency management) ensure transactional consistency, zero data loss, and rapid one-day rollbacks.
]