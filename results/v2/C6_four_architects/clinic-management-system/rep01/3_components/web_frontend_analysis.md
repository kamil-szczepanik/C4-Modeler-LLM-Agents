## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability, strict security compliance, and rapid performance across hybrid cloud environments.

## Key Elements
- Patients, Clinicians/Staff, and Hospital Administrators
- AWS CloudFront (CDN & Edge Hosting)
- Web Frontend Container (React/TypeScript SPA, Nginx origin)
- Internal Web Frontend Components: Routing & Shell, Auth & Session Module, Feature Modules, API Client & Interceptor, Local State & Cache Manager, Telemetry Agent
- API Gateway (Kong/Envoy)
- Observability & Monitoring Collector (OpenTelemetry / Prometheus / Grafana Loki)

## Relationships
- Users -> AWS CloudFront: Fetches static web assets [HTTPS]
- Web Frontend -> API Gateway: Executes all data queries, mutations, and authentication [HTTPS/REST, WSS]
- Telemetry Agent -> Observability & Monitoring Collector: Exports client performance and error metrics [gRPC/OTLP over TLS]

## Technology Stack
- React / TypeScript: Modern SPA framework for building reactive clinical UI modules
- AWS CloudFront & Nginx: Global edge caching and origin server ensuring high availability (99.99%) and strict security headers (CSP, HSTS)
- Axios/Fetch & TanStack Query/Redux Toolkit: Centralized API interception, token injection, and server-state caching for sub-second EMR load times (<1s P95)
- OpenTelemetry JS SDK: Standardized client telemetry tracking for performance and error monitoring

## Rationale
This architecture eliminates insecure direct browser-to-KMS communication by routing all dynamic interactions through an API Gateway and BFF pattern. Utilizing a React SPA backed by global CDN caching ensures HIPAA/GDPR compliance, active-active high availability (99.99%), and optimized EMR performance.