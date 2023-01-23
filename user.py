class User:
 def __init__(self, email, name, password, current_job_title):
  self.email = email
  self.name = name
  self.password = password
  self.current_job_title = current_job_title\

 def change_password(self, new_password):
  self.password = new_password

 def change_job_title(self, new_job_title):
  self.current_job_title = new_job_title

 def get_user_info(self):
  print(f"User {self.name} currently works as a {self.current_job_title}. You may contact them at {self.email}")

user = User("t@mail.com", "Tekle", "pass", "Software Engineer")
user.get_user_info()
user.change_job_title("Fullstack Software Developer")
user.get_user_info()
