from dotenv import load_dotenv
from groq import Groq
import json
import re


load_dotenv()

groq = Groq()

def classify_with_llm(log_msg):
    """
    Use LLM to classify a log message if regex and BERT fail.
    """

    prompt = f"""Classify the following log message into one of these categories:
    - Security Alert
    - Workflow Error
    - Login Activity
    - File Operation
    - Deprecation Warning
    - Server/API Activity
    - Backup Process
    If unsure, classify as "Unclassified".
    Put the result inside <category></category> tags.
    
    Log message: {log_msg}
    """

    chat_completion = groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        # model="llama-3.3-70b-versatile",
        model="deepseek-r1-distill-llama-70b",
        temperature=0.5
    )

    content = chat_completion.choices[0].message.content
    match = re.search(r'<category>(.*)<\/category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1)

    return category


if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))