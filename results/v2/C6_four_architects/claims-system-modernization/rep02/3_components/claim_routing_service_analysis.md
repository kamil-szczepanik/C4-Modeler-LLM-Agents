## Overview
[The system modernizes a 30-year-old regional insurer mainframe claims system by gradually migrating claim types to a hybrid cloud platform. The Claim Routing Service dynamically directs claims between legacy and modern pipelines to ensure seamless migration.]

## Key Elements
- Claim Routing Service (Apache Camel on Azure Container Apps container)
- Event Ingress Router
- Routing Rules Engine
- Feature Flag Evaluator (with local in-memory cache and short TTL)
- Modern Platform Dispatcher
- Mainframe Fallback Dispatcher
- Dead Letter & Audit Handler

## Relationships
- Event Ingress Router -> Feature Flag Evaluator [In-memory function call]
- Feature Flag Evaluator -> Primary Datastore [JDBC/TLS]
- Event Ingress Router -> Modern Platform Dispatcher -> Claims Processing Service [gRPC/HTTP]
- Event Ingress Router -> Mainframe Fallback Dispatcher -> Mainframe Integration Adapter [AMQP/JMS via IBM MQ]
- Dead Letter & Audit Handler -> Azure Blob Storage / Audit Service [HTTPS]

## Technology Stack
- Apache Camel: Selected for native Enterprise Integration Patterns and circuit-breaker support
- Azure Container Apps: Chosen to abstract Kubernetes complexity and align with the Java team's stack
- Azure SQL Database: Used as the Primary Datastore for real-time migration status flags
- Redis / In-memory cache: Provides low-latency feature flag evaluation with a short TTL

## Rationale
[This architecture fits requirements by decoupling legacy and modern processing through content-based routing, enabling a one-day rollback per claim type. Furthermore, local caching protects performance while ensuring zero lost claims during the hybrid migration.]