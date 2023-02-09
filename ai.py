import os
import openai
from generators import lstrip

openai.api_key = os.getenv('OPENAI_API_KEY')
shell = os.path.basename(os.getenv('SHELL'))

model = 'text-davinci-003'
max_tokens = 4000


def nl2cl(request):
    prompt = f'{request}. Provide only {shell} shell command as output.'
    generator = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=100,
        temperature=0,
        stream=True
    )
    return lstrip(comp['choices'][0]['text'] for comp in generator)


def explain_command(command):
    prompt = f'{shell} shell command: {command}' \
             '\n\nVery briefly, list each parameter and what it does.'
    generator = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=100,
        temperature=0,
        stream=True
    )
    return lstrip(comp['choices'][0]['text'] for comp in generator)
