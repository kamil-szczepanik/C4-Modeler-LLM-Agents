## Overview
[A hybrid modernization platform that gradually replaces a legacy COBOL/DB2 mainframe claims system with a cloud-native Azure architecture while maintaining business continuity. The system processes online claims via a secure web portal while preserving legacy batch processing constraints.]

## Key Elements
* Customer Portal Container (React / Node.js)
* Claims SPA Component (React, TypeScript)
* Claim Validation & Mapping Component (Node.js, Zod)
* BFF Routing & Session Component (Node.js, Express)
* API Gateway (Azure API Management / NGINX)
* Integration & Anti-Corruption Layer (.NET Core / MassTransit)
* Legacy Mainframe System (COBOL/DB2)
* Corporate Active Directory / Azure AD

## Relationships
* Claims SPA -> Claim Validation & Mapping: Validates payloads locally [In-process]
* Claim Validation & Mapping -> BFF Routing & Session: Passes validated claim data [In-process]
* BFF Routing & Session -> API Gateway: Proxies authenticated requests [HTTPS / REST]
* API Gateway -> Integration & Anti-Corruption Layer: Routes domain requests [Internal HTTPS]
* Integration & Anti-Corruption Layer -> Legacy Mainframe: Synchronizes data [MQ / DB2 Connect]

## Technology Stack
* React & TypeScript: Frontend user interface for customer and broker claim submissions
* Node.js & Express: Backend-for-Frontend (BFF) handling sessions and API aggregation
* Zod: Server-side schema validation for input sanitization
* Azure Container Apps: Stateless containerized deployment target for the portal tier
* Azure Active Directory: Single sign-on authentication and RBAC via Azure Managed Identity
* OpenTelemetry & Azure Monitor: Distributed tracing and observability for hybrid latency tracking

## Rationale
[This hybrid architecture isolates complex legacy mainframe dependencies behind an anti-corruption layer while delivering a modern, responsive web experience. It minimizes risk by migrating claim types incrementally, keeping migration downtime low and ensuring seamless compliance with security and latency constraints.]