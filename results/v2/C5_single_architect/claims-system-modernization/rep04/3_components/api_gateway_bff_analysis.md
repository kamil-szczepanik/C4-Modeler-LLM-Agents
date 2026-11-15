## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe with a hybrid cloud solution. It enables online claim submission and adjuster workflows while ensuring data consistency and sub-two-second UI performance.

## Key Elements
* **Users:** Customers, Brokers, Claims Adjusters
* **External Systems:** Legacy Mainframe (COBOL/DB2), Active Directory, Azure API Management, Payment Gateway, Document Management System
* **Containers:** Claims Web Application (React, Azure Static Web Apps), API Gateway / BFF (Azure Container Apps, .NET Core), Migration Router / Anti-Corruption Layer (Azure Container Apps, .NET Core), Mainframe Integration Adapter (Azure Container Apps, .NET Core), Azure Service Bus, Azure Cache for Redis, Azure SQL Managed Instance
* **API Gateway / BFF Components:** Routing & Aggregation Controller (.NET Core / ASP.NET Web API), Authentication Middleware (.NET Core / Microsoft.Identity.Web), Response Caching & Transformation Service (.NET Core), Async Polling / WebSocket Notifier (.NET Core / SignalR)

## Relationships
* **Claims Web Application** -> **Authentication Middleware**: validates session via [HTTPS/OIDC]
* **Claims Web Application** -> **Async Polling / Notifier**: receives background updates via [WebSockets/WSS]
* **Routing & Aggregation Controller** -> **Azure Cache for Redis**: reads/writes UI state via [RESP]
* **Routing & Aggregation Controller** -> **Migration Router / ACL**: forwards domain requests via [HTTPS/REST]
* **Routing & Aggregation Controller** -> **Async Polling / Notifier**: dispatches async job statuses via [Internal Channel]
* **API Gateway / BFF** -> **Active Directory**: authenticates against [OIDC/OAuth2]

## Technology Stack
* **Azure Container Apps & .NET Core:** Chosen for the BFF and micro-services due to containerization flexibility and team maintainability.
* **Microsoft.Identity.Web:** Implements secure single sign-on with Azure Active Directory (R-07).
* **Azure Cache for Redis:** Provides fast caching to meet the sub-2s performance requirement (R-05) despite slow legacy backends.
* **SignalR (WebSockets):** Enables asynchronous notifications to prevent connection timeouts during long-running mainframe mutations.
* **React & Azure Static Web Apps:** Delivers a modern responsive frontend for customers and brokers (R-01) and claims adjusters (R-02).

## Rationale
This architecture successfully decouples the modern cloud UI from the slow, expensive-to-change COBOL mainframe using an Anti-Corruption Layer and asynchronous messaging. It satisfies strict migration, performance, and hybrid constraints while allowing gradual claim-type transitions.