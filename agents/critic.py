from langchain_google_genai import ChatGoogleGenerativeAI

class CriticAgent:
    def __init__(self):
        gemini_api_key = "AIzaSyCDvE1YrktUPzWyK6t7-RhFxq0_Ny2qIfo"
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=gemini_api_key,
        )

    async def validate_claims(self, research_results):
        validated = []
        for res in research_results:
            critique_prompt = f"Review this research summary for factual accuracy and clarity. If unclear, improve it.\n\nSummary:\n{res['summary']}"
            improved = await self.llm.ainvoke(critique_prompt)
            res["summary"] = improved.content.strip() if improved else res["summary"]
            validated.append(res)
        return validated
