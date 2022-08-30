import os,sys,time,json,requests

# Sumber API: https://short-link-api.vercel.app/?query=
# Author Vebrian Developer
# don't forget follow my github @vebriann

os.system("cls")
url = "https://short-link-api.vercel.app/?query="

mylink = input(" masukan link anda: ")
if mylink in ["", " "]:
    print(" maaf pilihan tidak boleh kosong ")
    exit()
else:
    try:
        response = requests.get(url+mylink).json()
        print("\n results shortner link\n")
        for i in response:
            print(" Domain: "+response[i])
    except requests.exceptions.ConnectionError:
        print(" Maaf terjadi kesalahan jaringan")
        exit()