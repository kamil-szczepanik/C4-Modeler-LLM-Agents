## Overview
The Clinic Management System is a hybrid healthcare platform designed to manage patient admissions, EMRs, scheduling, and billing for clinics. It ensures strict HIPAA/GDPR compliance, sub-second EMR performance, and 99.99% high availability.

## Key Elements
- Users: Patients, Receptionists, Physicians, Billing Specialists
- Systems: Clinic Management System (CMS), Payment Gateways, Lab and Imaging Systems, Enterprise IDP
- Containers: API Gateway, EMR Service, Scheduling Service, Billing Service, Apache Camel Integration Layer
- Infrastructure: On-premises Kubernetes clusters, AWS (eu-central-1), Apache Kafka, Hardware Security Modules (HSMs)

## Relationships
- Users to API Gateway: HTTPS/TLS for secure web and mobile access
- CMS to Payment Gateways: REST/JSON APIs for payment processing
- CMS to Lab/Imaging Systems: HL7 FHIR standard over secure HTTPS
- Hybrid Nodes to Nodes: mTLS and application-layer payload encryption over WAN

## Technology Stack
- Kubernetes & AWS: Hybrid deployment for active-active high availability and regional data pinning
- Apache Camel: Enterprise Service Bus pattern for asynchronous HL7 FHIR translation
- Apache Kafka: Event-driven architecture for reliable billing transactions
- OAuth 2.0 / OIDC / SAML: Identity management and fine-grained token validation
- AES-256 & HSM: Data encryption at rest and envelope encryption for EMR data

## Rationale
This hybrid architecture combines on-premises resilience with AWS cloud scale to meet strict 99.99% availability and regional data residency mandates. Event-driven streaming and asynchronous integration patterns ensure sub-second EMR performance and zero financial data loss during network partitions.