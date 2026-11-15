## Overview
[Component-level architecture for the Claims Core API within the modern hybrid Azure claims platform, replacing a legacy mainframe incrementally.]

## Key Elements
• Claim Submission Controller (Spring gRPC)
• Claim Management Service (Spring Service / Domain Model)
• Mainframe Anti-Corruption Layer (Spring Integration / WebClient)
• Event Publisher (Spring Kafka)
• Claim Read Model Updater (Spring Data Cosmos / Kafka Consumer)

## Relationships
• Claim Submission Controller -> Claim Management Service [In-process Java Method Call]
• Claim Management Service -> Mainframe ACL [In-process Java Method Call]
• Claim Management Service -> Event Publisher [In-process Java Method Call]
• Claim Management Service -> Claim Read Model Updater [In-process Application Event]
• Claim Read Model Updater -> Claims Read Model & Cache [HTTPS/TCP]
• Event Publisher -> Integration & Sync Engine [Kafka native protocol over mTLS]

## Technology Stack
• Spring Boot / Java: Core framework for microservices providing robust enterprise capabilities.
• Azure Kubernetes Service (AKS): Container orchestration platform with KEDA autoscaling.
• Azure Cosmos DB: NoSQL database for low-latency read models and asynchronous caching.
• OpenTelemetry: Distributed tracing framework for cross-boundary observability with PII masking.
• Spring gRPC & REST/HTTPS: Hybrid ingress and internal communication protocols.

## Rationale
[This component architecture isolates brittle legacy mainframe dependencies via an Anti-Corruption Layer and asynchronous read models to guarantee sub-2-second UI performance. It enforces strict zero-trust security and transactional consistency while accommodating a team with limited cloud experience.]