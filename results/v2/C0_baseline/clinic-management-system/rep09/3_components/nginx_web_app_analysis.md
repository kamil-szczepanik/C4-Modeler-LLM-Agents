## Overview
The Nginx Web App container provides the secure frontend gateway for staff users of the Clinic Management System. It delivers high-performance static asset delivery and reverse proxy capabilities to ensure HIPAA and GDPR compliance.

## Key Elements
- Nginx Reverse Proxy & Static File Server (Nginx Alpine)
- Single Page Application (SPA) Runtime (React / TypeScript)
- Client-Side Router / State Manager Component
- Kubernetes Ingress Controller
- Kubernetes Deployment (Min 3 replicas with HPA)

## Relationships
- Clinician / Receptionist / Billing Specialist / Compliance Officer -> Nginx Web App: Accesses clinical and administrative workflows via HTTPS (TLS)
- Nginx Reverse Proxy -> SPA Runtime: Serves static HTML/JS/CSS assets via local disk read
- SPA Runtime -> API Gateway: Forwards authenticated API calls via HTTPS / REST / JSON over TLS
- Kubernetes Ingress Controller -> Nginx Web App: Routes external traffic using mTLS

## Technology Stack
- Nginx Alpine: Chosen for a minimal attack surface, low resource footprint, and robust static caching
- React / TypeScript: Provides a dynamic, type-safe Single Page Application runtime for staff workflows
- Kubernetes & HPA: Guarantees 99.99% availability (R-06) across hybrid targets (`on-prem-k8s`, `eu-central-1`)
- OpenTelemetry / Prometheus: Used for real-time metrics scraping and observability

## Rationale
This architecture uses a hardened Nginx reverse proxy combined with a secure SPA runtime to deliver sub-second EMR screen loads. Strict security headers, BFF pattern token handling, and non-root container constraints ensure full HIPAA and GDPR compliance.