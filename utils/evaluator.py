def evaluate_answers(user_answers):
    # Correct answers (example)
    correct_answers = {
        "q1": "B",
        "q2": "B",
        
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