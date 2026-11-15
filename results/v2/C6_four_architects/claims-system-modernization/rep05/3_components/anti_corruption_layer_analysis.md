## Overview
[The system is a hybrid cloud Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based web application. Its core purpose is to enable online claims submission and adjuster workflows while maintaining seamless data consistency during a 3-year migration window.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Azure API Management (API Gateway / Edge)
- React on Azure Static Web Apps (Claims Web App)
- Java / Spring Boot on Azure App Service (Claims Core Service)
- Azure Functions (Anti-Corruption Layer with 5 internal components: Routing & Feature Flag Dispatcher, Async Event Translator, Model Transformer, State & Deduplication Ledger, Circuit Breaker & Fallback Policy)
- Azure SQL Database (Modern Claims Database)
- Azure Cache for Redis (Read-Through Cache)
- Azure Service Bus (Message Broker)
- On-Premise Integration Agent
- Legacy Mainframe (COBOL/DB2)
- Active Directory (Identity Provider)

## Relationships
- Customers & Brokers interact with Claims Web App via HTTPS
- Claims Adjusters interact with Claims Web App via HTTPS
- Claims Web App communicates with Claims Core Service via REST/HTTPS through Azure API Management
- Claims Core Service interacts with Anti-Corruption Layer (Routing & Feature Flag Dispatcher) via REST/HTTPS
- Message Broker communicates with Anti-Corruption Layer (Async Event Translator) via AMQP
- Anti-Corruption Layer communicates with On-Premise Integration Agent via gRPC over mutual TLS (mTLS)
- On-Premise Integration Agent communicates with Legacy Mainframe via proprietary legacy protocols
- Claims Core Service reads/writes Modern Claims Database via JDBC/SQL
- Claims Core Service utilizes Azure Cache for Redis via RESP
- Claims Core Service publishes events to Azure Service Bus via AMQP

## Technology Stack
- Azure App Service (Platform for Claims Core Service for managed scalability)
- Azure Functions (.NET 8 Isolated Worker / Java for serverless Anti-Corruption Layer execution)
- Azure SQL Database (Relational storage for modern claims data)
- Azure Service Bus (Asynchronous messaging for reliable event distribution)
- Azure Cosmos DB Serverless (State & Deduplication Ledger for tracking in-flight transactions)
- Resilience4j / Polly (.NET/Java resilience libraries embedded in Anti-Corruption Layer for circuit breaking)
- React on Azure Static Web Apps (Modern frontend for adjuster interface)

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies behind an Anti-Corruption Layer, ensuring the legacy system can remain the system of record without slowing down modern UI performance. Azure managed services provide high availability and scalability while accommodating the team's cloud skill level.]