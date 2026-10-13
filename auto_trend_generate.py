import requests
import xml.etree.ElementTree as ET
from openai import OpenAI
import os
import time
import re

# 1. 配置 DeepSeek API
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

OUTPUT_DIR = "src/markdown"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 3. 改用极其稳定的 Google News RSS


def get_trending_topics(limit=5):
    print("🌐 正在连接 Google News RSS 获取今日全球热点...")
    # 谷歌新闻美国区头条，官方 RSS，极度稳定绝对不会 404
    # 如果想做德国市场，可以换成: https://news.google.com/rss?hl=de&gl=DE&ceid=DE:de
    url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        topics = []

        # 提取新闻标题，并清洗掉末尾的媒体名称 (例如 "- CNN" 或 "- BBC")
        for item in root.findall('.//channel/item/title'):
            if item.text:
                clean_title = re.sub(r'\s*-.*$', '', item.text)
                if clean_title not in topics:
                    topics.append(clean_title)

        topics = topics[:limit]
        print(f"🔥 成功获取 {len(topics)} 个热点话题: {topics}")
        return topics

    except Exception as e:
        print(f"获取热点失败: {e}")
        return []


def generate_seo_article(topic):
    # 【核心防崩补丁】将话题中的双引号强制转换为单引号，专门用于 YAML 头部，防止 Vercel 解析报错
    safe_yaml_topic = topic.replace('"', "'")

    prompt = f"""
        You are an expert tech and news blogger. 
        The current trending topic is "{topic}". 
        Write a highly detailed, engaging, and SEO-optimized comprehensive guide.
        
        CRITICAL RULES:
        1. Output EXACTLY in Markdown format.
        2. MUST include YAML Frontmatter at the beginning. DO NOT use double quotes inside the title and description values.
        3. Write AT LEAST 600 words. Make it detailed to increase user time-on-page.
        4. Use multiple H2 (##) and H3 (###) headings to structure the content.

        Follow this exact structure:

        ---
        title: "Complete Guide: What You Need to Know About {safe_yaml_topic}"
        description: "Trending now: A deep dive into {safe_yaml_topic}. Read our comprehensive analysis and latest updates."
        tags: ["Trending", "News", "Deep Dive"]
        ---

        ## Introduction to {topic}
        [Write 2-3 engaging paragraphs explaining the core of the trend]

        ## Key Highlights and Breakdown
        [Provide detailed context, using bullet points for readability]

        ## Why is Everyone Talking About This?
        [Analyze the public reaction, market impact, or social significance]

        ## Frequently Asked Questions (FAQ)
        ### What does this mean for the future?
        [Answer explicitly]
        ### Who are the main people or entities involved?
        [Answer explicitly]

        ## Final Thoughts
        [A strong concluding paragraph summarizing the key takeaways]
        """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a professional SEO content writer."},
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

    topics = get_trending_topics(limit=ARTICLE_COUNT)

    if not topics:
        print("未能获取到热点词，程序退出。")
        return

    for i, topic in enumerate(topics):
        print(f"[{i+1}/{len(topics)}] 正在让 AI 撰写热门话题: {topic}")

        md_content = generate_seo_article(topic)

        if md_content:
            # 清理特殊字符，并将过长的标题截断（最多50个字符），防止文件系统报错
            safe_filename = "".join([c if c.isalnum() or c.isspace(
            ) else "" for c in topic.lower()]).replace(" ", "-")
            safe_filename = safe_filename[:50].strip('-')
            filepath = os.path.join(OUTPUT_DIR, f"{safe_filename}.md")

            if md_content.startswith("```markdown"):
                md_content = md_content.replace(
                    "```markdown\n", "").replace("\n```", "")

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            print(f"✅ 生成完毕: {filepath}")

        time.sleep(2)

    print("🎉 今日热点内容抓取与生成全部完成！")


if __name__ == "__main__":
    main()
