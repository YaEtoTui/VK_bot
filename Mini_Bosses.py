from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton

def battle_DestructiveTrojanHorse(self, text, user_id):
    if self.target == 'is_battle_mini-boss_DestructiveTrojanHorse':
        if text == 'Напасть' or text == 'Попытаться незаметно ускользнуть' or text == 'Начать бой сначала' or text == 'Продолжить':
            if text == 'Попытаться незаметно ускользнуть':
                self.send_message_not_buttons(user_id,
                                              'Упс, Но кажется, вам не удалось остаться незамеченным, так что убежать уже не представляется возможным ')

            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')

            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'На вид кажущаяся безобидной программой, Деструктивный троянский конь несет в себе немало вреда. '
                                              'Чтобы попасть в ваше устройство он использовал маскировку, но с недавнего времени он начал свою '
                                              'беспощадную атаку.')
            self.send_message_not_buttons(user_id, '1. Выполнить полную проверку системы и удалить вредоносное ПО')
            self.send_message_not_buttons(user_id,
                                          '2. Удалить корневую папку где находился вирус, подождать некоторое время, вдруг вирус сам испариться')
            self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse_choice', user_id,
                                                        keyboard, '3. Остановить программу через диспетчер задач')
    elif self.target == 'is_battle_mini-boss_DestructiveTrojanHorse_choice':
        if text == '1':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить путь')
            self.target = self.send_message_with_target('boss_1', user_id, keyboard,
                                                        'Поздравляем вы уничтожили своего первого противника, но впереди еще долгое путешествие, наберитесь сил и отправляйтесь дальше')
        elif text == '2':
            # переходим к проигрышному боссу
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'is_battle_mini-boss_DestructiveTrojanHorse'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Похоже, что удаление папки только разозлило деструктивного троянского коня. Разъярённый, он бросился на вас. Вы проиграли, но не отчаивайтесь и попробуйте ещё раз.')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse', user_id,
                                                            keyboard,
                                                            'Похоже, что удаление папки только разозлило деструктивного троянского коня. Разъярённый, он бросился на вас. Вы проиграли, но не отчаивайтесь и попробуйте ещё раз.')
        elif text == '3':
            # переходим к проигрышному боссу
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'is_battle_mini-boss_DestructiveTrojanHorse'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Вы остановили программу, но не самого вируса. Попробуйте ещё раз.')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse', user_id,
                                                            keyboard,
                                                            'Вы остановили программу, но не самого вируса. Попробуйте ещё раз.')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          'Подсказка: Если троянская программа проникла на Ваше устройство, то самый универсальный способ избавиться от нее и восстановить прежнюю функциональность системы это выполнить полную проверку системы с помощью эффективной программы, способной автоматически удалять вредоносное ПО.')
    return self

def battle_Rootkit(self, text, user_id):
    if self.target == 'mini-boss_Rootkit':
        if text == 'Опознать программу' or text == 'Начать бой сначала' or text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            keyboard.add_button('4')
            keyboard.add_button('5')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'Небольшой анализ позволил вам определить, что вы столкнулись с Руткитом. Используя эффект неожиданности, противник нанёс удар, но, благодаря молниеносной реакции, вам удалось увернуться, и удар прошёл мимо. ')
                self.send_message_not_buttons(user_id,
                                              'Похоже, что руткит серьёзно настроен устранить вас, поэтому избежать сражения не представляется возможным. Стоит попробовать ответить обидчику.')

            self.send_message_not_buttons(user_id, '1. Удалить все файлы руткита которые сразу заметны')
            self.send_message_not_buttons(user_id, '2. Позволить антивирусу разобраться')
            self.send_message_not_buttons(user_id,
                                          '3. Провести полный анализ системы и очистить все глубокие источники руткита')
            self.send_message_not_buttons(user_id, '4. Переустановить операционную систему')
            self.target = self.send_message_with_target('mini-boss_Rootkit_choice', user_id, keyboard,
                                                        '5. Сбросить настройки системы')
    elif self.target == 'mini-boss_Rootkit_choice':
        if text == '1':
            # переходим к проигрышному боссу
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Вирус проник намного глубже и удаление только заметных файлов не помогли окончательно избавиться от руткита ')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'Вирус проник намного глубже и удаление только заметных файлов не помогли окончательно избавиться от руткита')
        elif text == '2':
            if not self.isWin_boss_lossing:
                # переходим к проигрышному боссу
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Антивирус оказался не самым быстрым вашим другом, а следующий удар руткита всё же достиг задуманной цели и попал в вас')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'Антивирус оказался не самым быстрым вашим другом, а следующий удар руткита всё же достиг задуманной цели и попал в вас')
        elif text == '4':
            if not self.isWin_boss_lossing:
                # переходим к проигрышному боссу
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас')
        elif text == '5':
            if not self.isWin_boss_lossing:
                # переходим к проигрышному боссу
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Попытка была неплохой, но не самой действенной, ведь после сброса настроек вирус так и остался перед вами, да ещё и с очередным ударом, увернуться от которого уже не представляется возможным ')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'Попытка была неплохой, но не самой действенной, ведь после сброса настроек вирус так и остался перед вами, да ещё и с очередным ударом, увернуться от которого уже не представляется возможным ')
        elif text == '3':
            # Победа!!
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_KeyLogger', user_id, keyboard,
                                                        'Только руткит собрался ударить ещё раз, как начал распадаться на мелкие частички и через пару секунд совсем исчез')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка): Руткит обычно прячется глубоко в недрах операционной системы и специально написаны таким образом, чтобы избегать обнаружения антивирусом')
    return self

