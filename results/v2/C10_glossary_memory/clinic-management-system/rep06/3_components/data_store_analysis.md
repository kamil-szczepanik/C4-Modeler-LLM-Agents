## Overview
• Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
• Operates as a hybrid-cloud platform ensuring HIPAA/GDPR compliance, high availability, and secure clinical workflows.

## Key Elements
• Clinic Management System
• Patients, Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance/Security Officers, Hospital/Clinic Management
• External Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouse
• Patient Portal, Internal Staff Application, API Gateway
• Patient Admission Service, Scheduling Service, EMR Service, Billing Service, Integration Engine
• Data Store (Primary Relational Database, Audit & Archive Object Store, Read Replica Cluster)

## Relationships
• Patients, Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance/Security Officers, Hospital/Clinic Management -> Clinic Management System (HTTPS Web/Mobile)
• Clinic Management System -> External Identity Provider (IdP) (HTTPS)
• Clinic Management System -> External Lab & Imaging Systems (HL7 FHIR over HTTPS REST/JSON with mTLS)
• Clinic Management System -> Insurance Clearinghouse (EDI over SFTP / HTTPS)
• Patient Portal, Internal Staff Application -> API Gateway (HTTPS mTLS/OIDC)
• API Gateway -> Patient Admission Service, Scheduling Service, EMR Service, Billing Service (gRPC / REST over internal mesh)
• Patient Admission Service, Scheduling Service, EMR Service, Billing Service -> Primary Relational Database (PostgreSQL protocol with mTLS and AES-256)
• Primary Relational Database -> Audit & Archive Object Store (S3 API / TLS 1.3)

## Technology Stack
• React / TypeScript with Nginx: Powers Patient Portal and Internal Staff Application for responsive client access.
• Kong / Envoy: Acts as API Gateway providing mTLS, rate limiting, and token validation.
• Go / Node.js: Implements high-throughput backend microservices (Admission, Scheduling, EMR, Integration).
• Java Spring Boot: Handles enterprise billing workflows and insurance claims.
• PostgreSQL 16 & Read-Replicas: Provides core transactional data storage and offloads analytical queries with active-passive replication.
• S3-compatible Object Storage with Object Lock: Enforces immutable 10-year WORM retention and automated tiering.

## Rationale
• Combines relational databases and WORM object storage to satisfy strict HIPAA/GDPR 10-year retention and security mandates.
• Utilizes read-replicas, connection pooling, and microservices decomposition to maintain sub-second EMR performance and 99.99% availability.