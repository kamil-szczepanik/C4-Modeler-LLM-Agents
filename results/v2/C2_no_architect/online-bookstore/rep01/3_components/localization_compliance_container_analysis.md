## Overview
[The Online Bookstore platform provides a globally accessible e-commerce system for purchasing physical and electronic books with recommendations and reviews. The Localization & Compliance Container ensures strict adherence to GDPR, CCPA, and multi-currency requirements across international markets.]

## Key Elements
* Book Buyer, Book Reviewer, Store Administrator, Support Agent
* AWS API Gateway
* Localization & Compliance Container (Amazon ECS/EKS)
* AWS Aurora Database (Multi-Region)
* Amazon ElastiCache & Amazon SQS
* AWS KMS & AWS Secrets Manager
* Third-Party Payment Gateway & Shipping APIs

## Relationships
* Book Buyer -> AWS API Gateway: Invokes self-service privacy and checkout APIs [HTTPS / TLS 1.3, OAuth2/OIDC]
* AWS API Gateway -> Localization & Compliance Container: Routes regional localization and compliance requests [mTLS inside AWS VPC]
* Localization & Compliance Container -> AWS Aurora Database: Reads/writes compliance data [Encrypted SQL / AES-256 with AWS KMS CMKs]
* Localization & Compliance Container -> Amazon SQS: Publishes asynchronous GDPR/CCPA deletion requests [Encrypted TLS / AWS KMS]
* Localization & Compliance Container -> Amazon ElastiCache: Caches currency conversion and geo-lookup data [Redis Protocol]

## Technology Stack
* AWS ECS/EKS: Container orchestration ensuring scalable, regional deployments
* Amazon SQS: Asynchronous messaging for reliable GDPR/CCPA data purges
* AWS Aurora: Multi-region relational database with strict data residency controls
* AWS S3 Object Lock: WORM compliance storage for tamper-proof audit logs
* AWS Secrets Manager & KMS: Secure credential storage and customer-managed encryption keys

## Rationale
[This architecture enforces regional data residency and automated compliance tracking to meet statutory GDPR and CCPA mandates without degrading performance. Asynchronous processing via SQS and caching via ElastiCache ensure system scalability and high availability under heavy user loads.]