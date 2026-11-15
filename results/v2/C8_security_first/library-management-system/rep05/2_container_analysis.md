## Overview
[The Library Management System is a comprehensive solution designed for public and academic libraries to catalogue physical and digital items, manage circulation workflows, and deliver reliable 24/7 self-service portals.]

## Key Elements
* Patrons & Library Staff
* EU-bound API Gateway
* Patron Self-Service Portal (Web/Mobile App)
* Staff Management Console
* Search & Catalogue Service
* Circulation & Loan Engine
* Analytics & Reporting Service
* Notification Engine
* Primary Database & Read-Replica
* Message Broker (RabbitMQ/Kafka)
* External Systems (Payment Gateway, Digital Content Providers, Inter-Library Loan Networks)

## Relationships
* Patrons and Staff interact with portals via HTTPS/REST, authenticated via OAuth2/OIDC with JWTs.
* Portals route traffic through the EU-bound API Gateway using REST/HTTPS.
* Internal containers communicate synchronously via gRPC using mTLS (TLS 1.3).
* Circulation & Loan Engine connects to external Payment Gateway and Inter-Library Loan Networks.
* Notification Engine consumes events asynchronously via AMQP/Kafka.
* Analytics & Reporting Service queries PostgreSQL read-replicas.

## Technology Stack
* Java / Spring Boot: Powers the Search & Catalogue Service for performance.
* Python (FastAPI / Pandas): Powers the Circulation & Loan Engine and Analytics & Reporting Service.
* Go: Powers the lightweight Notification Engine.
* Elasticsearch: Powers sub-800ms item search (R-05).
* PostgreSQL: Stores core transactional data with AES-256 encryption at rest.
* Kubernetes & ArgoCD: Orchestrates containers using GitOps workflows.

## Rationale
[This architecture meets EU-only data residency constraints and sub-800ms search performance requirements through dedicated microservices and regional stateful storage. Container isolation, autoscaling, and strict security controls ensure high availability and compliance for academic and public library operations.]