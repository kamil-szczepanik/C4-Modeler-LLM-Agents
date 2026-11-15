## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for clinical environments. It provides high availability, stringent compliance, and reliable asynchronous event processing.

## Key Elements
*   **Users:** Patient, Clinician/Staff, Hospital Administrator
*   **External Systems:** Identity Provider, Payment Gateway, External Labs & Imaging Systems, Regulatory Archiving / Audit Storage
*   **Containers:** API Gateway (Kong / Nginx), Patient & Scheduling Service (NestJS), EMR Service (Spring Boot), Billing Service (FastAPI), FHIR Integration Broker (Apache Camel), Audit & Compliance Worker (Go), Database Cluster (PostgreSQL), Message Broker (Apache Kafka)
*   **Components (Message Broker):** Event Ingestion Router, Commit Log Partition Manager, Consumer Group Coordinator, Schema Registry

## Relationships
*   **EMR Service** -> **Schema Registry**: Validates message schemas [HTTP/REST]
*   **EMR Service** -> **Event Ingestion Router**: Publishes audit and domain events [TCP / Kafka Producer API]
*   **Event Ingestion Router** -> **Commit Log Partition Manager**: Persists validated streams to disk [Internal Binary Protocol]
*   **Audit & Compliance Worker** -> **Commit Log Partition Manager**: Consumes event streams [TCP / Kafka Consumer API]

## Technology Stack
*   **Apache Kafka**: Selected for Message Broker to meet 10-year data retention and active-active high availability (99.99%) constraints via immutable distributed commit logs.
*   **Avro / JSON Schema**: Used via Schema Registry to guarantee message compatibility and data contracts across microservices.
*   **PostgreSQL**: Provides robust relational data storage for core clinical and billing data.
*   **Kubernetes (Hybrid on-prem + eu-central-1)**: Ensures scalable, fault-tolerant infrastructure deployment across hybrid environments.

## Rationale
This architecture ensures HIPAA and GDPR compliance while delivering sub-second EMR performance and active-active high availability. The use of Apache Kafka and strict schema validation supports reliable, scalable asynchronous integration across clinical microservices.