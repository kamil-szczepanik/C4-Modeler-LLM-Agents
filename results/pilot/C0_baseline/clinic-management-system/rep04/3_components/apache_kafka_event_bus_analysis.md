## Overview
This system is an enterprise Clinic Management System that handles patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to provide a highly available, HIPAA and GDPR-compliant clinical platform with real-time event processing and robust data retention.

## Key Elements
*   **Users:** Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators
*   **External Systems:** Third-Party Payment Gateways, External Insurance Verification Services, External Lab and Imaging Systems
*   **Frontend Container:** React Single Page Application (React, CDN)
*   **Gateway Container:** API Gateway (NGINX / Kong, OAuth2, MFA)
*   **Core Services:** Go EMR Service (Go, gRPC), Node.js Scheduling Service (Node.js, REST), Reporting Container, Apache Camel ESB (Apache Camel, HL7 FHIR)
*   **Messaging Container:** Apache Kafka Event Bus (Apache Kafka, KRaft, Schema Registry, Strimzi Operator)
*   **Data & Caching Containers:** PostgreSQL Cluster (PostgreSQL, Read Replicas, AES-256), Redis Cluster (Redis, Redis Sentinel, TLS)

## Relationships
*   React SPA interacts with API Gateway via HTTPS / REST / WSS.
*   API Gateway routes traffic to Go EMR Service and Node.js Scheduling Service using gRPC and REST.
*   Go EMR Service and Node.js Scheduling Service produce and consume events from Apache Kafka Event Bus using the TCP-based Kafka binary protocol with TLS 1.3.
*   Apache Camel ESB connects to External Lab and Imaging Systems using HL7 FHIR APIs.
*   Core services persist and retrieve operational data from PostgreSQL Cluster and Redis Cluster using TLS.

## Technology Stack
*   **Frontend:** React Single Page Application deployed via CDN for responsive user interfaces.
*   **API Layer:** NGINX / Kong for routing, rate limiting, and OAuth2/MFA security enforcement.
*   **Backend Services:** Go (for high-performance EMR operations via gRPC) and Node.js (for scheduling services via REST).
*   **Messaging & Integration:** Apache Kafka (using KRaft mode, Strimzi Operator, and Schema Registry with Apache Avro) paired with Apache Camel for HL7 FHIR interoperability.
*   **Databases & Caching:** PostgreSQL Cluster with read replicas and AES-256 encryption, backed by a Redis Cluster with Redis Sentinel for session management and caching.

## Rationale
This architecture uses a hybrid cloud deployment across on-premise Kubernetes and AWS (`eu-central-1`) to meet the strict 99.99% availability and active-active constraints. Decoupling clinical and billing workflows via Apache Kafka ensures high-throughput resilience, strict HIPAA/GDPR compliance, and adherence to sub-second P95 performance targets.