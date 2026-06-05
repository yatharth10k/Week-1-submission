import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

def run_chatbot():
    """
    A terminal chatbot that holds a coherent multi-turn conversation.

    Your implementation should:
    - Start with a system message that sets the assistant's behaviour.
    - Maintain a `messages` list with alternating user/assistant turns.
    - Append the assistant's reply to `messages` after each call.
    - Resend the full history on every API call.
    - Allow the user to type 'exit' or 'quit' to end the session.

    Stretch:
    - Add a '/reset' command that clears history so you can feel context loss live.
    - Add a '/tokens' command that prints response.usage after the last call.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Chat started. Type 'exit' to quit.\n")
    response=None
    number_chats=0
    while True:
        # TODO: take user input
        # TODO: append the user turn to messages
        # TODO: call the API with the full messages list
        # TODO: extract the assistant's reply
        # TODO: append the assistant turn to messages
        # TODO: print the reply
        user_input=input("You: ").strip()
        if user_input=="quit" or user_input=="exit":
            print("Goodbye!!")
            break
        elif user_input=="/reset":
            messages=[{"role":"system","content":"You are a helpful assistant."}]
            response=None
            number_chats=0
            print("History has been cleared")
        elif user_input=="/tokens":
            if response:
                print(response.usage)
            else:
                print("No API calls yet!!")
        elif user_input=="/number_chats":
            print("Number of chats: ", number_chats)
        elif user_input=="/history":
            if len(messages)<2:
                print("No history yet!!")
            else:
                num=0;
                for i in messages:
                    if i["role"]=="user":
                        num+=1
                        print(num, ")", i["content"])
        else:            
            number_chats=number_chats+1
            messages.append({"role" : "user", "content" : user_input})
            response=client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages)
            ai_reply=response.choices[0].message.content
            messages.append({"role" : "assistant", "content" : ai_reply})
            print(f"AI: {ai_reply}")
        pass
if __name__ == "__main__":
    run_chatbot()