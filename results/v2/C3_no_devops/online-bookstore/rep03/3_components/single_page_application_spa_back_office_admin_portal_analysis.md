## Overview
The Online Bookstore provides a global, scalable e-commerce platform for physical and electronic books with recommendations and reviews. It utilizes a React-based Single-Page Application and Back-Office Admin Portal deployed on AWS to deliver high-performance, secure user experiences.

## Key Elements
- Customer
- Admin / Content Manager
- Single-Page Application (SPA) & Back-Office Admin Portal (React, Amazon S3, Amazon CloudFront)
- Storefront Module (React, Redux Toolkit, DOMPurify)
- Admin Portal Module (React, React Router)
- Auth & Consent Manager (React Context, AWS Amplify, AWS Cognito)
- API Client Interceptor (Axios)
- Amazon API Gateway

## Relationships
- Customer -> Single-Page Application (SPA) & Back-Office Admin Portal: Accesses storefront via HTTPS over CloudFront [HTTPS]
- Admin / Content Manager -> Single-Page Application (SPA) & Back-Office Admin Portal: Accesses admin portal via HTTPS with MFA [HTTPS, OIDC/AWS Cognito]
- Storefront Module & Admin Portal Module -> API Gateway: Communicates via centralized Axios interceptor [REST/HTTPS, JWT]

## Technology Stack
- React: Powers component-based UI for high performance on 3G networks
- Amazon CloudFront & Amazon S3: CDN and object storage for sub-2s global page loads and strict Content Security Policy enforcement
- AWS Amplify & AWS Cognito: Manages OIDC authentication, JWT sessions, and MFA enforcement
- Redux Toolkit: Manages state for shopping cart optimistic updates and localized multi-currency rendering
- DOMPurify: Sanitizes user-generated customer reviews against DOM-based XSS

## Rationale
This architecture separates public storefront and administrative bundles across distinct S3 buckets to eliminate privilege leakage risks. Furthermore, it implements strict token management and client-side sanitization to satisfy OWASP Top-10 security and GDPR/CCPA compliance at scale.