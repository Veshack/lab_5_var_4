import re
import csv
import itertools 



print('№1')
text = open('task1-en.txt').read().strip()

dashes = re.findall(r'\w+(?:-\w+)+', text)
for dash in dashes:
    print(dash)

staples = re.findall(r'\(.*?\)', text)
for staple in staples:
    print(staple)

print()
print('№2')

with open('task2.html', 'r', encoding='utf-8') as file:
    text2 = file.read()

links = re.findall(r'https?://[^\s"]+\.com', text2)

for link in links:
    print(link)



print('\nРезультат №3 в файле task3.csv')
text3 = open('task3.txt').read().strip()

ids = list(re.findall(r'\s\d+\s', text3))
surnames = list(re.findall(r'\s[A-Za-z]+\s', text3))
emails = list(re.findall(r'\w+@\w+', text3))
dates = list(re.findall(r'\d{4}-\d{2}-\d{2}', text3))
websites = list(re.findall(r'https?://[^\s"]+', text3))


with open('task3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(ids)):
        writer.writerow([f'{ids[i]} {surnames[i]} {emails[i]} {dates[i]} {websites[i]}'])
