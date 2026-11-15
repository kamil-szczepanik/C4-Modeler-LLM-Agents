## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring HIPAA/GDPR compliance and high availability. It utilizes Redis as a distributed caching and locking layer to support high-performance data access and appointment scheduling.

## Key Elements
* Session & Rate-Limiting Engine (Redis Core)
* Distributed Lock Manager (Redlock Algorithm)
* Data Caching Module
* Spring Boot Core Services
* Go Audit Logging Container
* HashiCorp Vault
* Istio Service Mesh

## Relationships
* Spring Boot Core Services -> Session & Rate-Limiting Engine: Manages user authentication tokens and API throttling [RESP3 over TLS via Istio mTLS]
* Spring Boot Core Services -> Distributed Lock Manager: Executes atomic operations to prevent appointment resource clashes [RESP3 over TLS via Istio mTLS]
* Spring Boot Core Services -> Data Caching Module: Retrieves non-PHI reference datasets [RESP3 over TLS via Istio mTLS]
* Redis -> Go Audit Logging Container: Ships security events and audit logs [Syslog over TCP/TLS]

## Technology Stack
* Redis: Distributed caching and state management for high performance and low-latency EMR screen loads (< 1s P95)
* RESP3 over TLS: Secure protocol for application-to-cache communication
* HashiCorp Vault: Dynamic credential generation, secret rotation, and encryption key management
* Istio Service Mesh: Mutual TLS enforcement, network policies, and telemetry
* Kubernetes: Container orchestration with network policies and resource isolation

## Rationale
This architecture uses Redis exclusively for non-PHI metadata, session states, and locks, mitigating HIPAA/GDPR compliance risks while delivering sub-second performance. High availability (99.99%) and secure communication are guaranteed via clustered topologies, Istio mTLS, and Vault-managed security controls.