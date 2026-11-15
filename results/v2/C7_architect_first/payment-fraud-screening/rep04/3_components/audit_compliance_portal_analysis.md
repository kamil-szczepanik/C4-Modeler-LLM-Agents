## Overview
Provides an AWS-hosted, secure portal enabling compliance officers and auditors to review 7-year tamper-evident audit logs and generate compliance reports. It uses a decoupled React SPA frontend and NestJS backend-for-frontend (BFF) architecture.

## Key Elements
- Compliance Officer / Auditor (Person)
- Portal UI Component (React SPA served via AWS S3 / CloudFront)
- BFF Routing & RBAC Component (Node.js/NestJS, AWS ECS Fargate in private subnet)
- Audit Query API (Backend service for retrieving audit records)
- Amazon ElastiCache (Redis) (Encrypted audit query caching layer)
- Identity Provider (IdP) (External OIDC/JWT authentication provider)

## Relationships
- Compliance Officer / Auditor -> Portal UI Component: Accesses interface via HTTPS
- Portal UI Component -> BFF Routing & RBAC Component: API requests via HTTPS/JSON using HTTP-only cookies
- BFF Routing & RBAC Component -> Audit Query API: Fetches audit data via HTTPS/gRPC over mTLS with propagated JWTs
- BFF Routing & RBAC Component -> Amazon ElastiCache (Redis): Caches and retrieves encrypted audit read results
- BFF Routing & RBAC Component -> Identity Provider (IdP): Authenticates users via OIDC/JWT

## Technology Stack
- React: Powers the SPA frontend for lightweight client-side routing and timeline visualization
- Node.js & NestJS: Powers the BFF container for centralized RBAC and session management
- AWS ECS Fargate: Runs containerized services within private subnets to minimize operational overhead
- Amazon S3 & CloudFront: Delivers static frontend assets securely and efficiently
- Amazon ElastiCache (Redis): Caches historical queries to optimize performance for auditor workloads
- AWS KMS: Encrypts cached audit data at rest (AES-256) for PCI-DSS compliance

## Rationale
This architecture balances a 3-engineer team constraint and a €25,000 monthly budget by leveraging serverless static hosting and minimal ECS Fargate sizing. It strictly enforces PCI-DSS Level 1 and 7-year audit requirements through encrypted caching, mTLS, private subnets, and robust RBAC.