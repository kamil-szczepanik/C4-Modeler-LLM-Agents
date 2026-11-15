## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises COBOL/DB2 mainframe with a cloud-native Azure platform. It processes insurance claims via a hybrid architecture while maintaining the mainframe as the system of record.

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Customer Portal (React SPA / Azure Container Apps)
- Adjuster Workspace (Node.js/Java / Azure Container Apps)
- Anti-Corruption Layer (ACA Integration Service)
- Azure Service Bus (Premium Tier)
- On-Premises COBOL/DB2 Mainframe

## Relationships
- Customer Portal -> Azure Service Bus: Publishes claim submission events [AMQP 1.0]
- Adjuster Workspace -> Azure Service Bus: Publishes and subscribes to claim processing events [AMQP 1.0]
- Anti-Corruption Layer -> Azure Service Bus: Integrates asynchronous messaging events [AMQP 1.0]
- Azure Service Bus -> On-Premises Mainframe: Relays sync queues via private hybrid connectivity [AMQP 1.0 / ExpressRoute]

## Technology Stack
- Azure Service Bus Premium: Required for VNet integration, Private Link, and Service Bus Sessions
- AMQP 1.0: Protocol for secure, cross-platform multiplexed messaging
- Terraform / Bicep: Infrastructure as Code for repeatable deployments and drift prevention
- Microsoft Entra ID: Authentication mechanism replacing SAS connection strings with Managed Identities and Azure RBAC Data Actions

## Rationale
This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while safely migrating claim types one by one. Azure Service Bus guarantees zero claim loss, FIFO processing order, and rapid rollback capabilities within the existing operational constraints.