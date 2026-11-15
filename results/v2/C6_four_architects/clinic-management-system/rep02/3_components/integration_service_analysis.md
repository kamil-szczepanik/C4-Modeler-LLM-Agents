## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, security compliance, and interoperability across hybrid cloud environments.

## Key Elements
* External Lab/Imaging Systems, Insurance Clearinghouses, Payment Gateway, Identity Provider, Notification Service
* API Gateway (Kong/Envoy), Web Application (React/Nginx), Core Services (Node.js/NestJS), EMR Service (Java/Spring Boot), Integration Service (Apache Camel/Java)
* Integration Service Components: FHIR Ingress/Egress Router, HL7 v2 MLLP Adapter, Schema Validation Component, Data Transformation Engine, Circuit Breaker & Resilience Engine, OAuth2/mTLS Security Interceptor, Dead Letter Channel & Audit Component, Integration Queue Producer, Metrics & Telemetry Publisher
* Async Worker Containers (Python/Celery or Java), Identity & Policy Container (Keycloak)
* Message Broker (Apache Kafka), Cache / State Store (Redis Cluster), Data Layer (PostgreSQL and MinIO/AWS S3)

## Relationships
* Web Application -> API Gateway: Client requests via HTTPS [REST/JSON]
* API Gateway -> Core Services & EMR Service: Internal routing via gRPC/HTTPS [HTTP/2]
* Integration Service (FHIR Ingress/Egress Router) -> External Lab/Imaging Systems: FHIR over HTTPS [HTTPS/JSON]
* Integration Service (HL7 v2 MLLP Adapter) -> External Lab/Imaging Systems: Legacy data ingestion via MLLP [TCP]
* Integration Service (Integration Queue Producer) -> Message Broker (Apache Kafka): Event publishing [TCP/Kafka]
* Integration Service (Circuit Breaker) -> Cache / State Store (Redis Cluster): State synchronization via RESP [RESP/TLS]
* Integration Service (Dead Letter Channel) -> Data Layer (PostgreSQL/MinIO): Audit persistence via JDBC [JDBC/TLS]
* Integration Service (Metrics Publisher) -> Monitoring Stack: Operational telemetry [HTTP/TLS]

## Technology Stack
* Hybrid Cloud (on-prem-k8s and eu-central-1): Meets local legacy integration needs and scalable cloud deployment.
* Apache Camel (Java runtime): Provides robust out-of-the-box healthcare data formats and routing capabilities.
* Apache Kafka: Enables reliable, high-throughput asynchronous messaging between services.
* PostgreSQL and MinIO/AWS S3: Ensures relational data persistence and compliant object storage with AES-256 encryption.
* Redis Cluster: Maintains distributed state for circuit breakers across hybrid nodes.

## Rationale
The hybrid architecture combines on-premise Kubernetes deployment for local MLLP lab integration with AWS cloud scaling to satisfy strict latency and uptime targets. Utilizing Apache Camel alongside robust encryption, auditing, and interoperability standards ensures full HIPAA and GDPR compliance while maintaining 99.99% availability.