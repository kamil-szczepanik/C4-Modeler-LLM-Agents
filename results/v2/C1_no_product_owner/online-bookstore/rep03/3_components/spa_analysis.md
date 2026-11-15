## Overview
The Online Bookstore SPA is a high-performance React application serving as the primary customer and admin interface for a global e-commerce platform. It enables scalable catalogue browsing, secure checkout, reviews, and personalized book recommendations while maintaining strict security and compliance.

## Key Elements
- **Users**: Customer, Admin / Support Staff
- **SPA Container**: React, TypeScript, Amazon CloudFront, Amazon S3
- **SPA Components**: Router / Navigation Component (React Router), State Management Store (Zustand), API Client Service (Axios, TanStack Query, Zod), Feature Views (Catalog, Cart, Reviews, Recommendations), Design System (Tailwind CSS), Security Monitoring Component
- **External Systems**: API Gateway, Payment Gateway, Shipping Provider APIs, Tax & Compliance Service, Identity & Access Management, Notification Service

## Relationships
- Customer -> SPA: Browses bookstore, manages account, and makes purchases [HTTPS / TLS 1.3]
- Admin / Support Staff -> SPA: Manages bookstore operations and support [HTTPS / TLS 1.3]
- SPA -> API Gateway: Sends API requests for data and actions [HTTPS/WSS]

## Technology Stack
- **Frontend Framework**: React with TypeScript for type-safe UI development
- **Build & Hosting**: Amazon S3 and Amazon CloudFront for static asset distribution across regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`)
- **State & Data Fetching**: Zustand for ephemeral client state and TanStack Query for API caching and synchronization
- **Validation & Styling**: Zod for input schema validation and Tailwind CSS for the design system

## Rationale
This component architecture uses static hosting behind CloudFront to ensure sub-2-second page loads on 3G and global scalability for 1M MAU. Strict security controls, including HTTP-only cookies and Zod validation, mitigate OWASP Top-10 risks while ensuring GDPR and CCPA compliance.