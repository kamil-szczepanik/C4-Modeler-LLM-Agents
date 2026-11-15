## Overview
The Insurance Claims Modernization platform gradually replaces a legacy COBOL/DB2 mainframe system with a modern hybrid cloud solution. It enables online claim submission, adjuster web workflows, and incremental claim type migration over a 3-year period.

## Key Elements
* Customers & Brokers (Users)
* Claims Adjusters (Users)
* Claims Web Application (React, Azure Static Web Apps)
* API Gateway / BFF (Azure Container Apps, .NET Core)
* Migration Router / Anti-Corruption Layer (Azure Container Apps, .NET Core)
* Mainframe Integration Adapter (Azure Container Apps, .NET Core)
* Azure Service Bus (Messaging Container)
* Azure Cache for Redis (Caching Container)
* Database (Azure SQL Managed Instance)
* Legacy Mainframe (COBOL/DB2, On-Premise)
* Active Directory (Identity Provider)

## Relationships
* Customers & Brokers interact with Claims Web Application via HTTPS
* Claims Adjusters interact with Claims Web Application via HTTPS
* Claims Web Application interacts with API Gateway / BFF via HTTPS/REST
* API Gateway / BFF interacts with Azure Cache for Redis via RESP
* API Gateway / BFF interacts with Migration Router / Anti-Corruption Layer via HTTPS/REST
* Migration Router / Anti-Corruption Layer interacts with Azure SQL Managed Instance via TDS
* Migration Router / Anti-Corruption Layer interacts with Azure Service Bus via AMQP/HTTPS
* Azure Service Bus interacts with Mainframe Integration Adapter via AMQP/HTTPS
* Mainframe Integration Adapter interacts with Legacy Mainframe via TCP/MQ or SFTP
* Claims Web Application and BFF authenticate against Active Directory via OIDC/OAuth2

## Technology Stack
* Azure Static Web Apps / React: Hosts and powers the modern web frontend for ease of deployment.
* Azure Container Apps / .NET Core: Runs microservices (BFF, Router, Adapter) to match the team's skillset.
* Azure SQL Managed Instance: Stores modern claim data with strong consistency guarantees (R-04).
* Azure Service Bus: Decouples systems and buffers messages to respect the quarterly mainframe change constraint.
* Azure Cache for Redis: Caches slow data to achieve sub-2s adjuster screen loads (R-05).

## Rationale
This hybrid architecture isolates rigid legacy mainframe constraints behind an Anti-Corruption Layer and asynchronous messaging, strictly limiting expensive mainframe modifications. Furthermore, it leverages managed Azure services to accommodate the team's limited cloud experience while meeting strict performance, consistency, and rollback requirements.