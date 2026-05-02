def evaluate_answers(user_answers):
    # Correct answers (example)
    correct_answers = {
        "q1": "A",
        "q2": "B",
        "q3": "C"
    }

    score = 0
    total = len(correct_answers)

    for q, ans in correct_answers.items():
        if user_answers.get(q) == ans:
            score += 1

    result = {
        "score": score,
        "total": total,
        "percentage": (score / total) * 100
    }

    return result