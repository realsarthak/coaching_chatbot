from institute_data import institute_info

def get_bot_response(user_message):
    msg = user_message.lower().strip()

    # Greeting
    if any(word in msg for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        return f"Hello! Welcome to {institute_info['name']}. How can I help you today with courses, fees, admissions, or batches?"

    # Courses
    if "course" in msg or "courses" in msg:
        return (
            "We offer the following courses:\n"
            "1. JEE Preparation Program\n"
            "2. NEET Preparation Program\n"
            "3. Class 11-12 Boards Excellence Batch\n"
            "4. Foundation Course (Class 8-10)\n\n"
            "You can ask me about any specific course."
        )

    # JEE
    if "jee" in msg:
        course = institute_info["courses"]["jee"]
        return (
            f"{course['name']}\n"
            f"Duration: {course['duration']}\n"
            f"Fees: {course['fees']}\n"
            f"Mode: {course['mode']}\n"
            f"Best For: {course['best_for']}"
        )

    # NEET
    if "neet" in msg:
        course = institute_info["courses"]["neet"]
        return (
            f"{course['name']}\n"
            f"Duration: {course['duration']}\n"
            f"Fees: {course['fees']}\n"
            f"Mode: {course['mode']}\n"
            f"Best For: {course['best_for']}"
        )

    # Boards
    if "board" in msg or "12th" in msg or "11th" in msg:
        course = institute_info["courses"]["boards"]
        return (
            f"{course['name']}\n"
            f"Duration: {course['duration']}\n"
            f"Fees: {course['fees']}\n"
            f"Mode: {course['mode']}\n"
            f"Best For: {course['best_for']}"
        )

    # Foundation
    if "foundation" in msg or "8th" in msg or "9th" in msg or "10th" in msg:
        course = institute_info["courses"]["foundation"]
        return (
            f"{course['name']}\n"
            f"Duration: {course['duration']}\n"
            f"Fees: {course['fees']}\n"
            f"Mode: {course['mode']}\n"
            f"Best For: {course['best_for']}"
        )

    # Fees
    if "fee" in msg or "fees" in msg or "price" in msg or "cost" in msg:
        return (
            "Our approximate fee structure is:\n"
            "- JEE: ₹85,000 - ₹1,20,000\n"
            "- NEET: ₹80,000 - ₹1,10,000\n"
            "- Boards: ₹35,000 - ₹50,000\n"
            "- Foundation: ₹25,000 - ₹40,000\n\n"
            "If you tell me the course name, I can guide you better."
        )

    # Admissions
    if "admission" in msg or "enroll" in msg or "join" in msg or "registration" in msg:
        return institute_info["admission_process"]

    # Demo class
    if "demo" in msg or "trial" in msg:
        return institute_info["demo_class"]

    # Online classes
    if "online" in msg or "recorded" in msg:
        return institute_info["online_classes"]

    # Hostel
    if "hostel" in msg or "accommodation" in msg:
        return institute_info["hostel"]

    # Scholarship
    if "scholarship" in msg or "discount" in msg:
        return institute_info["scholarship"]

    # Timing
    if "timing" in msg or "time" in msg or "open" in msg:
        return f"Our institute timings are: {institute_info['timings']}"

    # Location
    if "location" in msg or "address" in msg or "where" in msg:
        return f"We are located in {institute_info['location']}."

    # Contact
    if "contact" in msg or "phone" in msg or "email" in msg:
        return (
            f"You can contact us at:\n"
            f"Phone: {institute_info['contact']}\n"
            f"Email: {institute_info['email']}"
        )

    # Best course recommendation
    if "which course" in msg or "best course" in msg or "help me choose" in msg:
        return (
            "Sure! Here's a simple guide:\n"
            "- Choose JEE if you want engineering entrance preparation.\n"
            "- Choose NEET if you want medical entrance preparation.\n"
            "- Choose Boards Batch if your main goal is school exam performance.\n"
            "- Choose Foundation if you are in class 8-10 and want early preparation.\n\n"
            "Tell me your class and goal, and I’ll suggest the best course."
        )

    # Smart student guidance
    if "i am in class 11" in msg or "i'm in class 11" in msg:
        return "If you're in Class 11, JEE / NEET 2-year programs or Boards Excellence Batch would be ideal depending on your goal."

    if "i am in class 12" in msg or "i'm in class 12" in msg:
        return "If you're in Class 12, you can choose JEE / NEET 1-year batches or Boards Excellence Batch depending on your target."

    if "dropper" in msg:
        return "For droppers, our JEE and NEET crash/target batches are specially designed for focused preparation."

    # Restriction: unrelated queries
    institute_keywords = [
        "course", "jee", "neet", "board", "foundation", "fee", "admission",
        "enroll", "join", "demo", "online", "class", "hostel", "scholarship",
        "timing", "location", "address", "contact", "batch", "faculty", "student"
    ]

    if not any(keyword in msg for keyword in institute_keywords):
        return "I can only help with coaching institute related queries such as courses, fees, admissions, schedules, and batches."

    return "Can you please rephrase your question? I can help with courses, admissions, fees, schedules, demo classes, and student guidance."