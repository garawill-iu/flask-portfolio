from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Sample data for projects
project_list = [
    {
        "header": "Case Presentations",
        "projects": [
            {
                "id": 1,
                "name": "Volkswagen of America Case Analysis",
                "description": "Strategic IT analysis for optimizing VWoA's project portfolio. Based off of a true historic business case.",
                "link": "Case Presentations/Volkswagen Case Analysis.pdf",
                "date": "November 2024",
                "technologies": "Portfolio Management, Strategic Scoring Frameworks, Risk Mitigation",
            },
            {
                "id": 2,
                "name": "TeamViewer Security Analysis",
                "description": "A comprehensive analysis of security challenges and solutions at TeamViewer following an APT29 breach.",
                "link": "Case Presentations/GRC Final Case.pdf",
                "date": "November 2024",
                "technologies": "Cybersecurity, Multi-Factor Authentication, SIEM, Role-Based Access Control",
            },
            {
                "id": 3,
                "name": "LDI IT Transformation Case Study",
                "description": "A detailed transformation plan to centralize and optimize LDI's IT operations, reducing costs and improving efficiency.",
                "link": "Case Presentations/ITM Final Case.pdf",
                "date": "November 2024",
                "technologies": "IT Service Management, Multi-Factor Authentication, Data Center Consolidation, Centralized Helpdesk",
            },
            {
                "id": 4,
                "name": "High Gear Engines IT Risk Management",
                "description": "A strategic IT risk management plan using the ISACA RiskIT framework for identifying and mitigating quick-win risks.",
                "link": "annotated-GRC_ITRisk_HighGear%20%281%29.pptx.pdf",
                "date": "November 2024",
                "technologies": "IT Risk Management, ISACA RiskIT, Centralized IT Operations, Risk Heat Maps",
            }
        ]
    },
    {
        "header": "Business Briefings",
        "projects": [
            {
                "id": 5,
                "name": "Bridge: Interactive Learning Platform",
                "description": "A sales deck showcasing the transformative potential of Bridge, an interactive learning platform that enhances classroom engagement and retention.",
                "link": "Bridge Sales Deck.pdf",
                "date": "November 2024",
                "technologies": "Gamification, Real-Time Feedback, Customizable Challenges, Interactive Environment",
            },
            {
                "id": 6,
                "name": "Product Requirements Document (PRD) for Bridge",
                "description": "A detailed PRD for Bridge, outlining objectives, features, use cases, and technical requirements for implementation.",
                "link": "PRDBridge.pdf",
                "date": "November 2024",
                "technologies": "PRD Development, Gamification, Adaptive Learning",
            },
            {
                "id": 7,
                "name": "Data Modeling Group (DMG) Business Case",
                "description": "A comprehensive proposal to establish a Data Modeling Group for ABT Labs to unify analytics across HR, finance, and facilities.",
                "link": "Business Briefings/BusinessDMGCase.pdf",
                "date": "October 2024",
                "technologies": "Data Modeling, Centralized Analytics, Cross-Functional Integration, Cost Optimization",
            }
        ]
    },
    {
        "header": "Executive Briefings & IT Strategy",
        "projects": [
            {
                "id": 8,
                "name": "Sustainable IT Controls Program",
                "description": "A briefing on creating a sustainable IT controls program to ensure security, compliance, and operational efficiency.",
                "link": "Executive Briefings/LastExecBrifingGRC.pdf",
                "date": "November 2024",
                "technologies": "IT Controls, Risk Mitigation, Compliance",
            },
            {
                "id": 9,
                "name": "BCM and Disaster Recovery Strategy",
                "description": "A comprehensive business continuity and disaster recovery plan for Cocoa-Sassafras Corporation.",
                "link": "Executive Briefings/Williams_Garrett_BCMDR.pdf",
                "date": "November 2024",
                "technologies": "Business Continuity, Disaster Recovery, IT Resilience",
            },
            {
                "id": 10,
                "name": "Vendor Risk Management Briefing",
                "description": "Proposal for a vendor risk management program for HealthNext to address vendor oversight and compliance.",
                "link": "Executive Briefings/Williams_Garrett_VRM_Briefing.pdf",
                "date": "November 2024",
                "technologies": "Vendor Risk Management, Compliance, Risk Assessment",
            },
            {
                "id": 11,
                "name": "Nike Strategic Assessment",
                "description": "A SWOT analysis and IT-enabled strategies for Nike's market positioning and growth.",
                "link": "Williams, Garrett - ITS - Strategy.pdf",
                "date": "October 2024",
                "technologies": "Strategic Planning, SWOT Analysis, IT Enablement",
            },
            {
                "id": 12,
                "name": "Atlantic Paper IAM Debate",
                "description": "A debate around implementing an IAM system versus manual processes for compliance.",
                "link": "Williams_Garrett_AtlanticPaperCaseBriefing.pdf",
                "date": "November 2024",
                "technologies": "Identity Management, Compliance, Risk Mitigation",
            },
            {
                "id": 13,
                "name": "Segregation of Duties Case Briefing",
                "description": "A case analysis on the importance of SoD at Sabre Inc. to strengthen internal controls.",
                "link": "Williams_Garrett_SoDCaseBriefing.pdf",
                "date": "November 2024",
                "technologies": "Segregation of Duties, Internal Controls, Compliance",
            },
             {
                "id": 14,
                "name": "Nike IT Budget Framework",
                "description": "A detailed analysis of Nike's IT budget allocation strategies, focusing on balancing operational maintenance and competitive innovation.",
                "link": "annotated-Williams%2C%20Garrett%20-%20ITS%20-%20Budget%20Framework-1.pdf",
                "date": "October 2024",
                "technologies": "IT Budgeting, Cost Analysis, Innovation Management",
            },
            {
                "id": 15,
                "name": "Six Flags Drone Implementation ROI",
                "description": "An in-depth cost-benefit analysis of integrating drones into Six Flags' operations to enhance revenue and reduce operational costs.",
                "link": "Williams, Garrett - ITS-CA2.pdf",
                "date": "November 2024",
                "technologies": "Cost-Benefit Analysis, ROI Calculation, Drone Technology",
            },
            {
                "id": 16,
                "name": "Tesla Full Self-Driving Strategy",
                "description": "A comprehensive marketing and adoption strategy for Tesla's Full Self-Driving technology to expand market reach and improve user engagement.",
                "link": "Williams, Garrett - ITS-Frameworks.pdf",
                "date": "November 2024",
                "technologies": "Autonomous Driving, Marketing Strategy, Adoption Frameworks",
            }
        ]
    },
    {
        "header": "Not Listed",
        "projects": [
            {
                "id": 17,
                "name": "Digital Cloud Architecture",
                "description": "A project focused on creating zone diagrams and migrating a company’s applications to the cloud, considering vendor options, public/private cloud strategies, risks, security, and CASB solutions.",
                "date": "November 2024",
                "technologies": "Cloud Migration, Zone Diagrams, CASB, Security",
            },
            {
                "id": 18,
                "name": "Agility, Process, & Automation",
                "description": "An exploration of BPMN diagrams, RPA using Automation Anywhere, and workshops on Agile frameworks like Kanban, Scrum, and SAFe.",
                "date": "November 2024",
                "technologies": "BPMN Diagrams, RPA, Kanban, Agile, SAFe",
            },
            {
                "id": 19,
                "name": "Enterprise Platforms",
                "description": "Advanced ERP simulations, creating straw man diagrams, and exploring SAP implementation strategies.",
                "date": "November 2024",
                "technologies": "ERP Simulations, SAP Implementation, Straw Man Diagrams",
            }
        ]
    }
]

@app.route('/')
def home():
    """Route for the About Me page."""
    return render_template('index.html', title='About Me')

@app.route('/projects')
def projects():
    """Route for the Projects page."""
    return render_template('projects.html', title='Projects', project_list=project_list)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    """Route for the Project Details page."""
    # Flatten the project list for lookup
    flat_project_list = [proj for group in project_list for proj in group["projects"]]
    project = next((proj for proj in flat_project_list if proj["id"] == project_id), None)
    if project is None:
        return "Project not found", 404
    return render_template('project_detail.html', title=project["name"], project=project)

@app.route('/view/<int:project_id>')
def view_file(project_id):
    """Route to open project files in a new tab."""
    project = next(
        (proj for group in project_list for proj in group["projects"] if proj["id"] == project_id), None
    )
    if project is None:
        return "File not found", 404

    file_path = os.path.join("static/assets", project["link"])
    return send_file(file_path)

@app.route('/resume')
def resume():
    """Route for the Resume page."""
    return render_template('resume.html', title='Resume')

if __name__ == "__main__":
    app.run(debug=True)
