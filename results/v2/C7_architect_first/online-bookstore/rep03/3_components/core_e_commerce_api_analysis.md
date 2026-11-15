## Overview
The Core E-Commerce API is a Node.js and Express modular monolith running on Amazon ECS Fargate that manages online bookstore transactions, catalogs, and fulfillment. It provides secure, scalable e-commerce services supporting multi-currency checkout, fast browsing, and global availability.

## Key Elements
- **Catalog Component**: Express Router and pg query builder managing book browsing and keyword search.
- **Cart Management Component**: In-memory session manager handling ephemeral shopping carts and promotional discounts via Amazon ElastiCache.
- **Order & Checkout Component**: Domain service module handling secure checkout, tax calculation, payment processing, and inventory reservation.
- **Fulfillment Component**: Integration adapter managing shipping provider APIs and tracking data.

## Relationships
- **Amazon API Gateway** -> **Core E-Commerce API**: Routes validated HTTP requests using HTTPS via AWS App Mesh.
- **Catalog Component** -> **Amazon Aurora (PostgreSQL)** & **Amazon ElastiCache (Redis)**: Queries catalog data via TCP/SQL and Redis RESP.
- **Cart Management Component** -> **Amazon ElastiCache (Redis)**: Stores session and cart states via Redis RESP.
- **Order & Checkout Component** -> **Tax Calculation Service**, **Payment Gateway**, & **Notification Service**: Communicates via HTTPS/REST.
- **Fulfillment Component** -> **Shipping Provider API**: Manages order fulfillment via HTTPS/REST.

## Technology Stack
- **Node.js & Express**: Core runtime and framework for fast, lightweight routing.
- **Amazon ECS (Fargate)**: Serverless container orchestration for scalable microservice execution.
- **Amazon Aurora PostgreSQL**: Relational database for durable transactional data with global replication.
- **Amazon ElastiCache (Redis)**: In-memory cache for sub-millisecond cart retrieval and session management.
- **AWS App Mesh & CodeDeploy**: Handles service mesh networking, canary traffic shifting, and blue/green deployments.

## Rationale
This architecture uses a modular monolith on ECS Fargate to balance operational simplicity with strict domain isolation for cart, catalog, and checkout workflows. Integrating Redis for ephemeral cart state and Aurora for global transactional data ensures sub-2-second page loads and 99.95% availability under high concurrent load.