## Overview
The Online Bookstore Single-Page Application (SPA) provides a secure, accessible, and high-performance e-commerce user interface for browsing catalogs, managing carts, and processing multi-currency checkouts. It leverages modern frontend modularization and AWS edge services to serve a global user base while meeting strict security and compliance mandates.

## Key Elements
* Routing & Shell Component (React Router, React `lazy`, `Suspense`)
* Catalog & Search Component (React, local caching, accessibility features)
* Cart & Checkout Component (Zustand/React Context, multi-currency support)
* Recommendations & Reviews Component (React UI modules)
* Auth & Profile Component (AWS Cognito integration)
* Centralized API Client Module (fetch-based with interceptors)
* CloudFront Functions / Lambda@Edge (Edge computing)

## Relationships
* Customer -> Amazon CloudFront: Accesses SPA assets via HTTPS/TLS 1.3
* SPA -> Amazon API Gateway: Communicates via HTTPS/REST and WebSockets
* SPA -> AWS Cognito: Manages authentication and secure session tokens
* CloudFront -> AWS S3: Retrieves static frontend assets via Origin Access Control (OAC)

## Technology Stack
* React & TypeScript: Core frontend framework for type-safe component development
* Amazon CloudFront & AWS S3: Global content distribution and static asset hosting for sub-2s 3G page loads
* Zustand / React Context: Lightweight state management for transient UI and cart states without PII leaks
* AWS Cognito: Secure user authentication, RBAC, and HTTP-only cookie session management
* GitHub Actions: Automated CI/CD pipeline with atomic S3 deployments and cache-busting

## Rationale
This architecture decouples the React frontend from backend microservices via Amazon API Gateway, ensuring scalability for 1M MAU. Utilizing Amazon CloudFront edge caching, code splitting, and strict CSP headers achieves both the sub-2-second 3G load requirement and rigorous OWASP Top-10 security postures.