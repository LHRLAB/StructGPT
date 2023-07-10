import requests
# Get yourip: curl ipinfo.io/ip
url = 'http://yourip:80/'

def GPT(input, model):
    if model == 'gpt-3.5-turbo':
        json={
            'conversation': [
                {"role": "system", "content": "hello"},
                {"role": "user", "content": input},
                ],
            'model': 'gpt-3.5-turbo',
        }
    elif model == 'gpt-4':
        json={
            'conversation': [
                {"role": "system", "content": ""},
                {"role": "user", "content": input},
                ],
            'model': 'gpt-4',
        }        
    response = requests.post(url+'GPT_conversation', json=json)
    assert response.content.status_code == 200
    output=response.json()['data']['content']
    return output

# output = GPT(input="What is ChatGPT", model='gpt-3.5-turbo')
# # output = GPT(input="What is ChatGPT", model='gpt-4')
# print(output)

def GPT_Message(messages, model):
    if model == 'gpt-3.5-turbo':
        json={
            'conversation': messages,
            'model': 'gpt-3.5-turbo',
        }
    elif model == 'gpt-4':
        json={
            'conversation': [
                {"role": "system", "content": ""},
                {"role": "user", "content": input},
                ],
            'model': 'gpt-4',
        }        
    response = requests.post(url+'GPT_conversation', json=json)
    output=response.json()['data']
    return output