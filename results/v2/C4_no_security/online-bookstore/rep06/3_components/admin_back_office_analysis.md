## Overview
This architecture summary defines the Admin Back-Office container for the Online Bookstore platform, providing secure administrative and customer support tools. It ensures GDPR/CCPA compliance, robust access control, and operational stability.

## Key Elements
* Admin UI (React, Amazon S3, Amazon CloudFront)
* Auth & RBAC Controller (Spring Security, OAuth2/OIDC)
* Operations & Support API (Spring Boot)
* Catalog Management Component (Spring Boot)
* Dispute & Refund Component (Spring Boot)
* Audit Logger (Spring AOP, Amazon CloudWatch, Amazon S3 Object Lock)
* Asynchronous Processing Queue (Amazon SQS)

## Relationships
* Admin UI communicates with Auth & RBAC, Operations & Support API, and Catalog Management via REST over HTTPS through Amazon API Gateway VPC links.
* Operations & Support API and Catalog Management communicate with backend containers and payment systems via gRPC.
* Catalog Management offloads bulk operations to Amazon SQS.
* Audit Logger records events to Amazon S3 Object Lock and Amazon CloudWatch.

## Technology Stack
* React & S3/CloudFront: Delivers the internal management single-page application.
* Spring Boot: Powers scalable microservice components for business logic.
* Spring Security & OAuth2/OIDC: Enforces granular role-based access control.
* Amazon SQS: Enables asynchronous processing for bulk catalog updates.
* AWS X-Ray: Provides distributed tracing across workflows.

## Rationale
Private VPC isolation, MFA access, and WORM audit logging satisfy strict GDPR/CCPA security constraints without exposing endpoints publicly. Asynchronous SQS processing and gRPC circuit breakers prevent operational tooling from degrading core checkout performance.