## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe by gradually migrating claim types to a cloud platform. Azure Service Bus acts as the asynchronous backbone for hybrid integration and reliable message processing.]

## Key Elements
* Azure Service Bus (Asynchronous messaging backbone)
* Azure Modular Monolith Platform (Cloud processing components)
* COBOL/DB2 On-Premises Mainframe (System of record)
* Azure Blob Storage (Payload storage via Claim-Check pattern)
* Azure Application Insights (Distributed tracing and monitoring)

## Relationships
* Azure Modular Monolith Platform publishes asynchronous events to Azure Service Bus using AMQP protocol
* Azure Service Bus decouples cloud services from the COBOL/DB2 On-Premises Mainframe
* Azure Modular Monolith Platform offloads large claim attachments to Azure Blob Storage over HTTPS
* Azure Application Insights collects distributed trace headers and telemetry across all containers

## Technology Stack
* Azure Service Bus: Chosen for guaranteed message delivery and decoupling in hybrid environments
* Azure Blob Storage: Implements Claim-Check pattern to handle large payloads within Service Bus limits
* Bicep or Terraform: Infrastructure as Code for repeatable Azure Service Bus deployments
* Application Insights: Enables distributed tracing with correlation IDs to bridge cloud and mainframe boundaries

## Rationale
[This architecture ensures zero claim loss and strict ordering during hybrid migration while protecting the fragile legacy mainframe. Standardized messaging patterns and IaC mitigate the team's cloud skill gap.]