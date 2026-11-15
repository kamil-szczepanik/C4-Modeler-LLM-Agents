## Overview
The Self-Service Portal is a secure, high-performance web interface for the Library Management System, enabling patrons to catalogue items, manage loans, and settle fines. It complies with strict EU-only data residency requirements.

## Key Elements
* Library Patrons and Anonymous Visitors
* Self-Service Portal (React SPA hosted on Nginx)
* Routing & Layout Core Component (React Router)
* Catalogue Explorer Component (React)
* Patron Dashboard Component (React)
* Account & Fines Manager Component (React)
* State & API Client Module (Axios/Fetch)
* API Gateway (Kong/Envoy)
* EU Identity Provider & EU Payment Gateway

## Relationships
* Library Patrons & Anonymous Visitors -> Routing & Layout Core: Accesses unified SPA via HTTPS [TLS 1.3]
* Routing & Layout Core -> Catalogue Explorer, Patron Dashboard, Account & Fines Manager: Dynamically renders components [HTTPS]
* State & API Client Module -> API Gateway: Routes requests using HttpOnly cookies [HTTPS/JSON REST]
* API Gateway -> EU Identity Provider & EU Payment Gateway: Handles OAuth2/PKCE and fine settlements [HTTPS]

## Technology Stack
* React & Nginx: Frontend SPA and high-performance web server for responsive UI and immutable static asset delivery
* React Router: Manages shared application state, global navigation, and WCAG 2.1 AA accessibility compliance
* HttpOnly, Secure, SameSite=Strict Cookies: Mitigates XSS by preventing token storage in `localStorage`
* Content Security Policy (CSP) with Nonces: Blocks unauthorized script execution via Nginx header injection
* OAuth2 with PKCE: Secures authentication flow via the API Gateway

## Rationale
This architecture balances a seamless, accessible user journey with strict enterprise security by centralizing routing and isolating authentication state. Immutable artifact builds and robust Nginx caching ensure compliance with EU data residency and sub-800ms performance SLAs.