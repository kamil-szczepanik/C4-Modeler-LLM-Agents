## Overview
[The Claims Integration Service is a .NET Core Worker Service hosted in Azure Container Apps that orchestrates hybrid claims processing between a modern Azure cloud platform and an on-premise legacy mainframe. It ensures seamless, zero-data-loss claim migration while maintaining system reliability.]

## Key Elements
- Claim Router Component (.NET Core)
- Outbox Processor Component (.NET Core)
- Legacy Fallback Component (.NET Core)
- Audit & Telemetry Logger Component (.NET Core)
- Azure Service Bus (AMQP/AMQPS)
- Azure App Configuration (HTTPS/REST)
- Azure Key Vault (Managed Identities)
- Azure Application Insights / Azure Monitor (TLS 1.3)
- Mainframe Adapter (.NET Core API, On-Premises)

## Relationships
- Claim Router -> Legacy Fallback [Internal C# method calls]
- Claim Router -> Audit & Telemetry Logger [In-memory C# events]
- Outbox Processor -> Azure Service Bus [AMQP with AMQPS / TLS 1.3]
- Claims Integration Service -> Azure App Configuration [HTTPS/REST via Managed Identity]
- Claims Integration Service -> Mainframe Adapter [REST/JSON over mTLS]
- Claims Integration Service -> Azure Application Insights [TLS 1.3 with Customer-Managed Keys]

## Technology Stack
- .NET Core: Framework for high-performance backend worker services
- Azure Container Apps: Serverless container hosting tailored for limited cloud experience teams
- Azure Service Bus: Reliable message broker for asynchronous event processing
- Azure App Configuration: Centralized feature flagging to support quick claim-type rollbacks (R-06)
- Azure Key Vault: Secure credential management and envelope encryption using Managed Identities
- Bicep/Terraform: Infrastructure-as-Code to automate deployments and reduce cloud configuration errors

## Rationale
[This hybrid architecture securely bridges legacy mainframes and modern cloud components while strictly enforcing zero data loss (R-04) via the Transactional Outbox pattern. Centralized feature flags and robust auditing guarantee fast rollbacks and compliance without requiring container redeployments.]