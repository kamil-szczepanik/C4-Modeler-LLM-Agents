## Overview
The Patient Self-Service Container provides a secure, accessible web portal for patient registration, scheduling, and billing. It utilizes a React/Next.js SPA deployed across a global CDN and Kubernetes to ensure 99.99% availability and HIPAA/GDPR compliance.

## Key Elements
- Patient (User Persona)
- Patient Self-Service Container (React/Next.js SPA)
- Routing & Session Component
- Authentication & Consent Controller
- Appointment & Demographics Client Service (with Form Validation & State Cache / TanStack Query)
- Billing & Payment Widget Integration
- API Gateway (Kong / Nginx)

## Relationships
- Patient -> Patient Self-Service Container: Interacts via HTTPS (TLS 1.3)
- Patient Self-Service Container -> API Gateway: Communicates via internal mTLS over gRPC/REST
- CDN / Edge WAF -> Patient Self-Service Container: Protects and routes static assets and SSR routes

## Technology Stack
- React / Next.js SPA: Chosen for high performance, mobile responsiveness, and WCAG 2.1 AA accessibility compliance
- TanStack Query: Used for lightweight in-memory form state caching and optimistic UI updates
- Global CDN (AWS CloudFront / Cloudflare) + Kubernetes: Ensures global scale and 99.99% high availability
- TLS 1.3, HTTP-only Secure SameSite=Strict Cookies, and JWTs: Enforced for secure session management and zero PHI persistence at the edge

## Rationale
This architecture satisfies high availability and strict HIPAA/GDPR constraints by decoupling stateless UI components from backend services while preventing edge PHI leakage. It simultaneously delivers sub-second performance and an intuitive patient experience to reduce administrative overhead.