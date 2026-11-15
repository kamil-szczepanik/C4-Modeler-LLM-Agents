## Overview
The Web Application (SPA) is a React-based frontend providing a self-service portal and catalog management interface for library patrons and staff. It delivers performant, role-based workflows while complying with EU data residency by avoiding local PII storage.

## Key Elements
* **Routing & Layout Manager**: React Router
* **Authentication State Module**: React Context, Zustand, OIDC Client
* **Catalogue & Search Module**: React UI components
* **Circulation & Self-Service Portal**: React workflows for loans, renewals, and fines
* **API Client Layer**: Axios, Fetch API, TanStack Query

## Relationships
* **Patron / Librarian & Staff** -> **Web Application (SPA)**: Interacts with the application [HTTPS]
* **Authentication State Module** -> **Identity Provider**: OpenID Connect / OAuth 2.0 [HTTPS]
* **Catalogue & Search Module** & **Circulation & Self-Service Portal** -> **API Client Layer**: Invokes queries and mutations [In-memory / TypeScript imports]
* **API Client Layer** -> **API Gateway**: REST/JSON [HTTPS]

## Technology Stack
* **React & TypeScript**: Core UI library and type safety for maintainability
* **Nginx**: Web server for static asset delivery
* **Zustand & React Context**: Client-side state and authentication management
* **TanStack Query**: HTTP request caching, retry logic, and deduplication to meet performance targets
* **OIDC Client**: Secure token exchange without persistent local PII storage

## Rationale
This component architecture separates routing, authentication, and API handling to optimize client-side performance and meet the sub-800ms search requirement. Isolating authentication ensures strict adherence to EU data residency constraints.