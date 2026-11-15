## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical operations while maintaining strict regulatory compliance for healthcare data.

## Key Elements
* Users: Doctors, Nurses, Receptionists, Billing Specialists
* External Systems: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Enterprise Identity Provider, Third-Party Notification Service
* API Gateway (Kong/Nginx)
* Web Application Frontend (React/TypeScript)
* Core Services Container (Node.js/Java Spring Boot)
* EMR & Audit Service (Java Spring Boot)
* Async Message Broker (Apache Kafka / RabbitMQ)
* Data Tier: PostgreSQL (Primary DB) and WORM-compliant storage (Audit/Archive Store)

## Relationships
* Web Application Frontend calls API Gateway via HTTPS
* API Gateway routes to Core Services and EMR Service via internal gRPC/REST, enforcing OAuth2/OIDC via Enterprise Identity Provider
* EMR & Audit Service communicates with External Lab & Imaging Systems using HL7 FHIR APIs
* Core Services publishes events to Async Message Broker via AMQP/Kafka protocol
* Billing & Insurance Integration Worker consumes from Async Message Broker to transmit claims to Payment Gateway / Insurance Clearinghouse

## Technology Stack
* Frontend: React/TypeScript served via CDN/Nginx for sub-second UI performance
* Gateway: Kong/Nginx for TLS termination and multi-factor access enforcement
* Services: Node.js and Java Spring Boot for modular microservice execution
* Messaging: Apache Kafka or RabbitMQ for decoupled, resilient asynchronous processing
* Database: PostgreSQL with multi-region active-active setup and AES-256 encryption at rest
* Storage: WORM-compliant storage to meet the 10-year data retention mandate
* Deployment: Hybrid cloud using on-premise Kubernetes and AWS eu-central-1

## Rationale
This architecture leverages active-active PostgreSQL and an async message broker to guarantee 99.99% uptime and prevent cascading service failures. Separating the EMR and Audit services alongside AES-256 encryption and WORM storage strictly enforces HIPAA and GDPR compliance requirements.