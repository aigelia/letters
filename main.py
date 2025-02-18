from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
load_dotenv("/Users/mayakovskaya_k/Documents/Python projects/letters/login.env")

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

letter = """From: devmanorg@yandex.ru
To: 89372361065@list.ru
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.replace("%website%", "https://dvmn.org/profession-ref-program/e.mayakovskaya/6BNMc/")
letter = letter.replace("%friend_name%","Иван Иванов")
letter = letter.replace("%my_name%","Катерина Маяковская")
letter = letter.encode("UTF-8")
print(letter)

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(email, password)
server.sendmail("devmanorg@yandex.ru", "89372361065@list.ru", letter)
server.quit()