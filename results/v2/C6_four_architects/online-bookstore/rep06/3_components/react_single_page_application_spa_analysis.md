## Overview
This architecture defines a high-performance, globally distributed React Single-Page Application (SPA) for an online bookstore. It ensures rapid global page loads, secure client-side state management, and strict compliance with privacy regulations.

## Key Elements
- Routing & Shell Component (React Router, Vite)
- Catalogue & Search View (React, Zustand)
- Checkout & Cart Workflow Component
- Recommendation & Review Widget
- Localization & Currency Context
- API Client Service (TanStack React Query, Axios)
- AWS CloudFront & Amazon S3 (Edge Delivery)
- AWS API Gateway (Backend Interface)

## Relationships
- Routing & Shell -> Catalogue View, Checkout Workflow, Recommendation Widget (React props/context)
- Feature Components -> API Client Service (Function invocation / REST wrapper)
- API Client Service -> AWS API Gateway ([HTTPS/REST])
- AWS CloudFront -> Amazon S3 ([HTTPS])

## Technology Stack
- React: Core UI framework for component-based architecture
- Vite: Fast frontend build tool and bundler for optimized assets
- Zustand: Lightweight state management for client and auth state
- TanStack React Query: Server-state caching to optimize performance
- AWS CloudFront & S3: Global content delivery and static hosting for low latency

## Rationale
The component decomposition and TanStack React Query caching guarantee a sub-2-second page load on 3G connections. Memory-only token management via Zustand directly addresses OWASP Top-10 security and GDPR/CCPA privacy constraints.