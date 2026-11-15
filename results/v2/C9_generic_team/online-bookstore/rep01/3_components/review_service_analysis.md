## Overview
The Online Bookstore system is a scalable e-commerce platform providing catalog browsing, secure checkout, customer reviews, and personalized recommendations. It ensures high availability, multi-currency support, and strict GDPR/CCPA compliance across global AWS regions.

## Key Elements
- Customer & Store Administrator
- API Gateway (AWS API Gateway / Reverse Proxy)
- Review Service Microservice (Java/Spring Boot or Node.js)
- Hexagonal Architecture / Clean Architecture layers
- CQRS Write Model & Read Model
- Distributed Cache (Amazon ElastiCache)
- Asynchronous Message Broker (AWS SQS/SNS)
- Compliance/User Data Container (Segregated Isolated Database-per-Service)
- Internal Components: Moderation Pipeline, Data Retention & Anonymization Worker, Transactional Outbox Pattern, Bulkhead Thread Pools, Health Check Probes, and Rate Limiting / Input Sanitization Middleware

## Relationships
- API Gateway -> Review Service: Routes review requests [REST/gRPC]
- Review Service -> Asynchronous Message Broker: Publishes review events [AWS SQS/SNS]
- Review Service -> Compliance/User Data Container: Accesses segregated database [Database-per-Service (TCP)]
- Review Service -> Distributed Cache: Reads/writes aggregated ratings and reviews [Redis/Memcached Protocol]
- Review Service -> SIEM Provider: Exports structured JSON logs [HTTPS]

## Technology Stack
- Java/Spring Boot or Node.js: Core microservice runtime
- AWS API Gateway: Entry point, rate limiting, and request routing
- Amazon ElastiCache: Distributed caching for read-path performance optimization
- AWS SQS/SNS: Asynchronous messaging for event-driven decoupled workflows
- OpenTelemetry: Distributed tracing and observability correlation
- Prometheus/CloudWatch: Metrics, dashboards, error budgets, and alerting

## Rationale
This architecture uses CQRS, distributed caching, and bulkhead patterns to effortlessly scale past 1M MAU while guaranteeing sub-2-second page loads on 3G. Furthermore, segregated databases, transactional outboxes, and dedicated data retention workers ensure robust GDPR/CCPA compliance and 99.95% uptime availability.