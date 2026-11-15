## Overview
The Online Bookstore frontend provides a globally accessible, high-performance e-commerce single-page application for browsing and purchasing books. It ensures low-latency delivery, multi-currency support, and strict compliance with global privacy regulations.

## Key Elements
- Shoppers & Administrators: End-users and staff interacting via HTTPS.
- Frontend Container: React-based Single Page Application.
- SPA Router & Shell: Manages client-side routing and layout frames with React Router and Error Boundary.
- Localization & Currency Context: Manages runtime language and currency states for USD, EUR, and GBP using i18next.
- Compliance & Consent Manager: Handles GDPR/CCPA cookie banners locally.
- API Client Layer: Manages centralized request interception and caching via Axios/GraphQL.
- Design System & Accessible Component Library: Powers UI primitives using Tailwind CSS and Radix UI.
- AWS CloudFront & Amazon S3: Global CDN and static asset storage across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Relationships
- Users -> Frontend Container: Access the e-commerce interface via [HTTPS].
- Frontend Container -> Amazon CloudFront: Serves static assets and content globally via [HTTPS].
- Frontend Container -> API Gateway: Calls backend services and operations via [HTTPS / REST / GraphQL].
- Frontend Container -> AWS CloudWatch / Sentry: Pushes client-side telemetry and error logs via [HTTPS].

## Technology Stack
- React / React Router: Chosen for fast client-side rendering and component modularity.
- Amazon S3 & CloudFront: Selected for low-latency static asset delivery to achieve <2s load times on 3G.
- Tailwind CSS & Radix UI: Implemented for WCAG 2.1 AA accessibility compliance and responsive design.
- i18next & React Context API: Utilized for dynamic localization and multi-currency support (USD, EUR, GBP).
- AWS CodePipeline / GitHub Actions: Automated CI/CD for atomic deployments and cache invalidation.

## Rationale
This architecture leverages static asset caching via S3 and CloudFront to meet strict performance and global scalability requirements. Decomposing the React application into dedicated components guarantees regulatory compliance, accessibility, and resilient error recovery across multiple regions.