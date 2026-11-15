## Overview
The Single Page Application (SPA) serves as the primary user interface for the global online bookstore, enabling book discovery, secure multi-currency checkout, and reviews. It is architected for high performance, edge caching, and resilience to support 1 million monthly active users globally.

## Key Elements
- Routing & Shell Component
- Catalog & Search Module
- Cart & Checkout Module
- Reviews & Recommendations Module
- API Client & State Manager
- AWS API Gateway
- Amazon CloudFront & Amazon S3

## Relationships
- Routing & Shell Component -> Catalog, Cart & Checkout, and Reviews & Recommendations Modules [In-memory state and props]
- Catalog, Cart & Checkout, and Reviews & Recommendations Modules -> API Client & State Manager [In-memory function calls]
- API Client & State Manager -> AWS API Gateway [HTTPS, REST/GraphQL]
- Cart & Checkout Module -> Local Storage & IndexedDB [Zustand Persist Middleware]
- SPA Artifacts -> Amazon CloudFront & Amazon S3 [AWS CodePipeline deployment]

## Technology Stack
- React & TypeScript: Core frontend framework for robust, type-safe UI development
- React Router: Client-side routing and module lazy-loading to achieve sub-2-second 3G page loads
- Zustand & Zustand Persist Middleware: Lightweight state management and local cart persistence
- TanStack Query (React Query): Server-state management featuring caching, request deduplication, and offline retry logic
- AWS CodePipeline & CodeBuild: Automated CI/CD and multi-region artifact promotion

## Rationale
This component architecture enforces strict separation of concerns, enabling aggressive bundle optimization and edge caching to meet strict performance targets on 3G networks. Furthermore, local storage persistence and robust client-side error handling directly protect conversion rates and maintain high availability during transient network degradation.