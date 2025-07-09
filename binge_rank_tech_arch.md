**Technical Architecture: BingeRank MVP**

**Overview**
This document outlines the technical architecture for the BingeRank MVP, a mobile-first, socially-driven app that helps users rank and discover TV shows based on taste compatibility and availability.

---

**1. System Components**

| Component           | Tech Stack / Service                  | Description |
|---------------------|---------------------------------------|-------------|
| Frontend (Mobile)   | React Native                          | Cross-platform mobile app for iOS and Android |
| Backend API         | FastAPI (Python)                      | REST API server handling business logic |
| Database            | PostgreSQL (via Supabase or Neon)     | Stores users, rankings, shows, relationships |
| Authentication      | Firebase Auth / Auth0                 | Manages user login and identity |
| External APIs       | TMDb, Watchmode / JustWatch           | Provides metadata and streaming availability |
| Hosting             | Render / Railway / Fly.io             | Hosts FastAPI backend |
| Static Assets (optional) | Cloudflare Pages / Vercel       | Hosts web admin UI, docs, or previews |

---

**2. API Interactions**

- Mobile app communicates with the backend via HTTPS REST APIs
- Backend authenticates requests using Firebase/Auth0 JWTs
- Backend integrates with TMDb API (show search, metadata)
- Backend integrates with Watchmode API (availability info)

---

**3. Key Backend Modules**

- `auth`: Validate and parse user JWTs, handle sign-in/out
- `shows`: Search and cache TMDb metadata
- `rankings`: Handle pairwise comparisons and dynamic ranking logic
- `taste`: Generate and update user's taste profile
- `social`: Follow/unfollow logic, activity feed
- `availability`: Query Watchmode for streaming locations

---

**4. Database Schema (Simplified)**

- `users(id, name, email, auth_provider, joined_at)`
- `shows(id, tmdb_id, title, metadata_json)`
- `rankings(user_id, show_id, score, updated_at)`
- `comparisons(user_id, show1_id, show2_id, preferred_id)`
- `taste_profiles(user_id, genres, tones, pacing, score_json)`
- `follows(follower_id, followed_id, created_at)`
- `activity_log(user_id, action_type, target_id, timestamp)`

---

**5. Authentication & Security**

- Auth handled via Firebase Auth or Auth0 SDK in the app
- Backend validates JWTs and enforces route-level permissions
- OAuth with Google/Apple can be enabled later
- Role-based access for admin endpoints (e.g., `is_admin` flag in `users` table)

---

**6. Deployment Plan (MVP)**

- **Backend**: Deploy FastAPI container to Render or Railway
- **DB**: Use Supabase or Neon Postgres for managed, scalable storage
- **Frontend**: Distribute React Native app via Expo for testing
- **Monitoring**: Use built-in logs from Render/Railway or integrate Sentry for backend errors

---

**7. Future Considerations**

- **Graph DB**: Consider Neo4j or AWS Neptune if social graph needs become complex
- **Recommendation Engine**: Move ranking and taste inference to separate microservice
- **Caching Layer**: Redis for ranking speed and show metadata lookup
- **Web Frontend**: Admin portal or analytics dashboard in Next.js
- **CI/CD**: GitHub Actions or Render Deploy Hooks

---

Let me know if you’d like a visual system architecture diagram or schema ERD to go with this.

