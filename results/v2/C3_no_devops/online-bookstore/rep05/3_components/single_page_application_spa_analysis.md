## Overview
[Global SPA for the Online Bookstore delivering a responsive, secure e-commerce experience for customers and administrators. Built with React and hosted globally via AWS CloudFront and S3 to meet sub-2-second load time targets.]

## Key Elements
*   **Customers & Bookstore Administrators**: End users and operators interacting via browser.
*   **Single Page Application (SPA)**: React-based frontend container.
*   **Routing & View Manager**: React Router for client-side navigation.
*   **State & Session Store**: Redux Toolkit / React Context for cart, catalog cache, and multi-currency state (USD, EUR, GBP).
*   **API Client**: Axios/Fetch wrappers communicating with API Gateway via HTTPS/REST.
*   **Localization Engine**: Handles locale, formatting, and currency conversion.
*   **Telemetry & Event Tracker**: Asynchronous tracking for clickstream and recommendations.

## Relationships
*   Customer / Administrator -> Single Page Application (SPA): Browses, purchases, and manages via HTTPS / React & AWS CloudFront.
*   Single Page Application (SPA) -> API Gateway / Envoy: Sends API requests via HTTPS/REST using HttpOnly cookies.
*   Telemetry & Event Tracker -> Analytics & Event Tracking Container: Streams behavioral data via `navigator.sendBeacon` to AWS Kinesis.

## Technology Stack
*   **React & Vite**: Frontend library and bundler for minimal JS payload and fast rendering.
*   **AWS S3 & CloudFront**: Static asset hosting and global CDN for low latency and <2s page load.
*   **HttpOnly, Secure, SameSite=Strict Cookies**: Mitigates XSS and OWASP Top-10 risks by avoiding client-side token storage.
*   **React Router**: Enables seamless client-side navigation.

## Rationale
[This architecture guarantees high performance for 1M MAU globally by leveraging static edge caching and asynchronous telemetry. It strictly enforces security and compliance through robust CSP headers and cookie-based session management.]