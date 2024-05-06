import argparse
import json
import os
from typing import List, Dict

from read_funcs import *
from utils.merge_text import merge_text

data_dir_map = {'explanation': r"D:\Downloads\CRMU\baseline_track2\data\CRMUS"}

data_read_func = {'explanation': read_explanation_data}

def args_parser():
    parser = argparse.ArgumentParser(description="Data Preprocessing")

    parser.add_argument("--data_path", default=data_dir_map, help="Dir path to the data file")

    parser.add_argument("--data_name", type=list, default=["explanation"],
                        help="Name of the datasets")

    parser.add_argument("--save_dir", type=str, default="./data")


    args = parser.parse_args()

    return args

def sft_format(data_list: List[Dict], category: str) -> List[Dict]:
    """
    :param data: {'input': xxx, 'output': xxx}
    :return: sft format
    """
    new_data_list = []
    idx = 0

    for data in data_list:
        input_text = data['input']
        output_text = data['output']

        conversation = {'human': input_text, 'assistant': output_text}
        new_data_list.append({'conversation_id': idx, 'category': category, 'conversation': [conversation]})

        idx += 1

    return new_data_list


args = args_parser()

def main(args):
    data_name = args.data_name
    data_path_map = args.data_path
    save_dir = args.save_dir

    for name in data_name:
        dataset = data_read_func[name](data_path_map[name])

        for key in dataset:
            data_list = sft_format(dataset[key], key)
            dataset[key] = data_list

        for key in dataset:
            save_path = os.path.join(save_dir, f"{key}.jsonl")
            with open(save_path, 'w', encoding='utf8') as f:
                for d in dataset[key]:
                    f.write(json.dumps(d, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    args = args_parser()
    main(args)
