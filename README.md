训练部分大家直接看Firefly的原始仓库即可，我们主要处理数据

然后sft_preprocess.py是处理成Firefly接受的sft数据，需要提供一个读入的函数，输出为{"数据集名字": [{'input': xxx, 'output': xxx}, {'input': xxx, 'output': xxx}]}
