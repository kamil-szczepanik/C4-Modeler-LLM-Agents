## Overview
The Online Bookstore system is a scalable e-commerce platform designed to process book sales, secure checkouts, and personalized recommendations for 1 million monthly active users. It utilizes a microservices architecture deployed across AWS regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`) to meet strict performance and availability targets.

## Key Elements
- Recommendations Service (Python, FastAPI, AWS ECS Fargate)
- Amazon DynamoDB (NoSQL Data Store)
- `ItemCoOccurrence` Table (Global Table for adjacency lists)
- `UserAffinityProfiles` Table (Regional table for user interaction weights)
- Amazon DynamoDB Accelerator (DAX)
- AWS VPC Endpoints (AWS PrivateLink)
- AWS KMS (Customer-Managed Keys)

## Relationships
- Recommendations Service -> Amazon DynamoDB: Reads/writes recommendation data via AWS SDK (HTTPS/TLS 1.3) over VPC Endpoints
- Recommendations Service -> Amazon DynamoDB Accelerator (DAX): Caches high-frequency read requests via TCP/IP

## Technology Stack
- Amazon DynamoDB: Chosen for single-digit millisecond latency to meet sub-2-second page load requirements
- Amazon DynamoDB Accelerator (DAX): Deployed in-memory to absorb read spikes for popular books
- AWS KMS: Implemented with customer-managed keys for storage and multi-region encryption
- Terraform / AWS CDK: Used for Infrastructure as Code and global table deployments

## Rationale
This architecture ensures 99.95% availability, global scalability, and low-latency data access via multi-region Global Tables. It natively satisfies GDPR/CCPA data residency, TTL expiration, and strict OWASP security controls.