## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across hybrid cloud environments.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists
- **External Systems**: Identity Provider, Third-Party Payment Gateway, Insurance Clearinghouse, External Lab & Imaging Systems
- **Containers**: API Gateway (Envoy/NGINX), Web Application Container (React/Next.js), Clinical & EMR Core Container (Spring Boot/Java), Billing & Claims Container (Node.js/Express), HL7 FHIR Integration Container (Apache Camel), Edge Sync Container (Go Daemon), Primary DB & Audit Store (PostgreSQL with Patroni)
- **Web Application Components**: Routing & Layout Component, Authentication & Session Component, Feature Modules, API Client Component, State Management & Caching Component

## Relationships
- **Users -> Web Application Container**: Interacts via [HTTPS]
- **Web Application Container -> API Gateway**: Sends user requests via [HTTPS]
- **Authentication & Session Component -> Identity Provider**: Token exchange via [OAuth2/OIDC]
- **Feature Modules -> State Management & Caching Component**: Reads/writes state [In-Memory]

## Technology Stack
- **React / Next.js**: Powers the Web Application Container for SSR/SSG and responsive clinician dashboards (R-07).
- **TypeScript**: Ensures type safety across frontend feature modules and API clients.
- **React Query / Zustand**: Manages local client state and caching to minimize network round-trips.
- **Kubernetes**: Deploys immutable container images to `on-prem-k8s` and `eu-central-1` with rolling updates (R-06).
- **CDN (CloudFront/Cloudflare)**: Accelerates static asset delivery for <1s P95 EMR load times (R-07).
- **OpenTelemetry**: Provides real-user monitoring (RUM) and performance tracking.

## Rationale
This hybrid architecture combines scalable cloud infrastructure with localized caching to guarantee sub-second EMR responsiveness and 99.99% uptime. Immutable deployments, robust RBAC, and encrypted transmission fulfill strict HIPAA and GDPR security mandates.