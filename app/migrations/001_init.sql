-- Initial DB schema (simplified)
CREATE TABLE orgs (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    org_id INT REFERENCES orgs(id),
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    org_id INT REFERENCES orgs(id),
    name TEXT NOT NULL,
    location TEXT,
    notes TEXT,
    status TEXT,
    created_by INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);
