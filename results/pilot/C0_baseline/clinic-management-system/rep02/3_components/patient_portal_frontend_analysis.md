## Overview
The Patient Portal Frontend is a secure, responsive single-page application designed for patients to independently manage registrations, scheduling, and billing. It serves as the primary digital interface within the Clinic Management System to reduce administrative burdens.

## Key Elements
* Patients (End users)
* Patient Portal Frontend Container (React.js, Nginx, Node.js)
* Internal Components: Authentication Handler, Registration Module, Scheduling Widget, Session Management Module, API Client Service
* External Systems: Enterprise IDP, API Gateway, Billing Service, Apache Kafka

## Relationships
* Patients -> Patient Portal Frontend: Accesses portal UI [HTTPS, TLS 1.3]
* Patient Portal Frontend -> API Gateway: Routes client requests and authenticates [HTTPS]
* Patient Portal Frontend -> Billing Service: Communicates for billing operations [gRPC with mTLS]
* Authentication Handler -> Enterprise IDP: Manages user authentication and multi-factor auth [OAuth 2.0 / OIDC]

## Technology Stack
* React.js & Node.js: Powers the dynamic, accessible Single Page Application interface
* Nginx: Serves static assets and frontend container within Kubernetes
* gRPC with mTLS: Secures downstream backend service communication
* OpenTelemetry: Provides distributed tracing and Real User Monitoring (RUM)

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict token security, zero plaintext PHI caching, and robust TLS 1.3 encryption. Geo-distributed Kubernetes deployments and CDN edge-routing guarantee high availability (99.99%) and low-latency performance.