## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce web application designed to support 1 million monthly active users with multi-currency browsing, secure checkout, and personalized recommendations. The system ensures high performance, GDPR/CCPA compliance, and high availability across global AWS regions.

## Key Elements
- Casual Shoppers, Buyers, and Contributors/Reviewers (Users)
- Client Frontend (React Single Page Application hosted on AWS CloudFront and Amazon S3)
- Routing & Shell Component (React Router)
- Catalog & Recommendation UI (React, Tailwind CSS)
- Cart & Checkout UI (React)
- Review & Rating UI (React)
- Compliance & Localization Service (Client-side module)
- State & Storage Manager (Zustand, LocalStorage Adapter)
- Edge & Ingress (Amazon Route 53, Amazon API Gateway)

## Relationships
- Users -> Client Frontend: Accesses catalog, cart, checkout, and reviews [HTTPS over TLS]
- Routing & Shell Component -> Compliance & Localization Service & State & Storage Manager: Initializes services [In-memory]
- Cart & Checkout UI -> State & Storage Manager: Reads and writes local cart and currency state [In-memory / LocalStorage]
- Client Frontend Components -> Edge & Ingress: Sends API requests for backend operations [HTTPS over TLS, WebSockets]

## Technology Stack
- React: Provides a responsive, component-based user interface for rapid client-side rendering.
- AWS CloudFront & S3: Delivers static assets globally with low latency to meet sub-2-second page load goals.
- Zustand & LocalStorage: Manages persistent local state for carts and currency preferences without server roundtrips.
- Tailwind CSS: Enables rapid, lightweight styling to maintain strict performance budgets.

## Rationale
This architecture leverages static edge hosting and modular client-side state management to achieve rapid global performance and high availability. Decoupling the UI components ensures targeted scalability and maintainability while meeting stringent compliance and multi-currency requirements.