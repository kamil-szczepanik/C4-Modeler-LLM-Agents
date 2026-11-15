## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and long-term data retention.

## Key Elements
- **Users**: Clinic Receptionist, Physician, Billing Specialist, Administrator, Patient
- **External Systems**: Enterprise IdP, External Lab & Imaging Systems, Payment Gateway, Audit Archival / SIEM System
- **Containers**: API Gateway (Kong/Node.js), Patient Portal BFF (Node.js/GraphQL), Patient & Scheduling Service (Go), EMR Core Service (Spring Boot), Billing & Integration Service (FastAPI), Billing Operations UI Container (React/Nginx)
- **Data Stores & Brokers**: PostgreSQL (AES-256), RabbitMQ

## Relationships
- Patient Portal BFF -> Patient & Scheduling Service: gRPC over mTLS
- API Gateway / UI Containers -> Core Services: gRPC over mTLS & HTTPS/REST with JWT
- Billing & Integration Service -> External Lab & Imaging Systems: HL7 FHIR APIs
- EMR Core Service -> Audit Archival: Asynchronous append-only logging

## Technology Stack
- **API Gateway & Routing**: Kong / Node.js for rate limiting and MFA termination
- **Frontend & BFF**: Node.js, GraphQL, React, and Nginx for secure, consumer-grade user interfaces
- **Core Microservices**: Go (Patient & Scheduling), Java Spring Boot (EMR), and Python FastAPI (Billing)
- **Messaging & Persistence**: RabbitMQ for offline-resilient queuing; PostgreSQL with AES-256 for PHI storage

## Rationale
This architecture uses a hybrid deployment model with decoupled services, asynchronous audit trails, and resilient message queuing to guarantee 99.99% uptime and <1s EMR loads. Strict trust boundaries, mTLS, and httpOnly cookies enforce comprehensive HIPAA and GDPR compliance without sacrificing performance.