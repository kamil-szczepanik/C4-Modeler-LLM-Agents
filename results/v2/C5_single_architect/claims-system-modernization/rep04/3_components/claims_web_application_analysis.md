## Overview
The Claims Web Application provides a modern React frontend for online claim submissions and adjuster workflows. It ensures high performance and reliable state management despite legacy mainframe latency constraints.

## Key Elements
- **Claim Submission Module**: React wizard-style forms for online submissions (R-01).
- **Adjuster Dashboard & Case Workspace**: React UI for claims handling (R-02).
- **Optimistic UI / Cache State Manager**: Redux Toolkit / React Query for local data caching (R-05).
- **Auth Client**: MSAL.js managing OIDC/OAuth2 tokens for Azure Active Directory SSO (R-07).
- **Offline Draft Storage**: React / IndexedDB via Dexie.js for persistent local draft saves (R-04).

## Relationships
- Customers & Brokers -> Claims Web Application: interact via [HTTPS]
- Claims Adjusters -> Claims Web Application: interact via [HTTPS]
- Claims Web Application -> API Gateway / BFF: interacts via [HTTPS/REST]
- Claims Web Application -> Active Directory: authenticate via [OIDC/OAuth2]

## Technology Stack
- **React**: Frontend UI library, chosen for team familiarity and component reusability.
- **Azure Static Web Apps**: Hosting provider, minimizing infrastructure overhead for a team with low cloud experience.
- **Redux Toolkit / React Query**: State and cache management to mitigate slow backend responses.
- **MSAL.js**: Authentication library integrating securely with enterprise Active Directory.
- **IndexedDB / Dexie.js**: Client-side browser storage for local draft persistence and offline resilience.

## Rationale
This component architecture insulates users from mainframe latency and network drops through local caching and offline storage. It aligns with the team's cloud skill level by utilizing managed static hosting and client-side state management.