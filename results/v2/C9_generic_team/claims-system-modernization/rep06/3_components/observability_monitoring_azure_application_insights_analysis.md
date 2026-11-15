## Overview
The system is a hybrid insurance claims modernization platform designed to gradually replace a legacy mainframe while maintaining continuous claims processing. It provides online submission and adjuster management capabilities while ensuring data consistency and low latency.

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- On-Premise COBOL/DB2 Mainframe (System of Record)
- On-Premise Active Directory (Identity Provider)
- Azure App Service containers (Web SPA, BFF, Claim Management Core, ACL, Feature Flag Service)
- Azure Service Bus (Message Broker)
- Azure Application Insights (Observability / Monitoring)

## Relationships
- Customers/Brokers interact with Web SPA via HTTPS
- Claims Adjusters interact with Web Application via HTTPS
- Web SPA and BFF communicate via HTTPS / REST
- BFF and Claim Management Core communicate via Azure Service Bus (AMQP)
- Anti-Corruption Layer (ACL) communicates with On-Premise COBOL/DB2 Mainframe via Secure Mainframe Protocols
- Backend containers emit telemetry to Azure Application Insights via HTTPS / W3C Trace Context

## Technology Stack
- Azure App Service: Hosts containerized microservices and backend components for scalable cloud execution
- Azure Service Bus: Asynchronous message broker ensuring reliable, decoupled event processing across containers
- Azure Application Insights: Centralized observability platform providing distributed tracing, structured logging, and automated alerting
- W3C Trace Context: Standardized protocol injected into HTTP headers for end-to-end distributed tracing across hybrid boundaries
- Kusto Query Language (KQL): Version-controlled query templates for rapid triage and operational monitoring

## Rationale
The hybrid architecture allows gradual claim-type migration off the expensive legacy mainframe while maintaining a 3-year system-of-record constraint. Azure App Service and Application Insights provide the necessary cloud observability and rapid fallback capabilities required for a team with limited cloud experience.