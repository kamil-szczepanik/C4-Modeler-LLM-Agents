## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system ensures EU-only data residency and meets strict performance constraints for search queries.

## Key Elements
- **Library Patron**: End-user accessing catalog and circulation features.
- **Librarian**: Administrative user managing items and circulation.
- **Web Application Container**: React and TypeScript Single Page Application.
  - **UI Router & View Layer**: React Router and Tailwind CSS.
  - **State & Session Store**: Zustand.
  - **Search & Filter Controller**: React Hook / Local State.
  - **Auth & Authorization Guard**: React Context / JWT Decoder.
  - **API Client**: Axios.
  - **Telemetry & Error Boundary**: Sentry SDK / React Error Boundary.
- **API Gateway**: Nginx / Kong.

## Relationships
- Library Patron -> Web Application: Accesses features [HTTPS]
- Librarian -> Web Application: Manages system [HTTPS]
- UI Router & View Layer -> State & Session Store: Reads/writes state [In-memory]
- State & Session Store -> API Client: Triggers data fetching [In-memory]
- UI Router & View Layer -> Search & Filter Controller: Delegates search input [In-memory]
- Search & Filter Controller -> API Client: Triggers debounced search [HTTPS]
- UI Router & View Layer -> Auth & Authorization Guard: Checks permissions [In-memory]
- Auth & Authorization Guard -> API Client: Injects Bearer tokens [In-memory]
- UI Router & View Layer -> Telemetry & Error Boundary: Reports exceptions [In-memory]
- Telemetry & Error Boundary -> EU-hosted Monitoring Endpoint: Forwards logs [HTTPS]
- API Client -> API Gateway: Makes API requests [HTTPS (REST/JSON)]

## Technology Stack
- **React & TypeScript**: Powers the responsive Single Page Application UI.
- **Zustand**: Manages client-side application state and user sessions lightweight.
- **Axios**: Handles outbound REST/JSON communication.
- **Sentry SDK**: Captures client-side exceptions while routing to EU-hosted endpoints.
- **Nginx / Kong**: Manages incoming API requests at the gateway.

## Rationale
The component decomposition enforces a clean separation of concerns and maintains security by keeping tokens strictly in memory. Client-side search debouncing protects backend performance to meet the < 800 ms response requirement.