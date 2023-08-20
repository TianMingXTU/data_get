# 数据获取（data_get）

在数据获取阶段，您可以通过修改爬虫文件中的URL，以获取不同百度贴吧的数据。此外，您还可以自行调整`range`中的数值，以灵活选择爬取的深度。

# 模型训练与权重获取

在模型文件方面，您需要执行训练操作，以获得模型的权重。这些权重将在后续的预测和数据可视化阶段用于对数据进行分析。

# 预测数据分类

在预测数据分类步骤中，您将使用已经训练好的预训练模型，对数据进行标签分类。这使得您能够自动将数据划分为不同的分类，从而得到更加清晰的数据分析结果。

# 数据可视化处理

数据可视化是对预测数据的一项关键处理步骤。在此阶段，您将采用图表、图像等视觉化手段，将预测到的数据以更易于理解的形式呈现，从而揭示数据的趋势和特点。

# 数据源及深度选择

预测数据是从特定网站上获取的，您在此选择了抓取的深度为300页。这意味着您将从该网站中抓取大量数据用于后续的分析和处理。

# 预测结果及标签含义

在预测数据处理后，您将得到带有额外标签字段的数据集。根据您的分类设定，标签0代表负面，1代表正面，2代表中性且客观，3代表提问。这样的分类将为您提供对数据进行更精细分类的能力，从而更好地洞察数据的内在含义。
