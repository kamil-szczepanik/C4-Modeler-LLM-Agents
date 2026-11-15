## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability, strict HIPAA/GDPR compliance, and interoperability across hybrid cloud infrastructure.

## Key Elements
- **SPA Frontend**: React, TypeScript, and Nginx application serving internal clinical and administrative staff.
- **Backend Services**: EMR Core Service, Billing & Claims Service, and Audit & Compliance Service built with Spring Boot and Java.
- **Integration Gateway**: Apache Camel and Spring Cloud Gateway managing external and internal routing.
- **Data Stores**: PostgreSQL with Patroni for relational data, Redis Cluster for caching, and Apache Kafka for event streaming.
- **External Systems**: External Lab & Imaging Systems, Insurance Clearinghouses, Enterprise Identity Provider, and Patient Portal.

## Relationships
- **SPA Frontend -> Integration Gateway**: Requests clinical and administrative data via HTTPS / WSS.
- **Integration Gateway -> EMR Core Service**: Routes electronic medical record operations via gRPC / REST.
- **Integration Gateway -> Billing & Claims Service**: Forwards insurance and financial transaction data via REST.
- **Integration Gateway -> External Lab & Imaging Systems**: Exchanges diagnostic data via HL7 FHIR APIs.

## Technology Stack
- **React & TypeScript**: Powers the modular frontend with type safety and role-based UI rendering.
- **Spring Boot & Java**: Implements robust, enterprise-grade business logic for core clinical and billing services.
- **PostgreSQL & Patroni**: Ensures high availability and strict ACID compliance for sensitive patient data.
- **Apache Kafka**: Enables asynchronous, event-driven communication across microservices.
- **Nginx & CDN**: Delivers high-performance static asset distribution with edge caching and strict security headers.

## Rationale
This hybrid architecture isolates critical workloads across on-premise Kubernetes and AWS eu-central-1 to guarantee 99.99% availability and meet strict 10-year data retention mandates. Modular microservices and explicit FHIR integration gateways ensure scalability, high performance (<1s EMR load), and full regulatory compliance.