## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across hybrid environments.

## Key Elements
- Users: Clinic Receptionist, Physician, Billing Specialist, Administrator, Patient
- Containers: API Gateway (Kong / Node.js), Patient Portal BFF (Node.js / GraphQL), Billing Operations UI (React / Nginx), Patient & Scheduling Service (Go), EMR Core Service (Spring Boot), Billing & Integration Service (FastAPI)
- Data/Broker: PostgreSQL (AES-256), RabbitMQ
- External Systems: Enterprise IdP, External Lab & Imaging Systems, Payment Gateway, SIEM System
- Gateway Components: Authentication & Authorization Filter, Rate Limiting & Throttling Engine (Redis), Routing & Load Balancing Proxy, Audit & Telemetry Interceptor, Edge WAF & Sanitization Filter, Tenant & Usage Metering Component

## Relationships
- Users -> API Gateway: Accesses system features [HTTPS/REST with JWT]
- API Gateway -> Patient Portal BFF & Billing Operations UI: Routes frontend traffic [HTTPS]
- API Gateway -> Patient & Scheduling, EMR Core, and Billing Services: Proxies backend requests [gRPC over mTLS]
- Audit Interceptor -> SIEM System: Asynchronously emits access logs [HTTPS]

## Technology Stack
- Kong / Node.js: API Gateway implementation chosen for high-performance active-active hybrid deployment and rich plugin ecosystem.
- Redis: Powers persona-based rate limiting and throttling quotas.
- gRPC over mTLS: Secures microservice-to-microservice communication and meets performance goals.
- PostgreSQL with AES-256: Secures relational data at rest for strict compliance.
- RabbitMQ: Asynchronous messaging broker for decoupling backend workflows.

## Rationale
This hybrid active-active architecture guarantees 99.99% uptime and <1s P95 EMR load times by utilizing an optimized Kong API Gateway with asynchronous auditing and metering. Strict edge security controls, mTLS, and AES-256 encryption ensure complete HIPAA and GDPR compliance.