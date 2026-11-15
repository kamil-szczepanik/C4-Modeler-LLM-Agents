## Overview
The application tier of the insurance claims modernization platform is built on a unified Java/Spring Boot architecture running on Azure Container Apps. It gradually replaces the legacy mainframe by routing unmigrated claim types through an Anti-Corruption Layer while maintaining strict transactional consistency.

## Key Elements
- Claim Submission Component (Spring Boot)
- Adjuster Workspace Component (Spring Boot)
- Anti-Corruption Layer (ACL) & Router Component (Spring Boot)
- Outbox Processor Component (Spring Boot)
- Unified Workers (Java/Spring Boot on Azure Container Apps)
- Audit & Compliance Component (Spring Boot)

## Relationships
- Claim Submission & Adjuster Workspace -> Data Tier [Spring Data JPA / PostgreSQL Protocol]
- ACL & Router -> Hybrid Bridge [gRPC over Azure Relay / TCP]
- Outbox Processor -> Integration Tier [AMQP via Azure Service Bus]
- Unified Workers -> Core Banking & Notification Services [HTTPS / REST]
- Internal Components -> Audit & Compliance [Spring AOP]

## Technology Stack
- Java 17 and Spring Boot 3: Chosen for robust enterprise patterns and team familiarity.
- Azure Container Apps with KEDA: Enables event-driven autoscaling of unified background workers without polyglot complexity.
- Spring Data JPA: Standardizes relational data access for PostgreSQL.
- gRPC over Azure Relay: Provides low-latency, strongly typed hybrid communication with the on-premise mainframe.

## Rationale
This unified single-technology architecture minimizes cognitive load for a team with limited cloud experience while meeting strict performance and consistency constraints. The Anti-Corruption Layer and transactional outbox pattern ensure a safe, incremental migration with a one-day rollback capability.