## Overview
[A Node.js Backend-for-Frontend (BFF) and React single-page application running on Azure App Service, serving as the adjuster workspace for the hybrid claims modernization platform.]

## Key Elements
- Claims UI Router & View Controller (React/TypeScript)
- BFF Session & State Manager (Node.js/Express)
- Claims Query Aggregator (Node.js)
- Command Dispatcher (Node.js)
- Session Cache Client (Node.js ioredis)
- Azure App Service
- Azure Cache for Redis
- Azure Cosmos DB (SQL API)
- Claims Core API (AKS)
- Azure Key Vault

## Relationships
- Claims UI Router & View Controller -> BFF Session & State Manager [HTTPS]
- BFF Session & State Manager -> Session Cache Client [TCP/Redis Protocol with TLS]
- Claims Query Aggregator -> Azure Cosmos DB [HTTPS/SQL API]
- Command Dispatcher -> Claims Core API [gRPC with TLS 1.3]
- Node.js BFF -> Azure Key Vault [HTTPS via CSI Secret Store Drivers]

## Technology Stack
- Node.js & Express: Lightweight backend runtime for BFF aggregation and fast I/O
- React & TypeScript: Type-safe single-page application framework for UI components
- Azure App Service: Managed PaaS hosting for containerized BFF deployment
- Azure Cache for Redis: Distributed session cache ensuring stateless scaling
- Zod / Joi: Schema validation for robust input sanitization
- Azure Key Vault: Secure secrets management via CSI secret store drivers

## Rationale
[This architecture uses a Node.js BFF and parallel Cosmos DB reads to guarantee sub-2-second adjuster screen loads despite slow mainframe backend responses. Distributed caching and stateless App Service design ensure high scalability while accommodating the team's limited cloud experience.]