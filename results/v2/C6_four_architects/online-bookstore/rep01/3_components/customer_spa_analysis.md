## Overview
The Customer SPA is a React-based single-page application that provides customers with a high-performance interface for browsing, purchasing, and reviewing books. It delivers resilient e-commerce capabilities optimized for global scalability and sub-2-second page loads.

## Key Elements
- Catalog Module: Handles book browsing and keyword search.
- Checkout & Cart Module: Manages shopping cart and secure checkout.
- Reviews & Ratings Module: Processes 5-star ratings and customer reviews.
- Recommendation Display Module: Renders "Customers also bought" suggestions.
- Auth Context Provider: Manages user authentication via OIDC.
- State Management Layer: Utilizes Zustand for local cart and UI state.
- API Client Layer: Centralizes requests using Axios with interceptors.
- Telemetry & Error Modules: Captures web vitals and implements React Error Boundaries.

## Relationships
- Customer -> Customer SPA: Interacts via browser for catalog browsing, checkout, and reviews [HTTPS].
- Customer SPA -> AWS API Gateway: Sends API requests for data and transactions [HTTPS/REST].
- Customer SPA -> Amazon Cognito: Authenticates users and manages tokens [HTTPS/OIDC].

## Technology Stack
- React & Vite: Chosen for modular component architecture and fast frontend bundling.
- Zustand: Selected for lightweight local state management of the shopping cart.
- Axios: Implemented as a centralized API client with request interceptors for JWTs and multi-currency headers.
- Amazon S3 & CloudFront: Deployed for static asset hosting and low-latency global delivery.

## Rationale
This architecture ensures sub-2-second performance on 3G networks through Vite code-splitting and static S3/CloudFront delivery. It guarantees high availability and fault tolerance via React Error Boundaries and centralized telemetry.