def battle_lossing_boss(self, text, user_id):
    if self.target == 'boss_lossing':
        if text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('Снова включить компьютер')
            keyboard.add_line()
            keyboard.add_button('Закончить игру')
            self.target = self.send_message_with_target('boss_lossing_choice', user_id, keyboard,
                                                        'Вы оказались снова у себя в комнате, а компьютер перед вами выключен.')
    elif self.target == 'boss_lossing_choice':
        if text == 'Снова включить компьютер' or text == 'Начать бой сначала':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            keyboard.add_button('4')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'Как только вы нажали кнопку включения, компьютер сразу затянул вас внутрь. Но ввести пароль для входа вам мешает ещё один вирус, Спуфер. Чтобы обратно вернуться в цифровой мир вам следует избавиться от него. Что предпримите?')
            self.send_message_not_buttons(user_id, '1. Буду использую двухфакторную аутентификацию')
            self.send_message_not_buttons(user_id, '2. Дам доступ к личной информации другим')
            self.send_message_not_buttons(user_id, '3. Буду использовать спам-фильтр ')
            self.target = self.send_message_with_target('boss_lossing_choice_2', user_id, keyboard,
                                                        '4. Везде буду использовать один и тот же пароль')
        elif text == 'Закончить игру':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('the_end', user_id, keyboard,
                                                        'Вы закончили игру! Нажмите, чтобы продолжить')
    elif self.target == 'boss_lossing_choice_2':
        if text == '1' or text == '3':
            self.isWin_boss_lossing = True
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target(self.target_return_to_mini_boss, user_id, keyboard,
                                                        'Прекрасно! Вы справились с шпионом на вашем компьютере и можете продолжить свой путь.')
        elif text == '2' or text == '4':
            keyboard = VkKeyboard()
            keyboard.add_button('Начать бой сначала')
            self.target = self.send_message_with_target('boss_lossing_choice', user_id, keyboard,
                                                        'Похоже, что ваши действия не возымели действия, стоит попробовать сделать что-то другое')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка): Никогда не следует давать свою личную информацию, использовать один пароль, отвечать на звонки незнакомым людям')
    return self

