from boxsdk import Client, OAuth2

CLIENT_ID = '1y5e8nsv6lcyx9i05y5rfjuvdv4rxu1k'
CLIENT_SECRET = 'TOSKaweCeV9i85tLnyRto4YuZk6fYlqK'
ACCESS_TOKEN = 'GIoGjW9h3kD53fBTjnGGuRAFBQdZT4je' # this is the developer token
BDFOLDERNAME='BDTest'

oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN)

client = Client(oauth2)

my = client.user(user_id='me').get()
print(my.name)
print(my.login)
print(my.avatar_url)
folder = client.search().query(
    'BDTest'
)
for item in folder:
    folder = item #jankball code, I know, but having needless nested for loops hurts my eyes even more.
print(folder)