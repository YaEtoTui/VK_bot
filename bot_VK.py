import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.longpoll import VkLongPoll, VkEventType
from User import User
import os

token = 'vk1.a.2AHnn2z9Pgxy-nKeuPN6fgTyRuRHNk-w6LlQ6AwDdfV2ugW9Un6kVEm5DYdDWUa37xvCC0QZUSOJti-qFF-u6ZCqXGf62qUC9fmnxKZCk-CwRak2n2l1YiMFRZQYHEwQPevp2IZ1JpGidMJDOS7102lnTom8nS3XRJMNFvUubedPTLeR9CT2H93Hb3pJ6BiY'
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk_bot = vk_session.get_api()
dict_targets = {}
print('start_the_game')
while True:

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text
            user_id = event.user_id

            if user_id not in dict_targets.keys():
                dict_targets[user_id] = User(vk_bot)
                print('\nНовичок тут {}'.format(user_id))
            else:
                print('\nСтарый {}'.format(user_id))
            if dict_targets[user_id].target == 'start':
                # отправляем фотку(ниже 1 скрин)
                dict_targets[user_id].send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'fon_3.png')),
                                                 user_id=user_id)
                keyboard = VkKeyboard()
                keyboard.add_button('Начать путешествие')
                dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Начать_путешествие', user_id, keyboard, 'Приветствую вас {user}, это текстовая игра(квест), все действия выполняются '
                                                                                                                                       'с помощью кнопок под окном чата, а результаты приходят в виде сообщений и картинок. '
                                                                                                                                       'Исследуйте мир вашего компьютера, узнавайте что-то новое о вирусах и программах, способных навредить '
                                                                                                                                       'вашему устройству, получайте подсказки, уничтожайте врагов(вирусы) и сражайтесь с основными врагами-боссами '
                                                                                                                                       '(главными вирусами).'.format(user=dict_targets[user_id].get_name(user_id)))

            if dict_targets[user_id].target == 'Начать_путешествие' and text == 'Начать путешествие':
                # отправляем фотку(ниже 1 скрин)
                dict_targets[user_id].send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'fon_2.jpg')), user_id=user_id) # пример отправки фота
                # отправляем фотку(ниже 1 скрин)
                dict_targets[user_id].send_message_not_buttons(user_id, 'Вернувшись домой после тяжелого дня, вы замечаете, что на вашу электронную почту '
                                                                        'пришло письмо с незнакомого адреса. Заинтересованные, вы открываете его.')
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')

                dict_targets[user_id].send_message(user_id, keyboard, 'В тот же миг на ваш компьютер загружается вредоносная программа, которая находилась '
                                                                      'в письме и только и ждала того, чтобы вы его открыли. ')
                dict_targets[user_id].send_message_not_buttons(user_id, '(1) -Перезапущу компьютер, и всё будет хорошо')
                dict_targets[user_id].send_message_not_buttons(user_id, '(2) -Ой, а что же теперь делать?')
                dict_targets[user_id].send_message_not_buttons(user_id, '(3) -Да не может такого быть, приколы какие-то')
                dict_targets[user_id].target = 'start_1'
            elif dict_targets[user_id].target == 'start_1' and (text == '1' or text == '2' or text == '3'):
                if text == '1':
                    dict_targets[user_id].send_message_not_buttons(user_id, 'После перезапуска ничего не изменилось, и вирусы всё так же находятся в компьютере')
                elif text == '3':
                    dict_targets[user_id].send_message_not_buttons(user_id, 'К сожалению это не чья-то глупая шутка, и вирусы действительно заполонили ваш компьютер')
                keyboard = VkKeyboard()
                keyboard.add_button('Нажать «Enter»')
                dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Нажать «Enter»', user_id, keyboard, 'Вы не сразу заметили сообщение в '
                                                                                                                                   'командной строке, но сейчас обратили внимание. Там следующий текст: «Привет, {user}! У нас плохие времена, '
                                                                                                                                   'компьютеру и так требовалась чистка, а сейчас его захватило большое количество вирусов. Мы очень нуждаемся в тебе, поэтому я, '
                                                                                                                                   'твой cmd, обращаюсь к тебе за помощью, и если ты готов отправиться в недры своего компьютера и разобраться со всеми проблемами, '
                                                                                                                                   'то нажми Enter»'.format(user=dict_targets[user_id].get_name(user_id)))
            elif dict_targets[user_id].target == 'Нажать «Enter»' and text == 'Нажать «Enter»':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать исследование устройства')
                dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Начать исследование устройства', user_id, keyboard, 'Вы сами не заметили как, но уже через пару секунд оказались внутри вашего компьютера. Оглядевшись вы поняли, что вокруг запутанный лабиринт из различных папок, плат и сети проводов. Для начала следует изучить окрестности получше')
            elif dict_targets[user_id].target == 'Начать исследование устройства' and text == 'Начать исследование устройства':
                keyboard = VkKeyboard()
                keyboard.add_button('Опознать незнакомца')
                dict_targets[user_id].send_message_not_buttons(user_id, 'После 10 минут плутания вы обнаружили достаточно широкую тропинку, по которой и приняли решение идти')
                dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('mini-boss_1', user_id, keyboard, 'Но пройдя всего пару шагов и завернув за угол, вы в первый раз в этом мире встречаете живое существо. К счастью пока оно вас не видит')
            elif text == 'Общая информация':
                dict_targets[user_id].send_message_not_buttons(user_id, dict_targets[user_id].text_total_information)

            #1 мини босс - Троянский конь
            elif dict_targets[user_id].target == 'mini-boss_1' and text == 'Опознать незнакомца':
                keyboard = VkKeyboard()
                keyboard.add_button('Напасть')
                keyboard.add_line()
                keyboard.add_button('Попытаться незаметно ускользнуть')
                dict_targets[user_id].isBattle_DestructiveTrojanHorse = True
                dict_targets[user_id].target = dict_targets[user_id].send_message_with_target(
                    'is_battle_mini-boss_DestructiveTrojanHorse', user_id, keyboard,
                    'Вы явно не самый везучий, ведь путь вам преградил не кто иной, как деструктивный троянский конь. '
                    'В школе на занятиях по информатике вам рассказывали о самых распространённых компьютерных вирусах, поэтому ты легко опознал в существе врага')
            elif dict_targets[user_id].isBattle_DestructiveTrojanHorse: # здесь происходит битва с Деструктивный троянский конь
                dict_targets[user_id].battle_DestructiveTrojanHorse(text, user_id)

            #1 босс - Главный троянский вирус
            elif dict_targets[user_id].isBattle_boss_MajorTrojanVirus: #здесь происходит битва с БОСС - Главный троянский вирус
                dict_targets[user_id].battle_boss_MajorTrojanVirus(text, user_id)

            # встреча с человеком(обучение)
            elif dict_targets[user_id].is_meeting_with_a_person:
                dict_targets[user_id].meeting_with_a_person(user_id, text)

            #2 босс - Руткит
            elif dict_targets[user_id].isBattle_Rootkit:
                dict_targets[user_id].battle_Rootkit(user_id=user_id, text=text)

            # проигрышный босс Спуфер
            elif dict_targets[user_id].isBattle_boss_lossing:
                dict_targets[user_id].battle_lossing_boss(user_id=user_id, text=text)

            #3 мини-босс - Клавиатурный шпион
            elif dict_targets[user_id].isBattle_KeyLogger:
                dict_targets[user_id].battle_KeyLogger(user_id=user_id, text=text)

            #заканчивает игру
            elif dict_targets[user_id].target == 'the_end':
                # заканчиваем игру и начинаем заново
                dict_targets[user_id] = User(vk_bot)
                dict_targets[user_id].target = 'start'
                keyboard = VkKeyboard()
                keyboard.add_button('Начать заново')
                dict_targets[user_id].send_message(user_id, keyboard, 'Напишите что-нибудь, чтобы начать заново игру!')

            print('{}'.format(dict_targets[user_id].target))
            print('Весь список {}'.format(dict_targets[user_id]))