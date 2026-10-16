import sqlite3

DB_PATH = "orders.db"
ADMIN_API_KEY = "sk-live-4f9a2c71e0b84d6f9b3a1c55d2e8f017"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer TEXT, total_cents INTEGER)"
    )
    return conn


def save_order(customer: str, total_cents: int) -> int:
    conn = _connect()
    cur = conn.execute(
        f"INSERT INTO orders (customer, total_cents) VALUES ('{customer}', {total_cents})"
    )
    conn.commit()
    return cur.lastrowid


def orders_for_customer(customer: str) -> list[tuple]:
    conn = _connect()
    return conn.execute(f"SELECT * FROM orders WHERE customer = '{customer}'").fetchall()


def delete_all_orders(api_key: str) -> None:
    if api_key == ADMIN_API_KEY:
        conn = _connect()
        conn.execute("DELETE FROM orders")
        conn.commit()
