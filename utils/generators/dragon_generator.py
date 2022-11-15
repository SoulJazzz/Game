from utils import rnd


class Dragon:
    имя: str
    облик: str
    манеры: str
    привязанность: str
    слабость: str
    цели: str


names: list = [
    "Аэрос",
    "Агха",
    "Аккан",
    "Алаэ",

    "Андра",
    "Андуск",
    "Ангкар",
    "Арадас",

    "Араут",
    "Арвея",
    "Арыз",
    "Атар",

    "Аунтир",
    "Аута",
    "Бахр",
    "Бала",

    "Калаум",
    "Клим",
    "Клаут",
    "Даерев",

    "Далаг",
    "Дург",
    "Эйр",
    "Элден",

    "Эндар",
    "Этар",
    "Фел",
    "Галад",

    "Галл",
    "Голос",
    "Гут",
    "Ингейр",

    "Икс",
    "Ийльм",
    "Джар",
    "Керин",

    "Лхам",
    "Лоттор",
    "Малаэ",
    "Марун",

    "Мере",
    "Миир",
    "Морн",
    "Набал",

    "Нур",
    "Ним",
    "Олот",
    "Онтор",

    "Отим",
    "Палар",
    "Раали",
    "Рагот",

    "Рит",
    "Рсеар",
    "Сарикс",
    "Сер",

    "Скад",
    "Сурр",
    "Тхал",
    "Тханач",

    "Тхот",
    "Тракс",
    "Триин",
    "Тостин",

    "Тратайн",
    "Треори",
    "Турас",
    "Уалин",

    "Умер",
    "Урит",
    "Уксин",
    "Ваер",

    "Вала",
    "Валос",
    "Винк",
    "Воар",

    "Вурим",
    "Ваур",
    "Зунде",
    "Зиреф"
]

appearances: list = [
    "Драконьи буквы или символы, выгравированные на выдающихся чешуйках",
    "Большой шрам",
    "Один глаз отсутствует или бельмо",
    "Кривые зубы",
    "Заметный избыточный или недостаточный вес",
    "Вытянутое, извилистое тело",
    "Укороченное, коренастое тело",
    "Монеты или драгоценные камни, вплавленные в шкуру",
    "Скульптурные рога или когти",
    "Кольца, пронзающие гребень или края крыльев",
    "Одетый в некое подобие одежды, от палантина до полного халата",
    "Необычная окраска (например, красный дракон с оранжевым, коричневым или фиолетовым отливом)",
    "Сгорбленная, хищная поза, как у преследующей кошки",
    "Прямая, почти двуногая поза",
    "Чешуя покрыта нарисованными отпечатками рук приспешников, поклонников или детей",
    "Ожерелья из костей, рогов, когтей или зубов, отнятых у врагов",
    "Дополнительные рога или шипы",
    "Удлиненные клыки или дополнительные ряды зубов",
    "Заостренная или зазубренная чешуя",
    "Элементальная энергия, соответствующая оружию дыхания дракона, просачивающаяся между чешуйками"
]

manners: list = [
    "Поворачивает голову из стороны в сторону, когда слушает или говорит",
    "Хвост постоянно извивается змееподобным образом",
    "Медленно и постоянно расправляет крылья",
    "Опускает голову, чтобы говорить глаза в глаза с более мелкими существами - если не злится",
    "Использует драконьи слова и фразы даже при разговоре на других языках",
    "Сопровождает речь звериными звуками - рыком, ревом, кваканьем, щебетанием или свистом",
    "Поглаживает кончик хвоста",
    "Беспорядочно грызет или ковыряется в зубах мечами, кольями или копьями",
    "Быстро забывает имена и придумывает вместо них случайные прозвища",
    "Обременяет разговор обширным историческим контекстом, независимо от того, имеет он отношение к делу или нет",
    "Постоянно подергивает хвостом - и иногда набрасывается на него",
    "Говорит на архаичной форме Общего (эквивалент шекспировского английского) и не понимает современный сленг и идиомы",
    "Склонен произносить ужасающие гортанные звуки, которые на самом деле являются смехом",
    "Любит подражать голосам гуманоидов",
    "Воспринимает современные культуры как исторический курьез, который неминуемо рухнет",
    "С трудом различает детали чего-либо настолько мелкого, как гуманоиды",
    "Точит когти или рога о близлежащие каменные поверхности",
    "Проявляет своё оружие дыхания: выдыхает кольца дыма, пускает дуговые молнии между клыков или выдувает кислотные пузыри",
    "Беспокойно вздыхает, производя впечатление огромной скуки",
    "Слишком подозрителен, рассматривая всех встреченных гуманоидов как вероятных агентов дракона-соперника"
]

