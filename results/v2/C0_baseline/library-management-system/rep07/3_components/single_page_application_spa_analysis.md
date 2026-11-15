## Overview
• Single Page Application (SPA) providing self-service patron portals and staff circulation workflows for the Library Management System.
• Centralizes user interactions while adhering strictly to EU data residency and WCAG 2.1 AA accessibility mandates.

## Key Elements
• Library Patrons, Librarians/Circulation Staff, Library Administrators
• Single Page Application (SPA) Container
• Routing & Authentication Module
• Catalog & Search Component
• Circulation & Admin Workspace
• API Client Layer (HTTP Interceptor) & State/Cache Manager
• API Gateway

## Relationships
• Library Patrons/Staff/Administrators -> Single Page Application (SPA): Interacts with portal and workspace via `[HTTPS/REST]`
• Single Page Application (SPA) -> API Gateway: Sends user requests and proxies session handling via `[HTTPS/REST/JSON]`
• Nginx Container -> Client Browser: Delivers static assets using `[HTTPS/TLS 1.3]` with EU-only edge pinning

## Technology Stack
• React with TypeScript: Core frontend library for building type-safe, component-driven user interfaces.
• Nginx: High-performance web server for serving static assets and enforcing Content Security Policy (CSP) headers.
• Docker & Global CDN: Immutable containerization and EU-pinned edge nodes for deployment and data residency compliance.

## Rationale
• The decoupled React/TypeScript architecture isolates high-frequency search input to help achieve the sub-800ms performance NFR.
• Centralizing security controls and API interactions ensures robust XSS mitigation, strict token handling, and EU data residency compliance.