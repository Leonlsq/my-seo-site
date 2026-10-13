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

# 2. 混合多个高质量长尾/垂直领域的 RSS 数据源 (重点优化: 流量生命周期更长)
RSS_FEEDS = [
    "https://techcrunch.com/feed/",  # TechCrunch 科技创投前沿
    "https://www.reddit.com/r/technology/top.rss?t=day",  # Reddit 真实科技热点
    "https://www.reddit.com/r/pcgaming/top.rss?t=day",  # Reddit 游戏长尾问题
    "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"  # 谷歌综合新闻 (保底)
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

            # 抓取标题
            for item in root.findall('.//item/title') + root.findall('.//entry/title'):
                if item.text:
                    clean_title = re.sub(r'\s*-.*$', '', item.text)  # 清理尾部媒体名
                    # 过滤掉太短的废话标题
                    if clean_title not in topics and len(clean_title) > 15:
                        topics.append(clean_title)
        except Exception as e:
            print(f"⚠️ 抓取 {url} 失败: {e}")
            continue

    # 随机打乱话题，保证每天生成的文章领域多样化
    random.shuffle(topics)
    final_topics = topics[:limit]
    print(f"🔥 成功获取 {len(final_topics)} 个精选热点话题！")
    return final_topics


def generate_seo_article(topic):
    # 防崩补丁：清理可能破坏 YAML 的双引号
    safe_yaml_topic = topic.replace('"', "'")

    # 重点优化: 自动注入当前时间 (YYYY-MM-DD 格式)
    current_date = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
        You are an expert tech, gaming, and news blogger. 
        The current trending topic/keyword is "{topic}". 
        Write a highly detailed, engaging, and SEO-optimized comprehensive guide or analysis.
        
        CRITICAL RULES:
        1. Output EXACTLY in valid Markdown format.
        2. MUST include YAML Frontmatter at the beginning. 
        3. NO DOUBLE QUOTES inside the YAML values to prevent build errors. Use single quotes if needed.
        4. Write AT LEAST 600 words. Use H2 (##) and H3 (###) headings.
        5. Craft an irresistible, highly clickable, and human-like SEO headline (under 65 characters) for the `title` frontmatter. DO NOT use repetitive prefixes like "Complete Guide:". Make it sound natural and click-worthy.

        Follow this exact structure for the Frontmatter:

        ---
        title: [Your engaging, highly clickable SEO headline here]
        description: [A compelling meta description under 150 characters summarizing the article]
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
            # 清理特殊字符生成文件名，并过滤连续的横杠
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

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            print(f"✅ 生成完毕: {filepath}")

        time.sleep(2)

    print("🎉 今日高质量 SEO 内容抓取与生成全部完成！")


if __name__ == "__main__":
    main()
