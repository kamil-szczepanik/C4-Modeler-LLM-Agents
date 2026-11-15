## Overview
Decomposition of the Single-Page Application (SPA) container for the Online Bookstore, providing a secure, performant, and compliant client-side architecture. It ensures sub-2s 3G performance, GDPR/CCPA compliance, and multi-currency support for 1M MAU.

## Key Elements
- **Router Component**: React Router for client-side navigation and code-splitting
- **Feature Modules**: Lazy-loaded views for catalogue, search, checkout, cart, reviews, and recommendations
- **State Management Store**: Redux Toolkit for global application state
- **API Client Layer**: Axios wrapper incorporating a Security & Token Interceptor for in-memory JWT handling
- **Privacy & Consent Manager**: Local management of cookie banners and GDPR/CCPA compliance states
- **Localization & Currency Provider**: Manages locale dictionaries and multi-currency formatting (USD, EUR, GBP)
- **External Hosting**: Amazon S3 and Amazon CloudFront for static asset delivery

## Relationships
- **Router Component** -> **Feature Modules**: Dynamically imports and lazy-loads views on demand [ES Modules]
- **Feature Modules** -> **State Management Store**: Reads and writes global state [Redux Dispatch]
- **Feature Modules** -> **API Client Layer**: Invokes remote operations [HTTPS / REST / JSON]
- **Privacy & Consent Manager** -> **API Client Layer**: Sends compliance triggers to the Privacy Service [HTTPS / JSON]
- **API Client Layer** -> **API Gateway**: Sends authenticated requests [HTTPS / JSON]
- **GitHub Actions (CI/CD)** -> **Amazon S3 & CloudFront**: Deploys optimized React build bundles [HTTPS]

## Technology Stack
- **React & TypeScript**: Core framework for type-safe, component-driven UI development
- **React Router**: Enables code-splitting and lazy-loading to achieve <2s 3G page load performance
- **Redux Toolkit**: Centralizes global state for cart, session, and currency preferences
- **Axios & Custom Interceptors**: Handles secure HTTP communication and in-memory JWT storage to mitigate OWASP Top-10 XSS vulnerabilities
- **Amazon S3 & CloudFront**: Provides global edge caching and static asset distribution

## Rationale
This component architecture optimizes frontend performance through lazy-loading to meet strict 3G constraints while isolating compliance and security logic in memory. It directly supports multi-currency retail requirements and global scalability on AWS.