from webserver import keep_alive
import requests

channelID = 994165816981475379
headers = {
    "authorization":
    "token here"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
