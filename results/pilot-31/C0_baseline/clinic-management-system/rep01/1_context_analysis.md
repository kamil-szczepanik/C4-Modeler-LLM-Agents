## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient records, billing, and clinical scheduling. It ensures 99.99% availability and strict HIPAA/GDPR compliance through a secure, distributed architecture.

## Key Elements
*   **EMR Core:** On-premise system for patient records and imaging archives.
*   **Patient Portal & Billing Services:** Cloud-hosted (AWS eu-central-1) for elastic scaling.
*   **FHIR Integration Broker:** Gateway for standardized lab and imaging data exchange.
*   **Audit & Compliance Engine:** Asynchronous system for immutable log ingestion and reporting.
*   **Unified Management Plane:** Centralized dashboard for hybrid infrastructure monitoring.
*   **Identity Provider (IdP):** Centralized service for MFA, RBAC, and ABAC.

## Relationships
*   **Service Mesh:** Manages cross-environment traffic between on-premise K8s and AWS via mTLS.
*   **FHIR Integration Broker:** Uses HL7 FHIR APIs for external interoperability.
*   **Clearinghouse Gateway:** Connects to billing services via HTTPS/TLS 1.3.
*   **Event Bus:** Asynchronously streams logs from core services to the Audit Engine.
*   **Management Plane:** Uses dedicated VPC/VPN tunnels for administrative control.

## Technology Stack
*   **Hybrid Infrastructure:** On-premise K8s and AWS (eu-central-1) managed via IaC.
*   **Security:** AES-256 encryption at rest, FIPS 140-2 Level 3 HSM for key management.
*   **Compliance:** WORM storage for audit logs; OPA/Gatekeeper for policy-as-code.
*   **Observability:** Distributed tracing with correlation IDs and centralized logging.

## Rationale
The hybrid architecture balances low-latency on-premise access for clinical imaging with cloud-based scalability for public-facing services. Zero-trust principles and decoupled compliance engines ensure regulatory adherence while maintaining high operational availability.