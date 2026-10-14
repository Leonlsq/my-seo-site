import requests
import xml.etree.ElementTree as ET
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

# 2. 混合多个高质量长尾/垂直领域的 RSS 数据源
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.reddit.com/r/technology/top.rss?t=day",
    "https://www.reddit.com/r/pcgaming/top.rss?t=day",
    "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
]


def get_mixed_topics(limit=30):
    print("🌐 正在从多个垂直领域抓取热点话题...")
    topics = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    for url in RSS_FEEDS:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            root = ET.fromstring(response.content)

            for item in root.findall('.//item/title') + root.findall('.//entry/title'):
                if item.text:
                    clean_title = re.sub(r'\s*-.*$', '', item.text)
                    if clean_title not in topics and len(clean_title) > 15:
                        topics.append(clean_title)
        except Exception as e:
            print(f"⚠️ 抓取 {url} 失败: {e}")
            continue

    random.shuffle(topics)
    final_topics = topics[:limit]
    print(f"🔥 成功获取 {len(final_topics)} 个精选热点话题！")
    return final_topics


def sanitize_frontmatter(md_text):
    """代码级防崩清洗：强制将 title 和 description 用双引号包裹，内部双引号全部转为单引号"""
    lines = md_text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, min(10, len(lines))):
            if lines[i].strip() == "---":
                break
            if lines[i].startswith(("title:", "description:")):
                key, val = lines[i].split(":", 1)
                # 去除首尾多余空格和引号，并将内部所有双引号替换为单引号
                val = val.strip().strip('"').strip("'").replace('"', "'")
                # 统一在最外层包裹标准双引号，彻底免疫冒号(: )和特殊符号报错
                lines[i] = f'{key}: "{val}"'
    return "\n".join(lines)


def generate_seo_article(topic):
    current_date = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
        You are an expert tech, gaming, and news blogger. 
        The current trending topic/keyword is "{topic}". 
        Write a highly detailed, engaging, and SEO-optimized comprehensive guide or analysis.
        
        CRITICAL RULES:
        1. Output EXACTLY in valid Markdown format.
        2. MUST include YAML Frontmatter at the beginning.
        3. Always wrap title and description values in double quotes, and ONLY use single quotes inside them.
        4. Write AT LEAST 600 words. Use H2 (##) and H3 (###) headings.
        5. Craft an irresistible, highly clickable, and human-like SEO headline (under 65 characters) for the `title` frontmatter. DO NOT use repetitive prefixes like "Complete Guide:".

        Follow this exact structure for the Frontmatter:

        ---
        title: "[Your engaging, highly clickable SEO headline here]"
        description: "[A compelling meta description under 150 characters summarizing the article]"
        pubDate: {current_date}
        tags: ['Trending', 'Tech', 'Guide']
        ---

        ## [Catchy H2 Heading related to {topic}]
        [Write 2-3 engaging paragraphs explaining the core of the trend, issue, or problem]

        ## [Detailed Breakdown / Step-by-Step Solutions / Key Highlights]
        [Provide detailed context, solutions, or analysis. Use bullet points or numbered lists for readability]

        ## Why is Everyone Talking About This? (or Impact Analysis)
        [Analyze the public reaction, market impact, or social significance]

        ## Frequently Asked Questions (FAQ)
        ### [Relevant Question 1]?
        [Answer]
        ### [Relevant Question 2]?
        [Answer]

        ## Final Thoughts
        [A strong concluding paragraph summarizing the key takeaways]
        """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a professional SEO content writer and technical blogger."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"生成文章失败 {topic}: {e}")
        return None


def main():
    ARTICLE_COUNT = 30
    topics = get_mixed_topics(limit=ARTICLE_COUNT)

    if not topics:
        print("未能获取到热点词，程序退出。")
        return

    for i, topic in enumerate(topics):
        print(f"[{i+1}/{len(topics)}] 正在让 AI 撰写热门话题: {topic}")

        md_content = generate_seo_article(topic)

        if md_content:
            safe_filename = "".join([c if c.isalnum() or c.isspace(
            ) else "" for c in topic.lower()]).replace(" ", "-")
            safe_filename = re.sub(r'-+', '-', safe_filename)[:50].strip('-')
            filepath = os.path.join(OUTPUT_DIR, f"{safe_filename}.md")

            if md_content.startswith("```markdown"):
                md_content = md_content.replace(
                    "```markdown\n", "").replace("\n```", "")
            elif md_content.startswith("```"):
                md_content = md_content.replace(
                    "```\n", "").replace("\n```", "")

            # 在写入文件前，强制执行代码级 YAML 头部清洗
            md_content = sanitize_frontmatter(md_content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            print(f"✅ 生成完毕: {filepath}")

        time.sleep(2)

    print("🎉 今日高质量 SEO 内容抓取与生成全部完成！")


if __name__ == "__main__":
    main()
