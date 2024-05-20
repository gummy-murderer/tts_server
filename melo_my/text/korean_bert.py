import torch
from transformers import BertTokenizerFast, BertModel

from lib.const import KR_MODEL_PATH

tokenizer = BertTokenizerFast.from_pretrained(KR_MODEL_PATH)
model = BertModel.from_pretrained(KR_MODEL_PATH).to('cpu')


def get_bert_feature(text, word2ph, device=None):

    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt")
        for i in inputs:
            inputs[i] = inputs[i].to(device)
        res = model(**inputs, output_hidden_states=True)
        res = torch.cat(res["hidden_states"][-3:-2], -1)[0].cpu()

    assert inputs["input_ids"].shape[-1] == len(word2ph), f"{inputs['input_ids'].shape[-1]}/{len(word2ph)}"
    word2phone = word2ph
    phone_level_feature = []
    for i in range(len(word2phone)):
        repeat_feature = res[i].repeat(word2phone[i], 1)
        phone_level_feature.append(repeat_feature)

    phone_level_feature = torch.cat(phone_level_feature, dim=0)

    return phone_level_feature.T
