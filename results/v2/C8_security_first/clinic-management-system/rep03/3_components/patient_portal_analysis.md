## Overview
The Patient Portal is a secure, patient-facing subsystem of the Clinic Management System that enables self-service appointment scheduling, lab result viewing, and notifications. It is architected for HIPAA/GDPR compliance, high availability (99.99%), and frictionless user adoption.

## Key Elements
- Patients: End-users accessing self-service health management features.
- Patient Auth Delegator: Component handling OIDC/OAuth 2.1 authentication, adaptive MFA, and httpOnly JWT session management.
- Appointment & Scheduling Facade: Component managing patient appointment rescheduling and real-time slot validation.
- Record Retrieval Component: Component fetching EMR subsets with server-side tenant isolation and IDOR checks.
- Notification Dispatcher: Component pushing real-time appointment reminders and alerts.
- External Identity Provider (IdP): Manages primary user authentication credentials.
- Clinical Core Services: Downstream backend infrastructure handling core clinic operations.

## Relationships
- Patients interact with Patient-Facing UI via TLS 1.3.
- Patient Auth Delegator communicates with External IdP using OpenID Connect (OIDC) / OAuth 2.1.
- Appointment & Scheduling Facade connects to Clinical Core Services via gRPC over mTLS.
- Record Retrieval Component queries EMR data via REST/JSON.
- Notification Dispatcher pushes alerts to clients via WebSockets (TLS 1.3).

## Technology Stack
- Node.js / TypeScript: Chosen for all portal components to provide a lightweight, high-throughput asynchronous footprint.
- Redis: Used for distributed session state and encrypted AES-256 caching to support hybrid-cloud failover.
- Socket.io: Powers real-time persistent WebSocket communication for notifications.
- Kubernetes: Deployed across `on-prem-k8s` and `eu-central-1` for active-active auto-scaling and high availability.
- OpenTelemetry: Implemented for distributed tracing and observability.

## Rationale
This architecture decouples authentication and core logic to balance strict HIPAA/GDPR security controls (like mTLS, AES-256, and adaptive MFA) with a frictionless user experience. Distributed hybrid-cloud deployment on Kubernetes ensures the required 99.99% availability and low-latency performance.