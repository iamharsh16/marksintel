"""
Seeds the database with initial SPPU subjects data.
Run: python scripts/seed_db.py
"""
SUBJECTS = [
    {"name": "Digital Electronics", "semester": 3, "department": "Computer Engineering"},
    {"name": "Data Structures", "semester": 3, "department": "Computer Engineering"},
    {"name": "Computer Networks", "semester": 5, "department": "Computer Engineering"},
]

if __name__ == "__main__":
    print("Seeding database...")
    # TODO: connect to DB and insert subjects
    print("Done.")