def battle_KeyLogger(self, text, user_id):
    if self.target == 'mini_boss_KeyLogger':
        if text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            self.send_message_not_buttons(user_id,
                                          'Дальнейший ваш путь прошёл без происшествий. Вы уже видите указатель на корневую папку, но тут ваш взгляд привлек к себе небольшой странный комок, состоящий из проводов.')
            self.send_message_not_buttons(user_id,
                                          'Подойдя чуть ближе, вы смогли разглядеть, что узел проводов подключён к самому компьютеру и перекачивает ваши данные. Скорее всего, это клавиатурный шпион. Как поступите?')
            self.send_message_not_buttons(user_id,
                                          '1. Пройду мимо, незачем отвлекаться от намеченной цели, сейчас есть дела поважнее')
            self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                        '2. Нельзя позволять вирусам так безнаказанно воровать информацию у меня под носом!')
    elif self.target == 'mini_boss_KeyLogger_choice':
        if text == '1':
            # убежали
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_Hijacker', user_id, keyboard, 'Вам удалось сбежать от клавиатурного шпиона')
        elif text == '2' or text == 'Начать бой сначала':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            keyboard.add_button('4')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id, 'Что предпримите?')
            self.send_message_not_buttons(user_id, '1. Установлю антишпионский продукт')
            self.send_message_not_buttons(user_id, '2. Буду всегда вводить пароли вручную')
            self.send_message_not_buttons(user_id,
                                          '3. Буду сохранять пароли и вводить их на любых сайтах, даже не очень защищённых')
            self.target = self.send_message_with_target('mini_boss_KeyLogger_choice_2', user_id, keyboard,
                                                        '4. Обновлю систему и программные продукты и в будущем буду делать так регулярно')
    elif self.target == 'mini_boss_KeyLogger_choice_2':
        if text == '1' or text == '4':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_Hijacker', user_id, keyboard,
                                                        'К огромному сожалению вируса, вам удалось перекрыть ему доступ к данным, так что делать ему здесь больше нечего и он просто быстро уполз ')
        elif text == '2':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_KeyLogger'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Данные действия только упростили вирусу задачу, стоит попробовать что-то другое')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Данные действия только упростили вирусу задачу, стоит попробовать что-то другое')
        elif text == '3':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_KeyLogger'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Кажется, что перекачка пошла ещё быстрее, давайте попытаемся ещё раз')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Кажется, что перекачка пошла ещё быстрее, давайте попытаемся ещё раз')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Клавиатурный шпион(KeyLogger)- это отслеживание нажатий каждой клавиши клавиатуры, поэтому ввод паролей на незащищенных сайтах и ввод его в ручную является грубой ошибкой при пользовании устройством)')
    return self

def battle_Hijacker(self, text, user_id):
    if self.target == 'mini_boss_Hijacker':
        if text == 'Продолжить' or text == 'Начать бой сначала':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            keyboard.add_button('4')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id, 'До вашей цели осталось всего лишь повернуть за угол. И вот вы уже воодушевлены и готовы к встрече с новыми '
                                                       'противниками, как вдруг что-то хватает вас за ногу и резко тянет назад. Вы падаете, и нечто утягивает вас в расщелину, '
                                                       'не замеченную вами ранее. Как оказалось, вы слишком рано переключились на мысли о своих дальнейших действиях и не '
                                                       'обратили внимание на осторожно ползущие за вами щупальца хиджакера. Ваша легкомысленность приводит к тому, что, '
                                                       'находясь в нескольких шагах от заветной папки, вы оказались затянуты очередным вирусом в недра компьютера, внешне '
                                                       'напоминающие чащу леса. Оглядев своё новое местоположение, чуть поодаль вы увидели иконку браузера, из чего вами был '
                                                       'сделан вывод, что вирус пришёл из Интернета.')
                self.send_message_not_buttons(user_id, 'Сам же монстр наконец предстал перед вами во всей красе, и вы снова оказались перед непростым выбором: каким же образом вступить с противником в бой')
            self.send_message_not_buttons(user_id, '1. Удалить браузер')
            self.send_message_not_buttons(user_id, '2. Удалить в браузере все ненужных и подозрительных инструментов и расширений')
            self.send_message_not_buttons(user_id, '3. Поменять основной браузер на другой')
            self.target = self.send_message_with_target('mini_boss_Hijacker_choice', user_id, keyboard,
                                                        '4. Сбросить настройки поисковой системы')
    elif self.target == 'mini_boss_Hijacker_choice':
        if text == '2':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_AdWare', user_id, keyboard,
                                                        'Поздравляем, удаление инструментов и расширений сработало, и враг оказался повержен!')
        elif text == '1':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_Hijacker'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Простое удаление не всегда решает проблему, а особенно, если эта проблема способна наносить такие удары, как те, что полетели в вас')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Простое удаление не всегда решает проблему, а особенно, если эта проблема способна наносить такие удары, как те, что полетели в вас')
        elif text == '3':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_Hijacker'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Похоже, что дело не в простой смене браузера, ведь монстр уже успел уложить вас на лопатки')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Похоже, что дело не в простой смене браузера, ведь монстр уже успел уложить вас на лопатки')
        elif text == '4':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_Hijacker'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Принятое вами решение не возымело успеха, а время было утрачено, и удар Хиджакера вам отразить не удалось')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Принятое вами решение не возымело успеха, а время было утрачено, и удар Хиджакера вам отразить не удалось ')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка: Хиджакер может изменить поисковую систему по умолчанию и домашнюю страницу, замедлить загрузку веб-страниц, установить несколько панелей инструментов без разрешения пользователя и создать несколько контекстных предупреждений для рекламы)')
    return self

