CREATE TABLE IF NOT EXISTS revenue_tasks (
    id SERIAL PRIMARY KEY,
    content_title TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
