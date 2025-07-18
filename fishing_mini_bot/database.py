import sqlite3

conn =sqlite3.connect("профиль")
cursor = conn.cursor()

def add_user(user_id, name, fishes, love_fishes):
    cursor.execute( '''
    INSERT INTO users(id, name, fishes)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        name = execlude.name
        fishes = execlude.fishes
        like_fishes = execlude.like_fishes    
        
        
    ''', (user_id, name, fishes))
    conn.commit()