import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError

DEBUG = 1

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Get the current directory of input.py
current_dir = os.path.dirname(__file__)

# Construct the path to data.yml
credentials_path = os.path.join(current_dir, 'credentials.json')
token_path = os.path.join(current_dir, 'token.json')

async def authen_me() -> Resource:
	"""
	Authenticates the user and retrieves a Google Sheets API service resource.

	This function uses the Google Sheets API to print values from a sample spreadsheet.
	It first checks if the user has already authenticated by looking for the 'token.json' file.
	If the file exists, it loads the credentials from it.
	If the credentials are not valid or do not exist, the function prompts the user to log in.
	The user's credentials are then saved to the 'token.json' file for future use.

	Parameters:
	None

	Returns:
	service (Resource): A Google Sheets API service resource.
	"""
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	# TOKEN_PATH = "D:\\WORKING_container\\discord_bot_2\\discord-bot-ttcd\\main_app\\google_api\\token.json"
	# CREDENTIAL_PATH = "D:\\WORKING_container\\discord_bot_2\\discord-bot-ttcd\\main_app\\google_api\\credentials.json"
	
	if os.path.exists(token_path):
		creds = Credentials.from_authorized_user_file(token_path, SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				credentials_path, SCOPES
			)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open(token_path, "w") as token:
			token.write(creds.to_json())

	try:
		service = build("sheets", "v4", credentials=creds)
		if DEBUG:
			print("Service authenticated")
		return service
	except HttpError as err:
		print(err)

if __name__ == "__main__":
	api_service = authen_me()
	# Call the Sheets API
	# The ID and range of a sample spreadsheet.
	sheet_id = "1_SQyyxnUtre_HGpskjV9PQ9RHBfGOLLYEInrJJOFVGM"
	sheet_range = "Sheet1!A1:O5"
	sheet = api_service.spreadsheets()
	result = (
		sheet.values()
		.get(spreadsheetId=sheet_id, range=sheet_range)
		.execute()
	)
	values = result.get("values", [])

	if not values:
		print("No data found.")

	print("Name, Major:")
	for row in values:
		# Print columns A and E, which correspond to indices 0 and 4.
		print(f"{row[0]}, {row[4]}")