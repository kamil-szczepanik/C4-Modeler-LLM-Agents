## Overview
The React Single-Page Application (SPA) serves as the primary user interface for the Online Bookstore, providing browsing, cart management, checkout, and review functionalities. It operates within a secure client-side trust boundary to deliver high-performance e-commerce interactions globally.

## Key Elements
- Router Component (React Router)
- Catalog & Search Module
- Checkout & Cart Module
- Recommendation & Review Module
- API Client Layer (Axios REST Client & Apollo GraphQL Client)
- State Management Store (Zustand)
- Infrastructure: Amazon S3, Amazon CloudFront, Amazon API Gateway

## Relationships
- React SPA -> Amazon CloudFront: Delivers static assets and enforces TLS 1.3 [HTTPS]
- API Client Layer -> Amazon API Gateway: Sends REST and GraphQL queries with JWT injection [HTTPS/REST and GraphQL]

## Technology Stack
- React: Frontend UI library chosen for component modularity and rapid state updates
- Zustand: Client-side state management for instant UI feedback without persisting PII locally
- Axios & Apollo Client: Split HTTP/GraphQL clients for optimized payload fetching on 3G networks
- Amazon S3 & CloudFront: Static hosting and global CDN distribution to ensure sub-2s page load times

## Rationale
This component architecture meets strict scalability, security, and performance constraints by decoupling client state, leveraging targeted GraphQL/REST APIs, and enforcing edge-level security. These decisions directly support global low-latency delivery, OWASP mitigations, and GDPR/CCPA compliance.