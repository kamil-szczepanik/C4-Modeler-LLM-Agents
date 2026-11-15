## Overview
[The system modernizes a 30-year-old regional insurer mainframe claims system by gradually replacing claim types with a cloud platform while maintaining legacy operations.]
[It uses a hybrid cloud Backend-for-Frontend (BFF) architecture on Azure to optimize adjuster workflows, meet strict performance requirements, and ensure reliable failovers.]

## Key Elements
* Customer / Policyholder (Person)
* Broker (Person)
* Claims Adjuster (Person)
* Adjuster Web App (Azure Container Apps)
* Backend-for-Frontend (BFF) (Azure Container Apps / Azure Cache for Redis)
  * API Router & Auth Middleware
  * Aggregation & Orchestration Service
  * Caching & Resilience Layer
  * Feature-Flag Evaluation Engine
  * Telemetry & Correlation Middleware
* Claim Processing Core (Azure Container Apps / Azure Service Bus)
* Legacy Mainframe System (COBOL/DB2 on-prem)
* Azure App Configuration
* Azure AD / Entra ID

## Relationships
* Adjuster Web App -> Backend-for-Frontend (BFF): Requests claim data and workflows via HTTPS / gRPC over Azure Managed Identities
* API Router -> Azure AD / Entra ID: Validates JWT tokens and enforces RBAC via HTTPS / OIDC
* Aggregation Service -> Azure Cache for Redis: Reads/writes cached claim data using Cache-Aside pattern
* Feature-Flag Evaluation Engine -> Azure App Configuration: Evaluates claim-type migration state via HTTPS
* BFF -> Claim Processing Core: Forwards modern claim requests via gRPC over HTTP/2 with OpenTelemetry context
* BFF -> Legacy Mainframe System: Routes unmigrated or rolled-back claim requests via HTTPS / TLS

## Technology Stack
* Node.js (Fastify) or Go (Gin): Selected for high-throughput API routing in the BFF layer.
* Azure Container Apps: Provides serverless container hosting tailored for teams with low cloud experience.
* Azure Cache for Redis: Implements caching and circuit-breaker fallbacks to guarantee sub-2-second adjuster screen loads despite 5-second legacy responses.
* gRPC over HTTP/2: Ensures low-latency, strongly-typed inter-service communication.
* OpenTelemetry: Provides distributed tracing and observability for cross-service calls.
* Azure App Configuration: Stores dynamic feature flags enabling 1-day claim-type rollbacks to the mainframe.

## Rationale
[The BFF architecture isolates frontend clients from legacy system complexities, using caching and payload optimization to consistently meet the sub-2-second adjuster screen load requirement.]
[Feature-flagged routing and secure hybrid connectivity ensure zero data loss, strict RBAC security, and rapid 1-day rollback capabilities without requiring complex cloud expertise.]