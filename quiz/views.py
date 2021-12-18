from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from quiz.models import Quiz, SolvedQuiz

# Create your views here.


def quiz(request, quiz_no):
    if request.method == 'GET':
        quiz = Quiz.objects.get(quiz_no=quiz_no)
        try:
            solved_quiz = SolvedQuiz.objects.get(username = request.user.username)
            print(quiz.quiz_title)
            context = {
                'quiz': quiz,
                'solved_quiz' : solved_quiz
            }
        except:
            context = {
                'quiz': quiz,
            }
        return render(request, 'quiz/quiz.html', context)
    elif request.method == 'POST':
        num = request.POST.get('num')
        ans = request.POST.get('answer')
        quiz = Quiz.objects.get(quiz_no=num)
        answer_keyword = quiz.answer_keyword

        answer = []
        for i in range(0, len(answer_keyword), 2):
            answer.append(answer_keyword[i:i+2])

        cnt = 0

        for i in range(0, len(answer), 1):
            print(answer[i])
            if answer[i] in ans:
                cnt += 1

        print(cnt)
        if cnt >= 3:
            message = '<script> alert("정답입니다! 정말 대단하시군요."); document.location.href="/quiz/'
            message += quiz_no
            message += '";</script>'
            solved_quiz = SolvedQuiz()
            solved_quiz.username = request.user.username
            solved_quiz.quiz_no = num
            if solved_quiz.objects.get(username = request.user.username):
                id = solved_quiz.id
            solved_quiz.id = id
            solved_quiz.save()
            return HttpResponse(message)
        else:
            message = '<script> alert("오답입니다. 다시 도전해보세요"); document.location.href="/quiz/'
            message += quiz_no
            message += '";</script>'
            return HttpResponse(message)


