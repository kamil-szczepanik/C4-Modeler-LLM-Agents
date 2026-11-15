## Overview
[The Admin Dashboard Container provides internal management interfaces for catalogue inventory, order fulfillment, and review moderation within the Online Bookstore system.]

## Key Elements
*   Administrator / Content Manager
*   Admin Dashboard Container (Amazon ECS Fargate, Nginx, Node.js API backend)
*   Internal Application Load Balancer (ALB)
*   Core API Application
*   Identity Provider
*   Shipping Provider APIs
*   Amazon CloudWatch & AWS X-Ray

## Relationships
*   Administrator / Content Manager -> Internal ALB: Accesses dashboard via HTTPS with mandatory MFA
*   Internal ALB -> Admin Dashboard Container: Routes secure traffic using mTLS
*   Admin Dashboard Container -> Identity Provider: Validates JWT tokens and enforces RBAC [HTTPS]
*   Admin Dashboard Container -> Core API Application: Performs inventory and catalogue operations [gRPC over TLS]
*   Admin Dashboard Container -> Shipping Provider APIs: Monitors fulfillment and exceptions [HTTPS]
*   Admin Dashboard Container -> Amazon CloudWatch: Ships immutable audit logs and structured JSON logs [HTTPS]

## Technology Stack
*   **Amazon ECS Fargate:** Runs containerized workloads with zero server management overhead to support 99.95% uptime (R-07).
*   **Node.js & Nginx:** Implements a modular monolith pattern with a React/Nginx SPA frontend and a unified backend to simplify deployments.
*   **gRPC over TLS:** Provides high-performance, strongly-typed inter-container communication with the Core API Application.
*   **Internal Application Load Balancer (ALB):** Restricts network access via VPC peering and AWS Security Groups.
*   **Amazon CloudWatch & AWS X-Ray:** Centralizes structured JSON logging, immutable audit trails, and distributed tracing.

## Rationale
[This modular monolith architecture deployed on ECS Fargate minimizes operational complexity while enforcing strict security boundaries, GDPR/CCPA compliance, and high availability.]