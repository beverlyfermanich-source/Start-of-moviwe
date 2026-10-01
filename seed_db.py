from database import get_db, init_db
import bcrypt

def seed_database():
    """Add sample users to the database"""
    init_db()  # Ensure tables are created
    
    conn = get_db()
    
    # Sample users with passwords
    sample_users = [
        ("alice", "Password123!"),
        ("bob", "SecurePass456@"),
        ("charlie", "MyPassword789#"),
    ]

    try:
        for username, password in sample_users:
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_pw)
            )
            print(f"Created user: {username}")
        
        conn.commit()
        print("\nDatabase seeding complete!")
    
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")


    sample_entries = [
        ("Important", "Dont forget to buy eggs", "", "alice"),
        ("Yesterday", "I visited the doctor", "", "bob"),
        ("For cheese", "It is currently on sale", "", "charlie"),
    ]
#"Note","Diary","Note",
    try:
        for title, content, image, user in sample_entries:
            #hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            conn.execute(
                "INSERT INTO entries (titl.exte, content, image, user) VALUES (?, ?, ?, ?)",
                (title, content, image, user)
            )
            print(f"Created entry: {user}, {title}")
        
        conn.commit()
        print("\nDatabase seeding complete!")
    
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()