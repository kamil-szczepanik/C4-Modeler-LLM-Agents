## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability (99.99%) and strict HIPAA/GDPR compliance using secure microservices.

## Key Elements
- Users: Patients, Clinicians, Administrative Staff, Billing Officers, Compliance Officers
- External Systems: External Insurance/Clearinghouse System, External Laboratory & Imaging System
- Containers: Web Application (React/TypeScript), API Gateway (NGINX/Envoy), EMR Service (Node.js/Go), Billing & Claims Service (Java/Spring Boot), Scheduling Service (Node.js/Go), Notification Service (Python/FastAPI), Integration Service (Java/Spring Boot), PostgreSQL, Redis, RabbitMQ, HashiCorp Vault
- Vault Components: Auth Method (Kubernetes JWT/AppRole & mTLS), HTTP API / Request Router, Secrets Engine (Dynamic DB & KV), Transit Secrets Engine, Audit Device, Built-in Raft Storage Backend

## Relationships
- Backend Services -> HashiCorp Vault: Fetches secrets via REST over mTLS
- HashiCorp Vault Audit Device -> SIEM: Streams audit logs via Syslog
- Clinic Management System -> External Systems: Submits claims and exchanges lab data via HL7 FHIR APIs over TLS

## Technology Stack
- HashiCorp Vault: Centralized secrets management, dynamic database credentials, and transit encryption for AES-256 data protection
- PostgreSQL & Redis: Core data storage and caching with AES-256 at rest
- RabbitMQ: Asynchronous messaging broker
- React / TypeScript & Java Spring Boot / Node.js / Python FastAPI: Frontend and backend microservices implementation
- Kubernetes (On-prem & AWS eu-central-1): Hybrid cloud container orchestration

## Rationale
This architecture uses hybrid-deployed HashiCorp Vault clusters with Performance Replication and cloud-native auto-unseal to achieve 99.99% availability without compromising latency. Strict mTLS, dynamic database credentials, and fail-closed audit logging enforce HIPAA and GDPR compliance requirements.