"""
database.py - SQLite Master Database Manager for PlantaSanitus Smart Agriculture Platform
Manages Users, Roles, Scans, Multi-Farms, Fields, NPK Soil Tests, Marketplace Products,
Orders, Reviews, Forum Posts, Notifications, and System Audits.
"""

import sqlite3
import os
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(__file__), "plantasanitus.db")

def get_db_connection():
    """Create a database connection with dictionary-like row access."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize all master database tables if they do not exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Users & Account Manager Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'farmer', -- 'farmer', 'seller', 'admin'
            full_name TEXT,
            phone TEXT,
            created_at TEXT NOT NULL
        )
    """)

    # 2. Plant Leaf Scans & XAI Diagnostics Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            filename TEXT NOT NULL,
            image_path TEXT NOT NULL,
            crop TEXT NOT NULL,
            disease TEXT NOT NULL,
            label_key TEXT NOT NULL,
            status TEXT NOT NULL,
            confidence REAL NOT NULL,
            severity_level TEXT, -- 'Mild', 'Moderate', 'Severe'
            severity_percent REAL,
            urgency TEXT, -- 'Low', 'Medium', 'High', 'Critical'
            recovery_time TEXT,
            scientific_name TEXT,
            xai_highlights TEXT, -- JSON coordinates for bounding boxes
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    # 3. Multi-Farm & Field Management Tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS farms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            farm_name TEXT NOT NULL,
            area_acres REAL NOT NULL,
            crop_type TEXT NOT NULL,
            location TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fields (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farm_id INTEGER NOT NULL,
            field_name TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Healthy', -- 'Healthy', 'Diseased', 'Harvested'
            notes TEXT,
            FOREIGN KEY (farm_id) REFERENCES farms (id) ON DELETE CASCADE
        )
    """)

    # 4. NPK Soil Health Tests Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS soil_tests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            ph REAL NOT NULL,
            nitrogen REAL NOT NULL,
            phosphorus REAL NOT NULL,
            potassium REAL NOT NULL,
            recommendation TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    # 5. Marketplace Products & Inventory Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seller_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            type TEXT NOT NULL, -- 'organic' or 'chemical'
            target_disease TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 10,
            description TEXT,
            usage_steps TEXT,
            image_url TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (seller_id) REFERENCES users (id)
        )
    """)

    # 6. Orders & Digital Payment Tracking Tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            total_amount REAL NOT NULL,
            payment_method TEXT NOT NULL, -- 'UPI', 'CARD', 'COD'
            payment_status TEXT NOT NULL DEFAULT 'Completed',
            order_status TEXT NOT NULL DEFAULT 'Order Placed', -- 'Order Placed', 'Processing', 'In Transit', 'Delivered', 'Cancelled'
            delivery_date TEXT,
            shipping_address TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    """)

    # 7. Product Reviews Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            rating INTEGER NOT NULL, -- 1 to 5
            comment TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    """)

    # 8. Community Forum Tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS forum_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            image_url TEXT,
            is_expert_verified INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS forum_replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES forum_posts (id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    # 9. Notifications Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            type TEXT NOT NULL, -- 'weather', 'order', 'scan', 'system'
            is_read INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()
    conn.close()

# --- USER & ACCOUNT MANAGEMENT FUNCTIONS ---

def create_user(username, email, password_hash, role='farmer', full_name='', phone=''):
    """Create a new user account with specified role."""
    init_db()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, email, password_hash, role, full_name, phone, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (username, email, password_hash, role, full_name, phone, created_at))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except sqlite3.IntegrityError:
        conn.close()
        return None

def get_user_by_username(username):
    """Retrieve user by username."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_user_by_id(user_id):
    """Retrieve user profile by ID."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def update_user_profile(user_id, full_name, phone, email):
    """Update user account settings."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users SET full_name = ?, phone = ?, email = ? WHERE id = ?
    """, (full_name, phone, email, user_id))
    conn.commit()
    conn.close()

# --- SCAN HISTORY FUNCTIONS ---

def save_scan(user_id, filename, image_path, crop, disease, label_key, status, confidence, 
              severity_level="Mild", severity_percent=15.0, urgency="Medium", recovery_time="7-10 Days", 
              scientific_name="", xai_highlights="[]"):
    """Insert diagnostic scan record linked to user."""
    init_db()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO scans (user_id, filename, image_path, crop, disease, label_key, status, confidence, 
                           severity_level, severity_percent, urgency, recovery_time, scientific_name, xai_highlights, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, filename, image_path, crop, disease, label_key, status, confidence, 
          severity_level, severity_percent, urgency, recovery_time, scientific_name, xai_highlights, created_at))
    conn.commit()
    scan_id = cursor.lastrowid
    conn.close()
    return scan_id

