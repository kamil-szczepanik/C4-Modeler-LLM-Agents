## Overview
The Fraud Analyst Frontend is a React Single Page Application hosted on Amazon S3 and delivered via Amazon CloudFront, enabling fraud analysts to review suspicious transactions and update rules. It securely interfaces with backend services while enforcing strict PCI-DSS compliance and data redaction.

## Key Elements
- Fraud Analysts: End users accessing the system interface.
- Authentication & Authorization Module: AWS Cognito integration enforcing OAuth2/OIDC role-based access control.
- Case Management Dashboard: React/TypeScript component rendering transaction queues and risk metadata.
- Audit Logging & Redaction Guard: Client-side proxy interceptor preventing raw card primary account numbers (PANs) from rendering in the DOM.
- Rule & Model Management Console: Administrative interface for zero-downtime rule and scoring model updates.
- WebSocket Client Module: Native browser client maintaining real-time queue synchronization.

## Relationships
- Fraud Analysts -> Fraud Analyst Frontend: Accesses review interface via HTTPS
- Authentication & Authorization Module -> AWS Cognito: OAuth2/OIDC authentication via HTTPS
- Case Management Dashboard -> Case Management Backend: Fetches review queues and submits decisions via REST/JSON over HTTPS
- Rule & Model Management Console -> Case Management Backend: Triggers rule adjustments and model deployments via REST/JSON over HTTPS
- WebSocket Client Module -> Case Management Backend: Receives real-time queue synchronization updates via WSS over HTTPS

## Technology Stack
- React & TypeScript: Core frontend framework and type-safe language for robust UI development
- Tailwind CSS: Utility-first styling for rapid dashboard layout implementation
- TanStack Query (React Query): State management and API data caching to optimize network traffic
- AWS SDK for Browser: Integration toolkit for AWS service communication
- Native WebSocket API: Persistent connection layer for real-time updates

## Rationale
This component architecture fits the requirements by strictly isolating sensitive cardholder data on the client side to satisfy PCI-DSS Level 1 compliance (R-05). Furthermore, centralizing all backend interactions through the Case Management Backend minimizes infrastructure complexity for a three-engineer team within a fixed budget.