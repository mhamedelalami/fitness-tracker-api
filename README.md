## Fitness Tracker API 🏃‍♂️

    Track your fitness journey, one activity at a time.

Fitness Tracker API is a backend service built with Django and Django REST Framework that enables users to log, manage, and view their fitness activities such as running, cycling, walking, and swimming.

## 🌟 Features (Planned)

- User registration and authentication with JWT
- CRUD operations for fitness activities
- Filter activities by type and date
- Summary statistics endpoint (total calories, distance, duration)
- API documentation and deployment on PythonAnywhere

## 🔧 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default development database)

## 📅 Timeline (Week-by-Week)

| Week | Focus |
|------|-------|
| 1    | Idea & Planning, Project setup, virtual environment, models & migrations |
| 2    | User registration, authentication, serializers |
| 3    | 	Full CRUD functionality and filtering|
| 4    | Summary endpoint, validation, API documentation |
| 5    | Deployment, testing, final fixes, submission |

## ✅ Week 1 Progress

- Finalized project idea
- Set up virtual environment and installed dependencies
- Initialized Django project and created apps (users and activities)
- Designed Activity model and ran migrations
- Registered models in Django admin and accessed admin panel

## ✅ Week 2
 Progress

This week, I focused on the **design phase** of the project:

- **Created the Entity Relationship Diagram (ERD)** to visualize the database structure and relationships.  
  - Entities: **User**, **Activity**, **Activity Type**  
  - Relationships: One-to-Many between **User** and **Activity**, and between **Activity Type** and **Activity**.  
- **Defined the core API endpoints** to match the ERD and planned features.

---

### 📌 API Endpoints (Planned)

#### **Authentication**
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/auth/register/` | POST | Register a new user | No |
| `/api/auth/login/` | POST | Log in a user and return a token (JWT or session) | No |
| `/api/auth/logout/` | POST | Log out the current user | Yes |
| `/api/auth/user/` | GET | Get current authenticated user profile | Yes |
| `/api/auth/user/` | PUT/PATCH | Update current user profile | Yes |

---

#### **Activities**
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/activities/` | GET | List all activities for the logged-in user (optionally filter by type/date) | Yes |
| `/api/activities/` | POST | Create a new activity (type, duration, distance, calories, date) | Yes |
| `/api/activities/{id}/` | GET | Retrieve details of a specific activity | Yes |
| `/api/activities/{id}/` | PUT | Update an existing activity | Yes |
| `/api/activities/{id}/` | DELETE | Delete an activity | Yes |

---

#### **Activity Types**
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/activity-types/` | GET | List all available activity types | No |
| `/api/activity-types/{id}/` | GET | Retrieve details of a specific activity type | No |

---

#### **History & Filtering**
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/activities/history/` | GET | Get activities sorted by date (with optional filters like `?type=running&start=YYYY-MM-DD&end=YYYY-MM-DD`) | Yes |

---

#### **Summary**
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/api/activities/summary/` | GET | Get total distance, duration, and calories burned per week or month (`?period=week` or `?period=month`) | Yes |

