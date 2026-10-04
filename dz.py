def ask_question(question, correct_answer):
    answer = input(question + "\n> ")
    if answer.lower() == correct_answer.lower():
        print("Верно!")
        return True
    else:
        print("Неверно...")
        return False
score = 0

question = [
    ("8 * 3","24"),
    ("60 / 4","15"),
    ("Какая планета в солнечной системе 4 по удалённости от солнца?","марс"),
    ("Какое самое распростронённое имя в религии Ислам","Мухамед"),
    ("Какую планету нашей солнечной системе в древности астрономы называли 'Тусклая звезда'","Уран")]
for q, correct in question:
    if ask_question(q, correct):
        score += 1

print(f"\n Результат: {score} из 5")