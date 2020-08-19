from chalice import Chalice
import json
import requests

app = Chalice(app_name='lambda-medium-story-parser')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/get_stories', methods=['GET'], cors=True)
def get_stories():
    # Get query parameters
    request = app.current_request
    query_params = request.query_params
    profile = query_params['profile']

    # Send the request to medium
    target_url ='https://medium.com/@'+profile+'?format=json'
    r = requests.get(url=target_url)

    return {'status': r.status_code}


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
