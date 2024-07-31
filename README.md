# Random Person Data Generator
This project generates 100 Excel files, each containing 50 entries of random person data, including names, ages, and email addresses. The data is generated using the Faker library and saved in Excel format using pandas.

### Features
* Generates realistic random data for names, ages, and email addresses.
* Creates 100 Excel files with unique data.
* Customizable number of entries per file and age range.

### Requirements
* Python 3.6 or higher
* 'pandas' library
* 'faker' library

### Installation
1. Clone the repository:

`git clone https://github.com/vinodvv/generate-excel-files.git`

`cd generate-excel-files`

2. Install the required packages:

`pip install pandas faker openpyxl`

### Usage
1. ##### Run the script:

`python main.py`

By default, this will generate 100 Excel files, each containing 50 entries. The files will be saved in the 'person_data_files' directory with names in the format 'person_data_i.xlsx',
where 'i' is the file number.

2. ##### Modify the number of entries or files:

   You can change the number of entries per file by passing a different value to the 'generate_person_data' function. To change the number of files generated, modify the loop range in the main part of the script.

### File Structure
* 'main.py': The main script that generates the data and saves it to Excel files.

### Example Output
Each Excel file contains three columns:
* **Name**: A randomly generated full name.
* **Age**: A randomly generated age between 18 and 60.
* **Email**: A randomly generated email address.

### License
This project is licensed under the MIT License. See the 'LICENSE' file for details.

### Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

### Acknowledgements
* Faker for generating realistic random data.
* pandas for data manipulation and file handling.

### Contact
For any questions or inquiries, please contact Vinod VV at vinovijayan@gmail.com