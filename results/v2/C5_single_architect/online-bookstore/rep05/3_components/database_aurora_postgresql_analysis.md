## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. It provides highly available, scalable retail services supporting 1M monthly active users globally across AWS regions.

## Key Elements
- **Order Schema**: Manages ACID-compliant transactions, cart states, and immutable order history.
- **Catalog & Inventory Schema**: Handles book metadata, multi-currency pricing (USD, EUR, GBP), and stock levels.
- **Customer & Review Schema**: Stores user profiles and 5-star ratings with Row-Level Security.
- **Order & Checkout Service**: Processes secure customer transactions.
- **Catalog Service**: Manages catalogue browsing and keyword search.
- **Recommendation Service**: Powers "Customers also bought" analytics.

## Relationships
- Order & Checkout Service -> Order Schema: Persists transactional order data via `PostgreSQL Protocol`.
- Catalog Service -> Catalog & Inventory Schema: Reads/writes book and pricing data via `PostgreSQL Protocol`.
- Recommendation Service -> Catalog & Inventory Schema: Queries metadata and order history via `PostgreSQL Protocol`.

## Technology Stack
- **Amazon Aurora PostgreSQL**: Chosen for multi-region replication, automated failover, and ACID compliance to guarantee 99.95% uptime and reliable checkout.
- **Row-Level Security (RLS)**: Enforced in the Customer & Review Schema for GDPR and CCPA compliance.
- **AWS KMS**: Utilized for encryption at rest across the database cluster.

## Rationale
This architecture ensures robust data integrity and global compliance while maintaining sub-2-second performance. The schema-based decomposition supports scalability needs for 1M MAU without transactional degradation.