## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. The Admin Portal is a React SPA container that provides administrators with a secure UI to manage catalogue items, pricing, fulfillments, and operational analytics.

## Key Elements
- Store Administrator [person, container]
- Admin Portal [container, container] (React SPA)
- Authentication Module [component]
- Catalogue Management Dashboard [component]
- Operations & Fulfillment View [component]
- Reporting & Analytics View [component]
- Audit & Logging Client [component]
- Amazon API Gateway [container, container]
- Admin Service [container, container]
- Identity Provider [externalSystem, container]

## Relationships
- Store Administrator -> Authentication Module [OIDC/OAuth2]
- Authentication Module -> Identity Provider [HTTPS/OIDC]
- Catalogue Management Dashboard -> Amazon API Gateway [HTTPS/REST with JWT validation]
- Operations & Fulfillment View -> Amazon API Gateway [HTTPS/REST with JWT validation]
- Reporting & Analytics View -> Amazon API Gateway [HTTPS/REST with JWT validation]
- Audit & Logging Client -> Amazon API Gateway [HTTPS/REST]
- Amazon API Gateway -> Admin Service [HTTPS/REST with JWT validation]

## Technology Stack
- React & TypeScript [Admin Portal framework and component implementation]
- Material-UI [UI component library for administrative dashboards]
- AWS CloudFront & S3 [Global content delivery and static hosting]
- Amazon API Gateway [Secure ingress routing and JWT validation]
- AWS WAF [Edge security protecting administrative endpoints]

## Rationale
This component architecture enforces strict role-based access control, multi-factor authentication, and immutable audit logging to meet GDPR and CCPA compliance. Distributing the React SPA via AWS CloudFront ensures high availability and low latency across multi-region deployments.