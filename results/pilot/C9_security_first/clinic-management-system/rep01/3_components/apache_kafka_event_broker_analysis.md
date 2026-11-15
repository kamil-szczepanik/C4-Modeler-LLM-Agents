## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing while enforcing HIPAA/GDPR compliance and 99.99% availability. It utilizes an Apache Kafka Event Broker with KRaft, Confluent Schema Registry, and Kafka Connect for real-time, asynchronous clinical data streaming.]

## Key Elements
* Patients, Receptionists, Clinicians, Billing Specialists
* React SPA Frontend, NGINX/Kong API Gateway
* Patient Service, Scheduling Service, EMR Service, Billing Service, Apache Camel Integration Service
* Apache Kafka Event Broker (Topic Management Engine, KRaft metadata mode)
* Confluent Schema Registry
* Kafka Connect Framework (JDBC Sink Connector, Dead-Letter Queue)
* Distributed PostgreSQL Database

## Relationships
* React SPA Frontend -> NGINX/Kong API Gateway: HTTPS / REST / GraphQL
* Microservices -> Apache Kafka Event Broker: Binary TCP / TLS 1.3 / SASL/SCRAM / mTLS
* Kafka Connect Framework -> Distributed PostgreSQL Database: JDBC / TLS 1.3
* Microservices -> Third-Party Systems: HL7 FHIR APIs / HTTPS

## Technology Stack
* Java 21 & Spring Boot: Microservice runtime for performance and reliability
* Apache Kafka with KRaft: Event broker engine without ZooKeeper for high availability and rapid failovers
* Confluent Schema Registry: Apache Avro payload validation and schema enforcement (`BACKWARD_TRANSITIVE`)
* Kafka Connect: Real-time data pipeline with JDBC Sink and DLQ
* PostgreSQL: Active-active distributed hybrid data persistence

## Rationale
[This architecture combines event-driven microservices with KRaft-based Kafka clustering to achieve sub-second P95 performance and 99.99% uptime across hybrid environments. Strict mTLS transport encryption, envelope encryption, and Schema Registry validation satisfy mandatory HIPAA, GDPR, and 10-year audit retention constraints.]