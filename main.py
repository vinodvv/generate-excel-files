import pandas as pd
from faker import Faker

# Initialize Faker instance
fake = Faker()


# Function to generate random person data
def generate_person_data(num_entries=50):
    """
    Generates random person data including names, ages, and email address.
    :param num_entries: (int) The number of entries to generate. Default is 50.
    :return: A dictionary containing lists of names, ages, and email addresses.
    """
    data = {
        'Name': [fake.name() for _ in range(num_entries)],
        'Age': [fake.random_int(min=18, max=60) for _ in range(num_entries)],
        'Email': [fake.email() for _ in range(num_entries)],
    }
    return data


# Generate 100 Excel files
for i in range(1, 101):
    """
    Main loop to generate Excel files containing random person data.
    Each file contains 50 entries by default.
    
    The files are saved in the 'person_data_files' directory with names in the format: 'person_data_i.xlsx',
    where i is the file number.
    """
    # Generate data for one file
    person_data = generate_person_data()

    # Create a Dataframe
    df = pd.DataFrame(person_data)

    # Save DataFrame to an Excel file
    filename = f"person_data_files/person_data_{i}.xlsx"
    df.to_excel(filename, index=False)

    print(f"Generated {filename}")
