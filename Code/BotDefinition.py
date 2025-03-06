import openai
import re  # Fixed missing import
import os

class OpenAIBot:
    def __init__(self, engine="gpt-3.5-turbo"):
        """Initialize chatbot with OpenAI model and conversation history."""
        self.conversation = [{"role": "system", "content": "You are a helpful assistant."}]
        self.engine = engine
        self.api_key = ""  # Secure way to use API key

    def add_message(self, role, content):
        """Add a message to the conversation history."""
        self.conversation.append({"role": role, "content": content})

    def generate_response(self, prompt):
        """Generate response from OpenAI based on conversation context."""
        if not prompt.strip():
            return "Please enter a valid message."

        # Add user input to the conversation
        self.add_message("user", prompt)

        try:
            client = openai.OpenAI(api_key=self.api_key)  # Create client instance
            response = client.chat.completions.create(
                model=self.engine,
                messages=self.conversation
            )
            assistant_response = response.choices[0].message.content.strip()

            # Add assistant response to conversation
            self.add_message("assistant", assistant_response)

            return assistant_response
        except Exception as e:
            return f"Error generating response: {str(e)}"
