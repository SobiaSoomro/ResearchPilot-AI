from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

styles = getSampleStyleSheet()


def export_pdf(plan, analyses, gap, review):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ResearchPilot_Report_{timestamp}.pdf"
    pdf = SimpleDocTemplate(filename)

    elements = []

    elements.append(Paragraph("<b>ResearchPilot AI Report</b>", styles["Title"]))

    elements.append(Paragraph("<br/><b>Research Plan</b>", styles["Heading1"]))
    elements.append(Paragraph(plan.replace("\n", "<br/>"), styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Paper Analyses</b>", styles["Heading1"]))
    elements.append(Paragraph(
        "<br/><br/>".join(analyses).replace("\n", "<br/>"),
        styles["BodyText"]
    ))

    elements.append(Paragraph("<br/><b>Research Gap</b>", styles["Heading1"]))
    elements.append(Paragraph(gap.replace("\n", "<br/>"), styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Literature Review</b>", styles["Heading1"]))
    elements.append(Paragraph(review.replace("\n", "<br/>"), styles["BodyText"]))

    pdf.build(elements)

    return filename