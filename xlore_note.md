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
整体进度

一周安排
成员 | 任务 | deadline
------|------|------
成江 |  | 
方韦 |  | 
吕鑫 |  | 
书林 |  | 



## 0. 原数据（dump）

* dump原数据


## 1. 整理数据目录及格式（extraction）

* xx: 三种语言的wiki：en, fr, zh；(bd：百度数据)
* id为wiki的id

- 摘要：**xx_abstract.txt**
    - title \t\t id \t\t 
    - title \t\t id \t\t redirect_title
    - title \t\t id \t\t AbstractHere::;para_1
    - title \t\t id \t\t AbstractHere::;para_1::;para_2::;para_3
    - (title_h1 \t\t title_h2 \t\t url \t\t para_1::;para_2)

- 正文：**xx_article.txt**
    - title \t\t id \t\t 
    - title \t\t id \t\t redirect_title
    - title \t\t id \t\t ArticleHere::;== 一级标题 ==::;para_1::;=== 二级标题 ===::;para_2::;para_3
    - (title_h1 \t\t title_h2 \t\t url \t\t ArticleHere::;== 一级标题 ==::;para_1::;=== 二级标题 ===::;para_2)
    
- Category分类：**xx_category.txt**
    - title \t\t id \t\t 
    - title \t\t id \t\t redirect_title
    - title \t\t id \t\t [[Category:Anarchism| ]]::;[[Category:Anti-capitalism]]
    - (title_h1 \t\t title_h2 \t\t url \t\t [[tag_1| ]]::;[[tag_2| ]])

- 信息框：**xx_infobox.txt**
    - title \t\t id \t\t 
    - title \t\t id \t\t redirect_title
    - title \t\t id \t\t {attr_1 : val_1, attr_2 : val_2}
    - (title_h1 \t\t title_h2 \t\t url \t\t {attr_1 : val_1, attr_2 : val_2})

- 信息框模版：**xx_infobox-template.txt**
    - title \t\t id \t\t 
    - title \t\t id \t\t redirect_title
    - title \t\t id \t\t template_name \t\t attr_1::;attr_2::;attr_3


- 目录大纲：**xx_outline.txt**
    - title \t\t id \t\t 
    - title \t\t id \t\t redirect_title
    - title \t\t id \t\t 1#Terrestrial albedo::;1.1#White-sky and black-sky albedo::;2#Astronomical albedo
    - (title_h1 \t\t title_h2 \t\t url \t\t 1#Terrestrial albedo::;1.1#White-sky and black-sky albedo::;2#Astronomical albedo)


## 2. 初版的清洗（clean）// 统计关键条目（stats）

* xx: 三种语言的wiki：en, fr, zh；(bd：百度数据)
* id为wiki的id
* new_id为新的xlore的编号：en1, en2, ...; fr1, fr2, ...; zh1, zh2, ...; bd1, bd2, ...;

- 保留的entity列表：**xx_lite_entity_newid.txt**
    - title \t\t id \t\t new_id
        - 从wiki xx_abstract.txt 和 xx_article.txt，过滤掉 filter_words = ["wikipedia:", "wikiprojects", "lists", "mediawiki", "template:", "user:", "portal:", "category:", "categories:", "file:", "help:", "image:", "module:", "articles", "extension:", "manual:"] 获得


## 3. 精简处理（fine）

* xx: 三种语言的wiki：en, fr, zh；(bd：百度数据)
* id为重新编号的id

- 同义词表：**xx_synonym.txt**
    - title \t\t id \t\t syn_1::;syn_2
        - 从wiki redirect 获得
    - (title_h1+title_h2 \t\t id \t\t syn_1::;syn_2)
        - 从baidu redirect url 获得

- 多义词表：**xx_polysemy.txt**
    - title \t\t id \t\t [[pol_1|url]]::;[[pol_2|url]]
        - 从wiki (disambiguation) 获得（仅保留名字存在匹配的）
    - (title_h1+title_h2 \t\t id \t\t [[pol_1|url]]::;[[pol_2|url]])
        - 从baidu force=1?的url + 获得

- Mention表：**xx_mention.txt**
    - title \t\t id \t\t men_1::;men_2
        - 同义词表 + 页面内linkage指向 获得
    - (title_h1+title_h2 \t\t id \t\t men_1::;men_2)
        - 同义词表 + 页面内linkage指向 获得






## 4. 最终数据文件（ttl）


## 5. 代码（code）

* Extractor／ 项目



