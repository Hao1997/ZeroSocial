import psycopg2 as pgadmin
import uuid
from datetime import datetime

class Database:
    cursor = None
    db_name = "ZeroSocial"
    db_host = "localhost"
    db_user = "postgres"
    db_password = "delberter"
    def __init__(self):
        try:

            connection = pgadmin.connect(dbname = self.db_name, user = self.db_user, host = self.db_host, password = self.db_password);
            self.cursor = connection.cursor();
        except Exception as e:
            print("Failed to connect to database with error \n" + e)



    def add_instagram_user(self, username, posts, followers, following):
        try:
            user_uuid = uuid.uuid4()
            type = 'Instagram'
            self.cursor.execute("""
                INSERT INTO "Instagram_User" values ('{uuid}', '{username}', '{date_created}', '{date_modified}', '{type}', {posts}, {followers}, {following}, {isFollowing}, {isFollowed})

            """.format(uuid = str(uuid.uuid4()), username = username, date_created = datetime.utcnow(), date_modified = datetime.utcnow(), type = type,
                       posts = posts, followers = followers, following = following, isFollowing = True, isFollowed = False))
        except Exception as e:
            print(e)

print(datetime.utcnow())
database = Database()
database.add_instagram_user("Instagram User 1 ", 2, 3, 4)