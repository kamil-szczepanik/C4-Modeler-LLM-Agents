## Overview
The Patient Portal App is a Next.js-based container within the Clinic Management System that empowers patients with secure self-service scheduling, medical record access, and online billing. It ensures high availability, strict HIPAA/GDPR compliance, and an accessible, high-performance user experience across hybrid cloud environments.

## Key Elements
- Patients: Primary end-users accessing healthcare information and services.
- Authentication Controller: NextAuth.js / OpenID Connect Client managing secure login and multi-factor authentication.
- Appointment & Scheduling UI Module: React components for self-service visit booking and resource clash visibility.
- EMR Viewer Module: React components rendering medical records and lab results with data masking.
- Billing & Payments Interface: React components handling secure online payments and claim statuses.
- Accessibility & Design System Module: Enforces WCAG 2.1 AA compliance across all views.
- Telemetry & Client Monitoring Agent: Collects OpenTelemetry traces and RUM performance metrics.
- External Systems: Enterprise Identity Provider (IdP), API Gateway / Reverse Proxy, global CDN (AWS CloudFront / Vercel Edge).

## Relationships
- Patients -> Patient Portal App: Manages healthcare information and scheduling [HTTPS]
- Authentication Controller -> Identity Provider: Validates credentials & issues JWT [OIDC/HTTPS]
- Appointment, EMR, & Billing Modules -> API Gateway / Reverse Proxy: Fetches domain data [HTTPS/REST]
- UI Modules -> Accessibility Module: Applies a11y standards [React Context]
- All Components -> Telemetry Agent: Reports performance metrics & anonymized error logs [Internal Async]

## Technology Stack
- Next.js: Enables Server-Side Rendering (SSR) and optimal SEO/accessibility for web users.
- NextAuth.js: Secures session management and OpenID Connect integration.
- React: Provides modular UI components for scheduling, EMR viewing, and billing.
- OpenTelemetry SDK: Captures distributed traces and RUM performance data.
- Global CDN (AWS CloudFront / Vercel Edge): Delivers static assets and executes edge caching/routing for high availability.

## Rationale
This architecture uses Next.js with global edge deployment and stale-while-revalidate caching to achieve the required 99.99% availability and sub-second performance. Strict component decoupling, local telemetry scrubbing, and an OIDC-based authentication layer ensure rigorous adherence to HIPAA and GDPR data protection mandates.