# Importing Libraries
from flask import Flask, render_template, request, jsonify
from BotDefinition import OpenAIBot
import re  # Fixed missing import

# Creating the Flask App
app = Flask(__name__)

# Initialize Chatbot
chatbot = OpenAIBot("gpt-3.5-turbo")

@app.route('/')
def index():
    """Render the chatbot web page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle user messages and return chatbot response."""
    prompt = request.form.get('prompt', '').strip()  # Get input safely

    print(f"User input: {prompt}")  # Debugging print statement

    if not prompt:
        return jsonify({"error": "Empty input!"}), 400

    # Check for exit command
    if prompt.upper() == 'END CHAT':
        return jsonify({"message": "Chat ended"}), 200

    # Generate chatbot response
    response = chatbot.generate_response(prompt)

    print(f"Chatbot response: {response}")  # Debugging print statement

    return jsonify({"response": response})  # Return response as JSON

if __name__ == '__main__':
    app.run(debug=True)
