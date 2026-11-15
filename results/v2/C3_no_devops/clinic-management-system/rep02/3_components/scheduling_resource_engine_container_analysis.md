## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for clinical facilities. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Patient, Clinical Staff, Administrative Staff, Compliance Officer / Auditor
- **External Systems**: Payment Gateway, Insurance Clearinghouse, External Lab / Imaging Systems, Pharmacy Management System
- **Containers**: API Gateway, Patient Self-Service Container, EMR Backend Container, Scheduling & Resource Engine Container, Integration Broker Container, Audit & Compliance Daemon Container, EMR Database (PostgreSQL), Redis Cluster, Cold Storage, Apache Kafka
- **Scheduling & Resource Engine Components**: Appointment API Controller, Resource Conflict Validator, Distributed Lock Manager, Schedule Event Publisher, Resource Calendar Service

## Relationships
- **API Gateway -> Scheduling & Resource Engine Container**: Routes booking requests [Internal mTLS over gRPC/REST]
- **Distributed Lock Manager <-> Redis Cluster**: Atomic locking & state caching [Encrypted TLS / Redisson over TCP]
- **Resource Conflict Validator -> Resource Calendar Service**: Query availability [Internal JPA/SQL over JDBC with TLS 1.3]
- **Schedule Event Publisher -> Apache Kafka**: Emit sanitized schedule events [TCP / SASL over TLS]

## Technology Stack
- **Backend**: Java Spring Boot (Scheduling & Resource Engine Container) for robust enterprise logic
- **Caching/Locking**: Redis Cluster with Redisson client for distributed, real-time race-condition prevention
- **Database**: PostgreSQL with Row-Level Security (RLS) for secure, multi-tenant persistent storage
- **Messaging**: Apache Kafka for asynchronous, decoupled event publishing
- **Security**: AES-256 at rest, AES-GCM field-level encryption, TLS 1.3, and mTLS for network isolation

## Rationale
This architecture uses active-active hybrid components and in-memory distributed locking to satisfy the 99.99% uptime and low-latency scheduling constraints. Strict tenant isolation, encryption, and tokenization natively enforce HIPAA and GDPR mandates.