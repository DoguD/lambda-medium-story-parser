from chalice import Chalice
import json
import requests

app = Chalice(app_name='lambda-medium-story-parser')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/get_stories_by_username', methods=['GET'], cors=True)
def get_stories_by_username():
    # Get query parameters
    request = app.current_request
    query_params = request.query_params
    user_name = query_params['user_name']

    # Send the request to medium
    target_url = 'https://medium.com/@' + user_name + '?format=json'
    r = requests.get(url=target_url)

    # Parse data
    data = ''
    content = r.iter_lines()
    for element in content:
        data += str(element)
    data = json.loads(data.replace('])}while(1);</x>', '')[2:-1].replace('\\', ''))

    # Get stories
    stories = data['payload']['references']['Post']

    return {'status': r.status_code, 'stories': stories}
