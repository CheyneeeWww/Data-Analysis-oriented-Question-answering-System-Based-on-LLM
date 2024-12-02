import json

# 读取JSON文件
with open('medic question-answer.json', 'r') as file:
    data_list = json.load(file)

new_data_list = []
for data in data_list:
    new_data = {
        "conversations": [
            {
                "from": "human",
                "value": data["query"]
            },
            {
                "from": "gpt",
                "value": data["answer"]
            }
        ],
        "system": "",
        "tools": ""
    }
    new_data_list.append(new_data)

# 将转换后的数据保存为新的JSON文件
with open('med_data.json', 'w') as outfile:
    json.dump(new_data_list, outfile, indent=4)