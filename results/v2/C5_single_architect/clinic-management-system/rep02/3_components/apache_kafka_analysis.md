## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- Users: Patient, Clinician / Receptionist
- External Systems: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Notification Service
- Containers: API Gateway (Kong / NGINX), Patient & Scheduling Service, EMR Service, Billing & Claims Service, Integration Service (FHIR Adapter), Audit Service, Apache Kafka
- Kafka Components: Kafka Broker, KRaft Controller, Kafka Connect, Kafka Schema Registry, Kafka Security Interceptor Module

## Relationships
- Patient & Scheduling Service, EMR Service, Billing & Claims Service, Integration Service -> Kafka Broker: Publishes asynchronous clinical and billing events [mTLS over TCP / Kafka Protocol]
- Billing & Claims Service -> Kafka Schema Registry: Validates message schemas [HTTPS]
- Kafka Broker -> Kafka Schema Registry: Fetches schemas [HTTP/REST]
- Kafka Connect -> Elasticsearch / WORM storage: Syncs audit logs and clinical data securely [TLS]

## Technology Stack
- Apache Kafka & KRaft Mode: Fault-tolerant event-driven messaging with reduced operational complexity and eliminated ZooKeeper overhead.
- Kafka Schema Registry: Enforces Avro/Protobuf schema validation to prevent microservice breaking changes.
- Kafka Security Interceptor Module: Enforces fine-grained ACLs and mTLS for HIPAA-compliant PHI data transit.
- Spring Boot & Node.js: Core container runtimes for business logic services.
- PostgreSQL with AES-256: Secure, encrypted relational data persistence.

## Rationale
The hybrid architecture utilizes resilient event-driven messaging via Kafka with KRaft and schema enforcement to guarantee 99.99% uptime. Robust security components and HL7 FHIR integration ensure strict compliance with HIPAA and GDPR data standards.