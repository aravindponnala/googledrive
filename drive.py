import mimetypes
import googleapiclient.discovery
from google.oauth2 import service_account   



google_api_client = None
scope = ['https://www.googleapis.com/auth/drive']
num_of_retries = 3
parent_folder_id = '1PnnWB-y_2q2zZORac7nZ8n9EZQNAeWLa'

credentials = service_account.Credentials.from_service_account_file(
            'service-account.json', scopes=scope)

client = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)
google_api_client = client


data = {
    'name': 'Doc_1_Sheet',
    'mimeType': 'application/vnd.google-apps.spreadsheet',
    'parents': [parent_folder_id]
}
file = google_api_client.files().create(body=data).execute()


print(file)
