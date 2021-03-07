#
#   Save data to google sheets using a service account
#   https://cloud.google.com/iam/docs/service-accounts
#


from oauth2client.service_account import ServiceAccountCredentials
import gspread, time


def auth():

    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
        ]
    file_name = 'your key'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
    client = gspread.authorize(creds)

    return client


def savegsheet(gfile, gsheet, idata):

    client = auth()
    wsheet = client.open(gfile).worksheet(gsheet)

    i = 0

    for data in idata:

        data_len = len(data)
        i += 1
        row = 0

        while row < data_len:
            row += 1
            wsheet.update_cell(i, row, data[row - 1])
            

    i += 1
    date = time.strftime('%d-%m-%Y %H:%M:%S')
    wsheet.update_cell(i, 1, 'Updated at:')
    wsheet.update_cell(i, 2, date)
    