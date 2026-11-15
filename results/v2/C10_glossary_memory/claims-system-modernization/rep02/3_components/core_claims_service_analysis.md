## Overview
[The system is a cloud-based Core Claims Service hosted in Azure Container Apps that modernizes an insurance claims platform while integrating with an on-premises mainframe. Its core purpose is to process migrated claim types securely, maintain strict data consistency, and support gradual platform migration.]

## Key Elements
- Claim Domain Controller [component]
- Claim Processing Engine [component]
- Mainframe Anti-Corruption Layer (ACL) [component]
- Outbox Event Publisher [component]
- Repository / Data Access Component [component]

## Relationships
- Claim Domain Controller -> Claim Processing Engine [In-process method calls]
- Claim Processing Engine -> Mainframe Anti-Corruption Layer [In-process method calls]
- Claim Processing Engine -> Outbox Event Publisher [JDBC / Transactional Outbox]
- Claim Processing Engine -> Repository / Data Access Component [In-process method calls]
- Repository / Data Access Component -> Azure SQL Database [TDS with encryption]
- Outbox Event Publisher -> Data Sync Engine [AMQP / Azure Service Bus]

## Technology Stack
- Azure Container Apps [Hosts the Core Claims Service with managed identities and revision support]
- Java / Spring Boot or .NET [Implements the Core Claims Service domain logic and components]
- Spring Data JPA / Entity Framework [Encapsulates persistence logic in the Repository component]
- Azure SQL Database [Acts as the cloud system of record using Transparent Data Encryption]
- OpenTelemetry [Enables distributed tracing across the hybrid boundary]

## Rationale
[This architecture uses domain isolation and a Mainframe Anti-Corruption Layer to allow rapid one-day fallback of claim types to the legacy system. The Transactional Outbox pattern guarantees data consistency without complex distributed transactions, fitting a team with limited cloud experience.]