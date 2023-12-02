import google.generativeai as palm

API_KEY = ''
palm.configure(api_key=API_KEY)

model_list = [_ for _ in palm.list_models()]
for model in model_list:
    print(model.name)

model_id = 'models/text-bison-001'
prompt = '''
I am going on a date on Friday with a boy I like. What should I wear?
'''
completion = palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.8,
    max_output_tokens=800,
)

print(completion.result)