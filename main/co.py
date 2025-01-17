import cohere

ACCESS_KEY = ""
with open("../sec.txt", "r") as file:
    ACCESS_KEY = file.read().strip()


cohere = cohere.ClientV2(ACCESS_KEY)
in1 = input()
response = cohere.chat(
    model="command-r-plus", 
    messages=[{"role": "user", "content": in1}]
)
print(response.message.content[0].text)
