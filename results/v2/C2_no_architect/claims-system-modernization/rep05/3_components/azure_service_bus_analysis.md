## Overview
The system is a hybrid Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native Azure stack. Its core purpose is to decouple online claim submissions and adjuster workflows from the mainframe while guaranteeing zero message loss and seamless migration fallback.

## Key Elements
- **Azure Service Bus (Premium Tier):** Core messaging backbone handling asynchronous event publishing and queuing.
- **Backend-For-Frontend (BFF) Container (Node.js):** Message producer enforcing schema validation and envelope encryption.
- **Message Consumers (AKS):** Scaled via KEDA to process events asynchronously.
- **Azure Key Vault:** Manages Customer-Managed Keys (CMK) for encryption at rest.
- **ArgoCD & Terraform:** GitOps pipeline for infrastructure management.

## Relationships
- **BFF Container -> Azure Service Bus:** Publishes asynchronous claim events over AMQP with TLS 1.3 and Managed Identities (Azure RBAC).
- **Azure Service Bus -> Message Consumers:** Delivers queued events for downstream processing via secure Private Link endpoints.
- **Azure Service Bus -> Azure Key Vault:** Secures payload data at rest using Customer-Managed Keys.

## Technology Stack
- **Azure Service Bus Premium Tier:** Selected to support 14-day message retention, VNet integration, and partitioned throughput.
- **Azure Private Link & Private Endpoints:** Secures hybrid connectivity by bypassing the public internet entirely.
- **Azure RBAC & Managed Identities:** Replaces SAS keys to enforce least-privilege access control.
- **KEDA (Kubernetes Event-driven Autoscaling):** Scales processor pods dynamically based on queue depth (`MessagesActive`).

## Rationale
This architecture uses Azure Service Bus Premium with strict security, private networking, and idempotency controls to satisfy strict consistency (R-04) and security (R-07) requirements in a hybrid migration. It insulates the fragile on-premises mainframe from traffic spikes while safely handling operational retries and gradual claim-type migrations.