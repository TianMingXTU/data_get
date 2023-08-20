import torch
import pandas as pd
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset

# 加载预训练的DistilBERT模型和标记器
model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=4)

# 加载和准备数据
data = pd.read_excel('标签.xlsx')  # 替换成你的数据文件路径
sentences = data['内容'].tolist()
labels = data['标签'].tolist()

# 对文本进行编码和填充
max_length = 128  # 适当的文本长度
encoded_dict = tokenizer.batch_encode_plus(
    sentences,
    add_special_tokens=True,
    truncation=True,
    padding='max_length',
    max_length=max_length,
    return_tensors='pt'
)

input_ids = encoded_dict['input_ids']
attention_masks = encoded_dict['attention_mask']
labels = torch.tensor(labels)

# 创建数据加载器
dataset = TensorDataset(input_ids, attention_masks, labels)
batch_size = 32  # 适当的批量大小
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 设置GPU（如果可用）
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# 训练模型
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
num_epochs = 5  # 适当的训练轮数

for epoch in range(num_epochs):
    model.train()
    total_loss = 0

    for batch in dataloader:
        batch = tuple(t.to(device) for t in batch)
        inputs = {'input_ids': batch[0], 'attention_mask': batch[1], 'labels': batch[2]}

        optimizer.zero_grad()
        outputs = model(**inputs)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {avg_loss:.4f}')

# 保存模型
model.save_pretrained('path_to_save_model')