def battle_AdWare(self, text, user_id):
    if self.target == 'mini_boss_AdWare':
        if text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('Бой!')
            self.send_message_with_target('mini_boss_AdWare_choice', user_id, keyboard, 'Заинтересовавшись замеченной ранее иконкой, вы подошли туда. Конечно же, с вашей сегодняшней удачей около браузера вы заметили Рекламную программу считывающую полную информацию о вас, не спросив у вас разрешения. Так не годится!')
    elif self.target == 'mini_boss_AdWare_choice':
        if text == 'Бой!' or text == 'Попробовать ещё раз':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')
            if text == 'Попробовать ещё раз':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id, 'Недолго думая, вы решили настоятельно уничтожить программу')
            self.send_message_not_buttons(user_id, '1. Удалить браузер')
            self.send_message_not_buttons(user_id, '2. Использовать панель управления для удаления вредоносного ПО')
            self.target = self.send_message_with_target('mini_boss_AdWare_choice_2', user_id, keyboard, '3. Сбросить все настройки браузера, обнулить операционную систему')

    elif self.target == 'mini_boss_AdWare_choice_2':
        if text == '2':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_Clicker', user_id, keyboard,
                                                        'Да! Вы решили совершенно верно, и уже через секунду вирус пропал, будто его никогда и не было')
        elif text == '1':
            keyboard = VkKeyboard()
            keyboard.add_button('Попробовать ещё раз')
            self.target = self.send_message_with_target('mini_boss_AdWare_choice', user_id, keyboard,
                                                            'Самый простой способ — не всегда самый верный')
        elif text == '3':
            keyboard = VkKeyboard()
            keyboard.add_button('Попробовать ещё раз')
            self.target = self.send_message_with_target('mini_boss_AdWare_choice', user_id, keyboard,
                                                            'Можно и компьютер сразу разбить, тогда проблем точно не будет')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          'Подсказка: Рекламная программа (AdWare, SpyWare) — программа для демонстрации рекламных окон, открытия рекламируемых сайтов. Помимо этого может следить за действиями пользователя (посещенные сайты, введенные строки для поиска) и работать совместно с другими вредоносными программами')
    return self

def battle_Clicker(self, text, user_id):
    if self.target == 'mini_boss_Clicker':
        if text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('Опознать врага')
            self.send_message_with_target('mini_boss_Clicker_recognize', user_id, keyboard, 'И так как рекламная программа была удалена, вы решили следовать дальше, но ваши поиски верного пути в очередной раз были прерваны появлением нового врага.')
    elif self.target == 'mini_boss_Clicker_recognize':
        if text == 'Опознать врага':
            keyboard = VkKeyboard()
            keyboard.add_button('Бой!')
            self.send_message_with_target('mini_boss_Clicker_choice', user_id, keyboard, 'Перед вами появляется программа Кликер, которая занимается рассылкой спама, содержащий потенциально опасные приложения. И похоже, что он не особо рад вашему присутствию')
    elif self.target == 'mini_boss_Clicker_choice':
        if text == 'Бой!' or text == 'Попробовать ещё раз':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')
            if text == 'Попробовать ещё раз':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            self.send_message_not_buttons(user_id, '1. Удалить весь спам собственноручно')
            self.send_message_not_buttons(user_id, '2. Установить утилиту против кликера')
            self.target = self.send_message_with_target('mini_boss_Clicker_choice_2', user_id, keyboard, '3. Сообщить всем своим контактам, что ваши сообщения спам')

    elif self.target == 'mini_boss_Clicker_choice_2':
        if text == '2':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('unknown_file', user_id, keyboard,
                                                        'Конечно, пусть за нас работают специальные программы, а мы не будем сильно останавливаться на этом и двинемся дальше')
        elif text == '1':
            keyboard = VkKeyboard()
            keyboard.add_button('Попробовать ещё раз')
            self.target = self.send_message_with_target('mini_boss_Clicker_choice', user_id, keyboard,
                                                            'К сожалению, у нас не так много времени, да и это не избавляет от корня проблемы, подумайте ещё ')
        elif text == '3':
            keyboard = VkKeyboard()
            keyboard.add_button('Попробовать ещё раз')
            self.target = self.send_message_with_target('mini_boss_Clicker_choice', user_id, keyboard,
                                                            'Ну тут мы можем засесть на неделю, так что не самый действенный вариант, может попробуем что-то другое?')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          'Подсказка: Кликер (Clicker) — программа, для накручивания счетчиков (посещения страниц, показа баннеров), увеличения популярности сайта в поисковиках, несанкционированно использует ресурсы компьютера, увеличивает трафик, тем самым приводят к нарушению работы ЭВМ или их сети.')
    return self

