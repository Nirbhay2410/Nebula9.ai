import aiohttp
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI

class ResearcherAgent:
    def __init__(self):
        gemini_api_key = "Your Gemni API"

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=gemini_api_key,
        )

    async def search_web(self, query):
        """Search DuckDuckGo and return top 3 URLs"""
        search_url = f"https://duckduckgo.com/html/?q={query}"
        async with aiohttp.ClientSession() as session:
            async with session.get(search_url) as resp:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                links = [a["href"] for a in soup.select("a.result__a")[:3]]
                return links if links else ["https://en.wikipedia.org/wiki/" + query.replace(" ", "_")]

    async def scrape_page(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                text = await resp.text()
                soup = BeautifulSoup(text, "html.parser")
                paragraphs = " ".join(p.get_text() for p in soup.find_all("p"))
                return paragraphs[:4000]  # limit for LLM

    async def research_subtopic(self, subtopic_data):
        query = subtopic_data["query"]
        urls = await self.search_web(query)

        results = []
        for url in urls:
            try:
                content = await self.scrape_page(url)
                if not content.strip():
                    continue

                summary_prompt = f"Summarize key points from this text for subtopic '{subtopic_data['subtopic']}'. Text: {content}"
                summary_resp = await self.llm.ainvoke(summary_prompt)
                summary_text = summary_resp.content.strip() if summary_resp else "No summary generated."

                results.append({
                    "subtopic": subtopic_data["subtopic"],
                    "url": url,
                    "summary": summary_text,
                    "raw": content[:500]
                })
            except Exception as e:
                print("[Researcher] Error scraping:", url, e)

        # ✅ fallback if nothing scraped
        if not results:
            results.append({
                "subtopic": subtopic_data["subtopic"],
                "url": "N/A",
                "summary": f"Could not fetch live data. General overview of {subtopic_data['query']}.",
                "raw": ""
            })

        return results
