## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMRs, scheduling, and billing. Its core purpose is to provide high-availability, HIPAA/GDPR-compliant healthcare operations for medium-sized clinics.

## Key Elements
- EMR Backend Container (Java Spring Boot 3)
- EMR REST/gRPC Controller
- Clinical Record Service
- Audit Interceptor
- Clinical Summary Aggregator
- EMR Database (PostgreSQL with RLS)
- Redis Cluster
- HashiCorp Vault Agent Sidecar

## Relationships
- EMR REST Controller -> Clinical Record Service [In-process method calls]
- Clinical Record Service -> EMR Database [JDBC over TLS with connection pooling]
- Clinical Summary Aggregator -> Redis Cluster [Redis protocol over TLS]
- EMR Backend Container -> HashiCorp Vault [Ephemeral tokens via sidecar]

## Technology Stack
- Java Spring Boot 3: Chosen for robust enterprise clinical backend development
- Spring Data JPA: Provides `@Version`-based optimistic locking for concurrent chart updates
- PostgreSQL with RLS: Enforces row-level security for HIPAA/GDPR patient isolation
- Redis Cluster: Delivers sub-second P95 load times for cached clinical summaries
- HashiCorp Vault: Secures dynamic secret injection at container startup

## Rationale
This architecture ensures strict regulatory compliance through advanced security controls while meeting sub-second performance SLAs. The component breakdown provides high availability and resilient data handling for critical clinical workflows.