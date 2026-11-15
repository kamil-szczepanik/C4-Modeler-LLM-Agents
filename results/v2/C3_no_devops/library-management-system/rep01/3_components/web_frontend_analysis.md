## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets strict performance targets.

## Key Elements
* Library Patrons, Librarians / Circulation Staff, Library Administrators
* Web Frontend (React/TypeScript SPA with PWA capabilities)
* API Gateway (Kong or Nginx)
* Core Business Service, Search Service (Elasticsearch), Database (PostgreSQL)
* Identity Provider, Payment Gateway, Notification Service

## Relationships
* Library Patrons -> Web Frontend: Accesses self-service portals [HTTPS (TLS 1.3)]
* Librarians / Staff -> Web Frontend: Manages inventory and circulation [HTTPS (TLS 1.3)]
* Administrators -> Web Frontend: Handles reporting and compliance [HTTPS (TLS 1.3)]
* Web Frontend -> API Gateway: Sends API requests [HTTPS/REST]

## Technology Stack
* React/TypeScript: Powers the frontend SPA with role-based modules
* EU-Region CDN: Hosts static assets and enforces strict CSP/HSTS and TLS 1.3
* TanStack Query: Provides client-side state caching to meet sub-800ms search performance
* Service Worker: Manages offline PWA caching for public static assets only

## Rationale
This architecture ensures secure, low-latency access while strictly enforcing EU data residency constraints. Client-side caching and PWA capabilities meet performance goals without compromising patron data security.