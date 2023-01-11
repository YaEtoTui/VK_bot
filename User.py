import os

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.utils import get_random_id

import Mini_Bosses


class User():

    __text_information_boss_MajorTrojanVirus = 'Троянские вирусы — Trojan\n' \
                                              'Троянская программа маскируется в других безвредных программах. ' \
                                              'И до того момента как пользователь не запустит эту самую безвредную программу, ' \
                                              'троян не несет никакой опасности и обнаружить его нелегко. Троянская программа может ' \
                                              'нанести различный ущерб для компьютера. В основном трояны используются для кражи, изменения или ' \
                                              'удаления личных данных пользователя. Отличительной особенностью вируса-трояна является то, что он не ' \
                                              'может самостоятельно размножаться.\n\n'

    __text_information_boss_Adware = 'Рекламные вирусы — Adware\n' \
                                   'Программы-рекламы, без ведома пользователей встраиваются в различное программное ' \
                                   'обеспечение с целью демонстрации рекламных объявлений. Как правило, программы-рекламы встроены ' \
                                   'в программное обеспечение, распространяющееся бесплатно. Реклама располагается в рабочем интерфейсе. ' \
                                   'Данные программы также собирают и переправляют своему разработчику персональную информацию о пользователе.\n\n'

    __text_information_boss_Zombie = 'Зомби — Zombie\n' \
                                     'Зомби позволяют злоумышленнику управлять компьютером пользователя. ' \
                                     'Компьютеры – зомби могут быть объединены в сеть  и использоваться для массовой атаки на сайты или рассылки спама. ' \
                                     'Пользователь может даже не догадываться, что его компьютер зомбирован и используется злоумышленником.\n\n'

    __text_information_boss_Rootkit = 'Вирус-маскировщик — Rootkit\n' \
                                      'Маскировщики используются для сокрытия вредоносной активности. Они маскируют вредоносные программы, ' \
                                      'чтобы избежать их обнаружения антивирусными программами. Rootkit’ы также могут модифицировать операционную систему на ' \
                                      'компьютере и заменять основные ее функции, чтобы скрыть свое собственное присутствие и действия, которые предпринимает злоумышленник' \
                                      ' на зараженном компьютере.\n\n'

    def __init__(self, vk_bot, target='start', isWin_boss_lossing=False, isWin_boss_MajorTrojanVirus=False, target_return_to_mini_boss=''):
        self.vk_bot = vk_bot

        self.text_total_information = ''
        if (isWin_boss_MajorTrojanVirus):
            self.text_total_information += self.__text_information_boss_MajorTrojanVirus

        # боссы
        self.isWin_boss_MajorTrojanVirus = isWin_boss_MajorTrojanVirus  # Главный троянский вирус
        self.isWin_boss_lossing = isWin_boss_lossing # Проигрышный босс

        self.isWin_boss_Adware = False  # Рекламные вирусы
        self.isWin_boss_Zombie = False # Зомби
        self.isWin_boss_Rootkit = False  # Маскировщик

        self.target = target
        self.target_return_to_mini_boss = target_return_to_mini_boss # возвращает к прошлому мини-боссу при победе Проигрышного босса

    def get_name(self, user_id):
        id = user_id
        user_get = self.vk_bot.users.get(user_ids=(id))
        user_get = user_get[0]
        return user_get['first_name']  # Имя пользователя

    def send_photo(self, photo_1, user_id):
        global attachment
        upload = vk_api.VkUpload(self.vk_bot)
        photo = upload.photo_messages(photo_1)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        self.vk_bot.messages.send(user_id=user_id, random_id=get_random_id(), attachment=attachment)

    def send_message_with_target(self, target, user_id, keyboard, message):
        if self.isWin_boss_MajorTrojanVirus or self.isWin_boss_Adware:  # дальше тут дописываем боссов
            keyboard.add_line()
            keyboard.add_button('Общая информация')
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=message,
            keyboard=keyboard.get_keyboard()
        )
        return target

    def send_message(self, user_id, keyboard, message):
        if self.isWin_boss_MajorTrojanVirus or self.isWin_boss_Adware:  # дальше тут дописываем боссов
            keyboard.add_line()
            keyboard.add_button('Общая информация')
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id = get_random_id(),
            message = message,
            keyboard = keyboard.get_keyboard()
        )

    def send_message_not_buttons(self, user_id, message):
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=message
        )

    def add_button_start(self, user_id, keyboard):
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard()
        )

    def battle_DestructiveTrojanHorse(self, text, user_id):
        Mini_Bosses.battle_DestructiveTrojanHorse(self, text, user_id)

    def battle_boss_MajorTrojanVirus(self, text, user_id):
        if self.target == 'boss_1':
            if text == 'Продолжить путь':
                keyboard = VkKeyboard()
                keyboard.add_button('Опознать врага')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus', user_id, keyboard, 'Вы не успели отдышаться, как на вашем пути появилась новая неизвестная программа.')
        elif self.target == 'is_battle_boss_MajorTrojanVirus':
            if text == 'Опознать врага' or text == 'Начать бой сначала':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    try:
                        # отправляем фотку(ниже 1 скрин)
                        self.send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'конь_2_босс.png')),
                                        user_id=user_id)
                    except Exception as exc:
                        print('Картинка не прогрузилась!')
                    finally:
                        self.send_message_not_buttons(user_id, 'Программа кажется идентичной предыдущей, но стоит вам приглядеться, как вы понимаете, '
                                                         'что этот соперник гораздо больше, из это неудивительно, ведь перед вами Главный троянский вирус. '
                                                         'Он наносит первый удар настолько неожиданно, что вы не успели среагировать. К счастью нанести вам большой '
                                                         'урон у врага не получилось, и уже вы предпринимаете попытку атаковать. Так как вы уже встречались с трояном '
                                                         'вы решили попробовать сделать то же самое, "выполнить полную проверку системы и удалить вредоносное ПО", '
                                                         'но босс не так прост, чтобы убрать его с устройства нужно больше усилий.')
                self.send_message_not_buttons(user_id, '1. Попытаться проникнуть внутрь коня изнутри его уничтожить')
                self.send_message_not_buttons(user_id, '2. Отключить питание устройства и запустить его снова')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus_choice', user_id, keyboard, '3. Установить утилиту для удаления троянских коней')
        elif self.target == 'is_battle_boss_MajorTrojanVirus_choice':
            if text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Запуск антивируса')
                self.target = self.send_message_with_target('Запуск антивируса для удаления остатков коней', user_id, keyboard, 'Ого! Ваши действия нанесли сильный вред противнику, троян почти уничтожен, но остался последний удар, чтобы его добить.')
                self.send_message_not_buttons(user_id, 'Запуск антивируса для удаления остатков коней')
            elif text == '1':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus', user_id, keyboard, 'Вы оказались очень ловким и смогли проникнуть внутрь, '
                                                     'но там вам не удалось нанести врагу значительный урон, несмотря на все ваши удары')
            elif text == '2':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus', user_id, keyboard,
                                  'Похоже это было бесполезным действием, так как после того как вы перезапустили компьютер, монстр остался на том же месте')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, '(Подсказка: Если троянская программа проникла на Ваше устройство, '
                                                       'то самый универсальный способ избавиться от нее и восстановить прежнюю функциональность системы '
                                                       'это выполнить полную проверку системы с помощью эффективной программы, способной автоматически удалять '
                                                       'вредоносное ПО.)')
        elif self.target == 'Запуск антивируса для удаления остатков коней' and text == 'Запуск антивируса':
            self.isWin_boss_MajorTrojanVirus = True
            keyboard = VkKeyboard()
            self.text_total_information += self.__text_information_boss_MajorTrojanVirus
            keyboard.add_button('Отправиться дальше')
            self.target = self.send_message_with_target('meeting_with_a_person', user_id, keyboard, 'Поздравляем вы полностью избавились от троянских вирусов, '
                                                   'теперь вам доступна полная информация о них(теперь вы можете увидеть '
                                                   'всю информацию о вирусе, нажавав кнопку "Общая информация")')

    def meeting_with_a_person(self, user_id, text):
        if self.target == 'meeting_with_a_person' and text == 'Отправиться дальше':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')
            self.target = self.send_message_with_target('Выбрать_от_1_до_3', user_id, keyboard, 'Немного передохнув, вы двинулись дальше, но '
                                                                                                'пройдя совсем немного заметили, как на встречу вам бежит ещё '
                                                                                                'один совершенно незнакомый вам человечек')
            self.send_message_not_buttons(user_id, '(1) Остановиться и подождать ')
            self.send_message_not_buttons(user_id, '(2) Зачем нам ещё один бой? Попробовать убежать ')
            self.send_message_not_buttons(user_id, '(3) Этот мир не очень дружелюбный, не помешает подготовиться к битве')

        elif self.target == 'Выбрать_от_1_до_3' and (text == '1' or text == '2' or text == '3'):
            if text == '1':
                self.send_message_not_buttons(user_id, 'Через пару секунд существо нагнало вас, запыхавшись он начал говорить:')
            elif text == '2':
                self.send_message_not_buttons(user_id, 'Вы развернулись и даже успели сделать несколько шагов, после чего услышали как '
                                                       'вас окликнули по имени и остановились. Вам стало любопытно, откуда этому лицу известно ваше имя. '
                                                       'Решив разобраться в этой ситуации, вы развернулись и настороженно стали ждать, когда человечек подойдёт ближе.\n'
                                                       'Долго ждать не пришлось, и уже через несколько секунд он был около вас. Остановившись, он оглядел вас и начал говорить:')
            elif text == '3':
                self.send_message_not_buttons(user_id, 'Морально настроившись на ещё один бой, вы встали в оборонительную позицию. Приблизившись к вам на расстояние нескольких шагов, '
                                                       'человечек остановился, оглядел вас и, примирительно подняв руки, сказал: ')
            try:
                # отправляем фотку(ниже 1 скрин)
                self.send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'cmd.png')), user_id=user_id)
            except Exception as exc:
                print('Картинка не прогрузилась!')
            finally:
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')
                self.send_message(user_id, keyboard, '«{user}, я очень рад, что ты принял моё приглашение и пришёл помочь освободить '
                                                 'наш мир от непрошенных гостей. Судя по твоему виду, ты уже встретил кого-то из наших недоброжелателей. '
                                                 'Хорошо, что ты не пострадал! Ой, я совсем забыл представиться, меня зовут Cmd, надеюсь, мы быстро подружимся '
                                                 'и вместе одолеем всех вирусов.»'.format(user=self.get_name(user_id)))
                self.send_message_not_buttons(user_id, '(1) «А что здесь произошло, почему в моём компьютере одновременно оказалось столько вредоносных программ?» ')
                self.send_message_not_buttons(user_id, '(2) «И как нам справиться со всеми врагами?»')
                self.send_message_not_buttons(user_id, '(3) «Рад знакомству, какие будут предложения, что делать дальше?»')
                self.target = 'Дальнейшее развитие'
        elif self.target == 'Дальнейшее развитие' and (text == '1' or text == '2' or text == '3'):
            keyboard = VkKeyboard()
            keyboard.add_button('Что для этого нужно?')
            self.target = self.send_message_with_target('Что для этого нужно?', user_id, keyboard, '«Ты сидишь но многих незащищённых сайтах, скачиваешь с них различные файлы, а вместе с ними и вирусы разных видов. С каждым днём они становятся всё хитрее и изворотливее, иногда могут долгое время оставаться незаметными, усыпляя бдительность систем ПО и поджидая удобного случая напасть. Даже современные антивирусы не всегда успевают за их эволюцией. Таким образом на твоём компьютере появлялось всё больше и больше вредоносных программ, что привело к тому, что сейчас необходимо провести экстренную зачистку.»')
        elif self.target == 'Что для этого нужно?' and text == 'Что для этого нужно?':
            keyboard = VkKeyboard()
            keyboard.add_button('И где находится эта папка?')
            self.target = self.send_message_with_target('И где находится эта папка?', user_id, keyboard, '«В первую очередь тебе надо пробраться в корневую папку и найти там архив с фалами паролей. Их нужно изменить, чтобы вирусы больше не могли иметь доступ к любым файлам и операциям. Сейчас корневая папка находится под контролем зомби, поэтому будь готов к сражению. Также тебе стоит знать, что в нашем мире вирусы разделились на боссов и их помощников. Так что для того, чтобы разобраться со всеми вредителями, надо уничтожить их главаря.»')
        elif self.target == 'И где находится эта папка?' and text == 'И где находится эта папка?':
            self.send_message_not_buttons(user_id, '«Чтобы добраться до неё тебе следует идти по этой дороге через несколько других папок, если будешь быстро идти, то потребуется совсем немного времени, но будь осторожен, нельзя предсказать, что тебя ждёт на этом пути. У меня самого ещё есть дела, поэтому не могу пойти с тобой, но я верю, что ты со всем справишься! Встретимся позже.»')
            self.send_message_not_buttons(user_id, 'После этих слов ваш новый приятель сделал молниеносный рывок и скрылся за ближайшим поворотом.')
            self.send_message_not_buttons(user_id, 'Вы же постояли некоторое время на месте, обдумывая всё только что услышанное, и только после пары минут активной мозговой деятельности пришли к выводу, что нужно попытаться освободить свой компьютер от этих нежелательных гостей, и двинулись в указанном направлении.')
            keyboard = VkKeyboard()
            keyboard.add_button('Опознать программу')
            self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'Поначалу всё было спокойно, неподвижную тишину нарушал только звук ваших шагов. Направление вашего движения подсказывали указатели, расставленные на какой развилке. Вы уже даже успели подумать, что всё не так страшно, как показалось изначально, как вдруг прямо перед вами материализовалась какая-то программа.')

    #Руткит
    def battle_Rootkit(self, text, user_id):
        Mini_Bosses.battle_Rootkit(self, text, user_id)

    #проигрышный босс (Спуфер), ставим после проигрыша у мини-боссов
    def battle_lossing_boss(self, text, user_id):
        Mini_Bosses.battle_lossing_boss(self, text, user_id)

    def battle_KeyLogger(self, text, user_id):
        Mini_Bosses.battle_KeyLogger(self, text, user_id)

    def battle_Hijacker(self, text, user_id):
        Mini_Bosses.battle_Hijacker(self, text, user_id)

    def battle_AdWare(self, text, user_id):
        Mini_Bosses.battle_AdWare(self, text, user_id)

    def battle_Clicker(self, text, user_id):
        Mini_Bosses.battle_Clicker(self, text, user_id)

    def unknown_file(self, text, user_id):
        Mini_Bosses.unknown_file(self, text, user_id)

    def battle_RAT(self, text, user_id):
        Mini_Bosses.battle_RAT(self, text, user_id)

    def battle_Zombie(self, text, user_id):
        Mini_Bosses.battle_Zombie(self, text, user_id)