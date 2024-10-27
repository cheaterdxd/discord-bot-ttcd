from .authenticator import authen_me
from .sheet_info import SHEET_ID

def read_sheet_at(api_service, sheet_range:str,sheet_id=SHEET_ID,)-> list:
    """
    Read sheet data at sheet_id and range

    Args:
        service: googleapiclient.discovery.Resource
        sheet_id: sheet id
        sheet_range: sheet range

    Returns:
        sheet data: list of row in sheet
    """
    sheet = api_service.spreadsheets()
    result = (
        sheet.values()
       .get(spreadsheetId=sheet_id, range=sheet_range)
       .execute()
    )
    return result.get("values", [])

def check_user_exist(api_service, user_info:str)->dict:
    """
    Check if user exist in sheet and return {index, role} if it exists and False otherwise
    
    Args: 
        user_info (str): name of user

    Returns: 
        Value: {index, role} if user_info exists, False otherwise
    """
    if "@" in user_info and ".com" in user_info: 
        data_mail = read_sheet_at(api_service, sheet_range="Sheet2!A2:A")
        for row in data_mail:
            if user_info in row[0]:
                user_index = data_mail.index(row)
                user_role = read_sheet_at(api_service,"Sheet2!C2:C")[user_index][0]
                return {'role': user_role, 'index': user_index}
    else:
        data_phone = read_sheet_at(api_service, sheet_range="Sheet2!B2:B")
        for row in data_phone:
            print(row)
            if user_info in row[0]:
                user_index = data_phone.index(row)
                user_role = read_sheet_at(api_service,"Sheet2!C2:C")[user_index][0]
                return {'role': user_role, 'index': user_index}
    return False


if __name__ == "__main__":
    api_service = authen_me()
    # Call the Sheets API
    # The ID and range of a sample spreadsheet.
    sheet_id = "1_SQyyxnUtre_HGpskjV9PQ9RHBfGOLLYEInrJJOFVGM"
    sheet_range = "Sheet1!A1:O5"

    values = read_sheet_at(api_service, sheet_id, sheet_range)

    if not values:
        print("No data found.")

    # print("Name, Major:")
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        # print(f"{row[0]}, {row[4]}")
        print(row)