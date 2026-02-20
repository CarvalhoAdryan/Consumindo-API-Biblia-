import requests
from django.conf import settings

headers = {
        "Authorization": f"Bearer {settings.BIBLIA_TOKEN}"
    }

response = requests.get("https://www.abibliadigital.com.br/api/verses/nvi/sl/23", headers=headers)

data = response.json()

print(data)