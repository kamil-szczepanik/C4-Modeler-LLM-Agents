## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce web application designed for global retail operations, handling millions of users while maintaining strict security, privacy, and performance standards. It provides a React single-page frontend container that delivers a responsive user experience for browsing, purchasing, reviewing, and receiving book recommendations.

## Key Elements
* Routing & Shell Component (React, React Router)
* Catalog & Search Component
* Cart & Checkout Component
* Recommendation & Review Component
* Auth & Profile Component
* API Client & Interceptor Component (Axios)
* Localization & Currency Component (i18next)
* Amazon S3 & Amazon CloudFront
* Amazon API Gateway

## Relationships
* Customer / Store Administrator -> Amazon CloudFront: Browses catalogue and manages store [HTTPS]
* Amazon CloudFront -> Amazon S3: Serves static frontend assets [HTTPS]
* React Single Page Application -> Amazon API Gateway: Sends data queries and mutations [HTTPS/JSON]
* Internal Components -> API Client & Interceptor Component: Routes outbound traffic exclusively [In-memory]

## Technology Stack
* React & Vite: Chosen for fast bundling, lazy loading, and sub-2-second 3G page load performance.
* Zustand / Redux Toolkit: Provides lightweight, predictable client-side state management.
* i18next: Handles multi-currency display (USD, EUR, GBP) and client-side translation dictionaries.
* Axios: Centralizes HTTP requests, token injection, and OWASP security headers.

## Rationale
This architecture cleanly separates user interface concerns while enforcing strict security boundaries through a single API gateway egress point. The modular frontend design ensures high performance, maintainability, and multi-currency compliance globally across AWS regions.