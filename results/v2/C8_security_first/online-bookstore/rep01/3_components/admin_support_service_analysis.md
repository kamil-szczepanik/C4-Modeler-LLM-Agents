## Overview
The Admin & Support Service is a backend GraphQL container providing secure administrative and customer support capabilities for the Online Bookstore. It enables catalog moderation, regional pricing management, and dispute resolution while ensuring strict compliance with GDPR and CCPA.

## Key Elements
- GraphQL Gateway & Schema Engine (Node.js, Apollo Server)
- Authorization & Context Middleware
- Admin Core Domain Module
- Support Core Domain Module
- Audit & Compliance Logger
- Amazon Aurora PostgreSQL
- AWS ECS on Fargate
- Envoy Service Mesh

## Relationships
- Envoy Service Mesh -> GraphQL Gateway & Schema Engine: Routes inbound requests [gRPC over mTLS]
- Admin & Support Core Modules -> Amazon Aurora PostgreSQL: Executes transactional queries [PostgreSQL over TLS with IAM Auth]
- Admin Core Domain Module -> Catalog Service: Synchronous RPC [gRPC over mTLS]
- Support Core Domain Module -> Order & Checkout Service: Synchronous RPC [gRPC over mTLS]
- Audit & Compliance Logger -> Amazon CloudWatch: Ships immutable audit logs [HTTPS with AWS KMS]

## Technology Stack
- Node.js & Apollo Server: Provides flexible GraphQL querying to minimize round-trips for support agents.
- AWS ECS on Fargate: Runs containerized workloads with auto-scaling to maintain the 99.95% uptime SLA.
- Amazon Aurora PostgreSQL: Stores transactional admin and support data securely using IAM Database Authentication.
- AWS KMS: Encrypts immutable audit logs to satisfy GDPR and CCPA compliance mandates.

## Rationale
This architecture leverages GraphQL to deliver high support efficiency while enforcing strict RBAC/ABAC and query complexity limits to protect against DoS attacks. Asynchronous audit logging and IAM database auth ensure enterprise-grade security and compliance without degrading performance.