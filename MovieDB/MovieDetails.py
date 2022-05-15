import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(s)
    return conn;
if __name__ == '__main__':
    conn=create_connection(r"C:\sqlite\movieDatabase.db")
    cur=conn.cursor()
    cur.execute("SELECT m.movie_name, a.actor_name, d.director_name from movies m, actors a, directors d, actmovrel b where a.actor_ID=b.actor_ID and b.movie_ID=m.movie_ID and d.director_ID=m.director")
    rows=cur.fetchall()
    print("Movie Name\tActor Names\t\tDirector Name ")
    for row in rows:
        for col in row:
            print(col, end="\t")
        print()