from django.shortcuts import render

def quiz(request):
    return render(request, 'quizzer/quiz.html', {})

def results(request):
    question1_answer = request.GET.get('question1', '')
    question2_answer = request.GET.get('question2', '')
    question3_answer = request.GET.get('question3', '')
    score = 0
    results = ["Incorrect", "Incorrect", "Incorrect"]
    if question1_answer == 'Orange':
        score += 1
        results[0] = "Correct"
    if question2_answer == 'Assur':
        score += 1
        results[1] = "Correct"
    if question3_answer == 'which':
        score += 1
        results[2] = "Correct"
    if score == 3:
        score = "100%, You are a Genius!"
    else:
        score = f"{score/3:.0%}. Better luck next time"
    return render(request, 'quizzer/results.html', 
                  {"score": score, "results": results})
