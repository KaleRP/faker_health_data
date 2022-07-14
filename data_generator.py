import pandas as pd
import numpy as np
from typing import List
from faker import Faker
import datetime

def gen_data(num_rows: int = 10, inc_columns:List[str] = None) -> pd.DataFrame:
    """

    :param num_rows:
    :param inc_columns:
    :return:
    """
    fake = Faker()
    fake_data = []
    if inc_columns is None or len(inc_columns) == 0:
        inc_columns = ['Name', 'Age', 'Gender', 'BirthDate', 'Latitude', 'Longitude',
                       'BMI', 'HeartRate', 'SystolicBP', 'V02', 'BloodGroup']

        for _ in range(num_rows):
            extracted_data = {}
            fake_person = fake.profile()
            for col in inc_columns:
                val = None
                if col == 'Name':
                    val = fake_person['name']
                if col == 'Age':
                    val = (datetime.datetime.now().date() - fake_person['birthdate']).days / 362.25
                if col == 'Gender':
                    val = np.random.choice(["M", "F"])
                if col == 'BirthDate':
                    val = fake_person['birthdate']
                if col == 'Latitude':
                    val = fake_person['current_location'][0].real
                if col == 'Longitude':
                    val = fake_person['current_location'][1].real
                if col == 'BMI':
                    val = np.random.normal(loc=26, scale=27)
                if col == 'HeartRate':
                    val = np.random.normal(loc=80, scale=15)
                if col == 'SystolicBP':
                    val = np.random.normal(loc=128, scale=20)
                if col == 'V02':
                    val = np.random.normal(loc=44, scale=2.1)
                if col == 'BloodGroup':
                    val = fake_person['blood_group']

                extracted_data[col] = val
            fake_data.append(extracted_data)
    out = pd.DataFrame(fake_data, columns=inc_columns)
    out.to_csv('generated_data')
    return out

if __name__ == '__main__':
    print(gen_data())