# Manufacturer seeding script
import psycopg2

manufacturers = [
    {"name": "Nudura", "website": "https://www.nudura.com"},
    {"name": "Fox Blocks", "website": "https://www.foxblocks.com"},
    {"name": "BuildBlock", "website": "https://buildblock.com"},
    {"name": "SuperForm", "website": "https://www.superformicf.com"},
    {"name": "Element", "website": "https://elementicf.com"},
    {"name": "Alleguard", "website": "https://alleguard.com"},
    {"name": "QuadLock", "website": "https://quadlock.com"},
]

def seed(conn_str):
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    for m in manufacturers:
        cur.execute(
            "INSERT INTO manufacturers (name, website) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (m["name"], m["website"]),
        )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    import os
    conn_str = os.getenv("DATABASE_URL")
    seed(conn_str)
