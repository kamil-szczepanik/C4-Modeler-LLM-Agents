## Overview
Modernizes a regional insurer's 30-year-old mainframe claims system via a hybrid cloud platform while ensuring zero data loss during gradual migration. It decouples legacy components using asynchronous messaging to maintain high-performance user interfaces.

## Key Elements
- **Claims API (BFF)**: Node.js / TypeScript in Azure Kubernetes Service (AKS)
- **Mainframe Adapter**: Node.js / TypeScript in Azure Kubernetes Service (AKS)
- **Azure Service Bus**: Enterprise messaging platform (Premium Tier) containing Claim Submission Topic, Mainframe Sync Queue, and Audit Archive Subscription
- **Azure Functions**: Dead-Letter Handler and Replay Handler components
- **Storage**: Azure Blob Storage with immutable WORM policies
- **Security & Infrastructure**: Azure Key Vault, Azure Active Directory (Azure AD), Terraform/Bicep

## Relationships
- **Claims API (BFF)** -> **Claim Submission Topic**: Publishes claim events [AMQP]
- **Claim Submission Topic** -> **Mainframe Sync Queue**: Forwards messages via subscriptions [AMQP]
- **Mainframe Sync Queue** -> **Mainframe Adapter**: Consumes queued sync payloads [AMQP]
- **Claim Submission Topic** -> **Audit Archive Subscription**: Fans out event copies [AMQP]
- **Audit Archive Subscription** -> **Audit Trail Storage**: Persists raw event payloads [HTTPS]
- **Replay Handler** -> **Mainframe Sync Queue**: Re-injects replayed messages [AMQP]

## Technology Stack
- **Azure Service Bus (Premium Tier)**: Chosen for dedicated resources, strict message partitioning, and guaranteed throughput
- **Azure Functions**: Serverless execution for lightweight dead-letter and replay handling
- **Node.js / TypeScript (AKS)**: Containerized runtime for API and adapter services
- **Azure Blob Storage**: Immutable WORM storage for tamper-proof audit trails
- **Terraform / Bicep**: Infrastructure as Code for drift-free environment deployments

## Rationale
This hybrid architecture isolates the fragile, slow mainframe behind asynchronous queues to meet sub-2-second UI performance requirements. It ensures strict consistency and audit compliance to support a seamless, claim-type-by-claim-type migration.