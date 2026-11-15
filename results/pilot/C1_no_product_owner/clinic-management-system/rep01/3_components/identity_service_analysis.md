## Overview
The Clinic Management System is a secure, highly available healthcare platform that manages patient registration, EMRs, scheduling, and billing for clinics. It ensures HIPAA/GDPR compliance and 99.99% uptime across a hybrid cloud infrastructure.

## Key Elements
- **Users**: Patients & Clinic Staff
- **Systems**: External Labs & Imaging Systems, Third-Party Insurance Gateways
- **Containers**: API Gateway (NGINX/Kong), Identity Service (Keycloak), Patient & EMR Service, Appointment Service, Billing Service, HL7 FHIR Integration Engine (Apache Camel), Event Broker (Apache Kafka), Primary Database & Tiered Storage (PostgreSQL & S3-compatible WORM storage), Audit Logging Service
- **Identity Service Internal Components**: Authentication Engine, Authorization & Token Management Module, User Federation Provider

## Relationships
- **Patient & EMR Service -> Identity Service**: Authenticates and authorizes requests via OAuth2/OIDC and mTLS (Istio)
- **Appointment Service -> Identity Service**: Authenticates and authorizes requests via OAuth2/OIDC and mTLS (Istio)
- **Billing Service -> Identity Service**: Authenticates and authorizes requests via OAuth2/OIDC and mTLS (Istio)
- **Identity Service -> Enterprise LDAP Directories**: Interoperates for staff credentials over LDAPS

## Technology Stack
- **Keycloak**: Manages authentication, authorization, OAuth2/OIDC, and identity federation
- **Spring Boot**: Powers microservice containers for business logic
- **PostgreSQL**: Stores relational data with AES-256 encryption at rest
- **Redis & Infinispan**: Provides distributed caching and session management for sub-millisecond token validation
- **Apache Kafka**: Handles asynchronous event streaming
- **Apache Camel**: Implements HL7 FHIR integration engine for clinical interoperability
- **Istio & Envoy**: Enforces mutual TLS (mTLS) and service mesh security
- **Kubernetes (on-prem & AWS eu-central-1)**: Orchestrates active-active hybrid deployment

## Rationale
This architecture uses an active-active hybrid deployment with Keycloak, Redis, and PostgreSQL to meet the 99.99% availability requirement. Strict adherence to OAuth2/OIDC, mTLS, Argon2id hashing, and AES-256 encryption ensures HIPAA and GDPR compliance.