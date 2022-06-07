import json



def read_json(file_path):
    with open ('D:\Lina\Training\PYTHON-WORKSHOP\repositories\json_repository.py', 'r') as f:
        try:
                return json.load(f)
        except:
            print("An exception occurred")

