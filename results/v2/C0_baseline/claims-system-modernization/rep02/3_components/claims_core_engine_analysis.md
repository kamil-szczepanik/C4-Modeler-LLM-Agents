## Overview
• Modernizes a 30-year-old mainframe claims system via a hybrid cloud platform processing claims incrementally.
• Replaces legacy workflows using microservices while maintaining business continuity with the legacy system of record.

## Key Elements
• Claims Core Engine (Java, Spring Boot, Azure Container Apps)
• Claim Processing Service (Spring MVC/WebFlux)
• Anti-Corruption Layer (ACL) Component
• Parameterized Business Rules (Azure SQL)
• Event Publisher Component (Spring Cloud Stream)
• External Systems: Legacy Mainframe, Microsoft Entra ID, Azure Service Bus, Azure SQL Database

## Relationships
• Claim Processing Service -> Microsoft Entra ID: Validates OAuth2/OIDC JWT tokens [HTTPS]
• Claims Core Engine -> Azure SQL Database: Manages stateless transactions and parameterized rules [TDS over TLS 1.3]
• Anti-Corruption Layer -> Legacy Mainframe: Transmits tokenized payloads [Azure ExpressRoute with IPsec VPN, mTLS]
• Event Publisher -> Azure Service Bus Topics: Publishes fine-grained domain audit events [AMQP over TLS]

## Technology Stack
• Java / Spring Boot: Core runtime framework for the microservice
• Azure Container Apps: Scalable container hosting platform utilizing KEDA and blue/green revisions
• Azure SQL Database: Relational storage providing transactional guarantees and parameterized business rules
• Azure Service Bus Topics: Asynchronous event streaming for domain audit events
• Resilience4j: Provides circuit breaking and resiliency policies for legacy integration

## Rationale
• Utilizes a stateless, microservice-based architecture on Azure to overcome the team's limited cloud experience while ensuring rapid rollbacks and zero data loss.
• Implements strict security controls and an Anti-Corruption Layer to safely bridge modern cloud components with the legacy mainframe.