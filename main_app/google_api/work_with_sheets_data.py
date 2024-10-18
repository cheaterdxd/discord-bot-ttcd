from authenticator import authen_me

def read_sheet_at(api_service, sheet_id:str, sheet_range:str)-> list:
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