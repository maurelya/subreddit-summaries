# subreddit-summaries

This is a web application that sends an email to a subscribed user an AI generated summary of a subreddit's top post

## Want to use this project?

1. Fork/Clone

2. Project Setup
    ```sh
    $ export FLASK_APP=src/main/app.py
    $ python3 -m venv env
    $ source venv/bin/activate
    ```

3. Run the Flask locally app:

    ```sh
    (env)$ pip install -r requirements.txt
    (env)$ npm run dev
    ```

    Navigate to [http://localhost:2700](http://localhost:2700)

## Live application
1. Go to https://subreddit-summaries.onrender.com
2. Fill in the fields and click on the submit button


## API endpoints
- POST `/add_new_user`
- GET `/get_all_users`
- GET `/get_all_posts`
- POST `/add_post`
- POST `/send_email`
- GET `/send_all_email`
- GET `/rabbitmq_consume`

## Production Monitoring
- `/healthcheck` endpoint that returns a json object verifying the database is up and running
- `/metrics` endpoint uses the prometheus flask library to return metrics

## Testing
- Run the following command to run the tests: `pytest -s`
    - The tests are located under `src/test`

## Continuous Integration / Continuous Delivery
 - Github actions was used for CI under the `/.github/workflows/main.yml` folders
 - [Render](render.com) was used for CD

 ## Data Persistence

- SQLite was used as the database and SQLAlchemy was used as the ORM

## Data Analysis

- For each summary of a post, sentiment analysis is perform to detect the emotion the post is trying to convery
- This function can be found under `src/main/watsonx`

## Data Collection

- Data is collected from reddit by using the [PRAW](https://praw.readthedocs.io/en/stable/), The Python Reddit API Wrapper.
- This function can be found under `src/main/reddit`