## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to handle patient admissions, EMRs, scheduling, and billing. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators
- **Frontend Container**: React Single Page Application (SPA) deployed via CDN
- **Backend Containers**: API Gateway (NGINX/Kong), Go EMR Service, Node.js Scheduling Service, Reporting Container, Apache Camel ESB, Apache Kafka Event Bus
- **Data Stores**: PostgreSQL Cluster with Read Replicas, Redis Cluster with Redis Sentinel
- **External Systems**: Third-Party Payment Gateways, External Insurance Verification Services, External Lab and Imaging Systems

## Relationships
- **Users -> React SPA**: Access portal via HTTPS (TLS 1.3)
- **React SPA -> API Gateway**: Sends perimeter requests via HTTPS
- **API Gateway -> Go EMR Service / Node.js Scheduling Service**: Routes microservice traffic via gRPC and REST
- **Apache Camel ESB -> Lab & Imaging Systems**: Integrates via HL7 FHIR APIs
- **Services -> PostgreSQL & Redis**: Database persistence and caching via AES-256 and TLS

## Technology Stack
- **React & React Query**: Frontend SPA and state management for sub-second EMR loads
- **NGINX / Kong**: API Gateway for routing, OAuth2, and MFA enforcement
- **Go & Node.js**: High-performance backend microservices for EMR and scheduling
- **Apache Kafka & Apache Camel**: Real-time event streaming and HL7 FHIR integration
- **PostgreSQL & Redis**: Secure data persistence with AES-256 encryption at rest and in-memory caching

## Rationale
This architecture uses a hybrid-cloud, microservices approach to easily scale high-demand clinical workflows while maintaining active-active 99.99% availability. Strict multi-layer security protocols, in-memory token management, and HL7 FHIR interoperability ensure full HIPAA/GDPR compliance and sub-second performance.