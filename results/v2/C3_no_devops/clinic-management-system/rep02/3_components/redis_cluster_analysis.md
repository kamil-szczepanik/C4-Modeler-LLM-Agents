## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and low-latency performance using a hybrid cloud architecture.

## Key Elements
- Patients & Clinical Staff (Primary Users)
- API Gateway (Kong / Nginx in Kubernetes)
- EMR Backend Container (Node.js / Java Spring Boot)
- Scheduling & Resource Engine Container (Java Spring Boot)
- Redis Cluster (In-memory Redis with Primary Master Nodes, Replica/Failover Nodes, TLS Termination Module, and Policy & Eviction Manager)
- EMR Database (PostgreSQL with RLS)

## Relationships
- Scheduling & Resource Engine Container -> Primary Master Nodes: Caches scheduling states and locks [RESP3 protocol via TLS v1.3 with mTLS]
- Primary Master Nodes <=> Replica / Failover Nodes: Data replication and cluster heartbeat [Redis Cluster Bus protocol over TLS]
- API Gateway -> EMR Backend Container: Routes incoming clinical requests [HTTPS/REST]

## Technology Stack
- Redis Enterprise / Redis OSS: Provides in-memory caching and distributed slot allocation for low-latency scheduling.
- PostgreSQL: Stores structured patient data and EMR records with Row-Level Security.
- Java Spring Boot: Powers robust backend business logic and scheduling engines.
- Kubernetes: Orchestrates containers across on-prem and cloud environments to guarantee 99.99% uptime.

## Rationale
This architecture ensures high availability and low latency required for real-time clinical workflows and sub-second EMR screen loads. Strict data governance, mTLS, and AES-256 encryption guarantee full HIPAA and GDPR compliance.