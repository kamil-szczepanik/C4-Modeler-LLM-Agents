## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with recommendations and reviews. The frontend architecture delivers high performance and strict compliance for global users.

## Key Elements
- **Router & Layout Component**: Manages client-side routing via React Router and global layout shells.
- **Catalog & Search View**: Renders product grids and search interfaces.
- **Checkout & Cart Manager**: Handles shopping cart state and secure checkout flows.
- **API Client Layer**: Axios-based abstraction layer for REST/GraphQL communication.
- **State Management Store**: Redux Toolkit / Zustand for localized client state caching and multi-currency preferences (USD, EUR, GBP).
- **Consent & Privacy Manager**: Captures user consent preferences to enforce GDPR and CCPA rights.
- **Auth & Session Handler**: Manages user session state and token refresh lifecycles securely in memory.
- **Code-Split Boundary / Lazy Loader**: Manages dynamic import chunks per route to minimize initial bundle size.

## Relationships
- **Frontend SPA** to **Amazon CloudFront / AWS S3**: Fetches static assets via **HTTPS**.
- **Frontend SPA** components to **BFF Container**: Communicates exclusively via **HTTPS/JSON** using the API Client Layer.
- **Auth & Session Handler** to **External Identity Provider**: Manages authentication tokens through the BFF container.

## Technology Stack
- **React & TypeScript**: Chosen for type safety and component reusability.
- **AWS S3 & Amazon CloudFront**: Selected for global low-latency static asset delivery (<2s page load).
- **Zustand / Redux Toolkit**: Utilized for performant client-side state management.
- **Axios**: Implemented for standardized HTTP communication.

## Rationale
This component architecture meets 3G performance constraints and scales to 1M MAU while mitigating XSS risks. It ensures strict GDPR/CCPA compliance and multi-currency support.