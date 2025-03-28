from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')  # Serve the frontend page

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    dest_lang = data.get('lang', 'en')
    
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    
    try:
        translated = translator.translate(text, dest=dest_lang)
        return jsonify({'original_text': text, 'translated_text': translated.text, 'language': dest_lang})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
