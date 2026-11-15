## Overview
The Notification Service is a microservice component within the Online Bookstore architecture responsible for asynchronously processing, localizing, and dispatching multi-channel transactional alerts. It ensures reliable customer communication while enforcing strict GDPR, CCPA, and uptime requirements.

## Key Elements
- **Shoppers & Customer Support Agents**: End-users receiving alerts and internal staff auditing sent notifications.
- **Event Consumer Component**: Spring Boot / Node.js service ingesting messages from AWS SQS.
- **Notification Router Component**: Internal orchestrator managing message flow and idempotency via Amazon ElastiCache (Redis).
- **Preference & Compliance Manager Component**: Validator querying the User & Compliance Service via REST.
- **Template Engine Component**: Localized rendering engine with compiled resource bundles.
- **Channel Dispatcher Components**: Adapters using Resilience4j circuit breakers for SendGrid (Email) and Twilio (SMS).
- **Notification Repository Component**: Data access layer persisting audit trails in Amazon DynamoDB.

## Relationships
- **Event Consumer -> AWS SQS**: Consumes asynchronous notification requests [AMQP/SQS].
- **Preference Manager -> User & Compliance Service**: Verifies GDPR/CCPA consent and suppression lists [REST/HTTPS].
- **Channel Dispatcher -> SendGrid/Twilio APIs**: Dispatches final payloads to external providers [HTTPS].
- **Notification Repository -> Amazon DynamoDB**: Persists delivery states and audit logs [TCP].

## Technology Stack
- **Spring Boot / Node.js on Amazon ECS/Fargate**: Core container runtime for scalability across regions.
- **AWS SQS with DLQs**: Asynchronous messaging backbone ensuring message durability.
- **Amazon ElastiCache (Redis)**: Short-lived cache for message idempotency and deduplication.
- **Resilience4j**: Circuit breaker implementation for third-party provider failure mitigation.
- **Amazon DynamoDB**: NoSQL storage for audit trails and support lookup histories.

## Rationale
This architecture guarantees high availability (99.95% uptime SLA) and rapid scaling via SQS queue-depth metrics across multiple AWS regions. It robustly enforces data privacy compliance and protects against third-party provider outages using circuit breakers and idempotency checks.