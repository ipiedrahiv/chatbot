from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

while(True):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"Pick 5 categories (e.g person, profession, color, adjective, etc.) and list them as comma separated values."
    )
    #print(response.text)

    keywords = input(f"Please give me one of each: {response.text} -> ")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"Write a wimsical short story in under a paragraph using these keywords {keywords}"
    )

    print(response.text)
