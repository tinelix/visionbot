import importlib.util
spec = importlib.util.spec_from_file_location("botconfig", "/home/runner/visionbot/discord_bot/discord_botconfig.py")
botconfig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(botconfig)

def get():
    name = botconfig.botconfig['name']
    prefix = botconfig.botconfig['prefix'] 
    return [
            'Russian',
            [
                [
                    ' - простой и немного расширяемый. Developed by Tinelix. **Префикс:** `{0}`\n\n**А Вы знаете, что...** {1}',
                  [ # 1.0.1
                    'Основное', # 1.0.1.0
                    '`help`, `state`, `profile`, `tnews`, `feedback`, `info`' # 1.0.1.1
                  ],
                  [ # 1.0.2
                    'Развлечения', # 1.0.2.0
                    '`photo`, `8ball` (`crystball`)'
                  ],
                  [
                    'Служебное', # 1.0.3.0
                    '`settings`, `post`' # 1.0.3.1
                  ],
                  [ # 1.0.4
                    'Разное', # 1.0.4.0
                    '`calc`, `weather`, `codec`, `poll`, `rep`' # 1.0.4.1
                  ],
                  '**Префикс:** ' # 1.0.5
                ],
                [
                    'Состояние бота',
                    'Задержка',
                    ' мс',
                    'Под управлением',
                    'Центральный процессор',
                    'Версия Python',
                    'Дата сборки Python',
                    'Версии пакетов',
                    'Аналитика',
                    'Автор бота',
                    'Ссылки',
                ],
                [
                    'Настройки',
                    'Для доступа к нужной настройке нажмите на одну из соотвествующих реакций.\n\n**🗣️ Язык бота (Bot language)**\n**🕓 Часовой пояс**\n**🗨️ Счетчик сообщений**\n**🌈 Свой цвет вложенных сообщений**',
                    [
                        'Язык бота (Bot language)',
                        'Для изменения значения введите команды, которые указаны внизу.\n\n**🇷🇺 Русский**\n```{0}set -l ru-RU```\n\n**🇺🇸 English**\n```{0}set -l en-US```'.format(prefix)
                    ],
                    [
                        'Часовой пояс',
                        'Текущее время',
                        'Допустимые значения',
                        'От -120 до 140 (UTC)',
                        'Пример',
                        '```{0}set -tz -80\n{0}set -tz 30\n{0}set -tz 55```'.format(prefix),
                        '-80 для UTC-8:00, 30 для UTC+3:00 (Москва), 55 для UTC+5:30.'.format(prefix)
                    ],
                    [
                        'Ошибка',
                        'Это значение должно быть исключительно числовым.',
                        'Вы изменили часовой пояс на UTC'
                    ],
                    [ # 1.2.5
                        'Счетчик сообщений', # 1.2.5.0
                        'Вы настраиваете бота Vision на уровне Вашего сервера или лично для себя? Для выбора ответа нажмите одну из соответствующих реакций.\n||_да, мы используем БД SQLite_||\n\n🏠 - на уровне сервера\n👤 - для себя', # 1.2.5.1
                        'Счетчик сообщений включен.', # 1.2.5.2
                        'Счетчик сообщений выключен.', # 1.2.5.3
                        'Извините, но у Вас нет прав на управление сервером. Пожалуйста, воспользуйтесь личными настройками.', # 1.2.5.4
                        'Ошибка' # 1.2.5.5
                    ],
                    [ # 1.2.6
                        'Счетчик сообщений', # 1.2.6.0
                        'Всего подсчитанных сообщений с начала ', # 1.2.6.1
                        ' сообщений', # 1.2.6.2
                        'Допустимые значения', # 1.2.6.3
                        '`on` - включить, `off` - отключить', # 1.2.6.4
                        'Пример', # 1.2.6.5
                        '```{0}set -mc on```'.format(prefix) # 1.2.6.6
                    ],
                    [ # 1.2.7
                      'Свой цвет вложенных сообщений (🏠)', # 1.2.7.0
                      'Допустимые значения', # 1.2.7.1
                      '`red`, `orange`, `yellow`, `green`, `skyblue`, `blue`, `violet`, `rose`', # 1.2.7.2
                      'Пример', # 1.2.7.3
                      '```{0}set -ec skyblue```'.format(prefix), # 1.2.7.4
                      'Свой цвет вложенных сообщений (🏠)', # 1.2.7.5
                      'Изменения сохранены.' # 1.2.7.6
                    ]                    
            ],
            [ # 1.3
                'О пользователе ', # 1.3.0
                'Псевдоним', # 1.3.1
                'Дата прихода в сервер', # 1.3.2
                'Дата регистрации', # 1.3.3
                'Всего сообщений с ', # 1.3.4
                ' сообщ.', # 1.3.5
                '_У этого пользователя счетчик сообщений выключен_', # 1.3.6
                '[БОТ] ', # 1.3.7
                'Аватар пользователя ', # 1.3.8
                '', # 1.3.9
                'Статус', # 1.3.10
                [ # 1.3.11
                    '<:online_emoji:786943382651142145> Онлайн', # 1.3.11.0
                    '<:idle_emoji:786943383721213952> Отошел', # 1.3.11.1
                    '<:dnd_emoji:786943382316253204> Занят', # 1.3.11.2
                    '<:offline_emoji:786943380085145651> Оффлайн' # 1.3.11.3
                ],
                'Роли ', # 1.3.12
                'Дата отправки последнего сообщ.', # 1.3.13
                'Репутация'
            ],
            [
                'О сервере ',
                '',
                'Описание',
                'Владелец',
                'Дата создания',
                'Бустов',
                'Каналов',
                'Участников',
                'Фильтрация контента 18+',
                'Канал для правил',
                'Канал бездействия',
                'Защита 2FA',
                'Уровень верификации',
                [
                    'Без ограничений',
                    'Простой',
                    'Средний',
                    'Сложный',
                    'Строгий'
                ],
                [   
                    'Вкл.',
                    'Выкл.',
                    '_Не включено "Сообщество"_',
                    '_Нет канала бездействия_'
                ],
                [
                    '💎 ',
                    ' | 🧙 ',
                    '💬 ',
                    ' | 🔉 ',
                    '👤 ',
                    ' | 🔌 '
                ],
                'Сообщений',
                '_У этого сервера счетчик сообщений выключен_'
            ],
            [
                'Профили',
                '`{0}profile -u [ID]` - узнать информацию о пользователе.\n`{0}profile -g` - узнать информацию о сервере'.format(prefix),
                '**Свои параметры** (изменить можно в `{0}settings`)**:**\n'.format(prefix),
                'вкл. счетчик сообщений',
                'часовой пояс UTC',
                '',
                '🇷🇺',
                'выкл. счетчик сообщений',
            ],
            [ # 1.6
                'Новости Тинеликса', # 1.6.0
                'Для выбора заголовка нажмите одну из соответствующих реакций.\n\n' # 1.6.1
            ],
            [ # 1.7
                ' ', # 1.7.0
                ' ', # 1.7.1
                ' ', # 1.7.2
                ' ', # 1.7.3
                ' ', # 1.7.4
                ' ', # 1.7.5
                ' ', # 1.7.6
                ' ', # 1.7.7
                ' ', # 1.7.8
                ' ', # 1.7.9
                ' ', # 1.7.10
                ' ', # 1.7.11
                ' ', # 1.7.12
                ' ', # 1.7.13
                ' ' # 1.7.14      
            ],
            [ # 1.8
                'Случайные фото', # 1.8.0
                'Автор', # 1.8.1
                'Лайков', # 1.8.2
                'Пока хватит!', # 1.8.3
                'Посмотреть еще фотки можно будет только через час, так как в API Unsplash действует лимит - не больше 50 запросов за час. Приносим извинения за доставленные неудобства.', # 1.8.4
                '`{0}photo -u` - просмотр фотографий из Unsplash.\n`{0}photo -r` - просмотр фотографий из сабреддитов.'.format(prefix) # 1.8.5
            ],
            [ # 1.9
                'Калькулятор', # 1.9.0
                'Листинг', # 1.9.1
                'Результат', # 1.9.2
                'Обнаружено исключение!\n', # 1.9.3
                'Вы забыли ввести выражение.\n```{0}calc 4 * 58```'.format(prefix), # 1.9.4
                'В этой версии Калькулятора можно совершать только простые арифметические выражения.', # 1.9.5
                'Доступные знаки', # 1.9.7
                '`+` - прибавить\n`-` - убавить\n`*` - умножить\n`/` - разделить' # 1.9.8
            ],
            [ # 1.10
                'Обратная связь', # 1.10.0
                'Баг-трекер {0}'.format(name), # 1.10.1
                'Автор бота ответит на Ваш вопрос в ближайшее время, подождите.', # 1.10.2
                'Вы забыли указать аргументы. Кстати, можно скриншоты отправлять, так проще разобраться.\n\n```{0}feedback Привет!```'.format(prefix), # 1.10.3
                'Вам ответили: ' # 1.10.4
            ],
            [ # 1.11
                'Погода | ', # 1.11.0
                'Температура ', # 1.11.1
                'мин. ', # 1.11.2
                '\nсрд. ', # 1.11.3
                '\nмакс. ', # 1.11.4
                'Скорость ветра', # 1.11.5
                ' м/с', # 1.11.6
                'Влажность', # 1.11.7
                'Прогноз на ближайшие 12 часов', # 1.11.8
                'Используется OpenWeatherMap API', # 1.11.9
                'ru', # 1.11.10
                'Ошибка', # 1.11.11
                'Не удается найти город или населенный пункт по запросу.\n\nМожет, напишете по-другому?', # 1.11.12
                'Код ошибки', # 1.11.13
                'Вы забыли дописать имя города или населенного пункта.' # 1.11.14
            ],
            [ # 1.12
                'Магический шар', # 1.12.0
                'Вопрос', # 1.12.1
                'Он говорит', # 1.12.2
                'Все совпадения случайны', # 1.12.3
                'Ошибка', # 1.12.4
                'Сначала задайте ему вопрос.' # 1.12.5
            ],
            [ # 1.13
                'Ошибка', # 1.13.0
                'Вы должны обязательно включить функции сообщества на Вашем Discord-сервере для публикации новостей.', # 1.13.1
                'Вы забыли указать сообщение для публикации.', # 1.13.2
                'Команда недоступна, так как у Вас недостаточно прав на управление сообщениями.',
                'Сначала переключитесь на новостной канал.'
            ],
            [ # 1.14
              'Кодек', # 1.14.0 
              'Вам предстоит выбрать тип данных для декодирования в обычную строку. Выбор типа осуществляется нажатием на соответствующую реакцию.', # 1.14.1
              'Вам предстоит выбрать тип данных для кодирования из обычной строки. Выбор типа осуществляется нажатием на соответствующую реакцию.', # 1.14.2
              '1️⃣ Base64\n2️⃣ Base32\n3️⃣ Base16\n4️⃣ Двоичный код', # 1.14.3
              'Результат',
              '`{0}codec -d` - расшифровка текста\n`{0}codec -e` - зашифровка текста'.format(prefix),
              'Расшифровать не получилось. Неверно выбран тип данных.',
              'Просмотр в Embed-сообщении невозможен.',
              'Вы забыли ввести текст.\n\n```{0}codec -e Привет!\n{0}codec -d SGVsbG8h```'.format(prefix)
            ],
            [ # 1.15
              'О боте', # 1.15.0
              '{0} - простой и расширяемый бот от Tinelix. Этот бот является заменой бота Highflash, который был достаточно сырым для запуска на мониторинг ботов. Но не беспокойтесь, в боте Vision есть (пускай, неидеальная) интеграция с БД SQlite3, когда в Highflash был только примитивный JSON. Бот написан с нуля и учитывал ошибки, допущенные при разработке бота Highflash. Теперь он развивается не только благодаря Вам, но и авторе (Tinelix\'у) своей продуктивностью.\n\nОн может узнавать погоду в Вашем городе, шифровать или расшифровать тексты, показывать случайные и довольно интересные фотографии с Reddit и Unsplash, поиграть в \"Шар судьбы\" и т. д.\n\n_Бот Vision и его открытый исходный код распространяются с условиями лицензии Affero GPL версии 3 для веб-приложений_'.format(name), # 1.15.1
              'Написан на', # 1.15.2
              'Автор', # 1.15.3
              'Мониторинги ботов', # 1.15.4
              '[bots.server-discord.com](https://bots.server-discord.com/785383439196487720)\n[BotiCord](https://boticord.top/bot/785383439196487720)\n[Bots for Discord](https://botsfordiscord.com/bot/785383439196487720)', # 1.15.5
              'Ссылки', # 1.15.5
              '[Пригласить бота](https://discord.com/api/oauth2/authorize?client_id=785383439196487720&permissions=8&scope=bot)\n[GitHub](https://github.com/tinelix/visionbot)\n[ВКонтакте](https://vk.com/tinelix)\n[YouTube](https://www.youtube.com/channel/UCSPjn_Y0pLdPy6Ncb9NAdww)\n[Сервер в Discord](https://discord.gg/fYRjHvXntj)' # 1.15.6
            ],
            [ # 1.16
              'Голосование', # 1.16.0
              'Вести это голосование могут только администраторы сервера.', # 1.16.1
              'Время пошло! Время окончания: {0}', # 1.16.2
              'Голосование закончено.', # 1.16.3
              'Вы забыли указать требуемые аргументы к этой команде или разделить аргументы знаками `[` и `],`. Следуйте примером внизу. И да, между скобками запятая без каких-либо пробелов обязательна.\n\n```{0}poll Как встретили 2021 год? Хорошо или плохо? -o [Отлично],[Хорошо],[А мне все равно],[Ужасно] 2020-01-10=20:00```'.format(prefix), # 1.16.4
              'Дата окончания голосования не должна быть раньше, чем сегодняшняя.'
            ],
            [ # 1.17
              'Репутация',
              'Вы хотите повысить или понизить человека? Выбор осуществляется нажатием на реакцию.\n\n👍 **Повысить**\n👎 **Понизить**',
              'Повышать или понижать самого себя нельзя!',
              'Окей, Вы его понизили.',
              'Окей, Вы его повысили.',
              'Пример',
              '```{0}rep <ID участника>```'.format(prefix),
              'Этого человека нет в нашей базе данных.',
              'Вы его уже повысили.',
              'Вы его уже понизили.'
            ]
        ]
    ]
