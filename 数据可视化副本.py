import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定中文字体文件路径
font_path = "C:/Windows/Fonts/simsun.ttc"  # 将路径替换为实际字体文件的路径

# 设置字体属性
font_prop = FontProperties(fname=font_path)

# 读取Excel数据
excel_file = "合并.xlsx"  # 将文件名替换为您的实际文件名
df = pd.read_excel(excel_file)

# 统计不同类别的数量
category_counts = df['标签'].value_counts()

# 创建标签与类别的对应关系
label_mapping = {
    0: '不好',
    1: '好',
    2: '中肯',
    3: '提问'
}

# 将标签转换为可读性更高的文本
category_counts.index = category_counts.index.map(label_mapping)

# 使用Seaborn创建柱状图
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette="viridis")
plt.xlabel('言论分类', fontproperties=font_prop)  # 使用指定的字体属性
plt.ylabel('数量', fontproperties=font_prop)      # 使用指定的字体属性
plt.title('贴吧言论分类分布', fontproperties=font_prop)  # 使用指定的字体属性
plt.xticks(rotation=45, fontproperties=font_prop)     # 使用指定的字体属性
plt.tight_layout()

# 显示图像
plt.show()
