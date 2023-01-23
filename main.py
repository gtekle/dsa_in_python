from user import User
from post import Post

user_one = User("tek@mail.com", "Tekle", "password", "Software Architect")
user_one.get_user_info()

user_two = User("john@mail.com", "John", "pass", "Senior Software Architect")
user_two.get_user_info()

first_post = Post("Hello, this is my first post", user_one.name)
first_post.get_post_info()

