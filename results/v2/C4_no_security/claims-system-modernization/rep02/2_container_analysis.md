## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims platform with a modern hybrid cloud solution. It enables online claims submission and adjuster management while maintaining continuous operations and zero data loss.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- External Systems: Active Directory / Azure AD, Mainframe COBOL/DB2 System
- Web Application Container (React/Node.js on Azure App Service)
- API Gateway / Integration Container (Azure API Management)
- Claims Core Service Container (Azure Container Apps)
- Data & Caching Container (Azure Cosmos DB + Redis)
- Mainframe Adapter Container (Azure Service Bus with Dead Letter Queues)
- Configuration: Azure App Configuration

## Relationships
- Customers / Brokers interact with the Web Application Container via HTTPS
- Claims Adjusters interact with the Web Application Container via HTTPS, authenticated via Single Sign-On with Active Directory / Azure AD
- Web Application Container communicates with API Gateway via HTTPS / REST
- API Gateway routes requests dynamically using Azure App Configuration to either Claims Core Service or Mainframe COBOL/DB2 System
- Claims Core Service persists data in Azure Cosmos DB and caches read models in Redis via TCP/TLS
- Mainframe Adapter Container bridges Azure Service Bus asynchronously with the on-premise mainframe during the 23:00-05:00 batch window

## Technology Stack
- Azure App Service: Hosts the React/Node.js frontend for scalability and managed operations
- Azure API Management: Acts as anti-corruption layer, API gateway, and enforces circuit breakers for mainframe batch protection
- Azure Container Apps: Simplifies Kubernetes complexity for the Java/Spring Boot Claims Core Service given the team's low cloud experience
- Azure Cosmos DB & Redis: Provides persistent storage and low-latency state caching to guarantee sub-2-second adjuster screens
- Azure Service Bus: Asynchronous messaging with Dead Letter Queues to guarantee zero lost claims (R-04)
- Azure App Configuration: Implements feature flags for the 1-day claim type rollback requirement (R-06)

## Rationale
This hybrid architecture decouples sluggish mainframe responses from the new user interface, meeting strict performance and maintainability requirements. Utilizing managed Azure services minimizes operational complexity for a cloud-novice team while securely bridging legacy systems.