# app/routes.py

from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
from app.services import get_word_meaning, get_example_usage  # Import the updated service functions

# Load environment variables from .env file
load_dotenv()

# Blueprint setup
words_bp = Blueprint('words', __name__, url_prefix='/api/words')

# In-memory storage for words (for demonstration; use a database in production)
words_list = []

# Route to add a new word
@words_bp.route('', methods=['POST'])
def add_word():
    data = request.json
    word = data.get('word')

    if not word:
        return jsonify({"error": "No word provided"}), 400

    # Call the GPT API to get meaning
    meaning = get_word_meaning(word)
    if meaning is None:
        return jsonify({"error": "Failed to retrieve meaning"}), 500

    # Call the GPT API to get example usage
    example = get_example_usage(word)
    if example is None:
        return jsonify({"error": "Failed to retrieve example"}), 500

    # Append the word, meaning, and example to the list separately
    words_list.append({
        "word": word,
        "meaning": meaning,
        "example": example
    })

    return jsonify({"message": "Word added successfully", "word": word, "meaning": meaning, "example": example}), 201

# Route to retrieve all words
@words_bp.route('', methods=['GET'])
def get_words():
    return jsonify({"words": words_list}), 200
