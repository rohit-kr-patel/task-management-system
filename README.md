# Task Management System

A **production-style task management system** built with a clear focus on **API design, authentication, data correctness, and predictable failure handling**.

This project is intentionally scoped to demonstrate **backend engineering fundamentals** expected at an **SDE-1** level, while following patterns used in real-world systems.

---

## 🎯 Project Goals

- Build a **clean, versioned REST API**
- Design for **misbehaving clients**
- Implement **stateless authentication**
- Model real-world data access patterns
- Practice **production-minded decisions**, not just feature delivery

This is **not a UI-heavy product**.  
The frontend exists only to validate end-to-end system behavior.

---

## 🧠 Design Philosophy

> *“I designed the system assuming clients would misbehave.”*

Key principles:
- Clear API contracts
- Explicit validation
- Predictable error responses
- Ownership and access enforcement
- Minimal but sufficient client

---

## 🏗️ Architecture Overview

                                            Client (Streamlit)
                                            ↓ HTTP (JWT)
                                            FastAPI Backend
                                            ↓ ORM
                                            PostgreSQL


---

## 🧩 Components

### Backend
- REST API
- JWT-based authentication
- Task CRUD with ownership enforcement
- Pagination & filtering
- Structured error handling

---

## 🛠️ Tech Stack

### Backend
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0
- **Database:** PostgreSQL (SQLite for local development)
- **Auth:** JWT (access tokens)
- **Migrations:** Alembic
- **Validation:** Pydantic
- **Password Hashing:** bcrypt

---

## 📁 Repository Structure

        task-management-system/
        ├── app/
        │ ├── api/
        │ │ └── v1/
        │ ├── core/
        │ │ ├── config.py
        │ │ └── security.py
        │ ├── db/
        │ │ ├── base.py
        │ │ └── session.py
        │ ├── models/
        │ ├── schemas/
        │ └── main.py
        ├── migrations/
        ├── tests/
        ├── requirements.txt
        └── README.md

    
---

## 🔐 Authentication Model

- Stateless JWT-based authentication
- Access tokens with expiry
- Middleware / dependency-based auth guard
- Ownership checks enforced at the API layer

**Tradeoff considered:**  
JWT vs session-based auth — JWT chosen for statelessness and API scalability.

---

## 🌐 API Design

### Versioning
- All endpoints are versioned under `/api/v1`

### Resources
- `/users`
- `/tasks`

### HTTP Semantics
- `401` — authentication failure
- `403` — unauthorized access
- `404` — resource not found
- `409` — conflict (e.g. duplicate email)
- `422` — validation errors

---

## 📊 Database Design

- Indexed access patterns:
  - `user_id`
  - `(user_id, status)`
- Ownership enforced at query level
- Designed for predictable query behavior
- Soft deletes (optional, documented decision)

---

## 🧪 Testing Strategy

- Unit tests for business logic
- Integration tests for API behavior
- Manual misuse testing via client and API tools

Focus is on **correctness over coverage metrics**.

---

## 🚀 Running the Project

### Backend
    ```bash
    uvicorn app.main:app --reload


## 📈 Future Improvements

- Refresh token flow
- Role-based access control
- Rate limiting
- API v2 evolution
- Background tasks (notifications, cleanup)

## 🎤 Interview Talking Points

- Clean API contracts and failure handling
- Stateless authentication tradeoffs
- Indexing decisions driven by query patterns
- Clear separation of concerns
- Client-agnostic backend design

## 📌 Final Note

This project is built to demonstrate engineering judgment, not UI polish.

The focus is on:

- How decisions were made

- Why tradeoffs exist

- How the system behaves under failure