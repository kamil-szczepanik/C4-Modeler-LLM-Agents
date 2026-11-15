## Overview
The Clinic Management System is a secure, high-availability hybrid platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. It ensures strict HIPAA/GDPR compliance, 99.99% uptime, and robust data protection across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Users**: Patients, Clinicians, Hospital Administrators
- **External Systems**: Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateways/Insurance Clearinghouses
- **Containers & Services**: API Gateway (Kong/Nginx/Envoy), Patient Portal Service, Patient & Scheduling Service, EMR Service, Billing Service, Integration Service, PostgreSQL Databases, Apache Kafka, HashiCorp Vault
- **Vault Components**: HTTP API / Core Router, Secrets Engines Manager, Auth Methods Manager, Audit Log Subsystem, Consul Storage Backend / Raft Consensus

## Relationships
- **Microservices** call **Vault HTTP API** via **gRPC/HTTPS** for dynamic database credentials and EMR data decryption.
- **Microservices** authenticate against **Auth Methods Manager** via **HTTPS/REST** using **Kubernetes Auth** and **AppRole**.
- **Secrets Engines Manager** manages **PostgreSQL Databases** via **TCP/5432** for dynamic credential rotation.
- **Audit Log Subsystem** streams compliance logs to **Tamper-Evident Storage** via local file I/O or syslog.
- **API Gateway** routes traffic to microservices using **HTTPS/mTLS**.

## Technology Stack
- **Languages & Frameworks**: Node.js/TypeScript (Patient Portal, Scheduling), Java/Spring Boot (EMR), Python/FastAPI (Billing), Go (HashiCorp Vault internals), Apache Camel (Integration)
- **Data & Messaging**: PostgreSQL (with read replicas and dynamic credentials), Apache Kafka (Event Broker)
- **Security & Infrastructure**: HashiCorp Vault (Secrets, Transit AES-256 encryption, Raft Consensus), AWS KMS / local HSM (Transit Auto-Unseal), Kong/Nginx/Envoy (API Gateway), Kubernetes
- **Protocols**: HL7 FHIR APIs, TLS 1.3, mTLS, HTTPS/REST, gRPC, TCP/8200, TCP/5432

## Rationale
This architecture uses a hybrid deployment model with decentralized Vault clusters and Raft consensus to meet strict HIPAA/GDPR constraints without compromising the 99.99% availability SLA. Isolated microservices combined with automated dynamic credential rotation and strict token TTL limits ensure optimal performance and security compliance.