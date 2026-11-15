## Overview
The Clinic Management System (CMS) manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It operates as a hybrid cloud system ensuring HIPAA and GDPR compliance, 99.99% availability, and 10-year data retention.

## Key Elements
- **Actors:** Patient, Clinician / Staff, Hospital Administrator
- **External Systems:** Identity Provider (IdP), Insurance Gateway, External Lab & Imaging Systems, Notification Gateway, Cloud Backup (AWS S3 Glacier)
- **Containers:** Envoy API Gateway, EMR Service (Java/Spring Boot), Patient & Scheduling Service (Go), Billing & Claims Service (.NET Core), Apache Kafka, PostgreSQL Operational Databases

## Relationships
- **Patient & Staff to CMS:** HTTPS (TLS 1.3) with OIDC/SAML 2.0 MFA
- **CMS to External Lab & Imaging:** HL7 FHIR over HTTPS (RESTful)
- **CMS to Insurance Gateway:** REST/SOAP over TLS 1.3
- **Internal Microservices:** gRPC over mTLS and Apache Kafka event streaming
- **CMS to Cloud Backup:** Encrypted TLS links to AWS S3 Glacier

## Technology Stack
- **Kubernetes (`on-prem-k8s` & `eu-central-1`):** Hybrid cloud orchestration to support data residency and high availability.
- **PostgreSQL:** Multi-master operational databases enforcing the database-per-service pattern.
- **Apache Kafka:** Asynchronous event streaming for decoupled domain integration.
- **Envoy & Istio:** Edge routing, TLS 1.3 termination, and automated service mesh mTLS.
- **AWS S3 Glacier:** Secure cloud cold storage for the 10-year data retention requirement.

## Rationale
The hybrid architecture places the EMR service and operational database on-premise to guarantee sub-second P95 performance and strict HIPAA/GDPR data residency. Utilizing a database-per-service pattern with active-active replication and cloud archiving achieves 99.99% availability and long-term compliance cost-effectively.