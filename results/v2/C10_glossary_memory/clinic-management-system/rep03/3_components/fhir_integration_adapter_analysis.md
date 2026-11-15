## Overview
The Clinic Management System is a hybrid clinical IT platform designed to manage patient records, scheduling, billing, and interoperability for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and seamless integration with external medical systems.

## Key Elements
- **Clinician / Doctor**: Primary internal user accessing diagnostic results and EMR workflows.
- **FHIR Integration Adapter**: Dedicated integration container decoupling external clinical systems.
- **FHIR API Endpoint Controller**: Java/Spring Boot component handling secure REST endpoints, mTLS, and OAuth2.
- **Resource Mapper & Validator**: Java/HAPI FHIR component translating payloads and enforcing PHI filtering.
- **Outbound Sync Worker**: Go/Temporal.io component managing resilient asynchronous retries.
- **External Lab & Imaging Systems**: External medical systems exchanging clinical data.
- **Clinical Core Service**: Central backend service handling core EMR and domain logic.
- **Clinical Core Database**: Encrypted SQL database storing core patient records.

## Relationships
- **FHIR API Endpoint Controller -> Resource Mapper & Validator**: In-memory method calls
- **Resource Mapper & Validator -> Clinical Core Service**: gRPC over mTLS
- **Outbound Sync Worker -> External Lab & Imaging Systems**: HL7 FHIR APIs over encrypted HTTPS
- **FHIR Integration Adapter -> External Lab & Imaging Systems**: HL7 FHIR APIs over encrypted HTTPS
- **FHIR API Endpoint Controller -> Identity Provider (IdP)**: OAuth2 token introspection over HTTPS

## Technology Stack
- **Java / Spring Boot + Spring Security**: Powers the FHIR API Endpoint Controller for robust enterprise web capabilities.
- **Java / HAPI FHIR**: Used in the Resource Mapper & Validator for standard-compliant healthcare data processing.
- **Go / Temporal.io**: Powers the Outbound Sync Worker for durable, fault-tolerant workflow orchestration and retries.
- **Hybrid Kubernetes (on-prem-k8s & eu-central-1)**: Ensures local survivability, active-active redundancy, and low-latency local network routing.
- **mTLS & TLS 1.3**: Secures all internal and external communication channels to meet HIPAA and GDPR encryption mandates.

## Rationale
This architecture uses a hybrid deployment model with localized Kubernetes clusters to guarantee continuous local survivability during network outages, fulfilling the 99.99% uptime requirement. Enforcing strict perimeter security, mTLS, and centralized domain validation through the Clinical Core Service protects patient privacy while maintaining high-throughput clinical interoperability.