## Overview
- Single-Page Application for the online bookstore providing global access, catalogue browsing, and secure checkout.
- Built with React, Amazon S3, and Amazon CloudFront to satisfy performance and scalability constraints.

## Key Elements
- Routing & Shell Component (`React Router`)
- State Management Component (`Redux Toolkit / React Query`)
- API Client Component (`Axios / Fetch wrapper`)
- Error Boundary Component (`React Error Boundary`)
- Localization & Currency Component (`i18next`)

## Relationships
- Routing & Shell Component renders State Management Component, API Client Component, Error Boundary Component, and Localization & Currency Component [In-memory]
- API Client Component interacts with AWS API Gateway [HTTPS (TLS 1.3)]
- Single-Page Application assets served globally via Amazon CloudFront [HTTPS (TLS 1.3)]

## Technology Stack
- React: Core UI framework for component-based architecture and rendering
- Amazon S3: Static asset storage for immutable build artifacts
- Amazon CloudFront: Global CDN for low-latency edge delivery and cache invalidation
- React Router: Client-side routing and route-based code splitting
- Redux Toolkit / React Query: Client-side caching and state synchronization
- i18next: Multi-currency and multi-language internationalization

## Rationale
- Component modularization and aggressive code-splitting ensure page loads remain under 2 seconds on 3G networks.
- Strict security controls, token handling, and error boundaries protect revenue-critical checkout flows and user data globally.