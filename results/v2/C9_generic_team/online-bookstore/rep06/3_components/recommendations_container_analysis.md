## Overview
• The system is an online bookstore providing personalized book recommendations via a dedicated microservice.
• It ensures high performance, regional scalability, and regulatory compliance across global AWS regions.

## Key Elements
• Recommendations Container: Core microservice hosted on Amazon ECS.
• Amazon ElastiCache (Redis): In-memory cache for pre-computed recommendation matrices and rate limiting.
• Background Pre-computation Worker: ECS-based worker for periodic scoring updates.
• AWS SNS/SQS: Messaging queues for purchase events and GDPR compliance triggers.
• API Gateway & BFF: Entry point routing requests via HTTPS/REST.

## Relationships
• API Gateway & BFF -> Recommendations Container: Routes recommendation requests [HTTPS/REST]
• Recommendations Container -> Amazon ElastiCache (Redis): Reads cached scores and checks rate limits [TCP/Redis Protocol]
• AWS SNS/SQS -> Recommendations Container & Worker: Ingests purchase and compliance events [AMQP/SQS]

## Technology Stack
• Docker & Amazon ECS: Containerization and orchestration for stateless horizontal scaling.
• Amazon ElastiCache (Redis): Caching layer to guarantee sub-2-second page loads.
• OpenTelemetry & CloudWatch: Structured logging and tracing for 99.95% availability monitoring.
• Pact: Consumer-driven contract testing for API safety.

## Rationale
• Caching and regional data isolation meet stringent performance (<2s latency) and scalability (1M MAU) requirements.
• Fallback mechanisms, circuit breakers, and health probes ensure high availability (99.95%) during traffic spikes.