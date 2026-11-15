## Overview
The Online Bookstore SPA is a high-performance React application hosted on Amazon CloudFront and S3 that delivers secure, lightning-fast shopping and administrative interfaces. It is architected to support 1 million monthly active users globally while ensuring strict compliance with security, privacy, and accessibility standards.

## Key Elements
- **Single Page Application (SPA)**: React, TypeScript client-side application.
- **Catalog & Search UI Component**: React, TypeScript for product browsing and keyword search.
- **Checkout & Cart UI Component**: React, TypeScript for cart management and secure checkout.
- **Recommendation & Review UI Component**: React, TypeScript for ratings, reviews, and recommendations.
- **Admin Management UI Component**: React, TypeScript lazily-loaded module for store administration.
- **API Client & Auth Component**: Axios, OpenID Connect SDK for secure communication.
- **Infrastructure**: Amazon CloudFront, Amazon S3, AWS global regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
- **External Systems**: Identity Provider (IdP), Amazon API Gateway.

## Relationships
- Customer / Store Administrator -> Single Page Application (SPA): Interacts via [HTTPS/TLS].
- Catalog, Checkout, Recommendation, & Admin UI Components -> API Client & Auth Component: Internal modular calls.
- API Client & Auth Component -> Identity Provider (IdP): Authenticates via [OAuth 2.0 / PKCE].
- API Client & Auth Component -> Amazon API Gateway: Sends API requests via [HTTPS/TLS 1.3].

## Technology Stack
- **React & TypeScript**: Chosen for type safety, component reusability, and rich ecosystem support.
- **Amazon CloudFront & S3**: Selected for zero-downtime global distribution and sub-2-second page loads.
- **OAuth 2.0 with PKCE & In-Memory Tokens**: Implemented for robust client-side security against XSS.
- **Axios & OpenID Connect SDK**: Utilized for standardized API communication and authentication flows.

## Rationale
This architecture uses a React SPA backed by global CDN distribution to ensure low-latency performance and high scalability for 1M MAU. Modular code-splitting and strict token-handling protocols protect customer experience, bundle performance, and data security.