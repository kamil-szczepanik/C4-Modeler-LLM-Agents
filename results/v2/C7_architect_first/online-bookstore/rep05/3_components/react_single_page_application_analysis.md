## Overview
The React Single Page Application (SPA) serves as the core user interface for the Online Bookstore, delivering a high-performance, secure e-commerce experience across global regions. It handles catalog browsing, secure checkout, reviews, and personalized recommendations while supporting 1 million monthly active users.

## Key Elements
- Routing & App Shell (`react-router-dom`)
- Catalog & Search Module (`Redux Toolkit`)
- Cart & Checkout Flow (`React Hook Form`, Stripe Elements SDK)
- Recommendation & Review Widgets
- API Client (`Axios`, `GraphQL Client`)
- Browser Local Storage (Encrypted Guest Cart Fallback)
- Global Edge Layer (Amazon CloudFront, Amazon S3)
- Amazon API Gateway

## Relationships
- Routing & App Shell -> Catalog & Search Module / Cart & Checkout Flow [Dynamic Import / React.lazy]
- Catalog & Search Module, Cart & Checkout Flow, Recommendation Widgets -> API Client [HTTPS/REST/GraphQL]
- API Client -> Amazon API Gateway [HTTPS/WSS]
- Cart & Checkout Flow -> Local Storage (Browser) [Encrypted JSON, fallback only]
- Global Edge Layer -> React Single Page Application [HTTPS]

## Technology Stack
- React 18+: Frontend library for component-based UI development.
- Amazon S3 & CloudFront: Static asset hosting and global CDN delivery for low latency and high availability.
- Redux Toolkit & React Hook Form: Efficient client-side state management and form handling.
- Stripe Elements SDK: Secure, PCI-DSS compliant payment processing via isolated iframes.
- Brotli/Gzip & HTTP/2/3: Edge compression and transfer protocols ensuring sub-2-second 3G page loads.

## Rationale
This architecture leverages static asset caching on global CDNs and aggressive code-splitting to satisfy strict performance and scalability targets. Security controls, including strict CSP headers, encrypted guest cart storage, and isolated payment frames, ensure compliance with GDPR, CCPA, and PCI-DSS standards.