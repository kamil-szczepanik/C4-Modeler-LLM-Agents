## Overview
- Single Page Application (React / TypeScript) hosted on Amazon S3 and CloudFront delivering the core e-commerce experience.
- Provides secure catalogue browsing, multi-currency cart management, checkout, reviews, and personalized recommendations.

## Key Elements
- Routing & Layout Component (React Router, Zustand/React Context)
- Catalogue & Search Component (React)
- Cart & Checkout Component (React)
- Reviews & Ratings Component (React)
- Recommendation Component (React)
- API Client Module (Axios/Fetch)

## Relationships
- Single Page Application -> Amazon CloudFront / API Gateway / ALB: Sends API requests and fetches data [HTTPS (REST / GraphQL)]
- Feature Components -> API Client Module: Communicates with backend endpoints securely [In-memory function calls]
- Routing & Layout Component -> Feature Components: Delegates view rendering and orchestrates navigation [React props / Context]

## Technology Stack
- React & TypeScript: Type-safe, component-driven UI development
- Amazon S3 & CloudFront: Low-latency global static asset hosting and CDN delivery meeting sub-2s performance goals
- Zustand / React Context: Ephemeral local state management ensuring zero persistent PII storage
- AWS CodePipeline / GitHub Actions: Automated CI/CD deployment pipeline for immutable infrastructure releases

## Rationale
- Decoupling feature components through a centralized API client ensures strict adherence to security boundaries and OWASP guidelines.
- Global edge distribution via CloudFront satisfies scalability and high-availability requirements for 1M MAU across multiple geographic regions.