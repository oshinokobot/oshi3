import ast
import random
from auth import *

def getRandomFile():

    drive = getGoogleAuth()

    print("GETTING A FILE")

    with open('file_list.txt', 'r') as file:
        content = file.read()
   
    data = ast.literal_eval(content)

    file = random.choice(data)

    title = file
    file_list = drive.ListFile({'q': "title='" + title + "'"}).GetList()
    file_id = file_list[0]['id']
    file = drive.CreateFile({'id': file_id})
    
    extension = title.split(".")[1]

    file.GetContentFile(title)

    print(title)
    print(extension)

    return {'title': title, 'extension': extension}
