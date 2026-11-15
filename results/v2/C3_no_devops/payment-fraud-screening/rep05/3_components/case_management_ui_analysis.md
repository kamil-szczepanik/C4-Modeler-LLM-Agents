## Overview
React-based single-page application hosted on AWS S3 and distributed via CloudFront for fraud case review. Enables analysts to process suspended payments securely while strictly enforcing PCI-DSS Level 1 compliance.

## Key Elements
- Case Management UI Container (React on AWS S3 + CloudFront)
- Routing & Auth Controller Component (React Router)
- Case Workspace Component (React / TanStack Table)
- Audit & Explainability View Component (D3.js / Tailwind CSS)
- Queue Analytics & Filtering Engine Component (React Context / Zustand)
- External Identity Provider & Case Management Backend

## Relationships
- Fraud Analysts -> Case Management UI: Accesses secure case management interface [HTTPS]
- Routing & Auth Controller -> Identity Provider: Validates OIDC/JWT session tokens [HTTPS]
- Case Workspace Component & Audit & Explainability View -> Case Management Backend: Sends API requests for operations and data [HTTPS/REST JSON]
- Case Workspace Component -> Queue Analytics & Filtering Engine: Queries client-side risk queues [In-memory]

## Technology Stack
- React: Provides a modern, component-based UI framework.
- AWS S3 + CloudFront: Delivers zero-infrastructure-overhead static hosting supporting the 3-engineer team constraint and 25,000 EUR monthly budget.
- React Router: Handles client-side routing and OIDC/JWT session validation.
- React / TanStack Table: Renders high-performance risk queues and case workspaces.
- D3.js / Tailwind CSS: Visualizes model explainability data and feature attributions.
- React Context / Zustand: Manages client-side queue sorting, SLA timers, and risk prioritization state.

## Rationale
This architecture leverages serverless static hosting to eliminate infrastructure maintenance overhead for a three-engineer team while keeping costs within the 25,000 EUR monthly budget. Furthermore, strict client-side isolation ensures full card numbers never reach the browser, satisfying PCI-DSS Level 1 compliance requirements.