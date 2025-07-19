import requests

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        joke = response.json()["joke"]
        print("😂 Here's a joke for you:")
        print(joke)
    else:
        print("Failed to fetch joke")




def get_weather(city):
    API_KEY = "8157440a1936e2571661bc80bf38096a"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


    response = requests.get(url)
    print (response.json())
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"🌤️ Weather in {city}: {temp}°C, {weather}")
    else:
        print("City not found or API failed.")






def get_crypto_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr"

    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()[coin]["inr"]
        print(f"💰 Current {coin.capitalize()} price: ₹{price}")
    else:
        print("Failed to fetch crypto price")





if __name__ == "__main__":
    print("Choose an option:")
    print("1. Get a joke")
    print("2. Get weather")
    print("3. Get crypto price")
    
    choice = input("Enter 1/2/3: ")
    
    if choice == "1":
        get_joke()
    elif choice == "2":
        city = input("Enter city name: ")
        get_weather(city)
    elif choice == "3":
        coin = input("Enter crypto coin (e.g., bitcoin): ").lower()
        get_crypto_price(coin)
    else:
        print("Invalid choice.")
