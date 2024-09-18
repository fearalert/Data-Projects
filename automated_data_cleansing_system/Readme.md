# Automated Data Cleansing System

## Project Description

This project is designed to automate data cleansing and transformation processes. It fetches raw data from a database, cleanses and transforms it, and saves the cleaned data back into the database. Additionally, the system exports the cleaned data to a CSV file for easy visualization in Power BI or other data analysis tools.

### Key Features
- **Data Fetching**: Retrieve raw data from the database.
- **Data Cleansing**: Remove duplicates and handle missing values.
- **Data Transformation**: Standardize column names and formats.
- **Data Export**: Save the cleaned data back into the database and export it as a CSV file.

### Technologies Used
- Python
- SQLite (or MySQL)
- Pandas
- SQLAlchemy
- Airflow (for scheduling)
- Power BI (for data visualization)

## Folder Structure
```sh
data-cleansing-project/
│
├── dags/
│   └── data_cleansing_dag.py    
│
├── scripts/
│   └── data_cleansing.py           
│
├── data/
│   └── raw_data.csv                 
│
├── .env                            
├── requirements.txt                
├── README.md                       
├── data-cleansing-env/             
│   ├── bin/                        
│   ├── Scripts/                    
│   ├── lib/                        
│   ├── Lib/                        
│   └── pyvenv.cfg                 
│
```

## Project Setup Instructions

### Prerequisites
1. **Python 3.x**: Ensure that Python is installed on your system.
2. **SQLite or MySQL**: Choose either SQLite or MySQL as your database.
3. **Power BI**: Install Power BI for visualization (Optional).

### Steps to Run the Project

1. **Clone the Repository**
```bash
   git clone https://github.com/fearalert/Data-Projects
   cd automated_data_cleansing_system
```

## 2. Set Up Virtual Environment

It is recommended to use a virtual environment to avoid dependency conflicts.

```bash
# Create a virtual environment
python3 -m venv data-cleansing-env

# Activate the virtual environment
source data-cleansing-env/bin/activate  # On Windows: data-cleansing-env\Scripts\activate
```

## 3. Install the Dependencies
Install the required packages listed in the ```requirements.txt ``` file.

```bash
pip install -r requirements.txt
```
## 4. Configure the Environment Variables
Create a ```.env ``` file in the project root directory and define your database URI for SQLite or MySQL (If applicable).


## 5. Initialize the SQLite Database
If you're using SQLite, initialize the SQLite database using the following command:
```bash
sqlite3 my_databse.db
```

## 6. Create raw_data Table and Import Data
Create a raw_data table in the SQLite or MySQL database. Run the following SQL commands in your database:

```SQL
CREATE TABLE raw_data (
    PatientId TEXT,
    AppointmentID TEXT,
    Gender TEXT,
    ScheduledDay TEXT,
    AppointmentDay TEXT,
    Age INTEGER,
    Neighbourhood TEXT,
    Scholarship INTEGER,
    Hipertension INTEGER,
    Diabetes INTEGER,
    Alcoholism INTEGER,
    Handcap INTEGER,
    SMS_received INTEGER,
    No_show TEXT
);
```
Then, import the data from the CSV file into the ```raw_data``` table.

## 7. python3 scripts/data_cleansing.py
Now, run the Python script ```data_cleansing.py``` to fetch, cleanse, and transform the data: