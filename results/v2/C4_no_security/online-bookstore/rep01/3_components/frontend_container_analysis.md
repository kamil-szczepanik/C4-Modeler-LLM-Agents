## Overview
- Single-page application (SPA) providing an e-commerce interface for browsing, searching, and purchasing physical and electronic books globally.
- Architected for high scalability (1M MAU), strict availability (99.95%), and low latency (<2s page load on 3G).

## Key Elements
- **Frontend Container:** React and TypeScript SPA hosted on Amazon S3 and distributed via Amazon CloudFront.
- **Catalog & Search UI Module:** Handles book browsing, searching, and ratings/reviews display.
- **Checkout & Cart UI Module:** Manages multi-currency carts and secure checkout flows.
- **Recommendation Module:** Renders "Customers also bought" widgets.
- **Auth & Compliance Module:** Manages user sessions and GDPR/CCPA consent states.
- **API Client & State Layer:** Centralizes network calls via Axios/Apollo Client and global state via Zustand/React Context.

## Relationships
- **Guest Shopper, Registered Customer, Store Administrator, Customer Support Agent -> Frontend Container:** Interacts with application via HTTPS.
- **Frontend Container -> API Management:** Sends API requests using HTTPS via REST and GraphQL protocols.

## Technology Stack
- **React & TypeScript:** Core UI framework ensuring type safety and component reusability.
- **Zustand / React Context:** Manages cross-cutting client state like currency selection and consent flags.
- **Amazon S3 & CloudFront:** Hosts static assets and provides global edge caching.
- **AWS CloudWatch RUM & Sentry:** Tracks Core Web Vitals, business funnels, and client-side exceptions.

## Rationale
- Code-splitting modular React components guarantees fast page loads on 3G networks.
- Multi-region S3 and CloudFront deployments fulfill global availability and performance requirements.