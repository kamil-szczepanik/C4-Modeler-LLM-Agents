## Overview
[The User & Compliance Service manages user profiles, authentication, and GDPR/CCPA data compliance workflows within the Amazon ECS/Fargate architecture. It ensures secure handling of user data and asynchronous compliance event propagation.]

## Key Elements
*   Shopper, Customer Support Agent, Legal/Compliance Officer
*   User & Compliance Service (Amazon ECS/Fargate)
*   Profile Controller (Spring MVC / Express.js)
*   Compliance Manager (Spring Boot / Node.js)
*   Audit Logger (Spring Data JPA / TypeORM)
*   Erasure Event Publisher (AWS SDK)
*   Amazon RDS PostgreSQL
*   AWS SNS / SQS with DLQs

## Relationships
*   AWS API Gateway -> User & Compliance Service: Routes requests [gRPC over TLS]
*   User & Compliance Service -> Identity Provider: Authenticates users [OIDC/OAuth2]
*   User & Compliance Service -> Amazon RDS PostgreSQL: Persists metadata and audit logs [SQL over TLS]
*   Erasure Event Publisher -> AWS SNS/SQS: Publishes UserDeletedEvent [AMQP/HTTPS]

## Technology Stack
*   Spring Boot / Node.js: Application runtime for microservice containers
*   Amazon ECS/Fargate: Serverless container orchestration for regional scalability
*   Amazon RDS PostgreSQL: Relational persistence with AWS KMS encryption-at-rest
*   AWS SNS/SQS: Asynchronous messaging with DLQs for reliable event-driven data erasure

## Rationale
[This architecture guarantees strict regulatory compliance and high availability through decoupled asynchronous event handling and immutable audit logging. It ensures resilient multi-region operations while protecting sensitive user data.]