## Overview
The Clinic Management System is a clinical IT platform that handles patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. It utilizes a hybrid cloud architecture designed for high availability, security, and strict healthcare regulatory compliance.

## Key Elements
* Patients, Doctors, Administrators (Actors)
* Web Frontend (React / TypeScript / NGINX)
* API Gateway (Kong / NGINX) containing 6 internal components: TLS Termination & Routing Engine, Auth & Token Introspection Plugin, Rate Limiting & Threat Protection Component, Audit & Request Correlation Interceptor, Request Transformation & Payload Validation Engine, and Edge Caching & Session Store Component
* Core Microservices (Go / Spring Boot)
* Integration Service (Apache Camel / Node.js)
* Message Broker (Apache Kafka / RabbitMQ)
* PostgreSQL Database (AES-256 encrypted at rest)
* Redis Enterprise (Caching & Session Container)
* OpenSearch (Audit & Compliance Logging)
* Identity Provider, Third-Party Billing Gateway, External Lab/Imaging Systems

## Relationships
* Web Frontend -> API Gateway: Sends client requests [HTTPS / JSON]
* API Gateway -> Core Microservices: Routes validated traffic [gRPC / Internal mTLS]
* Auth & Token Introspection Plugin -> Identity Provider: Validates user tokens [HTTPS / OIDC]
* Audit & Request Correlation Interceptor -> Audit & Compliance Logging: Forwards access logs and security events [gRPC / mTLS]
* Integration Service -> External Lab/Imaging Systems: Interoperates via clinical standards [HL7 FHIR APIs]
* Core Microservices -> PostgreSQL Database: Persists clinical and patient records [TLS / SQL]

## Technology Stack
* Kong API Gateway: Selected for enterprise plugins, declarative configuration, and rate-limiting to meet 99.99% uptime constraints.
* Go & Spring Boot: Chosen for Core Microservices to ensure high-throughput and low-latency EMR screen loads.
* Apache Kafka & RabbitMQ: Implemented for asynchronous, reliable event-driven messaging across distributed services.
* PostgreSQL with AES-256: Used for persistent storage to satisfy strict HIPAA/GDPR encryption and data retention requirements.
* HL7 FHIR APIs: Adopted for seamless healthcare interoperability with external lab and imaging systems.

## Rationale
This hybrid cloud, microservices-based architecture guarantees 99.99% high availability through active-active deployments across on-premise Kubernetes and AWS eu-central-1. Furthermore, it strictly enforces HIPAA and GDPR compliance via edge-level OAuth2/OIDC token validation, mTLS service communication, and immutable audit logging.