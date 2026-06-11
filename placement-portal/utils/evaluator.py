def evaluate_answers(user_answers):

    correct_answers = {
        "q1": "B",
        "q2": "A"
    }

    score = 0

    for question, correct_answer in correct_answers.items():
        if user_answers.get(question) == correct_answer:
            score += 1

    total = len(correct_answers)

    percentage = round((score / total) * 100, 2)

    return {
        "score": score,
        "total": total,
        "percentage": percentage
    }