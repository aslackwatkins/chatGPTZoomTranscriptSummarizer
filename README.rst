ChatGPT Zoom Transcript Summarizer
==================================
This Python script allows users to summarize a Zoom transcript with the ChatGPT AI. This script may not keep track of which
speaker says what. It's main purpose is to provide a summary of the entire conversation.

In this document, I will give a step by step guide for setting up and using this script, including how to export the script
from Zoom, and what files you will need to create. 


Script Download and Setup
-------------------------
1. Start by downloading this script via zip file or gitclone, and open it in your prefered IDE.
2. To install the required packages, in the terminal, run the command::
    pip install -r /path/to/requirements.txt
3. Create a constants.py file with two variables:
    1. OPENAI_API_KEY = "<YOUR_API_KEY>"
    2. OPENAI_ORG_ID = "<YOUR_API_ORG_ID>"


Zoom Transcript Export 
----------------------
1. During your Zoom call, click on Closed Captioning, and click "View Full Transcript".
2. Once your call is over, click "Save Transcript".
3. Move the saved transcription file into the same folder as the script.
4. Rename the transcription file: base_transcript.txt


Running the Script
------------------
Once you have everything set up, in the project terminal, run the command::
    python3 main.py


While It's Running
------------------
The script will go through the base_transcript.txt and remove all the lines which relate to which speaker is speaking,
and datetime information. It will then add all the transcribed text to the cleaned_transcript.txt file.
Next, the AutoTokenizer object from the transformers package will estimate the number of tokens required to summarize the text 
with the ChatGPT API.The script then breaks the cleaned_transcript.txt into a list of sections which are all under the current 
4096 Token limit for the ChatGPT API. Finally, it uses the ChatCompletion object from the openai package to summarize the text. 
Because of the API rate limit of 20 RPM and 40,000 tokens per minute, it may take a few minutes to finish running the script.


Once It's Done
--------------
The summary will be structured in bullet format, in the summarized_transcript.txt file. Please let me know if you think there
are any improvements I should make to this script, and enjoy using it!