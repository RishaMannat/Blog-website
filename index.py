import sqlite3
conn = sqlite3.connect('blog_database.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the segments table
cursor.execute('''
    CREATE TABLE segments (
        segment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        segment_name TEXT NOT NULL
    )
''')

# Create the sub_segments table
cursor.execute('''
    CREATE TABLE sub_segments (
        sub_segment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sub_segment_name TEXT NOT NULL,
        segment_id INTEGER,
        FOREIGN KEY (segment_id) REFERENCES segments(segment_id)
    )
''')

# Create the blog_content table
cursor.execute('''
    CREATE TABLE blog_content (
        content_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        sub_segment_id INTEGER,
        FOREIGN KEY (sub_segment_id) REFERENCES sub_segments(sub_segment_id)
    )
''')

# Commit the changes to the database
conn.commit()
