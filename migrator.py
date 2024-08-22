import time
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Definir el alcance
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Autenticación y autorización
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES,  redirect_uri='http://localhost:8000')
credentials = flow.run_local_server(port=8080)
os.system('python -m webbrowser -t "http://localhost:8080"')
input("Inicia sesión en tu cuenta de YouTube y presiona Enter...")

# Crear un servicio de la API de YouTube
youtube = build('youtube', 'v3', credentials=credentials)

print("Elige una opción:")
print("1. Crear un archivo con los canales suscritos (canales_subscritos.txt)")
print("2. Suscribirse a los canales listados en canales_subscritos.txt")
opcion = input("Introduce el número de tu opción: ")

if opcion == "1":
    todos_los_canales = []
    request = youtube.subscriptions().list(
        part="snippet",
        mine=True,
        maxResults=500
        
    )
    response = request.execute()
    todos_los_canales.extend(response['items'])
    while 'nextPageToken' in response:
        request = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        todos_los_canales.extend(response['items'])
    with open('canales_subscritos.txt', 'w') as file:
        for item in todos_los_canales:
            channel_id = item['snippet']['resourceId']['channelId']
            file.write(f"{channel_id}\n")
        print("IDs de todos los canales suscritos guardados en canales_subscritos.txt.")

if opcion == "2":
    with open('canales_subscritos.txt', 'r') as file:
        canales = [line.strip() for line in file.readlines()]

    
    for canal in canales:
        try:
            youtube.subscriptions().insert(
                part="snippet",
                body={
                    "snippet": {
                        "resourceId": {
                            "kind": "youtube#channel",
                            "channelId": canal
                        }
                    }
                }
            ).execute()
            print(f"Suscrito a: {canal}")
        except Exception as e:
            print(f"Error al suscribirse a {canal}: {str(e)}")
        time.sleep(15)

