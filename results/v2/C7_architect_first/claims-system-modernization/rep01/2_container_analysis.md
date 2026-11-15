## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native platform on Azure. It ensures continuous hybrid operations while migrating claim types incrementally over a three-year period.

## Key Elements
* Claims Web Application (React, TypeScript)
* API Gateway / Backend-for-Frontend (BFF) (.NET Core)
* Claims Processing Service (.NET Core, Azure Container Apps)
* Integration & Anti-Corruption Layer (Azure Functions, Azure Service Bus)
* Claims Database (Azure SQL)
* Configuration & Feature Store (Azure App Configuration)
* Security & Observability (Azure Key Vault, Azure Monitor, Azure WAF)

## Relationships
* Users to Claims Web Application via HTTPS/JSON
* Claims Web Application to API Gateway/BFF via HTTPS/JSON (OIDC/JWT)
* API Gateway/BFF to Claims Processing Service and Configuration Store via HTTPS/gRPC
* Claims Processing Service to Claims Database via TDS/SQL
* Integration & Anti-Corruption Layer to Mainframe via mTLS/AMQP

## Technology Stack
* Frontend: Azure Static Web Apps with React for fast client-side rendering
* Backend & Compute: .NET Core on Azure Container Apps and Azure Functions for scalable business logic
* Database: Azure SQL with Transparent Data Encryption (TDE) for structured claim data
* Messaging & Integration: Azure Service Bus with AMQP for asynchronous hybrid synchronization
* Security: Azure Active Directory (Entra ID), Azure Key Vault, and Azure WAF for robust protection
* Configuration: Azure App Configuration for dynamic feature flagging and routing

## Rationale
This hybrid architecture decouples modern sub-second user experiences from slow mainframe responses while preserving the system of record. It satisfies strict fallback and consistency requirements through an asynchronous Anti-Corruption Layer and managed Azure components tailored for a team with limited cloud experience.