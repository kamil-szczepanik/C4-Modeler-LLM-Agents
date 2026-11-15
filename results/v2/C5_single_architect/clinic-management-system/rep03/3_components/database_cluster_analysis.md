## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient records, scheduling, EMRs, and billing. It provides high availability, stringent security compliance, and robust interoperability for clinical IT environments.

## Key Elements
- **Users**: Patient, Clinician/Staff, Hospital Administrator
- **External Systems**: Identity Provider, Payment Gateway, External Labs & Imaging Systems, Regulatory Archiving / Audit Storage
- **Containers**: API Gateway (Kong / Nginx), Patient & Scheduling Service (NestJS), EMR Service (Spring Boot), Billing Service (FastAPI), FHIR Integration Broker (Apache Camel), Audit & Compliance Worker (Go), Database Cluster (PostgreSQL), Message Broker (Kafka)
- **Database Components**: Primary Write Node, Read Replica Nodes, Encryption & Key Manager Agent, Distributed Consensus Manager (Patroni / etcd)

## Relationships
- **Patient/EMR/Billing Services -> Primary Write Node**: Executes ACID transactions and writes [PostgreSQL protocol over TLS 1.3]
- **EMR & Billing Services -> Read Replicas**: Offloads non-blocking read queries [PostgreSQL protocol over TLS 1.3]
- **Primary Write Node <-> Distributed Consensus Manager**: Heartbeating and state coordination [TCP/gRPC]
- **Encryption & Key Manager Agent -> Primary/Replica Nodes**: Injects envelope keys for TDE at rest [PKCS#11 / Vault API over TLS 1.3]
- **FHIR Integration Broker -> External Labs & Imaging**: Exchanges healthcare data [HL7 FHIR REST APIs over HTTPS]

## Technology Stack
- **Compute**: Hybrid infrastructure spanning `on-prem-k8s` and AWS `eu-central-1` for regional redundancy.
- **Database**: PostgreSQL 16 with Citus extension for distributed sharding and active-active replication.
- **Failover & Security**: Patroni/etcd for distributed consensus, and AES-256 envelope encryption via Vault for HIPAA/GDPR compliance.
- **Integration**: Apache Camel for FHIR protocol translation.

## Rationale
This hybrid architecture uses multi-region database clustering with automated consensus to guarantee 99.99% availability and active-active fault tolerance. Enterprise-grade encryption, immutable audit trails, and HL7 FHIR standards simultaneously satisfy strict HIPAA/GDPR constraints and clinical interoperability requirements.