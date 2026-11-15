## Overview
The Clinic Management System provides patient registration, EMR, scheduling, and billing for healthcare clinics. It features a decoupled, hybrid data tier designed for HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention.

## Key Elements
- **Users**: Patient, Clinician, Receptionist, Billing Specialist, Hospital Administrator, Compliance Officer
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- **Containers**: Frontend SPAs (React, Nginx), Envoy API Gateway, Domain Microservices (Spring Boot, Kubernetes, Istio), Integration Service (Node.js), Decoupled Data Tier
- **Data Tier Components**: Primary Operational Database, Reporting & Analytics Read Replica, Audit & Archive Manager, WORM Storage Vault

## Relationships
- **Frontend SPAs -> Envoy API Gateway**: Routes HTTPS traffic via TLS 1.3
- **Envoy API Gateway -> Domain Microservices**: Forwards internal requests via gRPC / mTLS (Istio)
- **Domain Microservices -> Primary Operational Database**: Executes SQL queries over TLS 1.3 with AES-256 encrypted drivers
- **Domain Microservices -> Reporting & Analytics Read Replica**: Offloads read-only queries over TLS 1.3
- **Primary Operational Database -> Audit & Archive Manager**: Streams change logs via Debezium CDC (TCP/IP)
- **Audit & Archive Manager -> WORM Storage Vault**: Writes immutable object archives via HTTPS

## Technology Stack
- **AWS RDS PostgreSQL & On-premise PostgreSQL**: Primary transactional and read-replica storage for sub-second EMR performance
- **Apache Kafka & Debezium**: Asynchronous Change Data Capture (CDC) for audit streaming without operational locking
- **AWS S3 Object Lock / MinIO**: Immutable WORM storage satisfying ≥ 10-year retention
- **Istio & Kubernetes**: Hybrid service mesh managing mTLS and traffic routing between on-prem-k8s and eu-central-1

## Rationale
The hybrid architecture separates operational clinical workloads from heavy administrative reporting and archival tasks. This decoupling guarantees sub-second EMR load times while enforcing strict HIPAA/GDPR compliance and 99.99% availability.