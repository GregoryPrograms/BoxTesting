from boxsdk import Client, OAuth2

CLIENT_ID = '1y5e8nsv6lcyx9i05y5rfjuvdv4rxu1k'
CLIENT_SECRET = 'TOSKaweCeV9i85tLnyRto4YuZk6fYlqK'
ACCESS_TOKEN = 'BJgvmJO9GDv14PKyOCT5CYMADgXz6xH7' # this is the developer token
BDFOLDERNAME='BDTest'

oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN)

client = Client(oauth2)

my = client.user(user_id='me').get()
rootFolder = client.search().query(
    'BDTest'
)
for contents in rootFolder:
    folderList = client.folder(folder_id=contents.id).get_items()
for folder in folderList:
    for charIndex in range(6,len(folder.name)):
        if folder.name[charIndex].isalpha():
            updated_folder = client.folder(folder.id).update_info({
                            'name': folder.name[:charIndex].strip()
                           })
            break
