import os
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("../.env")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def extract_python_code(input_string):
    # 使用正则表达式匹配行 ```python 和行 ``` 之间的内容
    pattern = r'(?<=```python\n).*?(?=\n```)'  # 更新正则表达式
    match = re.search(pattern, input_string, re.DOTALL)
    
    # 如果找到匹配项，则返回匹配的字符串，否则返回空字符串
    if match:
        return match.group(0)
    else:
        raise RuntimeError(f"Unable to extract Python code from response {input_string}")

def code_deepseek(source_code):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": source_code
                + "\nPlease add parameter types and return types for each function and class in this code, and return only the modified Python code inside a ```python fenced block."
            },
        ],
        temperature=0,
    )

    content = completion.choices[0].message.content
    print(content)
    return extract_python_code(content)
    