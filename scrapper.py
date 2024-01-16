import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://cse.kiit.ac.in/faculty/?_gl=1*3yy30x*_ga*MTM5NzUzODc5OC4xNzA1MzM2MjA0*_ga_34QZ5P9757*MTcwNTMzNjIwMy4xLjEuMTcwNTMzNjI2Mi4xLjAuMA.."

response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting faculty information
faculty_info_list = []

for faculty in soup.find_all('div', class_='wmts_member'):
    # Check if 'h2' element with class 'wph_name' exists
    # teacher_div = faculty.find('div', class_ = 'wph_element wmts_horizontal_round wmts_element  wmts_member ')
    name_element = faculty.find('h2')
    name = name_element.text.strip() if name_element else "Name not found"



    faculty_info = {"Name": name}
    faculty_info_list.append(faculty_info)

# Display the extracted information
df = pd.DataFrame(faculty_info_list, columns=["Name"])
print(df)
df.to_csv('teacher.csv')
