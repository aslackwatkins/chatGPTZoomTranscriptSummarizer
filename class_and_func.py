import openai
from transformers import AutoTokenizer
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(20,60)
def check_limit():
    return

def break_file_into_chunks(file, chunksize=1000, overlap=200):

    tokenizer = AutoTokenizer.from_pretrained("gpt2")

    with open(file, 'r') as f:
        text = f.read()
    
    tokens = tokenizer.encode(text)
    num_tokens = len(tokens)
    chunks = []

    for i in range(0, num_tokens, chunksize - overlap):
        chunk = tokens[i:i + chunksize]
        chunks.append(chunk)
    
    return chunks

def text_clean(file_1, file_2):
    new_text = []

    with open(f"{file_1}", "r") as my_file:
        for line in my_file:
            if line[0] != "[" and len(line) > 1:
                new_text += line
            else:
                continue
    my_file.close()

    new_file = open(f"{file_2}", "a")
    for item in new_text:
        new_file.writelines(item)
    new_file.close()


class OpenAICall():

    def __init__(self, org_id, open_api_key):
        self.org_id = org_id
        self.open_api_key = open_api_key

    def summarize_text(self, edited_text):
        check_limit()
        openai.api_key = self.open_api_key
        openai.organization = self.org_id

        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "This is a content summarization."},
                {"role": "user", "content": f"Please provide bullet points for each piece of this transcript. Break it down into sub categories as you see fit. This is only a piece of a transcript for a two hour lecture. Here is a piece of the transcript: {edited_text}"}
            ]
        )

        return result["choices"][0]["message"]["content"]

