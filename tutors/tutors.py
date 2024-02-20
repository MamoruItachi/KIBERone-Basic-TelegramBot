from bot_token import *

def send_tutors(msg_id):
  bot.send_photo(msg_id, open('tutors/images/img1.jpg', 'rb'), 'Тьютор проводит занятия на следующих локациях:\n\nВасилия Гольцова 10')
  bot.send_photo(msg_id, open('tutors/images/img2.jpg', 'rb'), 'Тьютор проводит занятия на следующих локациях:\n\nРеспублики 160\nВасилия Гольцова 10\nСолнечный проезд 24, Школа 94К1')
  bot.send_photo(msg_id, open('tutors/images/img3.jpg', 'rb'), 'Тьютор проводит занятия на следующих локациях:\n\nВасилия Гольцова 10\nТихий проезд 1, Школа 94К2')