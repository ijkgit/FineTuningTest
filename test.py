import os
import openai
import keyInfo

openai.api_key = keyInfo.OPENAI_API_KEY
# data = openai.File.create(
#   file=open(keyInfo.dataset, "rb"),
#   purpose='fine-tune'
# )
# print(data)
# test = openai.FineTuningJob.create(training_file='file-qzecCT5BIyufKDIxozGIs8DD', model="gpt-3.5-turbo")
# print(test)

while True:
    cmd = input().strip()
    completion = openai.ChatCompletion.create(
      model="ft:gpt-3.5-turbo-0613:personal::7w5B6dec",
      messages=[
        {"role": "user", "content": cmd}
      ]
    )
    print("answer : " + completion.choices[0].message.content)