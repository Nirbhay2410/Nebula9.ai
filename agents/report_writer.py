import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

class ReportWriter:
    def write_report(self, topic, validated_results):
        md_filename = "final_report.md"
        pdf_filename = "final_report.pdf"

        # --- Write Markdown for Streamlit preview ---
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(f"# Research Report: {topic}\n\n")
            for res in validated_results:
                f.write(f"## {res['subtopic']}\n\n")
                f.write(f"{res['summary']}\n\n")
                if res['url'] and res['url'] != "N/A":
                    f.write(f"🔗 [Source]({res['url']})\n\n")
            f.write("\n---\n\n## References\n")
            for res in validated_results:
                if res['url'] and res['url'] != "N/A":
                    f.write(f"- [{res['subtopic']}]({res['url']})\n")

        # --- Generate PDF ---
        doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Title style
        title_style = ParagraphStyle(
            "TitleStyle",
            parent=styles["Title"],
            fontSize=22,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#003366"),
        )

        story.append(Paragraph(f"Research Report: {topic}", title_style))
        story.append(Spacer(1, 20))

        # Section styles
        header_style = ParagraphStyle(
            "HeaderStyle",
            parent=styles["Heading2"],
            textColor=colors.darkblue,
        )
        body_style = ParagraphStyle(
            "BodyStyle",
            parent=styles["Normal"],
            fontSize=11,
            leading=16,
        )

        # Convert markdown bold **text** → <b>text</b>
        def markdown_to_html(text):
            return re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

        # Add content
        for res in validated_results:
            story.append(Paragraph(res["subtopic"], header_style))
            story.append(Spacer(1, 6))

            converted_summary = markdown_to_html(res["summary"])
            story.append(Paragraph(converted_summary, body_style))
            story.append(Spacer(1, 8))

            if res['url'] and res['url'] != "N/A":
                story.append(
                    Paragraph(
                        f"<b>Source:</b> <a href='{res['url']}'>{res['url']}</a>",
                        body_style,
                    )
                )
            story.append(Spacer(1, 12))

        # References
        story.append(Spacer(1, 20))
        story.append(Paragraph("References", header_style))
        for res in validated_results:
            if res['url'] and res['url'] != "N/A":
                story.append(
                    Paragraph(f"• <a href='{res['url']}'>{res['subtopic']}</a>", body_style)
                )

        doc.build(story)

        return md_filename, pdf_filename
