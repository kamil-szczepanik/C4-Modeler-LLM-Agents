## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% high availability, and secure interoperability with external healthcare systems.

## Key Elements
* **Users:** Patients, Clinicians/Staff, Hospital Administrators
* **External Systems:** Identity Provider, Payment Gateway, External Labs & Imaging Systems, Regulatory Archiving / Audit Storage
* **API Gateway:** Kong / Nginx container for entry point and token validation
* **Patient & Scheduling Service:** NestJS container managing registrations and appointments
* **EMR Service:** Spring Boot container handling Electronic Medical Records and audit trails
* **Billing Service:** Python FastAPI container handling claims and payments
* **FHIR Integration Broker:** Apache Camel / Node.js container for HL7 FHIR interoperability
* **Audit & Compliance Worker:** Go container for asynchronous audit logging
* **Database Cluster:** PostgreSQL multi-region active-active cluster

## Relationships
* **Users to API Gateway:** HTTPS / gRPC for secure client access and multi-factor authentication
* **API Gateway to Microservices:** mTLS within Kubernetes for inter-container communication
* **Billing Service to Payment Gateway:** AMQP / REST for asynchronous and secure insurance claims
* **FHIR Integration Broker to External Labs:** HL7 FHIR over HTTPS for lab and imaging system integration
* **Audit Worker to Regulatory Archiving:** AMQP / Kafka streaming for 10-year data retention

## Technology Stack
* **Kong / Nginx:** API Gateway for TLS termination and OAuth2/MFA validation
* **NestJS / Node.js:** Patient & Scheduling Service for robust TypeScript-based business logic
* **Spring Boot / Java:** EMR Service for high-performance sub-second P95 screen loads
* **FastAPI / Python:** Billing Service for rapid payment and claim processing
* **PostgreSQL:** Primary database with AES-256 encryption at rest for HIPAA/GDPR compliance
* **RabbitMQ / Kafka:** Message brokers for reliable asynchronous event processing
* **Kubernetes:** Hybrid deployment platform spanning on-prem-k8s and eu-central-1

## Rationale
This containerized microservices architecture meets the 99.99% uptime requirement through an active-active PostgreSQL database cluster deployed across hybrid Kubernetes regions. Security and compliance mandates (HIPAA/GDPR) are enforced via mTLS, AES-256 encryption at rest, and dedicated audit worker containers.