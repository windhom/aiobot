import requests
name = input("Введите имя покемона: ")
url = f"https://pokeapi.co/api/v2/pokemon/{name}"

response = requests.get(url, timeout=5)
if response.status_code == 200:
    data = response.json()
    poke_name = data["name"].capitalize()
    poke_weight = data["weight"]
    poke_height = data["height"]
    # print(poke_name, poke_weight, poke_height, sep="\n")
    print(data)