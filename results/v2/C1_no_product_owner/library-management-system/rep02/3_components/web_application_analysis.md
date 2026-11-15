## Overview
The Library Management System provides a cataloging, circulation, and self-service portal solution for libraries, meeting EU data residency constraints. The 'Web Application' container delivers responsive user interfaces for patrons and staff.

## Key Elements
* **Router/View Controller**: Manages client-side routing and page views using React Router.
* **Catalog Component**: UI modules for searching and viewing physical and digital items.
* **Circulation Component**: UI modules for managing checkouts, returns, and renewals.
* **Authentication Client**: Handles login flows and OIDC token validation.
* **API Client**: Encapsulates communication with the API Gateway.
* **State Management Component**: Manages transient application state in memory (Zustand/React Context).

## Relationships
* **Library Staff / Patrons** -> **Web Application**: Accesses via HTTPS/REST.
* **Catalog & Circulation Components** -> **State Management Component**: Interacts for transient state management.
* **Catalog & Circulation Components** -> **API Client**: Queries the API Gateway via HTTPS/REST.
* **Authentication Client** -> **Identity Provider**: Manages session tokens via OAuth2/OIDC over HTTPS.

## Technology Stack
* **React & TypeScript**: Chosen for building a responsive, strongly typed single-page application and UI components.
* **EU-based CDN**: Hosts static assets to enforce EU-only data residency and performance targets.
* **HttpOnly, SameSite=Strict Cookies**: Secures session tokens against XSS.
* **Zustand / React Context**: Manages memory-only transient state.

## Rationale
This component architecture separates routing, state, and feature domains while enforcing strict security controls like CSP and HttpOnly cookies. It ensures high performance (<800ms search NFR) and EU data residency compliance via CDN hosting.