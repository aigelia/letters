from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
mail_from = "devmanorg@yandex.ru"
mail_to = "89372361065@list.ru"

letter = """From: %mail_from%
To: %mail_to%
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
letter = letter.replace("%mail_from%", mail_from)
letter = letter.replace("%mail_to%", mail_to)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(email, password)
server.sendmail(email, mail_to, letter)
server.quit()