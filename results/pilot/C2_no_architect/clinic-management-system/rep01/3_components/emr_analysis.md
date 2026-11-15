## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability, strict security, and regulatory compliance across hybrid environments.

## Key Elements
* Front Desk Administrator, Clinician, Billing Specialist, Patient
* External Lab & Imaging Systems
* Patient Registration Container (Kubernetes, REST API)
* Appointment Scheduling Container (Kubernetes, REST API)
* EMR Container (Kubernetes, Encrypted Distributed Storage with NVMe & Tiered Object Storage)
* Billing & Claims Container (Kubernetes, Encrypted Distributed Storage)
* HL7 FHIR Interoperability Container (Kubernetes, HL7 FHIR APIs)
* Patient Portal Container (Kubernetes, REST API)

## Relationships
* Clinician -> EMR: Views and updates medical records via HTTPS (TLS 1.3), OAuth2/OIDC MFA
* Patient Registration -> EMR: Creates and updates patient records via gRPC / REST via mTLS (SPIFFE/SPIRE)
* Appointment Scheduling -> EMR: Links appointments to patient records via gRPC / REST via mTLS
* Billing & Claims -> EMR: Accesses clinical encounter data via gRPC / REST via mTLS
* HL7 FHIR Interoperability -> EMR: Ingests lab and imaging results via gRPC / REST via mTLS
* EMR -> External Lab & Imaging Systems: Exchanges data using HL7 FHIR APIs

## Technology Stack
* Kubernetes: Orchestrates containerized services across hybrid on-premise and AWS `eu-central-1` infrastructure to meet 99.99% uptime.
* Encrypted Distributed Storage: Provides active-active multi-master replication with AES-256 storage-at-rest and field-level encryption.
* Envoy Service Mesh / mTLS: Secures inter-container traffic with SPIFFE/SPIRE certificate management.
* HL7 FHIR: Standardizes interoperability with external lab and imaging systems.

## Rationale
This hybrid architecture combines on-premise clusters with cloud scalability to meet strict HIPAA and GDPR data sovereignty mandates. Active-active replication and tiered storage guarantee 99.99% availability and 10-year retention compliance.