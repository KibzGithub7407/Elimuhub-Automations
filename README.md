# Elimuhub-Automations

Automated workflow for generating, updating, and publishing SEO-friendly educational blog content for Elimuhub Education Consultants.

## Workflow Overview

1. **Extract Trending Data**  
   Uses Serper API to fetch top articles based on target keywords.
2. **Generate Content**  
   Uses OpenAI to generate a full blog post using the summaries.
3. **Publish**  
   Saves the content as a Markdown file suitable for static site hosting (e.g., GitHub Pages).
4. **Automate**  
   Runs via GitHub Actions on a schedule or manual trigger, and commits new posts.

## Getting Started

1. **Set up repository secrets**
   - `SERPER_API_KEY`: API key from [Serper](https://serper.dev/)
   - `OPENAI_API_KEY`: API key from [OpenAI](https://platform.openai.com/)

2. **Adjust the keyword**  
   Edit `scripts/extract_and_generate.py` and change the `query` variable to your desired keyword or automate its input.

3. **Run the workflow**  
   - Manually via GitHub Actions "Run workflow"
   - Or wait for the scheduled run

4. **Publish your blog**
   - Use GitHub Pages or another static site platform to serve your Markdown from `content/posts/`.

## Folder Structure

- `.github/workflows/automate-content.yml`: Automation workflow
- `scripts/extract_and_generate.py`: Main automation script
- `content/posts/`: Generated blog posts (Markdown)

## Example Output

See `content/posts/` for AI-generated blog posts.
