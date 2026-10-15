import os
from openai import OpenAI
import gradio as gr

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful Java teacher"}
]

def chatbot(user_input):
    try:
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="INTELLIGENT CHATBOT"
)

demo.launch()
