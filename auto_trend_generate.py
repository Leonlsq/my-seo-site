import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from openai import OpenAI
import os
import time
import re
import random
from datetime import datetime

# 1. 配置 DeepSeek API
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

OUTPUT_DIR = "src/markdown"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 2. 聚焦高搜索意图（排障、教程、硬件、AI与极客工具）的垂直 RSS 源，避开大众新闻巨头
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://hnrss.org/newest?points=100",
    "https://www.reddit.com/r/pcgaming/top.rss?t=day",
    "https://www.reddit.com/r/techsupport/top.rss?t=day",
    "https://www.reddit.com/r/LocalLLaMA/top.rss?t=day",
    "https://www.reddit.com/r/selfhosted/top.rss?t=day"
]


def clean_html(raw_html):
    """使用 BeautifulSoup 清洗 RSS 摘要中的 HTML 标签，提取纯文本 Context"""
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    return re.sub(r'\s+', ' ', text)[:800]  # 截取前 800 字符作为核心背景，节省 Token


def get_mixed_topics(limit=25):
    print("🌐 正在从多个垂直领域抓取高价值话题与上下文...")
    items_data = []
    seen_titles = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    for url in RSS_FEEDS:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            root = ET.fromstring(response.content)

            # 兼容标准 RSS (<item>) 和 Atom (<entry>) 格式
            entries = root.findall('.//item') + root.findall(
                './/{http://www.w3.org/2005/Atom}entry') + root.findall('.//entry')

            for entry in entries:
                title_el = entry.find('title') or entry.find(
                    '{http://www.w3.org/2005/Atom}title')
                desc_el = (
                    entry.find('description') or
                    entry.find('{http://www.w3.org/2005/Atom}content') or
                    entry.find('{http://www.w3.org/2005/Atom}summary') or
                    entry.find('content')
                )

                if title_el is not None and title_el.text:
                    clean_title = re.sub(
                        r'\s*[-|]\s*.*$', '', title_el.text).strip()
                    if clean_title not in seen_titles and len(clean_title) > 15:
                        seen_titles.add(clean_title)
                        raw_desc = desc_el.text if (
                            desc_el is not None and desc_el.text) else ""
                        context_text = clean_html(raw_desc)
                        items_data.append({
                            "title": clean_title,
                            "context": context_text
                        })
        except Exception as e:
            print(f"⚠️ 抓取 {url} 失败: {e}")
            continue

    random.shuffle(items_data)
    final_items = items_data[:limit]
    print(f"🔥 成功获取 {len(final_items)} 个带上下文的精选话题！")
    return final_items


def make_clean_slug(title, max_words=8):
    """按完整单词边界生成干净的 SEO URL Slug，杜绝半截单词"""
    words = re.findall(r'[a-z0-9]+', title.lower())
    return "-".join(words[:max_words])


def sanitize_frontmatter(md_text):
    """代码级防崩清洗：强制将 title 和 description 用双引号包裹，内部双引号全部转为单引号"""
    lines = md_text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, min(12, len(lines))):
            if lines[i].strip() == "---":
                break
            if lines[i].startswith(("title:", "description:")):
                key, val = lines[i].split(":", 1)
                val = val.strip().strip('"').strip("'").replace('"', "'")
                lines[i] = f'{key}: "{val}"'
    return "\n".join(lines)


def generate_seo_article(item):
    topic = item["title"]
    context = item["context"]
    current_date = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
You are a senior tech, gaming, and troubleshooting SEO strategist.
Trending Topic: "{topic}"
Background Context / Details: "{context if context else 'Use general technical knowledge related to this topic.'}"

CRITICAL SEO STRATEGY (DO NOT WRITE GENERIC NEWS):
Mainstream media already covers the basic news. To rank on Google Page 1 and get high CTR, you MUST pivot this topic into an **Actionable Long-Tail Guide, Troubleshooting Fix, Comparison, or Deep-Dive Setup Tutorial** that users will actually search for after hearing about this topic.
- If it's a bug/issue -> Write a "How to Fix / Workaround" guide.
- If it's a new product/tool/hardware -> Write a "Worth It? Specs, Alternatives & Buying Guide" or "How to Set Up / Use" tutorial.
- If it's a gaming/tech trend -> Write a practical optimization, settings, or impact analysis guide for players/users.

FORMATTING RULES:
1. Output EXACTLY in valid Markdown format, starting immediately with `---`.
2. Always wrap `title` and `description` values in double quotes, and ONLY use single quotes inside them.
3. Craft a high-CTR, specific long-tail SEO headline (under 65 chars) using proven hooks (e.g., "How to Fix...", "...vs...: Which is Better?", "Is ... Worth It in {current_date[:4]}?").
4. Write AT LEAST 700 words with concrete facts, tables/bullet points, parameters, or step-by-step instructions. Avoid vague filler sentences.

---
title: "[High-CTR Long-Tail SEO Title under 65 chars]"
description: "[Actionable meta description under 150 chars with primary long-tail keyword]"
pubDate: {current_date}
tags: ['Tech', 'Guide', 'Troubleshooting']
---

## [Actionable H2 Addressing the User's Core Search Intent]
[Hook the reader immediately: state the exact problem, release, or comparison and give the direct takeaway in the first paragraph.]

## [Step-by-Step Guide / Key Specs Comparison / Practical Solutions]
[Provide high-value, specific steps, configurations, pros & cons, or technical breakdowns. Use numbered lists or bullet points.]

## [Common Issues, Alternatives, or What You Should Know]
[Add unique Information Gain: workarounds, hidden settings, cost analysis, or competitor comparisons.]

## Frequently Asked Questions (FAQ)
### [Long-tail question users type into Google 1]?
[Direct, factual answer]
### [Long-tail question users type into Google 2]?
[Direct, factual answer]

## Final Verdict
[Clear, opinionated recommendation on what the user should do or buy next.]
"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an expert technical SEO writer who specializes in high-CTR long-tail tutorials, troubleshooting guides, and product comparisons."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"生成文章失败 {topic}: {e}")
        return None


def main():
    ARTICLE_COUNT = 20  # 贵精不贵多，每天 2 times * 20 篇 = 40 篇高质量长尾文章足够
    items = get_mixed_topics(limit=ARTICLE_COUNT)

    if not items:
        print("未能获取到热点词，程序退出。")
        return

    for i, item in enumerate(items):
        topic = item["title"]
        safe_slug = make_clean_slug(topic, max_words=8)
        if not safe_slug:
            continue
        filepath = os.path.join(OUTPUT_DIR, f"{safe_slug}.md")

        # 本地去重：如果已经生成过同名文章，直接跳过，省钱且防冲突
        if os.path.exists(filepath):
            print(f"⏭️ [{i+1}/{len(items)}] 已存在，跳过: {filepath}")
            continue

        print(f"✍️ [{i+1}/{len(items)}] 正在撰写长尾 SEO 文章: {topic}")
        md_content = generate_seo_article(item)

        if md_content:
            md_content = re.sub(r'^```(?:markdown)?\s*\n',
                                '', md_content.strip())
            md_content = re.sub(r'\n```\s*$', '', md_content.strip())
            md_content = sanitize_frontmatter(md_content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            print(f"✅ 生成完毕: {filepath}")

        time.sleep(2)

    print("🎉 今日高转化长尾 SEO 内容抓取与生成全部完成！")


if __name__ == "__main__":
    main()
