## Overview
The Frontend Container provides a decoupled, secure user interface for hospital staff and patients within the Clinic Management System. It delivers high-performance access to clinical workflows while strictly enforcing HIPAA and GDPR compliance mandates.

## Key Elements
- Frontend Container (Single Page Application / Next.js)
- Nginx Reverse Proxy
- Content Delivery Network (CDN)
- OpenTelemetry SDK
- API Client Abstraction Layer
- Component Library with WCAG 2.1 AA Compliance

## Relationships
- Hospital Staff and Patients -> Frontend Container: Accesses UI via HTTPS/TLS [HTTPS/TLS]
- Frontend Container -> API Gateway: Sends API requests via HTTPS with JWT/MFA validation [HTTPS, JWT/MFA]
- Frontend Container -> OpenTelemetry Container: Streams sanitized telemetry logs and RUM metrics [OpenTelemetry, gRPC/HTTPS]

## Technology Stack
- Next.js / Single Page Application: Decoupled architecture for rapid UI rendering and modular component design
- Nginx & Kubernetes: Reverse proxy and container orchestration ensuring high availability (99.99%) and health probes
- OpenTelemetry SDK: Client-side observability and real-user monitoring integration
- AbortController: Client-side request deduplication and race-condition handling

## Rationale
This architecture ensures sub-second EMR load times and high availability across hybrid cloud environments. Strict in-memory state management and zero local PHI storage satisfy rigorous healthcare compliance requirements.