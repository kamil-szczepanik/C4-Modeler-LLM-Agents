## Overview
[A secure, hybrid platform managing the modernization of a legacy insurance claims system while ensuring data consistency and minimal operational disruption.]

## Key Elements
- Migration Operations Managers (Primary Persona)
- Admin Web Frontend (React/TypeScript SPA)
- Operations BFF (.NET Core Web API)
- Migration Control Service (.NET Core Component)
- Reconciliation & Metrics Aggregator (.NET Core Component)
- Claims API Gateway
- Azure Service Bus / Apache Kafka

## Relationships
- Migration Operations Managers -> Admin Web Frontend: `HTTPS/TLS 1.3 (OIDC/OAuth2 SSO via Azure AD)`
- Admin Web Frontend -> Operations BFF: `HTTPS REST [JSON]`
- Operations BFF -> Claims API Gateway: `HTTPS REST/GraphQL`
- Operations BFF -> Reconciliation & Metrics Aggregator: `In-process gRPC / Direct Method Call`
- Reconciliation & Metrics Aggregator -> Azure Service Bus / Kafka: `AMQP / Kafka Protocol`

## Technology Stack
- React / TypeScript: Chosen for the admin frontend to maintain SPA performance and maintainability.
- .NET Core: Used for the BFF and internal components for architectural consistency and team skill alignment.
- Azure Active Directory & RBAC: Implements mandatory MFA and role-based access for security (R-07).
- Azure Key Vault & Managed Identities: Secures administrative secrets and enforces least privilege access.
- Azure Monitor / Sentinel: Captures immutable audit logs for compliance.

## Rationale
[The architecture mitigates migration risks by providing robust administrative controls and real-time consistency tracking while respecting the team's low cloud experience constraint. It strictly enforces security and maintainability (R-04, R-06) within a unified .NET and React stack.]