## Overview
[This system modernizes a regional insurer's 30-year-old mainframe by deploying a hybrid cloud claims platform on Azure Kubernetes Service. It enables gradual claim type migration while maintaining seamless legacy integration and business continuity.]

## Key Elements
- Azure Kubernetes Service (AKS)
- API Gateway / BFF (Node.js)
- Claim Processing Domain Services (Java/Spring Boot)
- Mainframe Anti-Corruption Layer (ACL) Adapter
- ArgoCD (GitOps)
- Azure Service Bus
- Azure SQL Database

## Relationships
- Azure API Management -> API Gateway / BFF: Forwards requests [HTTPS / REST]
- API Gateway / BFF -> Claim Processing Domain Services: Internal communication [gRPC / HTTP/2]
- Claim Processing Domain Services -> Mainframe ACL Adapter: Asynchronous messaging [AMQP / AMQPS]
- Claim Processing Domain Services -> Azure SQL Database: Reads/writes modern data [TDS / SQL]
- Claim Processing Domain Services -> Azure Service Bus: Publishes and consumes events [AMQPS]

## Technology Stack
- Azure Kubernetes Service: Container orchestration runtime chosen for gradual claim migration capability.
- Node.js & Java/Spring Boot: Microservices runtime supporting BFF UI composition and CQRS domain services.
- ArgoCD: GitOps deployment engine enabling automated canary releases for low-experience cloud teams.
- Azure CNI & Network Policies: Implements strict microsegmentation and security boundaries.

## Rationale
[The architecture decouples legacy mainframe latency via CQRS and an Anti-Corruption Layer to meet performance goals. It balances the team's low cloud experience with robust security controls and zero-downtime migration pathways.]