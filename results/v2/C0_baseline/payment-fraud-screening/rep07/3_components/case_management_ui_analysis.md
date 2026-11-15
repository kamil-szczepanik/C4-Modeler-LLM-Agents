## Overview
The Case Management UI is a secure, serverless Single-Page Application enabling fraud analysts to review suspicious transactions and risk managers to manage rules. It operates within AWS eu-west-1, strictly enforcing PCI-DSS compliance and auditability requirements.

## Key Elements
- **Fraud Analysts & Risk Managers**: Primary system users accessing the interface
- **Auth & Router Component**: React Router and `oidc-client-ts` managing PKCE authentication and RBAC
- **Case Queue & Investigation Component**: React and TanStack Query handling masked card data and review queues
- **Rule Management & Audit Component**: React, Formik, Zod, and Recharts for rule staging and metrics
- **Amazon S3 & CloudFront**: Static asset hosting and global content delivery
- **Case Management Backend**: Upstream API service communicating via HTTPS

## Relationships
- Fraud Analysts -> Case Management UI: Accesses investigation queues [HTTPS via TLS 1.3]
- Risk Managers -> Case Management UI: Manages rules and views metrics [HTTPS via TLS 1.3]
- Case Management UI -> Amazon CloudFront: Delivers static SPA assets [HTTPS]
- Case Management UI -> Case Management Backend: Submits API requests [HTTPS/REST, OAuth2/OIDC]

## Technology Stack
- **React & TypeScript**: Frontend framework for component-based UI development
- **Amazon S3 & CloudFront**: Serverless static hosting ensuring zero OS-level maintenance for a 3-engineer team
- **TanStack Query (React Query)**: State management for API polling and data synchronization
- **OIDC Client (`oidc-client-ts`)**: Secure PKCE token exchange handling

## Rationale
The serverless React/S3/CloudFront stack minimizes operational overhead to fit the 3-engineer constraint while maintaining the €25,000 monthly budget. Client-side security controls and TLS 1.3 enforce strict PCI-DSS compliance and data protection.