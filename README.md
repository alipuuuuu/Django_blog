# 📝 Django Blog — Markdown + 分类系统

一个基于 **Django** 构建的博客系统，支持 Markdown 渲染与分类浏览。

适合作为：

- Django 学习项目  
- 个人博客基础框架  
- Markdown 内容站点  
- CMS 原型  



## 📦 技术栈

- Python 3.12+  
- Django 6.x  
- SQLite（默认）  
- Bootstrap 5  
- Markdown  
- Bleach（XSS 安全过滤）  



## 📂 项目结构

```bash
.
├── config/ # Django 项目配置 
│ ├── settings.py 
│ ├── urls.py 
│ └── ... 
├── posts/ # 博客应用 
│ ├── models.py # Post / Category 模型 
│ ├── views.py # 列表 + 详情视图 
│ ├── admin.py # 后台管理配置 
│ ├── urls.py 
│ ├── templates/ 
│ │ └── posts/ 
│ │ ├── post_list.html 
│ │ └── post_detail.html 
│ └── static/ 
│ └── posts/ 
│ ├── bootstrap.min.css 
│ └── bootstrap.bundle.min.js 
├── db.sqlite3 
└── manage.py 
```


## 🚀 功能特性

### 📄 文章系统

- 标题、摘要、正文  
- Markdown 编写  
- 自动渲染为 HTML  
- 安全过滤（防 XSS）  
- 发布时间控制  
- 草稿 / 已发布状态  

---
### 🗂 分类系统

支持树状分类结构，如下：

```bash
Technology
├── Python
├── Django
└── AI
```


- 父分类 + 子分类  
- 分类筛选文章  
- 左侧导航树  

---

### 📚 列表页

- 按发布时间排序  
- 分页（每页 10 篇）  
- 分类过滤  
- Bootstrap 卡片布局  
- 创建时间显示  

---

### 📖 详情页

- Markdown 渲染内容  
- 安全 HTML 输出  
- 分类标签  
- 发布时间与更新时间  
- 返回列表按钮  

---

### 🛠 后台管理

增强的 Admin 界面：

- 发布时间信息展示  
- 最近发布标识  
- 搜索标题与内容  
- 按时间筛选  
- 折叠正文编辑区  


## 🧠 数据模型

### Category


name 分类名称 \
slug URL 标识 \
parent 父分类（可为空） 

支持无限层级树结构。

---

### Post

title \
description \
content \
category \
status draft / published \
published_at \
created_at \
updated_at 


---

## 🔐 Markdown 安全策略

使用：

- `markdown` — 渲染  
- `bleach` — 清洗  

允许标签示例：


p, pre, code, h1-h6, img, a, table 等


防止恶意脚本注入。

---

## ⚙️ 安装与运行

### 1️⃣ 克隆项目
```bash
git clone https://github.com/alipuuuuu/Django_blog.git
cd projects
```

### 2️⃣ 创建虚拟环境
```bash
python -m venv .venv 
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
```

### 3️⃣ 安装依赖
```bash
pip install django markdown bleach
```

### 4️⃣ 数据库迁移
```bash
python manage.py migrate
```

### 5️⃣ 创建管理员
```bash
python manage.py createsuperuser
```

### 6️⃣ 运行开发服务器
```bash
python manage.py runserver
```

访问：

http://127.0.0.1:8000/posts/

后台：

http://127.0.0.1:8000/admin/

## 使用说明
### 发布文章

在 Admin 中：

创建分类

新建 Post

设置 status = published

选择 category

保存



## 📌 URL 路由

| 页面 | URL |
|------|------|
| 文章列表 | `/posts/` |
| 分类列表 | `/posts/category/<slug>/` |
| 文章详情 | `/posts/<id>/` |
| 管理后台 | `/admin/` |



## 🔮 可扩展方向

- 评论系统  
- 标签系统  
- 搜索功能  
- 用户系统  
- RSS / Sitemap  
- SEO 优化  
- 图片上传  
- REST API（DRF）  
- 静态站点生成  



##  📄 License

MIT License