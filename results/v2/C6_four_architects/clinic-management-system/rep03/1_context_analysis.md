## Overview
• Manages patient admissions, EMR, scheduling, and billing for clinics via a hybrid cloud architecture.
• Ensures HIPAA/GDPR compliance, high availability (99.99%), and long-term data retention.

## Key Elements
• **Actors & Systems:** Patients, Doctors, Administrators, Identity Provider (OIDC/SAML), Third-Party Billing Gateway, External Lab/Imaging Systems (HL7 FHIR), Notification Gateway, Cloud Backup Archive.
• **Containers:** React SPA Frontend, Envoy/Nginx API Gateway, Core Services (Go/Spring Boot), Integration Service (Apache Kafka/Camel), Distributed SQL Database (CockroachDB/Aurora), Async Message Broker (Kafka/RabbitMQ).

## Relationships
• **Client to Gateway:** HTTPS / WSS over TLS 1.3.
• **Internal Containers:** gRPC over mTLS; Kafka Protocol over TLS 1.3 for async messaging.
• **External Systems:** HTTPS / REST for billing; HL7 FHIR over REST/JSON for labs; S5 / HTTPS with AES-256 for cloud backups.

## Technology Stack
• **Kubernetes:** `on-prem-k8s` and AWS `eu-central-1` for hybrid active-active deployment.
• **CockroachDB / AWS Aurora:** Distributed SQL ensuring cross-region high availability.
• **Apache Kafka / RabbitMQ:** Async messaging for decoupling and performance.
• **Go / Java Spring Boot:** High-performance core microservices.

## Rationale
• Hybrid active-active replication and distributed SQL guarantee 99.99% uptime and low-latency EMR access.
• Strict protocol security (mTLS, TLS 1.3, AES-256) and FHIR interoperability satisfy healthcare compliance constraints.