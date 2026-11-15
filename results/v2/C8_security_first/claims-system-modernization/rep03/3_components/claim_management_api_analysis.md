## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL mainframe with a modern Azure-based platform while maintaining uninterrupted hybrid operations. Its core purpose is to provide online claim submission for users and a responsive web application for claims adjusters.]

## Key Elements
* Claim Management API (.NET 8 running in Azure Container Apps)
* API Controller Layer with FluentValidation & ASP.NET Core Security
* Internal Routing Service & Anti-Corruption Layer (ACL)
* MediatR Domain / Command Handlers
* Azure SQL Database & Entity Framework Core
* Azure App Configuration & Azure Key Vault
* Azure Service Bus

## Relationships
* API Gateway -> Claim Management API [HTTPS REST APIs]
* API Controller Layer -> Domain Handlers [MediatR In-Process]
* Domain Handlers -> Claim Router / ACL [HTTP/REST with Polly resilience policies]
* Domain Handlers -> Azure SQL Database [Entity Framework Core with TDE]
* Domain Handlers -> Azure Service Bus [AMQP over TLS]
* Claim Management API -> Azure Key Vault [Managed Identities over HTTPS]

## Technology Stack
* .NET 8 / ASP.NET Core: Chosen for high performance, robust microservice support, and team maintainability.
* Azure Container Apps: Provides serverless container orchestration without requiring deep Kubernetes cloud expertise.
* Polly: Implements circuit breakers and retry policies to isolate mainframe latency.
* Azure SQL Database: Provides managed relational persistence with integrated security.
* Azure App Configuration: Enables dynamic feature flagging for gradual claim migration and rapid rollbacks.

## Rationale
[This hybrid architecture isolates the expensive legacy mainframe via an Anti-Corruption Layer and dynamic feature flags to meet strict 1-day rollback and zero-data-loss constraints. Additionally, it uses caching, Polly resilience, and managed Azure services to guarantee the <2s adjuster performance SLA despite team cloud inexperience.]