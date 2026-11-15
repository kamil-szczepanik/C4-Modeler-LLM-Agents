## Overview
The Single Page Application (SPA) container delivers a high-performance, client-side React interface for the Online Bookstore. It enables seamless catalog browsing, secure checkout, multi-currency display, and personalized recommendations for 1M MAU.

## Key Elements
* Customer & Store Administrator (Users)
* Single Page Application (SPA) (Container)
* Router Component (React Router)
* State Management Component (Zustand/Redux Toolkit)
* API Client Component (Axios/Fetch wrapper)
* Localization/Currency Component (React-i18next & Intl API)
* Catalog & Search UI Component
* Checkout & Cart UI Component
* Recommendations & Reviews UI Component

## Relationships
* Customer & Store Administrator -> Single Page Application (SPA): Interacts via [HTTPS / REST / GraphQL]
* API Client Component -> Amazon API Gateway: Sends backend requests via [HTTPS / JSON] with `Accept-Currency` headers
* UI Components -> Localization/Currency Component: Formats prices locally via [JavaScript function calls]
* Router Component -> Catalog, Checkout, and Recommendations UI Components: Renders views via [Client-side routing]

## Technology Stack
* React & TypeScript: Core UI framework ensuring type safety and robust component architecture.
* Amazon S3 & Amazon CloudFront: Global static asset hosting and CDN delivery for sub-2s page loads on 3G.
* Zustand/Redux Toolkit: In-memory global state management to mitigate XSS vulnerabilities.
* React-i18next & JavaScript Intl API: Client-side internationalization supporting USD, EUR, and GBP without network latency.

## Rationale
This component-driven SPA architecture ensures sub-2-second page loads on 3G networks by offloading routing, state, and currency formatting to the client via CloudFront. In-memory token handling and strict separation of concerns fulfill OWASP Top-10 security constraints while scaling effortlessly to 1M MAU.