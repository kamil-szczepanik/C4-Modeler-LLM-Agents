## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure cloud platform for a regional insurer. The Integration / ACL Service acts as an Anti-Corruption Layer, enabling seamless hybrid claims processing and incremental type migration.]

## Key Elements
* Mainframe Translator Component (.NET, Serviceakami copybook parsers)
* Sync Orchestrator Component (.NET Hosted Service, Serilog)
* Circuit Breaker & Fallback Component (Polly for .NET)
* Audit Logger Sub-component (Azure Monitor / Log Analytics)
* Infrastructure & Security (Azure Container Apps, Azure Service Bus, Azure Key Vault, Azure Database for PostgreSQL)

## Relationships
* Integration / ACL Service -> Legacy Mainframe System: Communicates via mTLS over IPsec VPN / Azure ExpressRoute
* Integration / ACL Service -> Azure Database for PostgreSQL: Synchronizes claim data via Entity Framework Core and Azure Managed Identities
* Integration / ACL Service -> Azure Service Bus: Publishes and consumes asynchronous messages using transport-level security
* GitHub Actions CI/CD Pipeline -> Mainframe Mocking Harness: Executes automated regression testing without live VPN connectivity

## Technology Stack
* .NET: Core framework for high performance and team familiarity given limited cloud experience
* Azure Container Apps: Serverless container hosting supporting blue-green deployments for 1-day fallback (R-06)
* Polly for .NET: Circuit breaker and retry policies to isolate 5-second mainframe latency (R-05)
* Azure Service Bus & PostgreSQL: Asynchronous messaging and relational persistence for consistency (R-04)
* Azure Key Vault: Secure runtime injection of mainframe gateway credentials

## Rationale
[This component-level architecture balances the strict 3-year hybrid migration constraint and limited team cloud experience by leveraging robust .NET resilience libraries and native Azure services. It protects business continuity through automated circuit breaking, strict schema translation, and dedicated operational safeguards.]