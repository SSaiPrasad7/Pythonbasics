import os,re
import sys


def Func(file_name):
    f = open(file_name, 'r')
    contents = f.read()
    phone_num=re.search(r'\d{3}-\d{3}-\d{4}', contents)
    if phone_num:
        print(f"Phone Number is {phone_num.group()} found at location {file_name}")
        return True
    f.close()
    return False



path="C:\\Users\\venKEY\\Desktop\\sai\\Pythonbasics\\Questionnaire\\extracted_content"
for folder,subfolders,files in os.walk(path):
    print(f"Currently looking folder at{folder}")
    print("\nThe subfolder has:")
    for sub_folder in subfolders:
        print(f"\t Subfolder:{sub_folder}")
    print(f'\nThe Files are:')
    for file in files:
        print(f"\t file:{file}")
        if Func(folder+"\\"+file):
            sys.exit()