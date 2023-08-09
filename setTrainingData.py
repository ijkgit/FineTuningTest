import json

def createJson(prompt, completion, file_path="dataset.jsonl"):
    data = {
        "prompt": prompt,
        "completion": completion
    }
    
    with open(file_path, "a", encoding="utf-8") as jsonl_file:
        jsonl_file.write(json.dumps(data, ensure_ascii=False) + "\n")

    print('prompt : ', prompt, 'completion : ', completion)


createJson('안녕하세요', '반갑습니다!')
createJson('회원가입이 하고 싶어', '안내해드릴게요!')
createJson('너는 누구야?', '저는 선문대학교 챗봇입니다!')