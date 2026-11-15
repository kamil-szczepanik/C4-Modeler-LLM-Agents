## Overview
The New Claims Platform is a hybrid cloud solution gradually replacing a 30-year-old on-premise COBOL/DB2 mainframe claims system. It enables online claim submission for customers and modern claims processing for adjusters via managed Azure services while maintaining core data integrity.

## Key Elements
- Claims Adjusters (person)
- Adjuster Web App (container: React/Node.js BFF)
- UI Shell & Routing (component)
- Claim Action Queue (component)
- BFF Orchestrator Service / BFF Claim Controller (component)
- Session & Token Manager (component)
- Claims Core API (container: .NET Core modular monolith, Azure Container Apps)
- Insurer Active Directory (externalSystem)

## Relationships
- Claims Adjuster -> UI Shell & Routing [HTTPS / HTML]
- UI Shell & Routing -> BFF Orchestrator Service [HTTP / JSON]
- BFF Orchestrator Service -> Claims Core API [HTTPS / JSON]
- Session & Token Manager -> Insurer Active Directory [OIDC / OAuth2 via Azure Entra ID Connect]

## Technology Stack
- React / TypeScript: Chosen for the SPA frontend to deliver sub-2-second adjuster screen loads.
- Node.js / Express: Implements the Backend-For-Frontend (BFF) pattern to isolate frontend from backend latency.
- Azure Container Apps: Simplifies deployment and KEDA auto-scaling for teams with low cloud experience.
- Zod / Joi: Used within the BFF for strict JSON payload validation and security hardening.

## Rationale
The hybrid architecture and BFF pattern protect operational stability by isolating legacy mainframe latency and supporting gradual, claim-type-by-claim-type migration. Unified Azure deployment minimizes operational complexity for a team with limited cloud expertise.