## Overview
[The system modernizes a 30-year-old mainframe claims platform using a hybrid cloud architecture to migrate claim types gradually. The Migration Control & Routing Engine dynamically directs claims to either the legacy mainframe or modern platform to ensure zero data loss and enable rapid emergency rollbacks.]

## Key Elements
- Routing Rules Evaluator (Azure Function)
- Migration Registry Store (Azure Cosmos DB)
- Control Plane API (Azure Function)
- Traffic Splitter & Scheduler (Azure Function)
- Azure API Management (APIM)
- Azure Key Vault
- Azure Monitor / Sentinel
- Operations/Migration Managers

## Relationships
- Operations/Migration Managers -> Control Plane API: Manages routing rules and emergency rollbacks [HTTPS / Azure AD RBAC]
- Azure API Management -> Routing Rules Evaluator: Evaluates claim destination [REST / HTTPS]
- Routing Rules Evaluator -> Migration Registry Store: Reads active routing flags [Cosmos DB SDK / TLS 1.3]
- Routing Rules Evaluator -> Traffic Splitter & Scheduler: Delegates canary and temporal cohorts [Internal Function-to-Function / VNet Integration]
- Control Plane API -> Migration Registry Store: Persists schedules and feature flags [Cosmos DB SDK]

## Technology Stack
- Azure Functions (Serverless compute for routing logic and control plane APIs)
- Azure Cosmos DB (Low-latency NoSQL storage for migration registry state and routing rules)
- Azure AD / RBAC (Identity and access management for secure control plane operations)
- Azure Key Vault (Secure storage for salts and customer-managed keys)
- HMAC-SHA256 (Deterministic hashing for secure canary traffic splitting)

## Rationale
[This serverless architecture provides the sub-second latency required for adjuster screens while decoupling modernization efforts from rigid legacy constraints. The dedicated migration control components enable instant emergency rollbacks and canary deployments, satisfying zero-loss consistency and one-day switchback mandates.]