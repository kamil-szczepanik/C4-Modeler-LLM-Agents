## Overview
• The system is a hybrid cloud messaging and infrastructure layer designed to support the gradual modernization of a 30-year-old mainframe claims platform.
• It provides reliable asynchronous messaging, secure secret management, container orchestration, and immutable auditing to ensure zero claim loss during migration.

## Key Elements
• Message Broker Interface: Azure Service Bus with AMQP 1.0 and Dead-Letter Queues.
• Container Runtime Host: Azure Container Apps with KEDA for microservices orchestration.
• Secret & Config Store: Azure Key Vault for credentials and connection strings.
• Audit & Telemetry Forwarder: Azure Monitor and OpenTelemetry exporter.
• Storage Sink: Azure Blob Storage with WORM policies for immutable audit logs.

## Relationships
• Claims Processing Service -> Message Broker Interface: Publishes and consumes claim events [AMQP 1.0].
• Container Runtime Host -> Audit & Telemetry Forwarder: Emits traces and audit logs [HTTPS].
• Azure Container Apps -> Azure Service Bus & Azure Key Vault: Authenticates via Microsoft Entra ID Managed Identities [mTLS / Private Endpoints].

## Technology Stack
• Azure Service Bus: Chosen for managed, reliable asynchronous messaging to prevent data loss (R-04).
• Azure Container Apps & KEDA: Selected to provide event-driven scaling while mitigating the team's lack of deep Kubernetes experience.
• Azure Key Vault: Implemented for centralized secret management and automated 90-day secret rotation.
• Azure Blob Storage WORM: Utilized for immutable audit logging to satisfy insurance compliance standards.
• Azure Bicep & GitHub Actions: Deployed via Infrastructure as Code with automated smoke tests for zero-downtime blue-green deployments.

## Rationale
• This architecture directly satisfies zero-loss consistency (R-04) and maintainability (R-06) requirements through reliable managed queuing and clear component boundaries.
• It minimizes operational overhead for a cloud-inexperienced team while meeting strict hybrid-cloud security and regulatory compliance constraints.