def unknown_file(self, text, user_id):
    if self.target == 'unknown_file':
        if text == 'Продолжить' or text == 'Начать бой сначала':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            keyboard.add_button('4')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'Оказывается, что в компьютерах путаются и теряются не только бабушки, так как вы сами уже битый час плутаете в лабиринте различных проводов, матриц и непонятных деталей и складывается ощущение, что бродите вы по кругу.')
                self.send_message_not_buttons(user_id,
                                              'И вот, когда вы в очередной раз заметили знакомый узел проводов, прямо из воздуха появилось всплывающее окно с сообщением от вашего друга:')
                self.send_message_not_buttons(user_id,
                                              '«Привет, {user}, вышла новая игра, и у меня есть доступ к бесплатной версии. Скачивай быстрее, иначе этот файл быстро почистят. Надо просто открыть файл, и загрузка пойдёт сама. Я вот уже несколько часов играю, это бомба!»'.format(user=self.get_name(user_id)))
                self.send_message_not_buttons(user_id,
                                              'К сообщению был прикреплён файл, а так как вы никогда не отказывались от халявных игр, то ваш первый порыв был просто запустить файл.')
                self.send_message_not_buttons(user_id,
                                              'Но уже в следующую секунду вы остановили себя и решили немного подумать. За последние пару часов вы столкнулись с таким количеством вредоносных программ, что подумали о том, что сразу же открывать незнакомый файл не стоит, а лучше')
            self.send_message_not_buttons(user_id, '1. Изменить расширение файла')
            self.send_message_not_buttons(user_id,
                                          '2. Отправить файл проверенному знакомому для проверки')
            self.send_message_not_buttons(user_id,
                                          '3. Считать файл в другом приложении для чтения ')
            self.target = self.send_message_with_target('unknown_file_choice', user_id, keyboard,
                                                        '4. Проверить файл на наличие вируса')
    elif self.target == 'unknown_file_choice':
        if text == '4':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_RAT', user_id, keyboard,
                                                        'Действительно, самый логичный выбор. Ну и теперь мы видим, что сообщение нам писал никакой не друг, а вирус «шутка», и открывающего точно не стоит. Так что двигаемся дальше.')
        elif text == '2':
            keyboard = VkKeyboard()
            keyboard.add_button('Начать бой сначала')
            self.target = self.send_message_with_target('unknown_file', user_id, keyboard,
                                                        'Мы что, хотим подставить знакомого?')
        elif text == '1':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'unknown_file'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Другое расширение файла никаким образом не гарантирует его безопасность. В эту ловушку то вы и попались, запустив файл')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('unknown_file', user_id, keyboard,
                                                            'Другое расширение файла никаким образом не гарантирует его безопасность. В эту ловушку то вы и попались, запустив файл')
        elif text == '3':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'unknown_file'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Слабая надежда на то, что другое приложение для чтения испугает вирус, что и произошло. +1 новый вирус на вашем компьютере')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('unknown_file', user_id, keyboard,
                                                            'Слабая надежда на то, что другое приложение для чтения испугает вирус, что и произошло. +1 новый вирус на вашем компьютере')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          'Подсказка: Шутка (Hoax, Joke) — программа, призванная испугать пользователя и спровоцировать его на действия, которые приведут к нанесению ущерба. Может маскироваться под полезную программу.')
    return self

