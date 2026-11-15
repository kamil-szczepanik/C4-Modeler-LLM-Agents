## Overview
Modernizes a regional insurer's legacy mainframe claims system by gradually migrating claim types to a cloud-native platform over three years. Maintains hybrid operations while ensuring continuous, consistent claims processing without downtime or data loss.

## Key Elements
* **Claims Core Service:** Spring Boot modular monolith running on Azure Container Apps.
* **Claim Submission REST API:** Spring Web component handling online submissions via HTTPS.
* **Claim Workflow Engine:** Spring State Machine managing adjuster lifecycles, SLAs, and audits.
* **Mainframe Sync Adaptor:** Component communicating with the Anti-Corruption Layer via Apache Kafka.
* **Data Access Repository:** Spring Data JPA component interacting with Azure SQL Database.
* **Feature Flag Router Component:** Spring Cloud Feature Management component for dynamic claim-type routing.

## Relationships
* **API Gateway / Router -> Claim Submission REST API:** Routes online claim requests [HTTPS / OAuth2]
* **Claim Submission REST API -> Claim Workflow Engine:** Forwards validated submissions for processing [Internal Method Call]
* **Claim Workflow Engine -> Data Access Repository:** Persists workflow state and claim data [Spring Data JPA / TLS 1.3]
* **Mainframe Sync Adaptor -> Integration & Sync Engine:** Publishes and consumes asynchronous events [AMQP / Apache Kafka Protocol with mTLS]
* **Claim Workflow Engine -> Audit & Activity Trail Service:** Emits cryptographically signed business audit events [REST / Internal Messaging]

## Technology Stack
* **Java & Spring Boot:** Provides a modular monolith architecture to reduce distributed-system complexity for a cloud-novice team.
* **Spring State Machine:** Manages complex adjuster workflows and enables rapid one-day rollback capabilities.
* **Azure Container Apps:** Hosts the core service with horizontal pod autoscaling based on Kafka consumer lag.
* **Azure SQL Database:** Provides relational persistence with Azure Managed Identity, TDE, and application-layer field encryption.
* **Apache Kafka & Azure Service Bus:** Handles reliable asynchronous messaging between the cloud platform and the on-prem mainframe.

## Rationale
The modular monolith architecture minimizes distributed-system complexity for a team with limited cloud experience while maintaining strict consistency (R-04) and sub-2s performance (R-05). Incremental claim migration and robust rollback mechanisms (R-03, R-06) are safely achieved via feature flags, state machines, and backward-compatible database migrations.