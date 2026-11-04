import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Modern Tech Theme Palette
    DARK_BG       = RGBColor(15, 23, 42)      # Deep Slate (#0F172A)
    SURFACE_DARK  = RGBColor(30, 41, 59)      # Slate (#1E293B)
    CARD_BG       = RGBColor(248, 250, 252)   # Crisp Off-White (#F8FAFC)
    BORDER_COLOR  = RGBColor(226, 232, 240)   # Light Slate Border (#E2E8F0)
    
    PRIMARY_BLUE  = RGBColor(37, 99, 235)     # Royal Blue (#2563EB)
    ACCENT_INDIGO = RGBColor(79, 70, 229)     # Indigo (#4F46E5)
    ACCENT_GREEN  = RGBColor(16, 185, 129)    # Emerald Green (#10B981)
    ACCENT_AMBER  = RGBColor(245, 158, 11)    # Amber Gold (#F59E0B)
    ACCENT_RED    = RGBColor(239, 68, 68)     # Crimson Red (#EF4444)
    ACCENT_CYAN   = RGBColor(6, 182, 212)     # Sky Cyan (#06B6D4)
    
    TEXT_DARK     = RGBColor(15, 23, 42)      # Dark Charcoal
    TEXT_MUTED    = RGBColor(100, 116, 139)   # Slate Muted Gray
    WHITE         = RGBColor(255, 255, 255)

    def add_header(slide, title, category="AUTOMATED CI/CD DEVOPS PROJECT"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_INDIGO

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.75))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 1: Title Slide (Professional Dark Theme)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = DARK_BG
    bg1.line.color.rgb = DARK_BG

    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Automated CI/CD Pipeline"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Production-Grade Student Management System with Jenkins, Docker, Maven, GitHub & AWS"
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.space_before = Pt(12)

    badges = [
        ("Java 17 & Spring Boot 3", ACCENT_INDIGO),
        ("Jenkins CI/CD Server", ACCENT_RED),
        ("Apache Maven & JUnit 5", ACCENT_AMBER),
        ("Docker Containers", ACCENT_CYAN),
        ("GitHub Cloud SCM", PRIMARY_BLUE),
        ("Amazon AWS EC2", ACCENT_GREEN)
    ]
    bx = Inches(1.0)
    by = Inches(4.3)
    for txt, col in badges:
        badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, by, Inches(1.8), Inches(0.55))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.color.rgb = col
        btf = badge.text_frame
        bp = btf.paragraphs[0]
        bp.text = txt
        bp.font.size = Pt(10)
        bp.font.bold = True
        bp.font.color.rgb = WHITE
        bp.alignment = PP_ALIGN.CENTER
        bx += Inches(1.9)

    info_box = s1.shapes.add_textbox(Inches(1.0), Inches(5.6), Inches(11.3), Inches(1.2))
    itf = info_box.text_frame
    ip1 = itf.paragraphs[0]
    ip1.text = "Developer & Presenter: Sanjay  |  Repository: github.com/sanjay-2005732/devopsproject"
    ip1.font.size = Pt(13)
    ip1.font.bold = True
    ip1.font.color.rgb = WHITE
    ip2 = itf.add_paragraph()
    ip2.text = "Project Scope: Automated Testing, Continuous Integration, Multi-Stage Containerization & Cloud Deployment"
    ip2.font.size = Pt(11)
    ip2.font.color.rgb = RGBColor(148, 163, 184)
    ip2.space_before = Pt(6)

    # =========================================================================
    # SLIDE 2: Project Objectives & Tech Stack Breakdown
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Project Objectives & Technology Stack Architecture", "SYSTEM SPECIFICATIONS")

    tools = [
        ("Git & GitHub", "Source Code Management", "Centralized repository for version control, collaborative branch management, and automated webhook triggers.", PRIMARY_BLUE),
        ("Apache Maven 3.9", "Build & Dependency Engine", "Automates dependency resolution, byte compilation, and produces standard 52.7 MB production executable JAR.", ACCENT_AMBER),
        ("JUnit 5 & Mockito", "Automated Testing Suite", "Executes 17 automated unit and integration tests across controllers, repositories, and services with 100% pass rate.", ACCENT_RED),
        ("Jenkins LTS 2.479", "CI/CD Orchestration", "Continuous Integration server running on Port 8081; executes automated build pipelines triggered via Git polling & webhooks.", ACCENT_RED),
        ("Docker Engine", "Containerization", "Multi-stage Dockerfile packaging the Spring Boot application into lightweight, portable, production-ready Alpine containers.", ACCENT_CYAN),
        ("Amazon AWS EC2", "Cloud Production Server", "Target cloud virtual machine (Ubuntu 24.04 LTS / t2.micro) with configured Security Groups on ports 22, 80, and 8080.", ACCENT_GREEN)
    ]

    for idx, (t_name, t_role, t_desc, col) in enumerate(tools):
        row = idx // 3
        col_idx = idx % 3
        cx = Inches(0.8 + col_idx * 3.95)
        cy = Inches(1.8 + row * 2.5)

        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, Inches(3.75), Inches(2.25))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.8)

        tb = s2.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.2), Inches(3.35), Inches(1.85))
        ctf = tb.text_frame
        ctf.word_wrap = True
        p_name = ctf.paragraphs[0]
        p_name.text = t_name
        p_name.font.size = Pt(14)
        p_name.font.bold = True
        p_name.font.color.rgb = col

        p_role = ctf.add_paragraph()
        p_role.text = t_role
        p_role.font.size = Pt(10)
        p_role.font.bold = True
        p_role.font.color.rgb = TEXT_DARK
        p_role.space_before = Pt(3)

        p_desc = ctf.add_paragraph()
        p_desc.text = t_desc
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_before = Pt(6)

    # =========================================================================
    # SLIDE 3: The Core DevOps Concept - Code vs User Data
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Crucial DevOps Distinction: What Goes to Git vs Database?", "FUNDAMENTAL CONCEPTS")

    # Left: Git Code
    c_git = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_git.fill.solid()
    c_git.fill.fore_color.rgb = CARD_BG
    c_git.line.color.rgb = PRIMARY_BLUE
    c_git.line.width = Pt(2)

    h_git = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(0.75))
    h_git.fill.solid()
    h_git.fill.fore_color.rgb = PRIMARY_BLUE
    h_git.line.color.rgb = PRIMARY_BLUE
    hp_g = h_git.text_frame.paragraphs[0]
    hp_g.text = "1. GITHUB REPOSITORY  (The Software Blueprint)"
    hp_g.font.size = Pt(12)
    hp_g.font.bold = True
    hp_g.font.color.rgb = WHITE
    hp_g.alignment = PP_ALIGN.CENTER

    tb_g = s3.shapes.add_textbox(Inches(1.0), Inches(2.7), Inches(5.2), Inches(3.8))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    g_p0 = tf_g.paragraphs[0]
    g_p0.text = "Git tracks only source code, configs, and pipeline files:"
    g_p0.font.size = Pt(11.5)
    g_p0.font.bold = True
    g_p0.font.color.rgb = TEXT_DARK
    g_p0.space_after = Pt(8)

    g_points = [
        "src/main/java/.. (REST controllers, entities, service logic)",
        "src/main/resources/static/ (HTML5, CSS3, JavaScript UI)",
        "pom.xml (Maven project object model & dependency rules)",
        "Dockerfile & docker-compose.yml (Container blueprints)",
        "Jenkinsfile (8-stage CI/CD automated pipeline script)",
        "RULE: User records (students, grades, emails) NEVER go to Git!"
    ]
    for pt in g_points:
        p = tf_g.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.bold = True if "RULE:" in pt else False
        p.font.color.rgb = TEXT_DARK if "RULE:" in pt else TEXT_MUTED
        p.space_after = Pt(5)

    # Right: Database Data
    c_db = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    c_db.fill.solid()
    c_db.fill.fore_color.rgb = CARD_BG
    c_db.line.color.rgb = ACCENT_GREEN
    c_db.line.width = Pt(2)

    h_db = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(0.75))
    h_db.fill.solid()
    h_db.fill.fore_color.rgb = ACCENT_GREEN
    h_db.line.color.rgb = ACCENT_GREEN
    hp_d = h_db.text_frame.paragraphs[0]
    hp_d.text = "2. DATABASE STORAGE  (The Dynamic Student Data)"
    hp_d.font.size = Pt(12)
    hp_d.font.bold = True
    hp_d.font.color.rgb = WHITE
    hp_d.alignment = PP_ALIGN.CENTER

    tb_d = s3.shapes.add_textbox(Inches(7.0), Inches(2.7), Inches(5.3), Inches(3.8))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True
    d_p0 = tf_d.paragraphs[0]
    d_p0.text = "The Database persists user input entered in the running app:"
    d_p0.font.size = Pt(11.5)
    d_p0.font.bold = True
    d_p0.font.color.rgb = TEXT_DARK
    d_p0.space_after = Pt(8)

    d_points = [
        "Student Names (e.g. Sanjay, Rahul Sharma, Priya Patel)",
        "Student Emails, Contact Phone, and Enrolled Courses",
        "Managed by JPA/Hibernate ORM with automated schema creation",
        "Persisted in H2 In-Memory DB or production AWS RDS MySQL",
        "CRUD Operations (Create, Read, Update, Delete) happen live",
        "RULE: Adding student records saves to DB, NOT a git commit!"
    ]
    for pt in d_points:
        p = tf_d.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(10.5)
        p.font.bold = True if "RULE:" in pt else False
        p.font.color.rgb = RGBColor(185, 28, 28) if "RULE:" in pt else TEXT_MUTED
        p.space_after = Pt(5)

    # =========================================================================
    # SLIDE 4: End-to-End System Workflow
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "The Complete End-to-End Automated DevOps Workflow", "PIPELINE LIFECYCLE")

    steps = [
        ("1. Developer Writes Code", "Developer writes Java classes and web assets in local environment. Tests are built locally to verify business logic.", PRIMARY_BLUE),
        ("2. Git Push to GitHub", "Developer executes 'git push origin main'. GitHub Cloud securely registers the commit and triggers automation.", PRIMARY_BLUE),
        ("3. Jenkins Automated Trigger", "Jenkins detects the push via SCM Polling / Webhook and automatically initiates Build #10, #11, etc. on Port 8081.", ACCENT_INDIGO),
        ("4. Maven Compile & Testing", "Maven automatically compiles Java bytecode and runs 17 JUnit 5 test cases. Builds fail immediately if tests break.", ACCENT_AMBER),
        ("5. Containerization with Docker", "Docker packages the tested Spring Boot JAR into a lightweight, isolated Linux container image ready for distribution.", ACCENT_CYAN),
        ("6. Cloud Deployment to AWS EC2", "The verified Docker image is deployed to an Amazon AWS EC2 virtual server on Port 8080 with live health checks.", ACCENT_GREEN)
    ]

    for idx, (st_t, st_d, st_c) in enumerate(steps):
        sy = Inches(1.75 + idx * 0.88)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), sy, Inches(11.7), Inches(0.78))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = st_c
        card.line.width = Pt(1.5)

        tb = s4.shapes.add_textbox(Inches(1.0), sy + Inches(0.05), Inches(11.3), Inches(0.68))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = st_t
        p1.font.size = Pt(11.5)
        p1.font.bold = True
        p1.font.color.rgb = st_c

        p2 = tf.add_paragraph()
        p2.text = st_d
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(2)

    # =========================================================================
    # SLIDE 5: The 8-Stage Jenkins Pipeline Breakdown
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Deep Dive: The 8 Stages Defined in Jenkinsfile", "JENKINS PIPELINE")

    pipeline_stages = [
        ("1. Git Checkout", "Git SCM", "Fetches latest commit from GitHub (github.com/sanjay-2005732/devopsproject).", PRIMARY_BLUE),
        ("2. Code Compile", "Maven Compile", "Executes: mvn clean compile to validate syntax and compile source code.", PRIMARY_BLUE),
        ("3. Unit Testing", "JUnit 5 / Mockito", "Executes: mvn test. Runs 17 unit test suites; validates all controller & DB constraints.", ACCENT_RED),
        ("4. Code Quality", "SonarQube Scan", "Analyzes code complexity, security vulnerabilities, code smells, and test coverage.", ACCENT_INDIGO),
        ("5. Artifact Packaging", "Spring Boot JAR", "Executes: mvn package. Creates production JAR student-management-app-1.0.0.jar (52.7 MB).", ACCENT_AMBER),
        ("6. Docker Build", "Multi-Stage Build", "Packages JAR into minimal Alpine container: docker build -t student-management-app:latest .", ACCENT_CYAN),
        ("7. Docker Push", "Container Registry", "Pushes built container image to registry (Docker Hub / AWS ECR) for cloud distribution.", ACCENT_CYAN),
        ("8. Cloud Deployment", "AWS EC2 / SSH", "Deploys container onto AWS EC2 instance at Port 8080 and verifies /actuator/health.", ACCENT_GREEN)
    ]

    for idx, (st_name, st_tool, st_desc, col) in enumerate(pipeline_stages):
        row = idx // 4
        c_idx = idx % 4
        sx = Inches(0.8 + c_idx * 2.95)
        sy = Inches(1.8 + row * 2.5)

        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, sy, Inches(2.8), Inches(2.3))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.8)

        tag = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx + Inches(0.12), sy + Inches(0.12), Inches(2.56), Inches(0.42))
        tag.fill.solid()
        tag.fill.fore_color.rgb = col
        tag.line.color.rgb = col
        ttp = tag.text_frame.paragraphs[0]
        ttp.text = st_name
        ttp.font.size = Pt(10.5)
        ttp.font.bold = True
        ttp.font.color.rgb = WHITE
        ttp.alignment = PP_ALIGN.CENTER

        tb = s5.shapes.add_textbox(sx + Inches(0.12), sy + Inches(0.62), Inches(2.56), Inches(1.55))
        tf = tb.text_frame
        tf.word_wrap = True
        tp1 = tf.paragraphs[0]
        tp1.text = f"Tool: {st_tool}"
        tp1.font.size = Pt(10.5)
        tp1.font.bold = True
        tp1.font.color.rgb = TEXT_DARK

        tp2 = tf.add_paragraph()
        tp2.text = st_desc
        tp2.font.size = Pt(9.5)
        tp2.font.color.rgb = TEXT_MUTED
        tp2.space_before = Pt(4)

    # =========================================================================
    # SLIDE 6: Real Execution Results & Verification Proof
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Live Project Execution & Verification Results", "VERIFIED RESULTS")

    results = [
        ("GitHub Repository", "35+ files committed & pushed", "Live on main branch with complete backend, frontend, Dockerfile, Jenkinsfile, and workflow configurations.", PRIMARY_BLUE),
        ("Jenkins Server (Port 8081)", "Builds #8, #9, #10, #11, #12 SUCCESS", "Automated builds executed with zero errors. Demonstrated automated polling detection on commit push.", ACCENT_GREEN),
        ("JUnit Test Automation", "17 / 17 Tests Passed (0 Failures)", "Comprehensive coverage across StudentControllerTest, StudentServiceTest, and StudentRepositoryTest.", ACCENT_GREEN),
        ("Maven Packaging", "52.7 MB Executable JAR Generated", "Single-command standalone executable bundled with embedded Tomcat container and all dependencies.", ACCENT_AMBER),
        ("Web Application (Port 8080)", "Real-Time CRUD Web Portal", "Student Registration, List, Search, Stats, and live interactive database operations working on localhost:8080.", PRIMARY_BLUE),
        ("DevOps Live Dashboard", "Multi-Tool Explorer & 8 Stages", "Interactive control center with real-time log streaming, tool tab inspection (Jenkins, Maven, Docker, AWS).", ACCENT_INDIGO)
    ]

    for idx, (res_title, res_stat, res_detail, col) in enumerate(results):
        row = idx // 2
        col_idx = idx % 2
        rx = Inches(0.8 + col_idx * 5.95)
        ry = Inches(1.8 + row * 1.65)

        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, ry, Inches(5.75), Inches(1.45))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.8)

        tb = s6.shapes.add_textbox(rx + Inches(0.2), ry + Inches(0.12), Inches(5.35), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = res_title + "  ➔  " + res_stat
        p_t.font.size = Pt(11.5)
        p_t.font.bold = True
        p_t.font.color.rgb = col

        p_d = tf.add_paragraph()
        p_d.text = res_detail
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_before = Pt(4)

    # =========================================================================
    # SLIDE 7: Amazon AWS EC2 Cloud Production Deployment
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Target Cloud Infrastructure: Amazon AWS EC2 Architecture", "AWS CLOUD ARCHITECTURE")

    aws_cards = [
        ("1. EC2 Virtual Machine Instance", "Ubuntu Server 24.04 LTS (t2.micro / t3.micro)", "Provisions a virtual cloud server in AWS Cloud. Free Tier eligible with 1 vCPU and 1 GB memory.", PRIMARY_BLUE),
        ("2. Security Group Firewall Rules", "Ports 22 (SSH), 80 (HTTP), 8080 (Custom TCP)", "Configured inbound firewall rules: Port 22 for secure admin terminal, Port 8080 for Student App access.", ACCENT_AMBER),
        ("3. SSH Key Pair Authentication", "RSA 2048-bit Private Key (.pem file)", "Provides cryptographic passwordless authentication for Jenkins and engineers to securely access the cloud node.", ACCENT_INDIGO),
        ("4. Containerized Execution", "Docker Engine on EC2 Instance", "Runs docker run -d -p 8080:8080 student-app. Guarantees identical execution between dev and cloud.", ACCENT_CYAN),
        ("5. Public Access & DNS", "Global Elastic IPv4 Address", "Accessible worldwide via browser at http://<EC2-PUBLIC-IP>:8080 by students, faculty, and administrators.", ACCENT_GREEN),
        ("6. Cloud Monitoring & Health", "AWS CloudWatch & Spring Boot Actuator", "Continuously monitors server CPU, memory, network I/O, and pings /actuator/health for self-healing restarts.", ACCENT_GREEN)
    ]

    for idx, (title, subtitle, desc, col) in enumerate(aws_cards):
        row = idx // 2
        col_idx = idx % 2
        ax = Inches(0.8 + col_idx * 5.95)
        ay = Inches(1.8 + row * 1.65)

        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ax, ay, Inches(5.75), Inches(1.45))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.8)

        tb = s7.shapes.add_textbox(ax + Inches(0.2), ay + Inches(0.12), Inches(5.35), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(11.5)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_DARK
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = TEXT_MUTED
        p3.space_before = Pt(2)

    # =========================================================================
    # SLIDE 8: Summary & Viva / Interview Quick Reference (Dark Closing Slide)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    bg8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg8.fill.solid()
    bg8.fill.fore_color.rgb = DARK_BG
    bg8.line.color.rgb = DARK_BG

    c_box = s8.shapes.add_textbox(Inches(1.0), Inches(1.0), Inches(11.3), Inches(5.8))
    ctf = c_box.text_frame
    ctf.word_wrap = True
    cp1 = ctf.paragraphs[0]
    cp1.text = "DevOps Viva & Interview Summary: 30-Second Elevator Pitch"
    cp1.font.size = Pt(26)
    cp1.font.bold = True
    cp1.font.color.rgb = WHITE

    takeaways = [
        "1. THE APPLICATION: A full-stack Spring Boot CRUD web application running on Java 17 with an H2 in-memory database.",
        "2. CODE VS DATA: Source code (Java, HTML, pom.xml, Jenkinsfile) is version-controlled in GitHub. Student records are saved in the Database.",
        "3. CONTINUOUS INTEGRATION: On git push, Jenkins automatically triggers, pulls code, compiles, and verifies 17/17 automated JUnit 5 tests.",
        "4. CONTINUOUS DELIVERY: Jenkins packages the production JAR (52.7 MB) and builds a portable Docker container using multi-stage builds.",
        "5. CLOUD DEPLOYMENT: Deployed to an Amazon AWS EC2 instance running Ubuntu 24.04 LTS on port 8080 with automated health checks.",
        "6. PROVEN RESULTS: Jenkins Builds #8, #9, #10, #11, and #12 verified with 100% SUCCESS; GitHub Actions green in cloud."
    ]
    for t in takeaways:
        tp = ctf.add_paragraph()
        tp.text = "✔ " + t
        tp.font.size = Pt(12)
        tp.font.color.rgb = RGBColor(226, 232, 240)
        tp.space_before = Pt(8)

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'Automated_CICD_Pipeline_DevOps_Project.pptx'
    create_deck(out)
