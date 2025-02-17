from kiwi_api import get_chat_completion_stream

messages = [
 {"role": "user", "content": "Who won the world series in 2020?"}
 ]

resp= get_chat_completion_stream(messages):

print(resp)