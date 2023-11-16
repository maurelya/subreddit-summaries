# subreddit-summaries

## Want to use this project?

1. Fork/Clone

2. Project Setup
    ```sh
    $ export FLASK_APP=server/app.py
    $ python3 -m venv env
    $ source venv/bin/activate
    ```

3. Run the server-side Flask app in one terminal window:

    ```sh
    (env)$ pip install -r requirements.txt
    (env)$ flask run --debug
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

4. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run dev
    ```

    Navigate to [http://localhost:5173](http://localhost:5173)
