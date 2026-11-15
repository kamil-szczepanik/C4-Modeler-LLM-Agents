## Overview
The Case Management Backend manages analyst review workflows and fraud cases for the Real-Time Payment Fraud Screening system. It operates on AWS ECS Fargate, providing secure, auditable case resolution while ensuring PCI-DSS compliance and strict data masking.

## Key Elements
- Workflow Engine Component (Spring State Machine)
- Analyst Portal API Controller (Spring MVC/REST)
- Case Repository Layer (Spring Data JPA)
- Tokenization & Masking Service Client (Spring Cloud OpenFeign with Resilience4j)

## Relationships
- Analyst Portal API Controller -> Workflow Engine Component: Invokes via direct method calls
- Analyst Portal API Controller -> Case Repository Layer: Persists and retrieves state via Amazon RDS PostgreSQL
- Workflow Engine Component -> Case Repository Layer: Persists state using optimistic locking via Amazon RDS PostgreSQL
- Analyst Portal API Controller -> Tokenization & Masking Service Client: Retrieves masked payload data for rendering case details
- Tokenization & Masking Service Client -> Card Networks & Tokenization Vault: Fetches tokenized card data via mTLS and IAM authentication

## Technology Stack
- Java Spring Boot: Core framework chosen for enterprise reliability and rapid feature delivery by a 3-engineer team.
- Amazon ECS on Fargate: Container runtime selected to eliminate OS-level patching overhead and maintain PCI-DSS compliance.
- Amazon RDS PostgreSQL: Relational database utilizing Row-Level Security and encryption for tamper-evident audit trails.
- Resilience4j: Fault-tolerance library used in the Feign client to ensure fail-fast resilience during external vault degradation.
- AWS Secrets Manager: Used for runtime credential injection via IAM task roles.

## Rationale
This architecture balances strict PCI-DSS security constraints and 7-year auditability with the operational limitations of a 3-engineer team through managed AWS services. Containerizing on Fargate and leveraging robust Spring components ensures high availability, strict data isolation, and a predictable cost structure within the 25,000 EUR monthly budget.