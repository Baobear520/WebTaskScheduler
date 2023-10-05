import requests
import random


def main():
    make_connection()

def make_connection():

    """ Making a request to the URL """

    title, body = content_creator()
    payload = {
        'userId': 1,
        "title": title,
        "body": body
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts',data=payload)
    print(response.status_code, response.json())
    

def task_schedule():
    pass

def content_creator():

    """Creating title and body of the post"""

    title = random.choice(['sup','hi there','hello'])
    body = random.choice(["I'm ok","Awesome","Oki doki"])
    return title, body

if __name__ == '__main__':
    main()