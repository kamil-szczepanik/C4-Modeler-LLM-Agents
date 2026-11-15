## Overview
This system gradually replaces a 30-year-old regional insurance mainframe with a modern hybrid cloud platform. It processes online claims and adjuster workflows while maintaining legacy synchronization.

## Key Elements
- Web Frontend: React application hosted on Azure App Service
- BFF / API Gateway: Azure API Management with Node.js/Java Spring Boot
- Claims Processing Service: Java Spring Boot with JPA/PostgreSQL repositories
- Integration & ACL: Azure Service Bus with a custom Routing & Circuit-Breaker Worker
- Caching & Database: Azure Redis Cache and Azure SQL Database
- Identity: Insurer's Active Directory via OAuth2/OIDC

## Relationships
- Customers & Brokers to Web Frontend via HTTPS/REST (R-01)
- Web Frontend to BFF via HTTPS/REST
- BFF to Azure Redis Cache for reference data retrieval (R-05)
- Claims Processing Service to Azure SQL Database via JDBC/JPA (R-03)
- Integration Layer to Legacy Mainframe via restricted interface protocols

## Technology Stack
- Azure Container Apps: Serverless Kubernetes to reduce operational overhead for low-cloud-experience teams
- Java Spring Boot: Simplified backend repositories dropping complex frameworks for maintainability
- Azure Service Bus: Asynchronous event messaging and dead-letter queuing to protect the mainframe (R-04)
- Azure Managed Identities & Key Vault: Secure, secretless authentication across cloud components

## Rationale
The hybrid architecture isolates the fragile legacy mainframe using an anti-corruption layer and rate-limiting circuit breakers. Cloud-native caching and decoupled read/write segregation guarantee sub-second adjuster screens despite slow mainframe responses.