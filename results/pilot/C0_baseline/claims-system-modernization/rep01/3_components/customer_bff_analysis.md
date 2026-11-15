## Overview
[The Customer BFF is a Node.js/TypeScript backend-for-frontend service deployed in Azure Container Apps that abstracts hybrid legacy migration complexities for policyholders and brokers.]
[It provides secure, resilient online claim submission routing, direct-to-cloud asset uploads, and multi-step session caching.]

## Key Elements
* Policyholders and Brokers
* Azure API Management Gateway (Azure API Management)
* Customer BFF (Node.js, TypeScript, Azure Container Apps)
* Authentication Controller, Claim Submission Router, Downstream Orchestrator
* Routing Anti-Corruption Layer (ACL), Validation and Sanitization Component (Zod)
* State Cache Manager (Redis Cache)
* Asset Direct-Upload Handler (Azure Blob Storage, SAS Tokens)
* Modular Monolith (Node.js, TypeScript)

## Relationships
* Policyholders and Brokers -> Azure API Management Gateway: Submits claims and uploads assets [HTTPS, OAuth2/OIDC]
* Azure API Management Gateway -> Customer BFF: Routes validated requests [HTTPS, TLS 1.3]
* Customer BFF -> Azure Blob Storage: Issues SAS tokens for direct media uploads [HTTPS]
* Customer BFF -> Redis Cache: Persists multi-step wizard state [TCP]
* Customer BFF -> Modular Monolith: Forwards validated claim operations [HTTP/REST, mTLS]

## Technology Stack
* Node.js with TypeScript: Core runtime for rapid development with limited cloud experience
* Azure Container Apps: Managed container platform simplifying orchestration and scaling
* Redis Cache: Distributed session storage for multi-step claim recovery
* Azure Blob Storage: Secure cloud storage for large media attachments via SAS tokens
* Zod: TypeScript-first schema validation for strict payload sanitization

## Rationale
[A managed Azure Container Apps deployment reduces operational overhead for a team with limited cloud experience while ensuring high availability.]
[Internal components like Redis caching and SAS token offloading optimize performance, security, and resilience during hybrid migration phases.]