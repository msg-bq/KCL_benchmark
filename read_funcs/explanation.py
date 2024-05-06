import json
import os
from typing import Dict, List


def post_process_explanation(data: Dict):
    """
    目前主要是，如果parsed_explanation为空，就直接使用explanation
    输入是title+story+question+options，输出是explanation
    :return: {'input': 'title\nstory\nquestion\noptions', 'output': 'explanation'}
    """
    if not data["parsed_explanation"]:
        data["parsed_explanation"] = data["explanation"]

    if isinstance(data["options"], list):
        data["options"] = "\n".join(data["options"])

    input_text = "\n".join([data["title"], data["story"], data["question"], data["options"]])
    output_text = data["parsed_explanation"]

    new_data = {"input": input_text, "output": output_text}

    return new_data

def read_explanation_data(data_dir) -> Dict[str, List[Dict]]:
    filename_list = ['dev_CRMUS_MU_explanation.json', 'dev_CRMUS_CR_explanation.json']

    dataset = {}
    for filename in filename_list:
        text_list = []
        with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                text_list.append(post_process_explanation(json.loads(line)))

        dataset[filename] = text_list

    return dataset

