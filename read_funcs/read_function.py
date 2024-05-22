import json
import os
from typing import Dict, List

def post_process_explanation(data: Dict) :
    input_text=data["question"]
    output_text=data["reference_answer"]
    new_data = {"input": input_text, "output": output_text}
    return new_data

def read(data_dir) -> Dict[str, List[Dict]] :
    file_name="all_data.jsonl"

    database={}

    text_list = []
    with open(os.path.join(data_dir, file_name), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            text_list.append(post_process_explanation(json.loads(line)))

    database["FinLongEval"]=text_list

    return database
