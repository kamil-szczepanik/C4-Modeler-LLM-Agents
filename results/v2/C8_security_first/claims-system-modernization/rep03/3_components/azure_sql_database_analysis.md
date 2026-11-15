## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old mainframe platform with a modern cloud-native solution while ensuring continuous business operations. It provides online claim submission for users and a high-performance web interface for adjusters.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Legacy Mainframe System
- Azure Active Directory (Entra ID)
- Azure API Gateway with Rate Limiter
- Customer Portal & Adjuster Web Apps (Azure Static Web Apps)
- Claim Management API & Claim Router / ACL & Audit Service (Azure Container Apps, .NET 8)
- Azure Service Bus
- Azure SQL Database

## Relationships
- Customers & Brokers -> Customer Portal [HTTPS]
- Claims Adjusters -> Adjuster Web Apps [HTTPS]
- Customer Portal & Adjuster Web Apps -> Azure API Gateway [HTTPS/REST]
- Azure API Gateway -> Claim Management API [HTTPS/REST]
- Claim Management API -> Claim Router / ACL [AMQP / Azure Service Bus]
- Claim Router / ACL -> Legacy Mainframe System [Batch / File Transfer]
- Claim Management API & Audit Service -> Azure SQL Database [Entity Framework Core / TDS]
- Claim Management API -> Azure Active Directory [OpenID Connect / OAuth 2.0]

## Technology Stack
- Azure SQL Database: Relational data store featuring Temporal Tables, CDC, and Serverless compute tier for elasticity and audit tracking.
- Azure Container Apps: Container hosting platform using .NET 8 for microservices without deep cloud expertise required.
- Azure Service Bus: Enterprise messaging broker ensuring reliable asynchronous processing between modern and legacy boundaries.
- Azure Static Web Apps: Globally distributed hosting for single-page adjuster and customer portals.
- Azure Active Directory (Entra ID): Centralized identity provider enforcing secure Single Sign-On (SSO).

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies while introducing scalable cloud components to meet strict performance and consistency goals. It enables gradual claim type migration with rapid fallback capabilities suited for a team with limited cloud experience.]