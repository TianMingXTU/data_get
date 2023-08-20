import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# 加载预训练的DistilBERT模型和标记器
model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=4)

# 加载训练好的模型
model.load_state_dict(torch.load('path_to_save_model/pytorch_model.bin', map_location='cpu'))  # 替换成你保存的模型文件路径
model.eval()

# 加载原始数据
data = pd.read_excel('预测数据.xlsx')  # 替换成你的Excel文件路径

# 对内容进行编码和预测
max_length = 128  # 适当的文本长度

predicted_labels = []
for content in data['内容']:
    inputs = tokenizer(content, add_special_tokens=True, truncation=True, padding='max_length', max_length=max_length, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits).item()
        predicted_labels.append(predicted_label)

# 将预测标签添加到原始数据
data['预测标签'] = predicted_labels

# 将结果保存回Excel文件
data.to_excel('预测后的数据.xlsx', index=False)  # 替换成你希望保存的Excel文件名
