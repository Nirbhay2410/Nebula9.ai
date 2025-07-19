from langchain_google_genai import ChatGoogleGenerativeAI
import json

class PlannerAgent:
    def __init__(self):
        gemini_api_key = "AIzaSyCDvE1YrktUPzWyK6t7-RhFxq0_Ny2qIfo"  # Replace with your key

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=gemini_api_key,
        )

    async def create_plan(self, topic: str):
        prompt = f"""
        You are a research planner. Break down the topic: \"{topic}\" into 3-5 key subtopics.
        For each subtopic, provide a short web search query.

        IMPORTANT: Return ONLY valid JSON list in this exact format:
        [
          {{"subtopic": "Some Subtopic", "query": "best search query"}},
          {{"subtopic": "Another One", "query": "another query"}}
        ]
        """

        response = await self.llm.ainvoke(prompt)

        try:
            return json.loads(response.content)
        except Exception as e:
            print("[PlannerAgent] JSON parse failed:", e)
            # ✅ fallback subtopics
            return [
                {"subtopic": f"Overview of {topic}", "query": f"{topic} overview"},
                {"subtopic": f"Latest research on {topic}", "query": f"latest research {topic}"},
                {"subtopic": f"Pros & cons of {topic}", "query": f"pros cons {topic}"}
            ]
