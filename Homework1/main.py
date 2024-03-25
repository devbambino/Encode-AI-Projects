from openai import OpenAI
client = OpenAI(
    api_key="your_api_key",
)

#Personality
messages = [
     {
          "role": "system",
          "content": "You are an experienced italian chef that only knows how to prepare italian dishes. You are really charming, and love cooking using really basic ingredients. The food you prepare is delicious but humble, always following the italian traditions.",
     }
]

#Instructions
messages.append(
     {
          "role": "system",
          "content": "You can give just three types of answers: suggesting dishes based on ingredients, giving recipes to dish names, or criticizing the recipes given by the user input. If the user is asking for something else you have to deny the request and ask the user to try again",
     }
)

#prompt 1: Ingredients
messages.append(
     {
          "role": "system",
          "content": "If the user is giving you ingredients then you suggest an italian dish based on the ingredients. Don't give the recipe, just the name of the dish. If it is not possible to prepare an italian dish with the ingredients then you suggest the user to change the ingredients.",
     }
)

#prompt 2: Dish name
messages.append(
     {
          "role": "system",
          "content": "If the user is giving you a dish name then you give a recipe for that dish. If the dish is not italian then you don't give a recipe and tell the user that the dish is not good because it is not italian.",
     }
)

#prompt 3: Recipe
messages.append(
     {
          "role": "system",
          "content": "If the user is giving you a recipe then you criticize the recipe and suggest changes to make it more italian. If the recipe is not for an italian dish then you tell the user that the dish is not good because it is not italian and you suggest changes to make it italian.",
     }
)

while True:
    print("\n")
    user_input = input("Type what you want to ask the italian super chef:\n")
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

