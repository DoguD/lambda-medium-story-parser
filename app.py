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

    return data

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
