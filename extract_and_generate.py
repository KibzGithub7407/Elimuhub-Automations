import requests
import openai

# 1. Fetch top articles from Serper API
SERPER_API_KEY = 'your_serper_api_key'
query = "Muslim school placement Kenya"
serper_resp = requests.post(
    "https://google.serper.dev/search",
    headers={"X-API-KEY": SERPER_API_KEY},
    json={"q": query}
).json()
top_articles = serper_resp['organic'][:5]

# 2. Prepare summary
summaries = [article['snippet'] for article in top_articles]
summaries_text = "\n".join(summaries)

# 3. Generate blog post using OpenAI (replace with your key)
openai.api_key = "your_openai_key"
prompt = f"Write an SEO-optimized blog post for Elimuhub about '{query}'. Use these article summaries as background:\n{summaries_text}"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=500
)
blog_post = response.choices[0].text.strip()

# 4. Save as Markdown
with open("2025-07-22-muslim-school-placement-kenya.md", "w") as f:
    f.write(f"# Muslim School Placement in Kenya\n\n{blog_post}")
