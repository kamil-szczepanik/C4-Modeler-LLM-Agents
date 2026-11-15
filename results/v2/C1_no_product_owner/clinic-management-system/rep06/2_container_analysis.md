## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, appointments, and billing. It ensures high availability (99.99%), strict regulatory compliance (HIPAA/GDPR), and long-term data retention.

## Key Elements
- **Users**: Doctor, Receptionist, Patient, Billing Administrator, System Administrator
- **External Systems**: External Lab / Imaging Systems, Payment Gateway, Insurance Payer APIs, Enterprise Identity Provider (IdP)
- **Containers**: API Gateway (Kong/NGINX), Identity & Access Management Service (Keycloak), Patient & Scheduling Service (Go/Java Spring Boot), EMR Core Service (Java Spring Boot), Billing & Claims Service (Node.js/Python), FHIR Interoperability Broker (Apache Camel / Azure Health Data Services)
- **Infrastructure & Data**: Kubernetes (`on-prem-k8s` and `eu-central-1`), PostgreSQL per service, Apache Kafka, HashiCorp Vault, Istio Service Mesh

## Relationships
- **Client to API Gateway**: HTTPS / JSON / OAuth2/OIDC with MFA.
- **API Gateway to Internal Services**: gRPC with Istio mTLS and propagated JWTs.
- **Services to Database**: SQL over TLS (PostgreSQL instances per service with AES-256 and envelope encryption).
- **Services to Event Broker**: Apache Kafka via mTLS with topic-level ACLs.
- **FHIR Broker to External Systems**: HL7 FHIR APIs over HTTPS.
- **Billing Service to External Services**: HTTPS/JSON to Payment Gateway and Insurance Payer APIs.

## Technology Stack
- **API Gateway**: Kong/NGINX for TLS termination, rate limiting, and routing.
- **Identity Provider**: Keycloak for OAuth2/OIDC, MFA, and integration with Enterprise IdP.
- **Backend Services**: Go and Java Spring Boot for core business logic and EMR; Node.js/Python for billing.
- **Interoperability**: Apache Camel or Azure Health Data Services engine for HL7 FHIR translation.
- **Messaging & Sync**: Apache Kafka with MirrorMaker 2 and Kafka cluster-linking.
- **Infrastructure & Security**: Kubernetes, Istio (mTLS & service mesh), HashiCorp Vault (secrets and dynamic credentials).
- **Databases**: PostgreSQL with AES-256 encryption at rest, envelope encryption, and database-per-service isolation.

## Rationale
The hybrid active-active architecture across on-premises and AWS (`eu-central-1`) guarantees 99.99% availability and strict GDPR data residency. Strict database isolation, Istio mTLS zero-trust security, envelope encryption, and immutable audit logs fulfill rigorous HIPAA, GDPR, and 10-year data retention mandates.