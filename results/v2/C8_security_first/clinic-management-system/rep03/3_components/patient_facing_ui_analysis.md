## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMR, scheduling, and billing for medium-sized clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and high-performance patient interactions.

## Key Elements
- Patient-Facing UI Container (React / Next.js)
- Next.js BFF Server (Node.js API Routes)
- Client-Side SPA Shell (React)
- Appointment, EMR & Billing Viewer, and Self-Service Onboarding Modules
- State Management & Session Guard Utility
- API Gateway (Kong / Nginx)
- Identity Provider (IdP)

## Relationships
- Client-Side SPA Shell -> Next.js BFF Server: Internal AJAX/Fetch [HTTPS, REST/JSON]
- Next.js BFF Server -> API Gateway: Proxies API requests [HTTPS, REST/JSON]
- Client-Side SPA Shell -> Identity Provider: Redirects for authentication [OpenID Connect]

## Technology Stack
- React / Next.js: Selected for mobile-first responsiveness, WCAG 2.1 AA accessibility, and BFF token abstraction.
- OpenTelemetry & RUM: Deployed for end-to-end tracing and Core Web Vitals performance monitoring.
- Kubernetes HPA: Utilized for dynamic scaling across on-prem-k8s and eu-central-1 to guarantee 99.99% availability.
- Encrypted HTTP-only Cookies: Implemented via BFF pattern to securely store tokens and eliminate XSS risks.

## Rationale
This architecture uses a Next.js Backend-for-Frontend (BFF) pattern and rigorous client-side security controls to safely handle Protected Health Information (PHI). Hybrid cloud deployment and robust observability ensure the system meets stringent HIPAA compliance, 99.99% uptime, and sub-second performance targets.