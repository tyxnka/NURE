import json
import requests
import matplotlib.pyplot as plt
from datetime import datetime

nbu_response = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json")
converted_response = json.loads(nbu_response.content)

euro_rates = {}

# Обробка JSON
for item in converted_response:
    date = item['exchangedate']
    rate = item['rate']
    euro_rates[date] = rate
    print(f"{date} - {rate} грн")

dates = list(euro_rates.keys())
rates = list(euro_rates.values())

dates = [datetime.strptime(d, "%d.%m.%Y") for d in dates]

plt.plot(dates, rates, marker='o', linestyle='-', color='blue')
plt.title("Курс EUR за останній тиждень")
plt.xlabel("Дата")
plt.ylabel("Курс в грн")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
