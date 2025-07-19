import asyncio
from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.critic import CriticAgent
from agents.report_writer import ReportWriter

async def run_research_pipeline(topic: str):
    print(f"[+] Research Topic: {topic}")

    # 1. Planner
    planner = PlannerAgent()
    subtopics = await planner.create_plan(topic)
    if not subtopics or len(subtopics) == 0:
        subtopics = [{"subtopic": topic, "query": topic}]
    print("[Planner] Subtopics:", subtopics)

    # 2. Researcher
    researcher = ResearcherAgent()
    research_results = []
    for s in subtopics:
        research_results.extend(await researcher.research_subtopic(s))

    # 3. Critic
    critic = CriticAgent()
    validated_results = await critic.validate_claims(research_results)

    # 4. Report Writer → returns both .md & .pdf
    writer = ReportWriter()
    md_path, pdf_path = writer.write_report(topic, validated_results)

    return md_path, pdf_path
