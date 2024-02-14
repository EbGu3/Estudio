from datetime import datetime


class BlogPost:
    def __init__(self, title, description, publish_date):
        self.title = title
        self.description = description
        self.publish_date = publish_date


def print_blog_post(blog_post):
    print('Title: ' + blog_post.title)
    print('Description: ' + blog_post.description)
    print('Published: ' + blog_post.publish_date)


title = 'Clean Code Is Great!'
description = 'Actually, writing Clean Code can be pretty fun. You\'ll see!'
date_now = datetime.now()
format_date = date_now.strftime('%Y-%m-%d %H:%M')

blog_post = BlogPost(title, description, format_date)

print_blog_post(blog_post)