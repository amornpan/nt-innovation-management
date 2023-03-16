import openai
from flask import Flask, request, jsonify
from flask import render_template

OPENAI_API_KEY = "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" # Replace with your API key
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/generate_report', methods=['POST'])
def generate_report():
    topic = request.json['topic']
    prompt = f"Please write a report on the topic: {topic}"
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        report = response.choices[0].text.strip()
        return jsonify({'report': report})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
