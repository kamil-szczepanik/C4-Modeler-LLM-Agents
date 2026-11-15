## Overview
The Online Bookstore is a scaled-down e-commerce platform that provides catalogue browsing, secure checkout, reviews, and personalized recommendations for 1M MAU. The Recommendation Worker container processes asynchronous events to generate and cache 'Customers also bought' suggestions while maintaining strict GDPR/CCPA compliance.

## Key Elements
- Shopper: Primary human user benefiting from personalized recommendations.
- Recommendation Worker: Parent container running on Amazon ECS/Fargate.
- Event Consumer Component: Built with Spring Boot/Node.js to poll SQS queues.
- Recommendation Processor Component: Core logic for external synchronization and fallbacks.
- Cache / State Sync Component: Manages local data in Amazon ElastiCache (Redis).
- Compliance Enforcement Component: Handles GDPR/CCPA data deletion events.
- Third-Party Recommendation Engine: External system providing recommendation data via HTTPS/REST.
- AWS SQS/SNS with DLQs: Message broker for asynchronous event ingestion.

## Relationships
- Recommendation Worker -> AWS SQS/SNS with DLQs: Consumes recommendation events [AWS SQS protocol]
- Event Consumer -> Recommendation Processor: Invokes processing pipeline [Internal Method Call]
- Recommendation Processor -> Third-Party Recommendation Engine: Syncs interaction data and fetches recommendations [HTTPS/REST]
- Recommendation Processor -> Amazon ElastiCache (Redis): Updates cache, retrieves defaults, and purges user profiles [RESP protocol]
- Compliance Enforcement Component -> Amazon ElastiCache (Redis): Purges user recommendation profiles on deletion requests [RESP protocol]

## Technology Stack
- Amazon ECS on AWS Fargate: Container orchestration for horizontal auto-scaling based on SQS queue depth.
- Spring Boot / Node.js: Application runtime for worker and internal components.
- Amazon ElastiCache (Redis): In-memory cache for fast retrieval of recommendation snippets and fallback defaults.
- AWS SQS/SNS with DLQs: Asynchronous messaging with dead-letter queues for resilience against poison pills.
- Resilience4j: Circuit breaker pattern for handling third-party engine failures.
- AWS Secrets Manager: Secure credential management for third-party API keys.

## Rationale
This architecture ensures 99.95% uptime and sub-second performance by decoupling event processing from user requests using SQS queues and Redis caching. It guarantees GDPR/CCPA compliance and business continuity through dedicated compliance enforcement components and graceful fallback strategies during third-party outages.