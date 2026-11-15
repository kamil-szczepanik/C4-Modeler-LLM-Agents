## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare clinics, ensuring HIPAA and GDPR compliance.]
[It provides an enterprise-grade, high-availability architecture utilizing a hybrid cloud model across on-premise Kubernetes and AWS eu-central-1.]

## Key Elements
- Users: Patients, Clinicians, Administrative Staff, Billing Officers, Regulatory Auditors
- External Systems: Enterprise Identity Provider, External Lab and Imaging Systems, Payment Gateway and Insurance Clearinghouse, Audit Archive
- Containers: API Gateway (Kong / Nginx), Frontend Container (Next.js / Node.js), Clinical Core Container (Node.js / Java Spring Boot), Scheduling & Resource Engine (Python / Go with Redis), Interoperability Service (Apache Camel / HAPI FHIR), Billing & Claims Worker (.NET Core with RabbitMQ), Analytics & Reporting Container (ClickHouse, PostgreSQL Replica)
- API Gateway Internal Components: Edge Router / Reverse Proxy, Authentication & Token Relay Plugin, Rate Limiting & Throttling Engine, Audit Logging & Tracing Interceptor, Metrics Exporter Component

## Relationships
- Patients, Clinicians, Administrative Staff, Billing Officers, Regulatory Auditors -> API Gateway: Access platform [HTTPS / REST, OAuth2/OIDC with MFA]
- Patient Portal BFF -> API Gateway: Routes requests [HTTPS / REST]
- API Gateway -> Clinical Core Container, Scheduling & Resource Engine, Interoperability Service: Routes requests [mTLS / gRPC / REST]
- API Gateway -> Redis: Checks rate limits [TCP / RESP]
- API Gateway -> Audit Archive: Exports security and compliance logs [HTTPS / Syslog]
- API Gateway (Metrics Exporter) -> Analytics & Reporting Container: Scrapes operational metrics [HTTP / Prometheus]

## Technology Stack
- Kong / Nginx: Centralized API Gateway routing, WAF, and reverse proxy for high availability and load management.
- Redis: Distributed token bucket backing for persona-based rate limiting and throttling.
- HashiCorp Vault: Dynamic runtime injection of secrets, TLS keys, and credentials.
- Prometheus: Asynchronous scraping of gateway operational metrics and error rates.
- SPIFFE/SPIRE: Service mesh short-lived certificate management for internal mTLS.

## Rationale
- The hybrid architecture with active-active scaling guarantees the required 99.99% uptime and <1s EMR response times.
- Strict OAuth2/OIDC, mTLS, WAF filtering, and centralized audit logging satisfy HIPAA, GDPR, and AES-256 data protection mandates.