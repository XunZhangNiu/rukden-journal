import json
import re
import sys

def main():
    # 从环境变量获取参数
    new_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    category = sys.argv[2] if len(sys.argv) > 2 else "📄 论著"
    title = sys.argv[3] if len(sys.argv) > 3 else "未命名"
    author = sys.argv[4] if len(sys.argv) > 4 else "匿名网友"
    abstract = sys.argv[5] if len(sys.argv) > 5 else ""
    editor_note = sys.argv[6] if len(sys.argv) > 6 else "🎉 录用自 Discussions"
    references = sys.argv[7] if len(sys.argv) > 7 else ""

    # 读取现有文件
    try:
        with open('articles.js', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = "window.articles = [];"

    # 提取现有文章数组
    match = re.search(r'window\.articles\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if match:
        try:
            articles = json.loads(match.group(1).replace("'", '"'))
        except:
            articles = []
    else:
        articles = []

    # 创建新文章
    new_article = {
        "id": new_id,
        "tag": category,
        "title": title,
        "authors": author,
        "abstract": abstract,
        "editorNote": editor_note,
        "fullContent": "<p>原文见 GitHub Discussions</p>",
        "references": references
    }

    articles.append(new_article)

    # 写入文件
    with open('articles.js', 'w', encoding='utf-8') as f:
        f.write('window.articles = ')
        f.write(json.dumps(articles, indent=4, ensure_ascii=False))
        f.write(';\n')

    print(f"✅ 文章已添加: {title}")

if __name__ == "__main__":
    main()