def get_user_scans(user_id=None, limit=100, status_filter=None):
    """Retrieve scans, optionally filtered by user ID and status."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM scans WHERE 1=1"
    params = []
    if user_id:
        query += " AND user_id = ?"
        params.append(user_id)
    if status_filter:
        query += " AND status = ?"
        params.append(status_filter)
    query += " ORDER BY id DESC LIMIT ?"
    params.append(limit)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_scan_by_id(scan_id):
    """Retrieve scan by ID."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans WHERE id = ?", (scan_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def delete_scan(scan_id):
    """Delete scan record."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scans WHERE id = ?", (scan_id,))
    conn.commit()
    conn.close()

# --- MARKETPLACE & PRODUCTS FUNCTIONS ---

def get_all_products(product_type=None, search=None):
    """Fetch marketplace products with optional filtering."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT p.*, u.username as seller_name FROM products p JOIN users u ON p.seller_id = u.id WHERE 1=1"
    params = []
    if product_type:
        query += " AND p.type = ?"
        params.append(product_type)
    if search:
        query += " AND (p.name LIKE ? OR p.target_disease LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])
    query += " ORDER BY p.id DESC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_product_by_id(product_id):
    """Fetch product details by ID."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT p.*, u.username as seller_name FROM products p JOIN users u ON p.seller_id = u.id WHERE p.id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def add_product(seller_id, name, p_type, target_disease, price, stock, description, usage_steps, image_url=''):
    """Seller tool to list new agro-medicine product."""
    init_db()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (seller_id, name, type, target_disease, price, stock, description, usage_steps, image_url, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (seller_id, name, p_type, target_disease, price, stock, description, usage_steps, image_url, created_at))
    conn.commit()
    prod_id = cursor.lastrowid
    conn.close()
    return prod_id

def get_seller_products(seller_id):
    """Get all products listed by a seller."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE seller_id = ? ORDER BY id DESC", (seller_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

# --- ORDERS & CHECKOUT FUNCTIONS ---

def create_order(user_id, items, total_amount, payment_method, shipping_address):
    """Create a new order and reduce stock."""
    init_db()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    delivery_date = datetime.now().strftime("%Y-%m-%d") + " (Est. 3-5 Days)"
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO orders (user_id, total_amount, payment_method, payment_status, order_status, delivery_date, shipping_address, created_at)
        VALUES (?, ?, ?, 'Completed', 'Order Placed', ?, ?, ?)
    """, (user_id, total_amount, payment_method, delivery_date, shipping_address, created_at))
    order_id = cursor.lastrowid
    
    for item in items:
        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, unit_price)
            VALUES (?, ?, ?, ?)
        """, (order_id, item['product_id'], item['quantity'], item['unit_price']))
        
        # Deduct product stock
        cursor.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (item['quantity'], item['product_id']))
        
    conn.commit()
    conn.close()
    return order_id

def get_user_orders(user_id):
    """Fetch orders for a specific user with item details."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE user_id = ? ORDER BY id DESC", (user_id,))
    orders = [dict(r) for r in cursor.fetchall()]
    
    for o in orders:
        cursor.execute("""
            SELECT oi.*, p.name as product_name, p.image_url 
            FROM order_items oi 
            JOIN products p ON oi.product_id = p.id 
            WHERE oi.order_id = ?
        """, (o['id'],))
        o['items'] = [dict(r) for r in cursor.fetchall()]
        
    conn.close()
    return orders

def update_order_status(order_id, new_status):
    """Update order shipping status."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET order_status = ? WHERE id = ?", (new_status, order_id))
    conn.commit()
    conn.close()

# --- SEED DEFAULT USERS & DEMO PRODUCTS ---

def seed_demo_data():
    """Populate default accounts (Farmer, Seller, Admin) and initial agro-medicine catalog."""
    init_db()
    from werkzeug.security import generate_password_hash
    
    # 1. Seed Accounts
    if not get_user_by_username("farmer"):
        create_user("farmer", "farmer@plantasanitus.org", generate_password_hash("farmer123"), "farmer", "Rajesh Kumar", "+91 9876543210")
    if not get_user_by_username("seller"):
        create_user("seller", "seller@plantasanitus.org", generate_password_hash("seller123"), "seller", "AgroCare Chemicals Ltd.", "+91 9812345678")
    if not get_user_by_username("admin"):
        create_user("admin", "admin@plantasanitus.org", generate_password_hash("admin123"), "admin", "System Administrator", "+91 9000000000")
        
    # 2. Seed Agro-Medicine Products
    seller = get_user_by_username("seller")
    if seller and len(get_all_products()) == 0:
        seller_id = seller['id']
        add_product(
            seller_id,
            "Bio-Neem Cold Pressed Organic Oil (1L)",
            "organic",
            "Early Blight, Spider Mites, Powdery Mildew",
            14.50,
            45,
            "100% pure cold-pressed neem oil rich in Azadirachtin. Inhibits fungal spore germination and smothers insect pests.",
            "Mix 10ml per 1 liter of warm water with 2 drops of liquid dish soap. Spray thoroughly on leaf uppers and undersides early in the morning every 7 days.",
            "/static/samples/tomato_late_blight.jpg"
        )
        add_product(
            seller_id,
            "Copper Fungicide Extra 50 WP (500g)",
            "chemical",
            "Late Blight, Apple Scab, Bacterial Spot",
            19.99,
            30,
            "High-grade Copper Hydroxide broad-spectrum protectant fungicide for controlling leaf blights, spot diseases, and cankers.",
            "Dissolve 25g in 10 liters of water. Apply using a fine mist sprayer. Repeat application every 10 to 14 days during wet risk periods.",
            "/static/samples/apple_scab.jpg"
        )
        add_product(
            seller_id,
            "Mancozeb 75% WDG Protectant (1kg)",
            "chemical",
            "Common Rust, Septoria Spot, Downy Mildew",
            22.00,
            12,
            "Multi-site protective fungicide preventing fungal cell respiration. Ideal for crop disease management.",
            "Mix 30g in 15 liters of clean water. Apply prior to disease establishment or upon first symptom sight.",
            "/static/samples/corn_common_rust.jpg"
        )

# Run seeding on module load
init_db()
seed_demo_data()
