# 20180704

数据目录：xlore@10.1.1.18:/home/xlore/Wikipedia20180301 $

```
xlore@KEG18:~/Wikipedia20180301$ ls
0_dump  1_extraction  2_clean  3_fine  4_ttl  5_code
xlore@KEG18:~/Wikipedia20180301$ tree
.
├── 0_dump
│   └── ...
├── 1_extraction
│   └── ...
├── 2_clean
│   └── ...
├── 3_fine
│   └── ...
├── 4_ttl
│   └── ...
└── 5_code
    ├── ...
    └── backup
```

## 0. 原数据（dump）

dump原数据


## 1. 整理数据目录及格式（extraction）

xx: 三种语言的wiki：en_, fr_, zh_

- 摘要：**xx_abstract.txt**

> title \t\t id \t\t 
> title \t\t id \t\t redirect_title
> title \t\t id \t\t para_1::;para_2::;para_3


- 正文：**xx_article.txt**

> title \t\t id \t\t 
> title \t\t id \t\t redirect_title
> title \t\t id \t\t == 一级标题 ==::;para_1::;=== 二级标题 ===::;para_2::;para_3


- Category分类：**xx_category.txt**

> title \t\t id \t\t 
> title \t\t id \t\t redirect_title
> title \t\t id \t\t [[Category:Anarchism| ]]::;[[Category:Anti-capitalism]]


- 信息框：**xx_infobox.txt**

> title \t\t id \t\t 
> title \t\t id \t\t redirect_title
> title \t\t id \t\t {attr_1 : val_1, attr_2 : val_2}


- 信息框模版：**xx_infobox-template.txt**

> title \t\t id \t\t 
> title \t\t id \t\t redirect_title
> title \t\t id \t\t template_name \t\t attr_1::;attr_2::;attr_3


- 目录：**xx_outline.txt**

> title \t\t id \t\t 
> title \t\t id \t\t redirect_title
> title \t\t id \t\t 1#Terrestrial albedo::;1.1#White-sky and black-sky albedo::;2#Astronomical albedo


## 2. 初版的清洗// 统计关键条目（stats）






## 3. 精简处理（fine）


## 4. 最终数据文件（ttl）


## 5. 代码（code）
Extractor／ 项目

