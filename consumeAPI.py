#agregar usuario a excel
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configuración de las credenciales
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'xenon-bit-350815-897648447697.json'

# Autenticación y creación del servicio de Google Sheets
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# ID de la hoja de cálculo y nombre de la hoja
spreadsheet_id = '1N0bIJxakDu8edHNZWt-qDzLj7Jf2DjI0x1MnWxSUre8'
sheet_name = 'Clientes'

# Datos a agregar
data = {
    "NIT": "1003742040",
    "CLIENTE": "Jeisson Infante",
    "SUCURSAL": "Bogota",
    "DIRECCION": "Cra 18A #9D-01",
    "CIUDAD": "Bogota",
    "TELEFONO": "3028305910",
    "ESTATUS": 0
}

# Agregar un nuevo campo a la hoja de cálculo
request = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=f"{sheet_name}!A:G",
    valueInputOption="USER_ENTERED",
    body={
        "values": [list(data.values())]
    }
)
response = request.execute()

print(f"Se agregó un nuevo campo a la hoja '{sheet_name}'")
