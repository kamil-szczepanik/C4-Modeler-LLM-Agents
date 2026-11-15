## Overview
The Patient Portal Container is a secure, server-side rendered web interface that enables patients to manage appointments, access electronic medical records, and handle onboarding. It ensures strict HIPAA and GDPR compliance while maintaining high availability across a hybrid cloud infrastructure.

## Key Elements
- **Patient**: End-user interacting with the portal for healthcare services.
- **Portal UI Component**: React and Tailwind CSS interface ensuring WCAG 2.1 AA accessibility.
- **Patient BFF Component**: Next.js API Routes and Node.js server runtime managing sessions and data aggregation.
- **Session & Token Manager Component**: Handles OAuth2/OIDC token exchange and multi-factor authentication.
- **Client-Side State & Cache Component**: React Query and React Context managing localized UI state and non-sensitive cache.
- **API Gateway**: Kong or Envoy routing requests between services.
- **Enterprise IdP**: External identity provider for authentication.

## Relationships
- Patient -> Portal UI Component: Interacts with portal for health records and scheduling [HTTPS / TLS]
- Portal UI Component -> Patient BFF Component: Internal API calls [HTTPS]
- Patient BFF Component -> API Gateway: Proxies backend requests [HTTPS / REST / GraphQL, TLS]
- Patient BFF Component -> Enterprise IdP: Exchanges and validates tokens [OAuth2/OIDC via HTTPS]
- Portal UI Component -> Client-Side State & Cache Component: Manages local data flow [In-Memory]

## Technology Stack
- **Next.js / React**: Framework choice providing Server-Side Rendering (SSR) for optimized load performance and secure HttpOnly cookie management.
- **OAuth2/OIDC**: Authentication protocol ensuring secure multi-factor authentication and token exchange.
- **Kubernetes**: Container orchestration platform deployed across `on-prem-k8s` and `eu-central-1` to meet 99.99% availability.
- **Edge CDN**: Offloads static Next.js assets while delivering strict security headers (CSP, HSTS).

## Rationale
This architecture uses a server-side Backend-for-Frontend (BFF) pattern to keep sensitive tokens out of the browser, satisfying strict HIPAA and GDPR security constraints. The componentized layout balances high availability and rapid UI performance while preventing unauthorized local storage of Protected Health Information (PHI).