Absolutely! Here’s your **full updated README** including everything from week 3, week 4 day 1 (summary endpoint), custom validations, and a Postman guide for testing the summary endpoint.

---

## Fitness Tracker API 🏃‍♂️

Track your fitness journey, one activity at a time.

Fitness Tracker API is a backend service built with Django and Django REST Framework that enables users to log, manage, and view their fitness activities such as running, cycling, walking, and swimming.

## 🌟 Features (Planned)

* User registration and authentication with JWT
* CRUD operations for fitness activities
* Filter activities by type and date
* Summary statistics endpoint (total calories, distance, duration)
* Custom validations for activity creation and updates
* API documentation and deployment on PythonAnywhere

## 🔧 Tech Stack

* Python 3.x
* Django
* Django REST Framework
* SQLite (default development database)

## 📅 Timeline (Week-by-Week)

| Week | Focus                                                                    |
| ---- | ------------------------------------------------------------------------ |
| 1    | Idea & Planning, Project setup, virtual environment, models & migrations |
| 2    | User registration, authentication, serializers                           |
| 3    | Full CRUD functionality and filtering                                    |
| 4    | Summary endpoint, validation, API documentation                          |
| 5    | Deployment, testing, final fixes, submission                             |

## ✅ Week 1 Progress

* Finalized project idea
* Set up virtual environment and installed dependencies
* Initialized Django project and created apps (users and activities)
* Designed Activity model and ran migrations
* Registered models in Django admin and accessed admin panel

## ✅ Week 2 Progress

This week, I focused on the **design phase** of the project:

* **Created the Entity Relationship Diagram (ERD)** to visualize the database structure and relationships.

  * Entities: **User**, **Activity**, **Activity Type**
  * Relationships: One-to-Many between **User** and **Activity**, and between **Activity Type** and **Activity**.
* **Defined the core API endpoints** to match the ERD and planned features.

---

### 📌 API Endpoints (Planned)

#### **Authentication**

| Endpoint              | Method    | Description                                       | Auth Required |
| --------------------- | --------- | ------------------------------------------------- | ------------- |
| `/api/auth/register/` | POST      | Register a new user                               | No            |
| `/api/auth/login/`    | POST      | Log in a user and return a token (JWT or session) | No            |
| `/api/auth/logout/`   | POST      | Log out the current user                          | Yes           |
| `/api/auth/user/`     | GET       | Get current authenticated user profile            | Yes           |
| `/api/auth/user/`     | PUT/PATCH | Update current user profile                       | Yes           |

---

#### **Activities**

| Endpoint                | Method | Description                                                                 | Auth Required |
| ----------------------- | ------ | --------------------------------------------------------------------------- | ------------- |
| `/api/activities/`      | GET    | List all activities for the logged-in user (optionally filter by type/date) | Yes           |
| `/api/activities/`      | POST   | Create a new activity (type, duration, distance, calories, date, notes)     | Yes           |
| `/api/activities/{id}/` | GET    | Retrieve details of a specific activity                                     | Yes           |
| `/api/activities/{id}/` | PUT    | Update an existing activity                                                 | Yes           |
| `/api/activities/{id}/` | DELETE | Delete an activity                                                          | Yes           |

---

#### **Activity Types**

| Endpoint                    | Method | Description                                  | Auth Required |
| --------------------------- | ------ | -------------------------------------------- | ------------- |
| `/api/activity-types/`      | GET    | List all available activity types            | No            |
| `/api/activity-types/{id}/` | GET    | Retrieve details of a specific activity type | No            |

---

#### **History & Filtering**

| Endpoint                   | Method | Description                                                                                                | Auth Required |
| -------------------------- | ------ | ---------------------------------------------------------------------------------------------------------- | ------------- |
| `/api/activities/history/` | GET    | Get activities sorted by date (with optional filters like `?type=running&start=YYYY-MM-DD&end=YYYY-MM-DD`) | Yes           |

---

#### **Summary**

| Endpoint                   | Method | Description                                                                                             | Auth Required |
| -------------------------- | ------ | ------------------------------------------------------------------------------------------------------- | ------------- |
| `/api/activities/summary/` | GET    | Get total distance, duration, and calories burned per week or month (`?period=week` or `?period=month`) | Yes           |

**Example Request (GET /api/activities/summary/?period=week)**

**Headers:**

```http
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

**Query Parameters:**

```
period=week
```

**Example Response (200 OK):**

```json
{
    "total_calories": 1450,
    "total_distance": 32.5,
    "total_duration": 210
}
```

**Notes:**

* `total_calories`: Sum of calories burned across all activities for the logged-in user in the selected period.
* `total_distance`: Sum of distance (in km) across all distance-based activities.
* `total_duration`: Sum of duration (in minutes) across all activities.
* The endpoint is **JWT-protected**, so you must include a valid access token in the `Authorization` header.

---

## ✅ Week 3 Progress Reflection

**User Authentication & Management:**

* Implemented user registration and profile endpoints.
* Configured JWT-based login and token refresh using `rest_framework_simplejwt`.
* Successfully tested user registration and login flows in Postman.

**Activity Management:**

* Created Activity model with fields for type, duration, distance, calories, date, and notes.
* Built serializers for Activity including automatic assignment of the logged-in user.
* Implemented activity CRUD endpoints:

  * Listing activities for the logged-in user.
  * Creating new activities.
  * Retrieving, updating, and deleting individual activities.
* Added filtering by activity type and date for activity listing.
* Successfully tested all endpoints in Postman; ensured proper authorization and response formats.

---

## ✅ Week 4 

**Activity Summary Endpoint**

* Implemented `ActivitySummaryView` to provide total calories, distance, and duration for the logged-in user.
* Created `ActivitySummarySerializer` to structure summary data.
* Configured JWT authentication to protect the endpoint.
* Tested endpoint in Postman with successful login and data retrieval.

**Custom Validations and Refined Logic**

* Added field-level and cross-field validations in `ActivitySerializer`:

  * Duration must be between 1 and 1440 minutes.
  * Calories burned cannot be negative or exceed a realistic max.
  * Distance is required for distance-based activities (running, cycling, walking, swimming) and must be greater than 0.
  * Date cannot be in the future.
* Added **custom error messages** for all validations.
* Made the list of activity types dynamic for validation messages.

---

### 🧪 Postman Testing Guide

1. **Register a new user**

   * POST `/api/auth/register/` with JSON body:

     ```json
     {
       "username": "testuser",
       "email": "test@example.com",
       "password": "strongpassword123"
     }
     ```
   * Expect `201 Created`.

2. **Login to get JWT token**

   * POST `/api/auth/login/` with JSON body:

     ```json
     {
       "username": "testuser",
       "password": "strongpassword123"
     }
     ```
   * Copy the `access` token from the response.

3. **Use token for authorized requests**

   * In Postman, go to the **Headers** tab and add:

     ```
     Key: Authorization
     Value: Bearer <your_access_token>
     ```

4. **Test Activity CRUD endpoints**

   * Create: POST `/api/activities/` with JSON body of activity.
   * List: GET `/api/activities/`
   * Retrieve/Update/Delete: `/api/activities/{id}/`

5. **Test Summary endpoint**

   * GET `/api/activities/summary/?period=week` with Authorization header.
   * Expect a JSON response with `total_calories`, `total_distance`, and `total_duration`.

---