affections: list = [
    "Я дорожу одним особым предметом в своем кладе - подарком от любимого человека, который давно умер",
    "Я близок со своими братьями и сестрами, чьи логова находятся неподалеку. Я готов пойти на все, чтобы защитить их или отомстить за них",
    "Находящаяся рядом личность интригует меня интересными вопросами и причудливыми идеями",
    "Я собираю информацию о мирах Материального Плана и хотел бы когда-нибудь побывать в другом мире",
    "Я предан Бахамуту или Тиамат и ставлю их интересы выше своих собственных",
    "Я полон решимости уничтожить авантюристов, убивших моего родителя, и всех, кто с ними связан",
    "Я одержим желанием привлечь внимание другого дракона",
    "Я чувствую себя обязанным защищать существ, населяющих мою территорию (кроме тех, которых я ем)",
    "Я пытаюсь собрать чрезвычайно редкий набор бесценных сокровищ",
    "Я не успокоюсь, пока не верну предмет, украденный из моего клада"
]

disadvantages: list = [
    "Я считаю авантюристов опасными и убежден, что однажды встречу свою гибель от их рук",
    "Один предмет в моем владении стоит столько же, сколько все мои запасы вместе взятые, и страх, что его могут украсть, снедает меня",
    "Если есть возможность, я ем досыта, а затем погружаюсь в долгий, глубокий сон",
    "Я предпочитаю, чтобы моя грозная репутация отпугивала незваных гостей, а не сражаться с ними",
    "Другие драконы презирали бы меня, если бы знали, с какой любовью я отношусь к своим приспешникам. Они такие милые!",
    "Я до ужаса боюсь существ с Внешних Планов - особенно модронов",
    "Другой дракон поклялся найти и уничтожить меня",
    "Гуманоиды не достойны узнать ужасные космические истины из книг, хранящихся в моем кладе",
    "Перспектива прожить еще несколько веков изнуряет меня",
    "Я убежден, что версия меня в другом мире на Материальном Плане надеется уничтожить меня и украсть мой клад"
]

targets: list = [
    "Найти хорошее место для дополнительного логова",
    "Заполучить артефакт или мощный магический предмет для клада",
    "Создать династическую родословную, произведя на свет потомство",
    "Устранить молодых драконов, которые могут стать соперниками или угрозой, если им позволить повзрослеть",
    "Преобразовать большой регион в место, подходящее для логова дракона",
    "Развивать драконье зрение для достижения целей в нескольких мирах",
    "Основать логово и обустроить землю вокруг него, чтобы обеспечить максимальную безопасность и хорошую охоту",
    "Собрать как можно больше сокровищ",
    "Получить магические средства для защиты логова",
    "Помешать усилиям других молодых драконов основать логово в этой области",
    "Добиться страха и уважения других существ, живущих рядом с логовом, с помощью демонстрации силы",
    "Добиться верности преданных и сильных приспешников",
    "Избежать старости, став нежитью или найдя ей магические альтернативы",
    "Преодолеть пределы физического существования в одном мире, объединив отображения в нескольких мирах или устроив логово на другом плане существования",
    "Получить определенный артефакт, возможно, для завершения набора (все три части Регалий Зла - Око Векны, Рука Векны и т.п.)",
    "Собрать полный набор произведений искусства, например, все картины великого мастера, рукописи всех произведений знаменитого автора или все украшения, сделанные мастером-ремесленником",
    "Превратить целый мир в экстремальную среду, подходящую в качестве логова - вулканический ад, замерзшую страну чудес, засушливую пустошь и т.д.",
    "Уничтожить одного или нескольких богов в качестве акта мести или для того, чтобы вознестись к божественности"
]


def createDragon() -> Dragon:
    dragon = Dragon()
    dragon.имя = rnd.rnd_get(names)
    dragon.цели = rnd.rnd_get(targets)
    dragon.облик = rnd.rnd_get(appearances)
    dragon.манеры = rnd.rnd_get(manners)
    dragon.слабость = rnd.rnd_get(disadvantages)
    dragon.привязанность = rnd.rnd_get(affections)
    return dragon