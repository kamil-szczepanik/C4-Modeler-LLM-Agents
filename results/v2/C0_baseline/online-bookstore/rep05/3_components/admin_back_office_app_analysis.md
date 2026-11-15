## Overview
The Online Bookstore Admin Back-Office App is a secure React-based single-page application enabling store administrators to manage retail operations efficiently. It provides capabilities for catalog management, multi-currency pricing, order fulfillment, and compliance auditing.

## Key Elements
- Store Administrator (User)
- Admin Back-Office App (React Container)
- Catalog Management Module (React / Redux Toolkit Component)
- Order Fulfillment Dashboard (React / TanStack Table Component)
- Authentication & RBAC Guard (React Context / JWT Component)
- Bulk Operations Orchestrator (React Hook Form / Web Workers Component)
- Audit & Telemetry Interceptor (Axios Interceptors Component)
- Amazon API Gateway (External Container)

## Relationships
- Store Administrator -> Admin Back-Office App: Manages store operations via [HTTPS/JSON]
- Admin Back-Office App -> Amazon API Gateway: Sends administrative API requests via [HTTPS/gRPC-web with mTLS]
- Amazon API Gateway -> Admin Back-Office App: Routes admin responses via [HTTPS/gRPC-web with mTLS via AWS Service Connect]

## Technology Stack
- React / Redux Toolkit / TanStack Table: Chosen for responsive UI components and efficient state management.
- Web Workers: Utilized for offloading heavy CSV/JSON batch parsing to prevent UI thread starvation.
- Axios Interceptors: Deployed for automated correlation ID injection and failure telemetry capture.
- AWS S3 / CloudFront / AWS WAF: Implemented for isolated static hosting, geo-filtering, and IP whitelisting.
- HTTP/2 & gRPC-web: Selected for multiplexed, secure transport of high-throughput bulk mutations.

## Rationale
This architecture isolates administrative traffic from customer-facing services to protect core availability and performance. Strict RBAC, `HttpOnly` token security, and audit logging satisfy GDPR/CCPA compliance while maintaining operational throughput across global AWS regions.