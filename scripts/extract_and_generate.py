import os
import requests
import openai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv('SERPER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

query = "Muslim school placement Kenya"  # Replace or automate as needed

# Fetch top articles from Serper API
response = requests.post(
    "https://google.serper.dev/search",
    headers={"X-API-KEY": SERPER_API_KEY},
    json={"q": query}
).json()
top_articles = response.get('organic', [])[:5]
summaries = [article.get('snippet', '') for article in top_articles]
summaries_text = "\n".join(summaries)

# Generate blog post with OpenAI
openai.api_key = OPENAI_API_KEY
prompt = (
    f"Write an SEO-optimized, 500-word blog post for Elimuhub about '{query}'. "
    f"Use these article summaries as background:\n{summaries_text}"
)
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=600
)
blog_post = response.choices[0].text.strip()

# Save as Markdown
date_str = datetime.now().strftime("%Y-%m-%d")
filename = f"content/posts/{date_str}-{query.lower().replace(' ', '-')}.md"
os.makedirs("content/posts", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"# {query.title()}\n\n{blog_post}\n\n*Published by Elimuhub Education Consultants*")
print(f"Blog post saved as {filename}")
