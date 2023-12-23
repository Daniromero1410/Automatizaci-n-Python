from pytube import YouTube
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Variables de excel
file_path = 'Enlaces_VIDEOS/enlaces.xlsx'
sheet_name = 'Hoja1'
column_name = 'Videos'

# Credenciales google drive

directorio_credenciales = 'credentials_module.json'
id_folder = 'ID_CLOUD

def login():
    GoogleAuth.DEFAULT_SETTINGS['cliente_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)

    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales


# Subir un archivo a drive
def subir_archivo (ruta_archivo,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'parents': [{"kind":"drive#fileLink",\
                                                    "id":id_folder}]})
    archivo['title'] = ruta_archivo.split("/")[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()


def main ():
    df=pd.read_excel(file_path,sheet_name= sheet_name)
    column_data= df[column_name]
    videos = column_data.values
    print(videos)


    # descargar videos de youtube y subirlos a drive
    for link_video in videos:
        #descarga
        yt= YouTube(link_video)
        video  = yt.streams.get_highest_resolution()
        video.download('./YT')


        #Subir
        subir_archivo(f'YT/{video.title}.mp4',id_folder)


if __name__ == "__main__":
    main()






