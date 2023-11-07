from flask import Flask, render_template, request, jsonify
import asyncio
# pip install torch nest_asyncio transformers flask
# from backend.chatbot import get_bot_response  # Ensure this is the correct path and function name

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page with the chatbot
    return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# async def chat():
    # user_message = request.json['message']

    # try:
        # Asynchronously get the bot response
        # bot_response = await get_bot_response(user_message)
    # except asyncio.TimeoutError:
        # bot_response = "The request timed out, please try again later."
    # except Exception as e:
        # Log the error and inform the user
        # app.logger.error(f"Error in get_bot_response: {e}")
        # bot_response = "An error occurred, please try again later."

    # return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)