def battle_RAT(self, text, user_id):
    if self.target == 'mini_boss_RAT':
        if text == 'Продолжить' or text == 'Начать бой сначала':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'Похоже, что мы всё-таки вышли на правильный путь, и буквально через 10 минут вы уже стоите у входа в корневую папку.')
                self.send_message_not_buttons(user_id,
                                              'Только зайдя внутрь, вы сразу встречаете двух зомби. Судя по всему, это Программы Удалённого Администрирования, и настроены они явно недружелюбно.')
                self.send_message_not_buttons(user_id,
                                              'Вы, может, и хотели разойтись мирно, но вирусы ваше желание не разделили, так что возникает необходимость атаковать. Что предпримите?')
            self.send_message_not_buttons(user_id, '1. Зайду на сайты, где требуется ввод логина и пароля')
            self.send_message_not_buttons(user_id,
                                          '2. Уберу удалённый доступ из процессов устройства')
            self.target = self.send_message_with_target('mini_boss_RAT_choice', user_id, keyboard,
                                                        '3. Запрещу подключения удалённого помощника к этому устройству')
    elif self.target == 'mini_boss_RAT_choice':
        if text == '3':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_Zombie', user_id, keyboard,
                                                        'Поздравляем! Запрет подключения, действительно, избавил вас от этих вредоносных программ.')
        elif text == '2':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_RAT'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Вирусы всё равно остались на вашем устройстве, так что это был неэффективный вариант решения проблемы ')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_RAT', user_id, keyboard,
                                                            'Вирусы всё равно остались на вашем устройстве, так что это был неэффективный вариант решения проблемы ')
        elif text == '1':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_RAT'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Такими действиями вы дали вирусам доступ к ещё большему количеству своих данных')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_RAT', user_id, keyboard,
                                                            'Такими действиями вы дали вирусам доступ к ещё большему количеству своих данных')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка: Удаленный доступ не может предоставляться без вашего разрешения)')
    return self

def battle_Zombie(self, text, user_id):
    if self.target == 'mini_boss_Zombie':
        if text == 'Продолжить' or text == 'Начать бой сначала':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_line()
            keyboard.add_button('3')
            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'Вы уже успели подумать, что всё закончено и вы справились со всеми трудностями и преодолели все препятствия, как вдруг, раздался громкий нечеловеческий рёв.')
                self.send_message_not_buttons(user_id,
                                              'Разворачиваетесь на звук и только сейчас замечаете большое чудище, чем-то напоминающее двух предыдущих. Но размерами он превышал их вместе взятых.')
                self.send_message_not_buttons(user_id,
                                              'Вы вспомнили о том, что cmd предупреждал вас о наличии боссов, и решили, что это именно он.')
                self.send_message_not_buttons(user_id,
                                              'Сейчас вы понимаете, что до победы остался один шаг, и перед вами встаёт последний выбор, который повлияет на то, избавитесь ли вы окончательно от всех вредоносных программ или нет.')
                self.send_message_not_buttons(user_id,
                                              'Как будете бороться с врагом?')
            self.send_message_not_buttons(user_id, '1. Полная переустановка системы ')
            self.send_message_not_buttons(user_id, '2. Полное сканирование устройства с помощью антивируса и удаления временных файлов')
            self.target = self.send_message_with_target('mini_boss_Zombie_choice', user_id, keyboard, '3. Считывание информации об утечке личных данных')
    elif self.target == 'mini_boss_Zombie_choice':
        if text == '2':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('the_good_end', user_id, keyboard,
                                                        'Поздравляем! Запрет подключения, действительно, избавил вас от этих вредоносных программ.')
        elif text == '1':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_Zombie'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Боюсь, это не возымело действия, а вот зомби, в свою очередь, нанёс вам очень сильный удар')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_Zombie', user_id, keyboard,
                                                            'Боюсь, это не возымело действия, а вот зомби, в свою очередь, нанёс вам очень сильный удар')
        elif text == '3':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_Zombie'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Вряд ли эта информация будет сейчас вам полезна. Но вот время, потраченное на считывание, позволило монстру наброситься на вас и в мгновение ока одолеть')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_Zombie', user_id, keyboard,
                                                            'Вряд ли эта информация будет сейчас вам полезна. Но вот время, потраченное на считывание, позволило монстру наброситься на вас и в мгновение ока одолеть')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка: найти вирус зомби не вооруженным глазом практически невозможно, но современные антивирусы способны избавиться от него)')
    return self