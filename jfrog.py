import requests
import subprocess

def jfrogUpload():
    url=""
    file_path=""
    username=""
    password=""

    with open(file_path,'rb') as file:
        response = requests.put(url,auth=(username,password),data=file)

    if response.status_code == 201:
        print("\nPUT request was successful !")
    else:
        print(f"PUT request failed with status code {response.status_code}")
        print("Response content:")
        print(response.text)

    
def main():
    jfrogUpload()

if __name__="__main__":
    main()