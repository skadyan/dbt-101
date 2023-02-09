import csv
import datetime
import os

from faker import Faker


def generate_data(record_count: int):
    headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id",
               "Address", "Zip Code", "City", "State", "Country", "Year", "Time", "Link", "Text"]
    fake = Faker('en_US')
    fake1 = Faker('en_GB')  # To generate phone numbers
    os.makedirs("target/", exist_ok=True)
    with open("target/People_data.csv", 'wt', newline='', encoding="utf-8") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(record_count):
            full_name = fake.name()
            f_name, l_name = full_name.split(" ")
            domain_name = "@testDomain.com"
            user_id = f_name + "." + l_name + domain_name

            writer.writerow({
                "Email Id": user_id,
                "Prefix": fake.prefix(),
                "Name": fake.name(),
                "Birth Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                "Phone Number": fake1.phone_number(),
                "Additional Email Id": fake.email(),
                "Address": fake.address(),
                "Zip Code": fake.zipcode(),
                "City": fake.city(),
                "State": fake.state(),
                "Country": fake.country(),
                "Year": fake.year(),
                "Time": fake.time(),
                "Link": fake.url(),
                "Text": fake.word(),
            })


if __name__ == '__main__':
    records = 500000

    generate_data(records)
    print("CSV generation complete!")
