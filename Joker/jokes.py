import requests
import time

tellajoke = True

category = "Any"
lang = "eng"
while tellajoke:
    ans = str(
        input("\n\nDo you want to read a joke?(y => yes; n => exit; s=> settings): ")
    )

    if ans == "y":
        x = requests.get("https://v2.jokeapi.dev/joke/" + category + "?lang=" + lang)
        x = x.json()