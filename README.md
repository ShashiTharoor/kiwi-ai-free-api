# kiwi-ai-free-api

This is a non-official Kiwi.ai API, designed to be compatible with OpenAI's API. It allows users to use Kiwi.ai services through simple interface calls. This project contains Python code to call the Kiwi.ai API and AWS Lambda Python code to implement it.

## file structure

- `kiwi_api.py`: Contains the main function function `get_chat_completion_stream(messages, session_id=None)`, used to get chat completion stream.
- `config.py`: The user needs to add to this file the headers obtained by Kiwi.ai.Cookies are optional.

## How to use and install dep.

Make sure the required dependencies are installed in your environment. Install using the following commands:

```bash
pip install requests
```

### configuration

1. Open the `config.py` file.
2. Add your Kiwi.ai headers. If you have cookies, you can also add them as well.


Here is an example of how to use the `get_chat_completion_stream` function in `kiwi_api.py`:

```python
from kiwi_api import get_chat_completion_stream

messages = [
 {"role": "user", "content": "Who won the world series in 2020?"}
 ]

resp= get_chat_completion_stream(messages):
print(resp)

```
This example shows how to call the API to get the dynamic output of chat responses.

### AWS Lambda deployment

This project also includes Python code examples for AWS Lambda. You can modify and deploy it to the Lambda service according to your needs.

## contribution

We welcome contributions of any kind, including but not limited to bug reports, feature requests, pull requests, etc. Please make sure all tests are run and passed before submitting a pull request.
