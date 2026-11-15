## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old regional insurer mainframe with a modern hybrid platform. The Audit & Compliance Worker container ensures transactional consistency and regulatory compliance without data loss.

## Key Elements
* Event Consumer Component (.NET 8 Hosted Service / MassTransit)
* Compliance Validator Component (.NET 8)
* Dead Letter Manager Component (.NET 8)
* Audit Repository Access Component (Entity Framework Core)
* Mainframe Sync Component (.NET 8 BackgroundService with native PeriodicTimer)
* External Systems: Azure Service Bus, Azure SQL Database, Azure Blob Storage, Audit & Compliance System

## Relationships
* Event Consumer Component consumes domain events from Azure Service Bus via AMQP.
* Compliance Validator Component evaluates events, routing valid data to Audit Repository Access Component and failures to Dead Letter Manager Component.
* Dead Letter Manager Component stores poisoned messages in Azure Blob Storage.
* Audit Repository Access Component persists compliance logs in Azure SQL Database.
* Mainframe Sync Component pushes compliance packages to the Audit & Compliance System via HTTPS/REST.

## Technology Stack
* .NET 8 / Azure Container Apps: Chosen for core runtime and hosting, leveraging team expertise.
* MassTransit: Simplifies idempotent message processing for consistency (R-04).
* Entity Framework Core: Provides reliable data persistence for Azure SQL Database.
* PeriodicTimer: Implements lightweight scheduling without external orchestrator dependencies.

## Rationale
This component architecture enforces strict consistency and prevents claim loss during migration by combining reliable message consumption with robust dead-lettering and audit logging. The design minimizes cloud complexity, aligning with the team's skillset while satisfying integration constraints.