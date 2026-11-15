## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing while ensuring high availability and strict regulatory compliance. It provides secure, interoperable clinical workflows for patients, staff, and external health systems.

## Key Elements
- **Users:** Patients, Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance/Security Officers, Hospital/Clinic Management
- **External Systems:** External Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouse
- **Containers:** Patient Portal (React / TypeScript, Nginx), Internal Staff Application (React / TypeScript, Nginx), API Gateway (Kong / Envoy), Patient Admission Service (Go / Node.js), Scheduling Service (Go / Node.js), EMR Service (Go / Node.js), Billing Service (Java Spring Boot), Integration Engine (Go / Node.js), Data Store (PostgreSQL, WORM Object Storage)

## Relationships
- **Patients -> Patient Portal:** Interacts via HTTPS (Web/Mobile)
- **Staff -> Internal Staff Application:** Interacts via HTTPS (Web)
- **Portals -> API Gateway:** Connects via HTTPS (mTLS/OIDC)
- **API Gateway -> Core Services:** Invokes services via gRPC / REST over internal mesh
- **Integration Engine -> External Lab & Imaging Systems:** Exchanges diagnostic data via HL7 FHIR over HTTPS (REST/JSON) with mTLS
- **Integration Engine -> Insurance Clearinghouse:** Submits claims via EDI over SFTP / HTTPS
- **Services -> Data Store:** Persists data via PostgreSQL protocol with AES-256

## Technology Stack
- **Frontend:** React, TypeScript, Nginx for Patient Portal and Internal Staff Application
- **API Gateway:** Kong / Envoy for mTLS, rate limiting, and token validation
- **Backend Services:** Go and Node.js for admission, scheduling, EMR, and integration services; Java Spring Boot for billing
- **Data & Storage:** PostgreSQL with AES-256 encryption and WORM Object Storage for 10-year audit retention
- **Integration & Security:** RabbitMQ / NATS for message routing, HashiCorp Vault for secrets management, OIDC / SAML 2.0 with MFA for authentication

## Rationale
This hybrid-cloud architecture combines high-performance microservices with strict security controls to satisfy HIPAA, GDPR, and 99.99% availability requirements. Standardized protocols like HL7 FHIR, EDI, and gRPC ensure seamless interoperability and sub-second EMR performance across distributed environments.