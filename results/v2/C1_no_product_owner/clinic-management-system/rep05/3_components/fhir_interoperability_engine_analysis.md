## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for clinical environments. It ensures high availability, strict HIPAA/GDPR compliance, and secure hybrid-cloud interoperability.

## Key Elements
- API Router & Validator Component (Apache Camel)
- Security & Policy Enforcement Component (Apache Camel Policy / Keycloak Adapter)
- Transformation Engine Component (Apache Camel / HAPI FHIR JPA)
- FHIR Repository Adapter Component (HAPI FHIR JPA)
- External Laboratory & Imaging Systems
- Keycloak Identity Provider
- SIEM & Audit Platform

## Relationships
- API Router & Validator -> Security & Policy Enforcement: Evaluates OAuth2/JWT claims and SMART scopes [In-memory Java filter]
- API Router & Validator -> Transformation Engine: Passes raw payloads for mapping [Internal Java Method / Camel Direct]
- Transformation Engine -> FHIR Repository Adapter: Persists and queries standardized resources [JPA / JDBC over TLS]
- FHIR Repository Adapter -> SIEM & Audit Platform: Streams structured PHI access logs [Syslog/HTTPS over mTLS]
- External Systems -> API Router & Validator: Exchanges clinical data [HL7 FHIR APIs over HTTPS with mTLS]

## Technology Stack
- Apache Camel: Core routing, integration, and circuit breaking for the interoperability engine
- HAPI FHIR JPA: FHIR resource parsing, validation, and data persistence
- Keycloak / OAuth2 / JWT: Identity management and SMART-on-FHIR scope enforcement
- Kubernetes (on-prem-k8s & eu-central-1): Hybrid deployment platform ensuring 99.99% active-active uptime
- PostgreSQL / Redis: Regional state management and data caching

## Rationale
This architecture uses decoupled microservices, robust validation, and asynchronous processing to meet high-availability and security mandates. Strict access controls and audit logging ensure full compliance with healthcare privacy regulations.