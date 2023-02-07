questions = ["Му name _ Vova", "I _ а coder", "I live _ Moscow"]
answers = ["is", "am", "in"]
correct_ans = 0
tries = 3
total_questions = len(questions)

def print_tries(try_n):
    if try_n == tries - 1:
        print(f"Увы, но нет. Верный ответ: {answers[i]}")
    else:
        print(f"Неправильно.\nОсталось попыток: { tries - try_n - 1}, попробуйте еще раз!")

# Приглашение на игру
print("Привет!\nПредлагаю проверить свои знания английского!\nНаберите \"ready\", чтобы начать!")
user_input = input()
if user_input == "ready":
    for i in range(len(questions)):
        print(questions[i])
        for try_n in range(tries):
            user_input = input()
            if user_input == answers[i]:
                print("ответ верный")
                correct_ans += 1
                break
            else:
                print_tries(try_n)
                
else:
    print("Кажется, вы не хотите играть. Очень жаль.")

# Cсообщаем результаты
correct_percent = round(correct_ans/total_questions*100)
print(f"Вот и все! вы ответили на {correct_ans} вопросов "
      f"из {total_questions} верно, "
      f"это {correct_percent} процентов."
      f"")
