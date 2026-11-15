## Overview
The Single Page Application (SPA) serves as the primary client-side user interface for the Online Bookstore, delivering high-performance catalogue browsing, secure checkout, and multi-currency support. It is engineered to provide a fast, responsive user experience while meeting strict global scalability, performance, and security requirements.

## Key Elements
- **Routing & Shell Component**: React Router managing client-side navigation, layout shells, and UX-level role-based access control (RBAC).
- **Catalogue & Search Module**: Handles browsing and instant filtering with local state caching.
- **Cart & Checkout Module**: Manages session cart state and purchase flows.
- **Localization & Personalization Context**: Manages currency formatting (USD, EUR, GBP) and user locale state.
- **API Client Layer**: Axios/Fetch with OpenAPI generated types communicating securely with the backend.
- **Infrastructure**: Amazon S3 for static hosting, Amazon CloudFront for content delivery, and AWS WAF for edge security.

## Relationships
- Customers, Authors/Publishers, and Store Administrators -> SPA: Accesses interface via HTTPS (TLS 1.3).
- SPA -> API Gateway: Routes all client traffic via HTTPS (TLS 1.3) with JWT bearer tokens or secure cookies.
- GitHub Actions CI/CD Pipeline -> Amazon S3: Deploys immutable static assets with automated bundle-size gates.
- AWS WAF / CloudFront -> SPA: Enforces security policies, DDoS protection, and Content Security Policy (CSP) headers at the edge.

## Technology Stack
- **React & TypeScript**: Chosen for type safety, component modularity, and high-performance UI rendering.
- **Amazon S3 & CloudFront**: Selected for scalable, low-latency global static asset delivery and instant cache invalidation.
- **AWS WAF**: Deployed at the edge for OWASP Top-10 mitigation and DDoS protection.
- **GitHub Actions & Lighthouse CI**: Used for automated deployment pipelines and performance budget enforcement.

## Rationale
This architecture ensures sub-2-second page loads on 3G networks and scales to support 1 million monthly active users globally across multiple AWS regions. Strict security controls, including edge WAF protection and secure token handling, safeguard user data while maintaining a seamless e-commerce experience.