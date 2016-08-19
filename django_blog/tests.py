# Reference: http://getblimp.github.io/django-rest-framework-jwt/

import datetime
import json
import os
import requests

base_url = 'http://127.0.0.1:8000/api/'

register_url = base_url + 'users/register/'

login_url = base_url + 'auth/token/'

verify_url = login_url + 'verify/'

refresh_url = login_url + 'refresh/'

posts_list_url = base_url + 'posts/'

posts_create_url = base_url + 'posts/create/'

comments_create_url = base_url + 'comments/create/'


# user information

class TestUser:
    """
    A user class for User Authentication API tests
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.token = ''

    def print_json(self, json_data, prompt=''):
        if len(prompt) > 0:
            print(prompt)
        print(json.dumps(json_data, indent=2))

    def register(self):
        """
        User register API test
        :return: response json object from register API
        """
        data = {
            'username': self.username,
            'email': self.email,
            'email2': self.email,
            'password': self.password,
        }
        register_r = requests.post(register_url, data=data)
        json_data = register_r.json()  # register_r.text
        self.print_json(json_data, 'The response of register API: ')
        return json_data

    def login(self):
        """
        login token API test
        :return: response json object from login API
        """
        data = {
            'username': self.username,
            'password': self.password,
        }
        login_r = requests.post(login_url, data=data)
        json_data = login_r.json()  # login_r.text
        self.print_json(json_data, 'The response of login token API: ')
        self.token = json_data['token']
        return json_data

    def verify_token(self, token):
        """
        Auth token verify API test
        :return: response json object from verify token API
        """
        data = {
            'token': token,
        }
        verify_r = requests.post(verify_url, data=data)
        json_data = verify_r.json()  # verify_r.text
        self.print_json(json_data, 'The response of verify token API: ')
        return json_data

    def refresh_token(self):
        """
        Auth token refresh API test
        :return: response json object from refresh token API
        """
        data = {
            'token': self.token,
        }
        refresh_r = requests.post(refresh_url, data=data)
        json_data = refresh_r.json()  # login_r.text
        self.print_json(json_data, 'The response of refresh token API: ')
        self.token = json_data['token']
        return json_data

    def create_post(self, title, content, publish):
        """
        posts create API test
        :param title: post title
        :param content: post content, support Markdown format
        :param publish: publish date time
        :return: response json object from posts create API
        """
        data = {
            'title' : title,
            'content' : content,
            'publish' : publish,
        }
        headers = {
            'Authorization': 'JWT %s' % (self.token)
        }
        post_c_r = requests.post(posts_create_url, headers=headers, data=data)
        json_data = post_c_r.json()
        self.print_json(json_data, 'The response of posts create API: ')
        return json_data

    def create_comment(self, content, slug):
        """
        comments create API test for commenting a post
        :param content: comment actual content
        :param slug: identifier for the post
        :return: response json object from comments create API
        """
        data = {
            'content': content,
        }
        headers = {
            'Authorization': 'JWT %s' % (self.token)
        }
        test_url = comments_create_url + '?type=post&slug=' + slug
        comment_c_r = requests.post(test_url, headers=headers, data=data)
        json_data = comment_c_r.json()
        self.print_json(json_data, 'The response of comments create API: ')
        return json_data

    def create_reply(self, content, parent_id):
        """
        comments create API test for commenting a comment
        :param content: comment actual content
        :param parent_id: identifier for the parent comment
        :return: response json object from comments create API
        """
        data = {
            'content': content,
        }
        headers = {
            'Authorization': 'JWT %s' % (self.token)
        }
        test_url = comments_create_url + '?type=comment&parent_id=' + str(parent_id)
        comment_c_r = requests.post(test_url, headers=headers, data=data)
        json_data = comment_c_r.json()
        self.print_json(json_data, 'The response of comments create API: ')
        return json_data



# Util function

def get_latest_post_url():
    posts_list_r = requests.get(posts_list_url)
    json_data = posts_list_r.json()
    return json_data['results'][0]['url']

def get_post_slug(url):
    post_detail_r = requests.get(url)
    json_data = post_detail_r.json()
    return json_data['slug']


# Test function

def run_api_test(test_username, test_email, test_password):
    """
    Test the authentication API, post create API, comment create API
    :param test_username: username for the test user
    :param test_email: email address for the test user
    :param test_password: password for the test user
    :return: print json object in the console
    """

    # Create a user instance
    test_user = TestUser(test_username, test_email, test_password)

    # User registration
    test_user.register()

    # User login
    test_user.login()

    # Verfity token
    test_user.verify_token(test_user.token)

    # Create a post
    post_title = 'Post API Test %s' % (os.getpid())
    post_content = 'This is some machine generated content by API test %s.' % (os.getpid())
    post_publish = datetime.datetime.now()
    test_user.create_post(post_title, post_content, post_publish)

    # Obtain post url
    post_url = get_latest_post_url()
    post_slug = get_post_slug(post_url)

    # Create a comment for post
    comment_content = 'Comment API test %s for creating comment' % (os.getpid())
    comment_c_json = test_user.create_comment(comment_content, post_slug)

    # Refresh token
    test_user.refresh_token()

    # Create a reply for comment
    comment_id = comment_c_json['id']
    reply_content = 'Comment API test %s for creating reply' % (os.getpid())
    reply_c_json = test_user.create_reply(reply_content, comment_id)


if __name__ == '__main__':
    # Basic information
    test_username = 'dirac'
    test_email = 'dirac@gmail.com'
    test_password = 'dirac1902'
    run_api_test(test_username, test_email, test_password)
