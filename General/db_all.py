import psycopg2 as pgadmin
import uuid
from datetime import datetime
from General import time_utility as time

class Database:
    cursor = None
    connection = None;
    db_name = "ZeroSocial"
    db_host = "localhost"
    db_user = "postgres"
    db_password = "delberter"
    def __init__(self):
        try:
            self.connection = pgadmin.connect(dbname = self.db_name, user = self.db_user, host = self.db_host, password = self.db_password);
            self.cursor = self.connection.cursor();
        except Exception as e:
            print("Failed to connect to database with error \n" + e)



    def add_instagram_user(self, username, posts, followers, following, isFollowing = True, isFollowed = False):
        try:

            user_uuid = uuid.uuid4()
            type = 'Instagram'
            # print("""
            #     INSERT INTO "Instagram_User" values ('{uuid}', '{username}', '{date_created}', '{date_modified}', '{type}', {posts}, {followers}, {following}, {isFollowing}, {isFollowed})
            #
            # """.format(uuid = str(uuid.uuid4()), username = username, date_created = datetime.utcnow(), date_modified = datetime.utcnow(), type = type,
            #            posts = posts, followers = followers, following = following, isFollowing = isFollowing, isFollowed = isFollowed))
            self.cursor.execute("""
                INSERT INTO "Instagram_User" values ('{uuid}', '{username}', '{date_created}', '{date_modified}', '{type}', {posts}, {followers}, {following}, {isFollowing}, {isFollowed})

            """.format(uuid = str(uuid.uuid4()), username = username, date_created = datetime.utcnow(), date_modified = datetime.utcnow(), type = type,
                       posts = posts, followers = followers, following = following, isFollowing = isFollowing, isFollowed = isFollowed))
        except Exception as e:
            print(e)

        print("Added " + username + " to database");
        time.small_timeout()

    def find_instagram_user_by_name(self, username):
        try:
            self.cursor.execute("""
                SELECT *
                FROM "Instagram_User"
                WHERE username = '{username}'

            """.format(username=username))
            time.small_timeout()
            return len(self.cursor.fetchall()) != 0
        except Exception as e:
            print(e)

    def commit(self):
        self.connection.commit()
