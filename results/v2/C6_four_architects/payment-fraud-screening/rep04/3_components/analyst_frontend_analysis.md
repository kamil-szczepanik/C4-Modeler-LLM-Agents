## Overview
The Analyst Frontend is a secure Single Page Application (SPA) that enables fraud analysts to review suspicious payment cases, inspect explainability payloads, and manage fraud rules. It is designed to maintain PCI-DSS compliance, support 7-year auditability, and operate within strict AWS infrastructure budgets.

## Key Elements
- Analyst Frontend (Amazon S3 + Amazon CloudFront SPA)
- Auth & Session Manager Component
- Case Dashboard & Queue Component
- Decision & Audit Inspector Component
- Rule & Model Management Console Component
- Audit Trail Viewer Component
- API Gateway Client / HTTP Interceptor Component
- Rule Simulation & Testing Sandbox Component
- Router & State Container Component

## Relationships
- Analyst Frontend -> Case Management Service: Communicates via HTTPS / REST (JSON) and WebSockets using short-lived JWTs
- Amazon CloudFront -> Analyst Frontend Users: Delivers static SPA assets via HTTPS (TLS 1.3) from Amazon S3

## Technology Stack
- React / Vue: Core framework ecosystem for component development
- TypeScript: Ensures type safety across internal application state and API contracts
- Amazon CloudFront & Amazon S3: Provides low-cost, highly available static web hosting with strict Content Security Policies (CSP)
- Zustand / Redux: Manages client-side global state and RBAC visibility

## Rationale
This architecture fits the requirements by maintaining a lightweight, serverless footprint that minimizes maintenance overhead for a three-engineer team while strictly enforcing client-side PCI-DSS data masking. Additionally, it integrates seamlessly with backend audit and rule management services to support zero-downtime updates and tamper-evident compliance tracking.