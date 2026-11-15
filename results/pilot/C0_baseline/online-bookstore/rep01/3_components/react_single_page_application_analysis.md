## Overview
The React Single Page Application serves as the primary client-side user interface for the global online bookstore platform. It delivers responsive catalogue browsing, secure checkouts, and administrative operations across multiple currencies and regions.

## Key Elements
* Customers: End-users browsing books, managing carts, and submitting reviews
* Administrators: Internal users managing inventory, orders, and review moderation
* React SPA Container: Client-side application providing storefront and admin views
* Feature Modules: Catalogue, Cart, Checkout, and Administration domains
* Global CDN: Amazon CloudFront edge network with AWS WAF protection

## Relationships
* Customers -> React SPA: Accesses storefront via HTTPS (TLS 1.3), Amazon CloudFront, and AWS WAF
* Administrators -> React SPA: Manages platform operations via secure HTTPS connection
* React SPA -> ECS Fargate Go Microservices: Communicates for backend APIs via gRPC-Web over HTTPS

## Technology Stack
* React 18: Core UI framework with functional components and hooks for rapid rendering
* Redux Toolkit & React Query: Global state management for caching, persistence, and asynchronous data fetching
* React Router: Client-side routing enforcing strict separation between customer and admin views
* Tailwind CSS: Utility-first styling framework minimizing bundle size for rapid 3G mobile load times
* Amazon CloudFront & S3: Global static asset delivery and hosting across multi-region deployments
* DOMPurify: Sanitization library for preventing DOM-based XSS and prototype pollution

## Rationale
This architecture uses modular feature domains and lazy loading to achieve sub-2-second 3G page load performance. Client-side state management and secure gRPC-Web communication ensure a scalable, type-safe e-commerce experience meeting global availability and security requirements.