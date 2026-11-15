## Overview
The Admin / Back-Office App is a secure web application enabling store administrators, marketing specialists, and support staff to manage catalog inventory, merchandising campaigns, GDPR/CCPA compliance requests, and order exceptions. It ensures operational oversight and regulatory adherence while maintaining a strict security boundary from the public e-commerce store.

## Key Elements
- Store Administrator: Manages store operations and catalog
- Marketing/Merchandising Specialist: Manages marketing campaigns and promotions
- Support Staff: Resolves shipping integrations and payment discrepancies
- Admin / Back-Office App Container: Angular/TypeScript SPA hosted on AWS S3 & CloudFront
- Catalog Management Component: Handles inventory CRUD operations
- Merchandising & Campaign Component: Manages promotions and recommendation overrides
- User Data & Compliance Component: Executes secure GDPR/CCPA data export and deletion workflows
- Audit Logging Service: Captures administrative state changes
- Order & Exception Operations Component: Powers the Reconciliation Dashboard
- Analytics & Reporting Component: Renders promotion performance metrics
- Amazon API Gateway: Secure entry point using REST/GraphQL over HTTPS
- Amazon EventBridge: Receives immutable audit logs via AWS SDK

## Relationships
- Store Administrator -> Admin / Back-Office App: Manages store operations [HTTPS]
- Marketing/Merchandising Specialist -> Admin / Back-Office App: Manages campaigns [HTTPS]
- Support Staff -> Admin / Back-Office App: Resolves order exceptions [HTTPS]
- Admin / Back-Office App -> Amazon API Gateway: Makes administrative API requests [HTTPS (REST/GraphQL)]
- Audit Logging Service -> Amazon EventBridge: Publishes audit events [AWS SDK / API]

## Technology Stack
- Frontend SPA: Angular with TypeScript and Tailwind CSS for responsive UI design
- Hosting Infrastructure: AWS S3 & CloudFront for performant static asset delivery and global reach
- API Layer: Amazon API Gateway (REST/GraphQL over HTTPS) for secure request routing and RBAC enforcement
- Integration & Logging: AWS SDK and Amazon EventBridge for immutable audit log transmission and asynchronous eventing

## Rationale
This architecture isolates sensitive administrative workflows behind multi-factor authentication and strict Role-Based Access Control (RBAC), satisfying GDPR/CCPA compliance and OWASP security mitigations. Utilizing Angular on AWS S3/CloudFront paired with API Gateway ensures high availability (99.95% uptime) and low-latency back-office operations.