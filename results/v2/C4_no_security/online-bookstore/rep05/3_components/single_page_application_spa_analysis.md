## Overview
The Online Bookstore SPA is a high-performance React application designed to provide global customers with fast catalogue browsing, recommendations, and secure checkout. It is hosted globally on AWS to serve 1M MAU while meeting strict performance and security constraints.

## Key Elements
- **Router Component**: React Router managing client-side navigation and lazy loading.
- **Authentication & User Context Component**: Handles JWT tokens and role-based access.
- **Catalog & Search UI Component**: Renders book search and recommendation widgets.
- **Cart & Checkout UI Component**: Manages local cart state and multi-step checkout.
- **API Client Component**: Encapsulates HTTPS/REST and WebSocket communication.

## Relationships
- **Router Component** -> **Catalog & Search UI Component**: Lazy-loads catalogue views [Client-side routing]
- **Router Component** -> **Cart & Checkout UI Component**: Lazy-loads checkout workflows [Client-side routing]
- **Catalog & Search UI Component** -> **API Client Component**: Requests book data and search indices [Internal method call]
- **Cart & Checkout UI Component** -> **API Client Component**: Sends cart mutations and orders [Internal method call]
- **API Client Component** -> **AWS API Gateway & Load Balancer**: Communicates via HTTPS/REST and WebSockets [TLS 1.3]

## Technology Stack
- **React & TypeScript**: Chosen for robust type safety and component reusability.
- **AWS CloudFront & S3**: Selected to deliver static assets globally with sub-2s load times.
- **W3C Trace Context**: Used for distributed tracing across frontend and backend services.

## Rationale
This component architecture enforces strict code-splitting to guarantee sub-2s page loads on 3G connections. Isolating transport logic within the API Client ensures resilient multi-currency transactions and high availability.