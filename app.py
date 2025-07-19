import streamlit as st
import nest_asyncio
import asyncio
from main import run_research_pipeline

nest_asyncio.apply()

st.set_page_config(page_title="Self-Correcting Multi-Agent Research", layout="wide")

st.title("🤖 Self-Correcting Multi-Agent Research Team")

topic = st.text_input("Enter your research topic:", "")

if st.button("🚀 Run Research") and topic:
    st.info(f"Running research on: **{topic}** ... please wait")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    md_path, pdf_path = loop.run_until_complete(run_research_pipeline(topic))

    st.success(f"✅ Research complete! Report generated.")

    # Show Markdown preview
    with open(md_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    st.subheader("📄 Final Report (Preview)")
    st.markdown(report_content)

    # Download PDF button
    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="⬇️ Download PDF Report",
            data=pdf_file,
            file_name="Research_Report.pdf",
            mime="application/pdf"
        )
