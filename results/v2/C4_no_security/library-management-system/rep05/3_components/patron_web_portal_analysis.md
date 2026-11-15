## Overview
The Patron Web Portal provides public and academic library patrons with a self-service interface for catalog discovery, account management, and real-time notifications. It ensures EU data residency compliance and meets performance targets for item search.

## Key Elements
* Library Patrons (Users)
* Patron Web Portal Container (React, Nginx)
* Routing & Shell Layout Component (React Router)
* Catalog Search & Discovery Component (React)
* Patron Account Dashboard Component (React)
* Auth & Session Management Component (React, OAuth2/OIDC SDK, Consent Management Sub-component)
* Notification Center Component (React)
* API Client Service Component (TypeScript, Axios)
* Core API Gateway (Spring Cloud Gateway)
* Centralized Observability Platform

## Relationships
* Library Patrons -> Patron Web Portal: Accesses self-service catalog and account features [HTTPS]
* Patron Web Portal -> Core API Gateway: Sends API requests for catalog and account actions [HTTPS REST/GraphQL]
* Patron Web Portal -> Centralized Observability Platform: Ships telemetry and logs [HTTP/OTel Exporter]

## Technology Stack
* React & TypeScript: Frontend UI development for component modularity and type safety
* Nginx: Static asset serving and reverse proxy for telemetry
* OAuth2/OIDC SDK & HttpOnly Cookies: Secure authentication and session management
* W3C Trace Context & Axios: Distributed tracing and centralized HTTP communication

## Rationale
This architecture decouples the frontend to guarantee rapid, responsive patron self-service while enforcing strict EU data residency and security constraints. Centralized API handling and telemetry ensure high observability to meet the sub-800ms search performance requirement.