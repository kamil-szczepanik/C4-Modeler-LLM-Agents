## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across a hybrid cloud architecture.]

## Key Elements
- Users: Receptionists, Clinicians, Billing Specialists, Compliance Officers, Patients
- External Systems: Lab & Imaging Systems, Insurance Clearinghouses, Enterprise Identity Provider, Patient Portal
- Containers: SPA Frontend (React, TypeScript, Nginx), EMR Core Service (Spring Boot, Java), Billing & Claims Service (Spring Boot, Java), Audit & Compliance Service (Spring Boot, Java), Integration Gateway (Apache Camel, Spring Cloud Gateway), PostgreSQL with Patroni, Redis Cluster, Apache Kafka
- Integration Gateway Components: Routing & Load Balancer Router, Protocol Translation Engine, Edge Security & Audit Interceptor, Resilience & Circuit Breaker Manager, Telemetry Publisher

## Relationships
- Integration Gateway -> Lab & Imaging Systems: Exchanges lab orders and imaging data [HL7 FHIR APIs over HTTPS]
- Integration Gateway -> Insurance Clearinghouses: Exchanges insurance claims [HL7 FHIR APIs over HTTPS]
- Integration Gateway -> Apache Kafka: Publishes integration events [Async / Kafka Protocol]
- Integration Gateway -> Redis Cluster: Caches OAuth2 tokens and rate-limiting counters [Redis Protocol over TCP]

## Technology Stack
- Spring Cloud Gateway & Spring Cloud: Manages dynamic routing and rate limiting with high performance.
- Apache Camel: Handles complex protocol translation between internal models and external FHIR standards.
- Resilience4j: Provides circuit breakers and bulkheading for outbound routes.
- OpenTelemetry: Enables distributed tracing across the hybrid boundary.
- Redis: Caches OAuth2 tokens and rate-limiting counters.
- PostgreSQL with Patroni: Ensures high availability and durable storage for EMR and billing data.

## Rationale
[This hybrid architecture utilizes Spring Cloud Gateway and Apache Camel to guarantee seamless interoperability via HL7 FHIR while meeting strict HIPAA/GDPR compliance. The integration of Resilience4j, Redis, and OpenTelemetry ensures 99.99% availability and robust fault tolerance across on-premises Kubernetes and cloud environments.]