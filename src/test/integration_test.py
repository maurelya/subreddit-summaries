
import json


def test_create_user(client, init_database):

    response = client.post("/add_new_user",
     data = {
         "name":"Maria Lopez",
         "email":"mlopez@gmail.com",
         "subreddit":"news"
     },
    )
    print("test_create_user: ", json.dumps(response.get_json(), indent=4))
    assert response.data == b'OK'


def test_get_all_users(client, init_database):

    response = client.get("/get_all_users")
    print("test_get_all_users: ", json.dumps(response.get_json(), indent=4))
    assert b'{"email":"test2@gmail.com","id":2,"name":"Test User 2","subreddit":"cats"}' in response.data



def test_get_all_posts(client, init_database):

    response = client.get("/get_all_posts")

    assert response.data == b'OK'


def test_add_post(client, init_database):

    response = client.post("/add_post",
     json = {
         "user_id":"1",
         "title":"mlopez@gmail.com",
         "subreddit":"tacos",
         "top_post_body":"My BF has a side hustle making and selling tacos with homemade everything from our garden. These are pollo asada yummmmmm... (via @tacos_and_beer) damn those look good. You seriously grow rice and beans in your garden?",
         "top_comment": "wow",
         "created_utc": "01/01/2024",
         "url": "url.com",
         "top_post_summary": "tacos are good",
         "summary_sentiment": "hungry",
     },
    )

    assert response.data == b'OK'

