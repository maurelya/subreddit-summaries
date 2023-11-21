import json
from src.main.app import app


def test_landing_page(client):
    landing = client.get('/')
    html = landing.data.decode()
    assert landing.status_code == 200
    assert "<title>Subreddit Summaries</title>" in html
    assert '<input class="submit" type="submit" value="Submit">' in html
    

def test_healthcheck_api(client):
    response = client.get('/healthcheck')
    response_json = response.get_json()
    assert response_json['results'][0]['output'] == 'SQLite database is ok'
    print("response: ", json.dumps(response_json, indent=4))

def test_metrics_api(client):
    response = client.get('/metrics')
    assert b"python_gc_objects_collected_total" in response.data
    

