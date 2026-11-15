## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The Staff Workflow Container manages administrative operations and bulk cataloguing for library staff.

## Key Elements
- Staff Workflow Container (Spring Boot 3 / Java 21)
- Workflow Orchestrator Component (Spring MVC / REST Controllers)
- Audit Logging Interceptor Component (Spring AOP)
- Catalogue Integration Client (gRPC Stub)
- Batch Job Manager Component (Spring Batch)
- External Identity Provider (IdP)
- Catalogue & Search Service Container
- Circulation & Loan Service Container

## Relationships
- API Gateway / Ingress -> Workflow Orchestrator Component: Routes staff traffic [HTTP / TLS 1.3]
- Workflow Orchestrator Component -> External IdP: Validates OAuth2/OIDC JWTs [HTTPS]
- Workflow Orchestrator Component -> Batch Job Manager Component: Submits asynchronous jobs [In-Process]
- Catalogue Integration Client -> Catalogue & Search Service Container: Queries and updates catalogue [gRPC over mTLS]
- Batch Job Manager Component -> Circulation & Loan Service Container: Executes batch mutations [gRPC over mTLS]

## Technology Stack
- Java 21 / Spring Boot 3: Selected for native virtual threads support to optimize high-concurrency staff operations.
- Spring AOP & Spring Batch: Used for implementing immutable audit logging and asynchronous bulk item processing.
- OAuth2/OIDC & HMAC-SHA256: Enforces role-based access control and tamper-proof administrative audit logs.

## Rationale
This architecture ensures secure, compliant, and high-performance staff operations adhering to EU data residency rules. Internal component decomposition and asynchronous batch processing maintain interface responsiveness under heavy administrative workloads.