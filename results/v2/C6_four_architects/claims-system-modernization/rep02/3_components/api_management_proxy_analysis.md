## Overview
[A hybrid cloud architecture that gradually modernizes a 30-year-old mainframe claims system using Azure and a Strangler Fig pattern. It ensures uninterrupted legacy batch processing while migrating claim types to a modern web platform.]

## Key Elements
- Web Portal (React on Azure Static Web Apps)
- Adjuster Workspace (React on Azure App Service)
- API Management Proxy (Azure API Management)
- Claims Processing Service (Java / Spring Boot on Azure Container Apps)
- Mainframe Integration Adapter (IBM MQ on-premises)
- Insurer's Active Directory (Azure AD / Entra ID)
- Legacy Mainframe (COBOL/DB2 on-premises)
- JWT Validation Component (APMS Validate-JWT policy)
- Claim Routing Evaluator (APMS Liquid templates)
- Mainframe Circuit Breaker (APMS Circuit Breaker policies)
- Payload Sanitization & Transformation Policy (APMS XSLT/Liquid policies)
- API Versioning & Deprecation Component (APMS Version Sets)

## Relationships
- Web Portal -> JWT Validation Component [HTTPS/OAuth2]
- Adjuster Workspace -> JWT Validation Component [HTTPS/OAuth2]
- JWT Validation Component -> API Versioning & Deprecation Component [Internal]
- API Versioning & Deprecation Component -> Claim Routing Evaluator [Internal]
- Claim Routing Evaluator -> Claims Processing Service [Internal mTLS]
- Claim Routing Evaluator -> Mainframe Circuit Breaker -> Payload Sanitization & Transformation Policy -> Mainframe Integration Adapter [mTLS/HTTPS]
- API Management Proxy -> Insurer's Active Directory [HTTPS]

## Technology Stack
- Azure API Management: API routing, security, and payload transformation to protect legacy interfaces.
- Azure Container Apps & Spring Boot: Scalable microservices for modern claims processing.
- IBM MQ: Reliable messaging for on-premises mainframe integration.
- Azure AD / Entra ID: Single Sign-On (SSO) security integration.
- React: Modern frontend framework for portals and adjuster workspace.

## Rationale
[This hybrid architecture isolates the fragile legacy mainframe using an API Management Proxy to handle traffic routing, payload transformation, and circuit breaking. It successfully meets all cloud-migration constraints while ensuring zero claim loss and rapid rollback capabilities.]