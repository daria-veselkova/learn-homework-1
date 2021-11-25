import timeit

questions_and_answers = {
  "Как дела?": "Хорошо!",
  "Ты как?": "Да ничего, жить буду",
  "Что делаешь?": "Программирую",
  "Как там погода?": "Зима пришла, надевай термуху",
  "О чем задумался?": "О вечном...",
  "Когда наступит конец света?": "Ты все проспал, он уже был!",
  "В чем сила, брат?": "В ньютонах",
  "А судьи кто?": "За древностию лет...",
  "Когла покупать доллар?": "В 2010-м, пожалуй"
}


def ask_user_1(question):
    if question in questions_and_answers.keys():
        return questions_and_answers[question]


def ask_user_2(question):
    if question in questions_and_answers:
        return questions_and_answers[question]


def ask_user_3(question):
    if questions_and_answers.get(question):
        return questions_and_answers[question]


print(timeit.timeit(lambda: ask_user_1('Как дела?')))
print(timeit.timeit(lambda: ask_user_2('Как дела?')))
print(timeit.timeit(lambda: ask_user_3('Как дела?')))

