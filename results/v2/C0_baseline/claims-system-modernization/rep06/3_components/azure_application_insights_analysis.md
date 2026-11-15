## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claim processing. It utilizes Azure cloud services integrated with on-premise infrastructure to provide secure, scalable claim submission, adjuster management, and monitored data migration.]

## Key Elements
- Users: Customer, Broker, Claims Adjuster, System Operators / Support Leads
- External Systems: On-premise COBOL/DB2 Legacy Mainframe
- Azure API Management (Azure API Management)
- Claims Processing Service (Java, Spring Boot, Azure Container Apps)
- Migration Dashboard (React, Node.js, Azure Container Apps)
- Azure Service Bus (Azure Service Bus)
- Azure Logic Apps / Functions (Azure Logic Apps, Azure Functions)
- Azure SQL Database (Azure SQL Database, TDS)
- Azure Key Vault (Azure Key Vault)
- Azure Active Directory (Entra ID) (Azure Active Directory (Entra ID), OAuth 2.0, OpenID Connect)
- Azure Application Insights (Azure Application Insights)
- Application Insights SDK / Auto-collection agents
- Log Analytics Workspace (Azure Log Analytics, Kusto Query Language)
- Application Insights Alert Rules (Azure Monitor alerts, Webhook/Action Groups)
- Application Insights Workbooks (Azure Workbooks, JSON/KQL)
- Application Insights Metrics Explorer (Azure Monitor, Time-series DB)

## Relationships
- Customer and Broker interact with Azure API Management via HTTPS (Port 443)
- Claims Adjuster interacts with Migration Dashboard via HTTPS (Port 443)
- Azure API Management routes requests to Claims Processing Service via HTTPS (Port 443)
- Claims Processing Service communicates with Azure Service Bus via AMQP (Port 5671)
- Claims Processing Service persists data in Azure SQL Database via TDS (Port 1433)
- Claims Processing Service and Migration Dashboard authenticate via Azure Active Directory (Entra ID) using OAuth 2.0 and OpenID Connect
- Claims Processing Service and Migration Dashboard send telemetry to Application Insights SDK via HTTPS (Port 443)
- System Operators query Log Analytics Workspace and view Application Insights Workbooks via Azure Portal / HTTPS (Port 443) / KQL

## Technology Stack
- Hybrid Cloud (Azure West Europe & On-Premise Mainframe) chosen to bridge legacy mainframe constraints with modern cloud capabilities.
- Java Spring Boot and React on Azure Container Apps chosen for scalable containerized microservices despite team's low cloud experience.
- Azure SQL Database chosen for managed relational persistence with TDS protocol support.
- Azure Service Bus chosen for reliable asynchronous messaging across the hybrid boundary.
- Azure Application Insights and Log Analytics Workspace chosen for zero-infrastructure APM, distributed tracing, and compliance auditing.
- Azure Active Directory (Entra ID) chosen for secure Single Sign-On (SSO) and RBAC integration.
- Terraform/Bicep chosen for Infrastructure-as-Code to prevent configuration drift.

## Rationale
[This hybrid architecture enables the incremental migration of claim types away from the expensive mainframe while strictly adhering to the 3-year coexistence mandate and zero-downtime constraints. Leveraging managed Azure services and robust observability mitigates risks associated with the team's low cloud experience and guarantees zero lost claims.]