## Overview
- Single Page Application (SPA) built for an online bookstore providing secure catalogue browsing, cart management, and checkout.
- Designed to deliver high performance globally across AWS regions while maintaining strict security and compliance standards.

## Key Elements
- Shoppers / Customers and Book Publishers / Administrators
- React Single Page Application (SPA) container
- Routing & Shell Component (React, React Router)
- Catalogue & Search UI Component (React, Zustand)
- Checkout & Cart UI Component (React, React Hook Form)
- API Client Component (Axios / Fetch API)
- Localization & Session Context Provider (React Context)
- Telemetry & Analytics Wrapper
- AWS CloudFront and Amazon S3

## Relationships
- Shoppers and Administrators -> React SPA: Access via HTTPS
- React SPA -> AWS API Gateway & Edge Lambda: Sends API requests via HTTPS/JSON
- Routing & Shell -> Catalogue & Search UI & Checkout & Cart UI: Loads dynamically in-memory
- UI Components -> API Client Component: Communicates via TypeScript interfaces and async calls

## Technology Stack
- React: Powers the component-based user interface for optimal performance
- Amazon S3 & Amazon CloudFront: Delivers static assets globally with low latency
- Zustand & React Context: Manages client-side state and localization (USD, EUR, GBP)
- Terraform: Automates multi-region infrastructure deployment

## Rationale
- Component-based lazy loading ensures fast page loads meeting 3G performance targets.
- Strict client-side isolation and centralized telemetry sanitization guarantee GDPR and CCPA compliance.