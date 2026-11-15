## Overview
The Patron Web App is a self-service portal within the Library Management System that enables library members to catalogue items, manage circulation, and execute searches. It is engineered with a Backend-for-Frontend (BFF) architecture to ensure secure session management and rapid response times.

## Key Elements
- Patron Web App container (React / TypeScript, Node.js BFF, NGINX)
- Search & Discovery UI component (React)
- Account & Circulation Manager component (React)
- Localization & Accessibility Engine component (React)
- BFF Security & Session Manager component (Node.js)
- API Gateway (NGINX / Envoy)
- EU Identity Provider
- EU Payment Gateway

## Relationships
- Patron Web App -> API Gateway: Communicates via gRPC over a private network
- Patron Web App -> EU Identity Provider: Authenticates users via OIDC/OAuth 2.0 authorization code flow with PKCE
- Account & Circulation Manager -> EU Payment Gateway: Processes fines and payments securely via the API Gateway

## Technology Stack
- React / TypeScript: Powers the responsive, client-side user interface
- Node.js BFF (Express): Manages server-side session state and HttpOnly cookies to mitigate XSS risks
- NGINX: Serves static assets and enforces strict security headers (CSP, HSTS)
- gRPC: Facilitates high-performance communication between the BFF and the API Gateway
- Kubernetes: Manages container deployment, autoscaling, and secure volume mounts

## Rationale
This architecture ensures strict EU-only data residency and guards against Personally Identifiable Information (PII) leakage by utilizing server-side HttpOnly cookies via a Node.js BFF. Additionally, it guarantees 99th-percentile search responses under 800 ms and meets public library accessibility and localization mandates.