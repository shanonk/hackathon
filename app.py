from flask import Flask, render_template, request
import openai
import re

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = '7d2e59ad-9838-4247-bf52-0ad42d7fb40e'

def evaluate_essay(essay):
    # Send essay to OpenAI API for evaluation
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=essay,
        temperature=0.5,
        max_tokens=100
    )
    feedback = response.choices[0].text.strip()
    
    # Wrap feedback sentences with <u> tag and apply class for styling
    highlighted_essay = essay
    feedback_sentences = re.findall(r'\b[A-Z][^.]*\.', feedback)  # Split feedback into sentences
    for sentence in feedback_sentences:
        highlighted_essay = highlighted_essay.replace(sentence, f'<u class="feedback">{sentence}</u>')
    
    return highlighted_essay, feedback

def generate_prompt(feedback):
    # Generate prompt indicating where information is lacking
    prompt = "Based on the feedback, provide additional information on the following points:\n"
    feedback_points = re.findall(r'\b[A-Z][^.]*\.', feedback)  # Extract feedback points
    for point in feedback_points:
        prompt += f"- {point}\n"
    return prompt

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        essay = request.form['essay']

        # Evaluate the essay and get feedback
        highlighted_essay, feedback = evaluate_essay(essay)

        # Generate prompt indicating where information is lacking
        prompt = generate_prompt(feedback)

        return render_template('result.html', essay=highlighted_essay, prompt=prompt)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
