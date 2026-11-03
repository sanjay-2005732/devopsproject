import sys
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

    # Theme Colors
    PRIMARY_COLOR = RGBColor(30, 41, 59)      # Navy / Slate (#1E293B)
    ACCENT_BLUE   = RGBColor(79, 70, 229)     # Indigo (#4F46E5)
    ACCENT_GREEN  = RGBColor(16, 185, 129)    # Emerald (#10B981)
    ACCENT_AMBER  = RGBColor(245, 158, 11)    # Amber (#F59E0B)
    ACCENT_RED    = RGBColor(239, 68, 68)     # Red (#EF4444)
    TEXT_DARK     = RGBColor(15, 23, 42)      # Dark Slate (#0F172A)
    TEXT_MUTED    = RGBColor(100, 116, 139)   # Slate Muted (#64748B)
    CARD_BG       = RGBColor(248, 250, 252)   # Light Gray (#F8FAFC)
    BORDER_COLOR  = RGBColor(226, 232, 240)   # Border Slate (#E2E8F0)
    WHITE         = RGBColor(255, 255, 255)

    def add_header(slide, title, category="AUTOMATED CI/CD PIPELINE"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.8))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(25)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY_COLOR
    bg1.line.color.rgb = PRIMARY_COLOR

    t_box = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(2.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Automated CI/CD Pipeline"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Student Management Web Application with Jenkins, Docker, Maven & AWS"
    p2.font.size = Pt(22)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.space_before = Pt(14)

    badges = [
        ("Java Spring Boot 3", ACCENT_BLUE),
        ("Jenkins CI/CD", ACCENT_RED),
        ("Docker Containers", RGBColor(14, 165, 233)),
        ("Maven & JUnit", ACCENT_AMBER),
        ("AWS EC2 Cloud", ACCENT_GREEN)
    ]
    bx = Inches(1.2)
    by = Inches(4.5)
    for txt, col in badges:
        badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, by, Inches(2.0), Inches(0.6))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.color.rgb = col
        btf = badge.text_frame
        bp = btf.paragraphs[0]
        bp.text = txt
        bp.font.size = Pt(11)
        bp.font.bold = True
        bp.font.color.rgb = WHITE
        bp.alignment = PP_ALIGN.CENTER
        bx += Inches(2.15)

    sub_box = s1.shapes.add_textbox(Inches(1.2), Inches(5.8), Inches(11.0), Inches(0.8))
    stf = sub_box.text_frame
    sp = stf.paragraphs[0]
    sp.text = "A Complete Guide to Code vs Data, Pipeline Automation, and Cloud Deployment"
    sp.font.size = Pt(13)
    sp.font.color.rgb = RGBColor(148, 163, 184)

    # ==========================================
    # SLIDE 2: THE KEY CONCEPT - Code vs Data
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "The Core Concept: What Goes to GitHub vs What Goes to Database?", "CRITICAL CLARIFICATION")

    # Left Column: GITHUB (Code)
    card_git = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    card_git.fill.solid()
    card_git.fill.fore_color.rgb = CARD_BG
    card_git.line.color.rgb = ACCENT_BLUE
    card_git.line.width = Pt(2)

    top_git = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(0.8))
    top_git.fill.solid()
    top_git.fill.fore_color.rgb = ACCENT_BLUE
    top_git.line.color.rgb = ACCENT_BLUE
    tp_g = top_git.text_frame.paragraphs[0]
    tp_g.text = "1. WHAT GOES INTO GITHUB?  (The Software Code)"
    tp_g.font.size = Pt(12)
    tp_g.font.bold = True
    tp_g.font.color.rgb = WHITE
    tp_g.alignment = PP_ALIGN.CENTER

    tb_g = s2.shapes.add_textbox(Inches(1.0), Inches(2.7), Inches(5.2), Inches(3.8))
    tf_g = tb_g.text_frame
    tf_g.word_wrap = True
    p_g0 = tf_g.paragraphs[0]
    p_g0.text = "GitHub ONLY stores the Blueprint / Software Files:"
    p_g0.font.size = Pt(12)
    p_g0.font.bold = True
    p_g0.font.color.rgb = TEXT_DARK
    p_g0.space_after = Pt(8)

    git_bullets = [
        "src/main/java/.. (Java controllers, entities, logic)",
        "src/main/resources/static/ (HTML pages, CSS, JavaScript)",
        "pom.xml (Tells Maven what libraries to download)",
        "Dockerfile (Tells Docker how to package the app)",
        "Jenkinsfile (Tells Jenkins what 8 stages to run)",
        "NOTE: NO student names or student emails are in GitHub!"
    ]
    for b in git_bullets:
        bp = tf_g.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(11)
        bp.font.color.rgb = TEXT_DARK if "NOTE:" in b else TEXT_MUTED
        bp.font.bold = True if "NOTE:" in b else False
        bp.space_after = Pt(4)

    # Right Column: DATABASE (User Data)
    card_db = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    card_db.fill.solid()
    card_db.fill.fore_color.rgb = CARD_BG
    card_db.line.color.rgb = ACCENT_GREEN
    card_db.line.width = Pt(2)

    top_db = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(0.8))
    top_db.fill.solid()
    top_db.fill.fore_color.rgb = ACCENT_GREEN
    top_db.line.color.rgb = ACCENT_GREEN
    tp_d = top_db.text_frame.paragraphs[0]
    tp_d.text = "2. WHAT GOES INTO DATABASE?  (The Student Records)"
    tp_d.font.size = Pt(12)
    tp_d.font.bold = True
    tp_d.font.color.rgb = WHITE
    tp_d.alignment = PP_ALIGN.CENTER

    tb_d = s2.shapes.add_textbox(Inches(7.0), Inches(2.7), Inches(5.3), Inches(3.8))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True
    p_d0 = tf_d.paragraphs[0]
    p_d0.text = "The Database stores User Input entered in the Browser:"
    p_d0.font.size = Pt(12)
    p_d0.font.bold = True
    p_d0.font.color.rgb = TEXT_DARK
    p_d0.space_after = Pt(8)

    db_bullets = [
        "Student Name (e.g. Rahul Sharma, Amit Kumar)",
        "Student Email (e.g. rahul@email.com)",
        "Department (e.g. Computer Science, Mechanical)",
        "Phone Number (e.g. 9876543210)",
        "Stored in H2 (Memory) or MySQL Database Table",
        "RULE: When you add a student, you are saving data in the Database, NOT editing or pushing code to Git!"
    ]
    for b in db_bullets:
        bp = tf_d.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(11)
        bp.font.color.rgb = RGBColor(185, 28, 28) if "RULE:" in b else TEXT_MUTED
        bp.font.bold = True if "RULE:" in b else False
        bp.space_after = Pt(4)

    # ==========================================
    # SLIDE 3: The Complete End-to-End Workflow
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "The Complete Picture: Developer ➔ Pipeline ➔ End User", "SYSTEM ARCHITECTURE")

    steps_flow = [
        ("Step 1: Developer Writes Code", "Developer writes Java & HTML on their computer in C:\\devopsproject. They do NOT type student data here—they write the code that creates the student form."),
        ("Step 2: Developer Pushes Code to GitHub", "Developer runs 'git push'. The Java files, pom.xml, and Jenkinsfile are stored safely in GitHub Cloud."),
        ("Step 3: GitHub Triggers Jenkins Robot", "GitHub fires a Webhook to Jenkins. Jenkins pulls the code, tests it with JUnit, and packages it with Maven."),
        ("Step 4: Jenkins Deploys via Docker to Server", "Docker builds the container and deploys it live on Port 8080 (locally or on Amazon AWS EC2)."),
        ("Step 5: End User Uses the Live Website", "A teacher or student opens http://localhost:8080 in their browser. NOW they enter student details, which are saved in the Database!")
    ]

    for idx, (title, desc) in enumerate(steps_flow):
        sy = Inches(1.8 + idx * 1.0)
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), sy, Inches(11.7), Inches(0.88))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_BLUE if idx < 3 else ACCENT_GREEN

        tb = s3.shapes.add_textbox(Inches(1.0), sy + Inches(0.06), Inches(11.3), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_BLUE if idx < 3 else ACCENT_GREEN

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(2)

    # ==========================================
    # SLIDE 4: The 8-Stage Jenkins Pipeline
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Detailed Breakdown of the 8 Automated Pipeline Stages", "JENKINS PIPELINE")

    stages = [
        ("1. Checkout", "Git SCM", "Downloads Java code & pom.xml from GitHub into Jenkins workspace.", ACCENT_BLUE),
        ("2. Build", "Maven Compile", "Runs: mvn clean compile to verify syntax and compile .class bytecode.", ACCENT_BLUE),
        ("3. Unit Test", "JUnit 5", "Runs: mvn test. Runs automated tests in StudentServiceTest.java. Fails if broken.", ACCENT_RED),
        ("4. Package", "Maven JAR", "Runs: mvn package. Bundles app into student-management-app-1.0.0.jar.", ACCENT_BLUE),
        ("5. Docker Build", "Multi-Stage", "Runs: docker build. Takes JAR and wraps it in a 148MB Alpine Linux container.", RGBColor(14, 165, 233)),
        ("6. Docker Push", "Registry", "Runs: docker push. Uploads image to Docker Hub or AWS ECR.", RGBColor(14, 165, 233)),
        ("7. Deploy", "AWS / Docker", "Stops old container and launches new container on port 8080.", ACCENT_GREEN),
        ("8. Verify", "Health Check", "Pings /actuator/health. If HTTP 200 OK -> Deployment Successful!", ACCENT_GREEN)
    ]

    for idx, (st_name, st_tool, st_desc, col) in enumerate(stages):
        row = idx // 4
        c_idx = idx % 4
        sx = Inches(0.8 + c_idx * 2.95)
        sy = Inches(1.8 + row * 2.5)

        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, sy, Inches(2.8), Inches(2.25))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(2)

        tag = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx + Inches(0.15), sy + Inches(0.15), Inches(2.5), Inches(0.45))
        tag.fill.solid()
        tag.fill.fore_color.rgb = col
        tag.line.color.rgb = col
        ttp = tag.text_frame.paragraphs[0]
        ttp.text = st_name
        ttp.font.size = Pt(11)
        ttp.font.bold = True
        ttp.font.color.rgb = WHITE
        ttp.alignment = PP_ALIGN.CENTER

        tb = s4.shapes.add_textbox(sx + Inches(0.15), sy + Inches(0.7), Inches(2.5), Inches(1.4))
        tf = tb.text_frame
        tf.word_wrap = True
        tp1 = tf.paragraphs[0]
        tp1.text = f"Tool: {st_tool}"
        tp1.font.size = Pt(11)
        tp1.font.bold = True
        tp1.font.color.rgb = TEXT_DARK

        tp2 = tf.add_paragraph()
        tp2.text = st_desc
        tp2.font.size = Pt(10)
        tp2.font.color.rgb = TEXT_MUTED
        tp2.space_before = Pt(4)

    # ==========================================
    # SLIDE 5: How Code Gets to AWS EC2
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "How Code Reaches AWS Cloud (Step-by-Step)", "AWS CLOUD DEPLOYMENT")

    aws_steps = [
        ("1. You Rent an EC2 Server on AWS", "You launch an Ubuntu/Amazon Linux virtual machine on Amazon Web Services. AWS gives it a Public IP address (e.g., 54.210.12.89)."),
        ("2. Docker is Installed on AWS EC2", "You install Docker on the EC2 machine so it can run containers: sudo apt install docker.io."),
        ("3. Jenkins Connects to AWS via SSH", "Jenkins uses an SSH Key (your-key.pem) to securely log into the AWS EC2 instance over the internet."),
        ("4. Jenkins Pulls and Runs the Container", "Jenkins issues command: docker run -d -p 8080:8080 your-dockerhub/student-management-app:latest on the EC2 machine."),
        ("5. Public Access via Web Browser", "Anyone anywhere in the world can now type http://54.210.12.89:8080 into their phone or laptop and use the Student Management System!")
    ]

    for idx, (title, desc) in enumerate(aws_steps):
        sy = Inches(1.8 + idx * 1.0)
        box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), sy, Inches(11.7), Inches(0.88))
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = ACCENT_AMBER

        tb = s5.shapes.add_textbox(Inches(1.0), sy + Inches(0.06), Inches(11.3), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = RGBColor(180, 83, 9)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(2)

    # ==========================================
    # SLIDE 6: Summary & Interview Guide
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg6.fill.solid()
    bg6.fill.fore_color.rgb = PRIMARY_COLOR
    bg6.line.color.rgb = PRIMARY_COLOR

    c_box = s6.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(11.0), Inches(5.5))
    ctf = c_box.text_frame
    ctf.word_wrap = True
    cp1 = ctf.paragraphs[0]
    cp1.text = "How to Explain this Project in 30 Seconds:"
    cp1.font.size = Pt(28)
    cp1.font.bold = True
    cp1.font.color.rgb = WHITE

    takeaways = [
        "1. THE APPLICATION: A Java Spring Boot & HTML/CSS web app for Student CRUD management with database storage.",
        "2. WHAT GOES TO GIT: The SOURCE CODE (Java files, pom.xml, Jenkinsfile, Dockerfile). NEVER the student records.",
        "3. WHAT GOES TO DB: When a user fills the student form, it saves into H2/MySQL database, NOT Git.",
        "4. THE CI/CD PIPELINE: Jenkins automatically takes code from GitHub, builds with Maven, tests with JUnit, and packages with Docker.",
        "5. THE DEPLOYMENT: Deploys container to AWS EC2 or localhost and verifies health with /actuator/health."
    ]
    for t in takeaways:
        tp = ctf.add_paragraph()
        tp.text = "✔ " + t
        tp.font.size = Pt(13)
        tp.font.color.rgb = RGBColor(226, 232, 240)
        tp.space_before = Pt(10)

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'Automated_CICD_Pipeline_DevOps_Project.pptx'
    create_deck(out)
