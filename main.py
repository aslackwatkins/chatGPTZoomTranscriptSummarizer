import time
import openai
import transformers
import constants as cst
import class_and_func as cf
from transformers import AutoTokenizer

org_id = cst.OPENAI_ORG_ID
openai_api_key = cst.OPENAI_API_KEY

api_obj = cf.OpenAICall(org_id, openai_api_key)
text_clean = cf.text_clean

file_1 = "base_transcript.txt"
file_2 = "cleaned_transcript.txt"
file_3 = "summarized_transcript.txt"

text_clean(file_1, file_2)

time.sleep(2)

tokenizer = AutoTokenizer.from_pretrained("GPT2")
chunks = cf.break_file_into_chunks(file_2)

time.sleep(2)

append_file = open(file_3, "a")
for i, chunk in enumerate(chunks):
    try:
        time.sleep(3)
        text_chunk = tokenizer.decode(chunks[i])
        append_file.writelines(api_obj.summarize_text(text_chunk))
    except:
        time.sleep(60)
        text_chunk = tokenizer.decode(chunks[i])
        append_file.writelines(api_obj.summarize_text(text_chunk))
append_file.close()