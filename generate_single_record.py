from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate a single name, age, and email
name = fake.name()
age = fake.random_int(min=18, max=80)
email = fake.email()

# Print the generated values
print(name, email, age)
