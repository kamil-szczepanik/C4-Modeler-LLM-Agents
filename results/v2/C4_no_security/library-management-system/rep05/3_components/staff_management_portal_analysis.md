## Overview
The Staff Management Portal provides role-based circulation, cataloging, and administrative interfaces for library staff within the Library Management System. It ensures EU data residency compliance and performance monitoring while supporting public and academic library operations.

## Key Elements
- Librarians, Circulation Staff, and Library Administrators (Users)
- Staff Management Portal (Angular, Nginx Container)
- Authentication & Authorization Guard (Angular Router Guard)
- Core Feature Modules (Angular Modules: Cataloging, Circulation, Admin)
- API Client Service (Angular HttpClient)
- Telemetry & Audit Interceptor (Angular HttpInterceptor)
- Core API Gateway (Spring Cloud Gateway)
- Centralized Observability Platform

## Relationships
- Librarians, Circulation Staff, Library Administrators -> Staff Management Portal: Manages operations [HTTPS]
- Authentication & Authorization Guard -> Core Feature Modules: Enforces role-based access [TypeScript Dependency]
- Core Feature Modules -> API Client Service: Communicates via service injection [TypeScript Service Injection, HTTPS]
- API Client Service -> Telemetry & Audit Interceptor: Forwards requests [TypeScript Dependency]
- Telemetry & Audit Interceptor -> Core API Gateway: Sends API requests with OTel and audit headers [HTTPS REST/GraphQL]
- Staff Management Portal -> Centralized Observability Platform: Ships browser telemetry, traces, and logs [gRPC]

## Technology Stack
- Angular & TypeScript: Powers dynamic role-based UI customization and component architecture
- Nginx: Serves static assets with blue/green deployment and `/healthz` liveness probes
- OpenTelemetry: Captures browser traces and performance metrics for <800ms NFR tracking
- JWT & HTTP Interceptors: Enforces EU data residency audit traceability and immutable user context

## Rationale
This component architecture implements strict role-based access and OpenTelemetry tracing directly into the frontend. It guarantees EU regulatory compliance, audit traceability, and sub-800ms performance visibility for staff operations.