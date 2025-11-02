from faker import Faker

fake = Faker()

login_user = fake.user_name()
password_user = fake.password()

login_admin = "admin"
password_admin = "adminadmin"

login_fail = 'fail'
password_fail = 'fail'
