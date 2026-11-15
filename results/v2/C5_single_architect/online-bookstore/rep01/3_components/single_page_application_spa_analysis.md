## Overview
The Online Bookstore SPA is a React-based single-page application providing customer-facing e-commerce features like catalog browsing, cart management, and checkout. It ensures high performance and security while interacting with backend microservices via an API gateway.

## Key Elements
- **Router / Shell**: Manages client-side routing, global context, and layouts using React Router and Context API.
- **Catalog & Search View**: Renders book grids, filters, and keyword search using React and TanStack Query.
- **Cart & Checkout View**: Manages shopping cart state and checkout workflows using React and Zustand.
- **Reviews & Ratings Widget**: Handles 5-star submissions and reviews display using React.
- **State Hydration / Caching Manager**: Handles local storage persistence, JWT memory management, and optimistic UI updates using TanStack Query and Zustand persist.
- **API Client Layer**: Centralized HTTP client managing requests and token injection using Axios/Fetch API.

## Relationships
- **Catalog & Search View** -> **API Gateway**: Fetches catalog and search data via HTTPS (REST/GraphQL)
- **Cart & Checkout View** -> **API Gateway**: Submits cart and checkout orders via HTTPS (REST/GraphQL)
- **All View Components** -> **API Client Layer**: Executes network requests via internal function calls
- **All View Components** -> **State Hydration / Caching Manager**: Persists state and caches data locally

## Technology Stack
- **React & TypeScript**: Core UI library and type safety for maintainability.
- **React Router & Context API**: Client-side routing and global state management.
- **TanStack Query & Zustand**: Server state caching, persistent caching, and client cart state management.
- **Axios / Fetch API**: Standardized HTTP communication layer.
- **Amazon S3 & CloudFront**: Global content delivery for static assets satisfying performance constraints.

## Rationale
This component architecture uses modular React patterns and client-side caching to meet the sub-2-second 3G page load constraint. Centralized API and state management layers ensure OWASP Top-10 security mitigations and seamless scaling for 1 million MAU.