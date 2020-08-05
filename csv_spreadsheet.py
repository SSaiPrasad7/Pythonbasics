import csv
data=open('C:\\Users\\venKEY\\Desktop\\sai\\Pythonbasics\\FL_insurance_sample.csv',encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
for line in data_lines[:5]:
    print(line)
#Writing into .csv file
new_file=open('C:\\Users\\venKEY\\Desktop\\sai\\Pythonbasics\\myfile.csv',mode='a',newline='')
file_writer=csv.writer(new_file,delimiter=',')
file_writer.writerow(['a','b','c','d'])
file_writer.writerows([[1,2,3,4],[5,6,7,8]])
#Reading from .csv file
read_file=open('C:\\Users\\venKEY\\Desktop\\sai\\Pythonbasics\\myfile.csv',encoding='utf-8')
text=csv.reader(read_file)
print(list(text))
new_file.close()
data.close()