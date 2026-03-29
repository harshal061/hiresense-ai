def calculate_match(found_skills, required_skills, full_text):
    score = 0

    # Combine everything (skills + resume text)
    combined_text = (" ".join(found_skills) + " " + full_text).lower()

    for skill in required_skills:
        if skill.lower() in combined_text:
            score += 20

    return min(score, 100)