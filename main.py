import asyncio
import discord
from discord.ext import commands
from time import sleep

name = "<@1212765542180720771>"
zrada = [
    "зрада", "Зрада"
]
about_s = "!о_сервере"
about_c = "!команды"
about_a = "!про_админов"
about_b = "!про_тебя"
about_m = "!про_меня"
artem = "Артемий Шнур"
cup_of_tea = "!сделай_чаю"
thx = [
    "Спасибо", "спасибо", "Спасиб", "спасиб", "Спс", "спс", "Сяб", "сяб", "Спасибочки", "спасибочки", "Дякую", "дякую",
    "Cgfcb,j", "cgfcb,j"
]
p1 = "https://hi-news.ru/wp-content/uploads/2022/05/Chaj_s_limonom.jpg"
p2 = "https://klopotenko.com/wp-content/uploads/2023/01/yak-zavaryuvaty-chay-1.jpg"
p3 = "https://korisno.24tv.ua/resources/photos/news/202309/2385499.jpg?v=1693898341000"
p4 = "https://miychay.com/upload/iblock/7c6/7c664063ba5e6215cb3567de3330c187.jpg"
p5 = "https://images.aif.by/007/653/0f28e017653d7087316469a75f946e74.jpg"
p6 = "https://worldrecipes.eu/storage/97802/raudonoji-arbata.jpg"
p7 = "https://teatrading.ru/wa-data/public/blog/img/strawberry_leaf_tea3-2.png"
p8 = "https://7cups.ru/images/blog/4/tea_with_jasmine.jpg"
p9 = "https://www.ogorod.ru/images/cache/1200x628/crop/images%7Ccms-image-000115237.jpg"
p10 = "https://www.5.ua/media/pictures/original/238727.jpg?t=1640279655"
sigma = ["Sigma", "sigma", "Сигма", "сигма"]
gword = ["Гей", "гей", "Gay", "gay"]
cup = [
    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
]

time_window_milliseconds = 10000
max_msg_per_window = 5
author_msg_times = {}

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'bot connected to server')

@bot.event
async def on_member_join(member):
    await member.send("Добро пожаловать на Gaмеrsы! Меня зовут Артемий Шнур, я главный бот на этом "
                      "прекрасном сервере! Я обладаю некоторыми функциями, вот список: \n"
                      "**Для сервера:**\n"
                      "!жалоба (Имя) причина (Причина) - пожаловаться на участника.\n"
                      "!рандом (Минимальное значение) (Максимальное значение) - написать рандомное число.\n"
                      "!перемога - пишет рандомную дату. Посмакуємо перемогу!\n"
                      "!мут (Имя) (Время) (Причина)- позволяет замутить участника. **Доступно только Бобрам!**\n"
                      "!размут (Имя) - позволяет разамутить участника раньше заданного времени. **Доступно только"
                      " Бобрам!**\n"
                      "!чистка (Количество) - удаляет сообщения в текстовом канале. **Доступно только Бобрам!**\n"
                      "**Для ЛС с ботом:**\n"
                      "!о\_сервере - краткая информация про сервер.\n"
                      "!про\_админов - краткая информация про Админов.\n"
                      "!про\_тебя - краткая информация про бота.\n"
                      "!про\_меня - краткая информация про тебя.\n"
                      "!сделай\_чаю - сделать себе чай.\n"
                      "!команды - показать этот список.\n"
                      )
    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == '├👋приветствие':
            await bot.get_channel(ch.id).send(f'{member.mention}, Добро пожаловать на Gaмеrsы!'
                                              f'Надеемся, тебе у нас понравится!')

@bot.event
async def on_member_remove(member):
    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == '├👋приветствие':
            await bot.get_channel(ch.id).send(f'{member.mention} покинул сервер.'
                                              f'Грустикс.')

@bot.command()
async def жалоба(ctx, *, arg):
    if isinstance(ctx.message.channel, discord.TextChannel) and ctx.message.author != bot.user:
        author = ctx.message.author
        for ch in bot.get_guild(author.guild.id).channels:
            if ch.name == 'moderator-only':
                await bot.get_channel(ch.id).send(f'Жалоба от {author.mention}: {arg}')


@bot.command(pass_context=True)
@commands.has_role("Бобр")
async def мут(ctx, member: discord.Member = None, time=None, *, reason=None):
    if isinstance(ctx.message.channel, discord.TextChannel) and ctx.message.author != bot.user:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        time_convert = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}

        if member == None:
            await ctx.send("Вы забыли указать имя")
        elif time == None:
            await ctx.send("Вы забыли указать время")
        elif reason == None:
            reason = "Без причины"
        temp_mute = int(time[:-1]) * time_convert[time[-1]]
        embed = discord.Embed(title="Замученные участники", description=f"{member.mention} был замучен",
                              color=discord.Color.blue())
        embed.add_field(name='Причина:', value=f"{reason}", inline=False)
        embed.add_field(name='Замучен участником:', value=f"{ctx.author.mention}", inline=False)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
        await member.send(embed=embed)
        await member.add_roles(muted_role)
        await asyncio.sleep(temp_mute)
        await member.remove_roles(muted_role)
        embed = discord.Embed(title="Размученные участники", description=f"{member.mention} был размучен",
                              color=discord.Color.blue())
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Бобр")
async def размут(ctx, member: discord.Member = None):
    if isinstance(ctx.message.channel, discord.TextChannel) and ctx.message.author != bot.user:
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role in member.roles:
            await member.remove_roles(role)
            await member.add_roles(role)
            embed = discord.Embed(title="Размученные участники", description=f"{member.mention} был размучен",
                                  color=discord.Color.blue())
            embed.add_field(name='Размучен участником:', value=f"{ctx.author.mention}")
            await member.remove_roles(role)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Неверные аргументы или учасник не замучен.")

@bot.command(pass_context=True)
@commands.has_role("Бобр")
async def чистка(ctx, amount=None):
    if isinstance(ctx.message.channel, discord.TextChannel) and ctx.message.author != bot.user:
        if amount == None:
            amount = 11
        await ctx.channel.purge(limit=int(amount))

@bot.command(pass_context=True)
async def рандом(ctx, min = None, max = None):
    if isinstance(ctx.message.channel, discord.TextChannel) and ctx.message.author != bot.user:

        if min == None:
            await ctx.send("Вы забыли указать минимальное значение")
        if max == None:
            await ctx.send("Вы забыли указать максимальное значение")
        a = random.randrange(start=int(min), stop=int(max), step=1)
        await ctx.send(f"Число: {a}")

@bot.command(pass_context=True)
async def перемога(ctx):
    if isinstance(ctx.message.channel, discord.TextChannel) and ctx.message.author != bot.user:
        em = [":fire:", ":zap:", ":muscle:", ":eyes:", ":v:", ":champagne_glass:", ":flag_ua:"]
        mes = [
            "січня", "лютого", "березня", "квітня", "травня", "червня",
            "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]
        b = random.choice(mes)
        if b == "січня" or "березня" or "травня" or "липень" or "серпня" or "жовтня" or "грудня":
            a = random.randrange(start=1, stop=31, step=1)
        elif b == "квітня" or "червня" or "вересня" or "липень" or "листопада":
            a = random.randrange(start=1, stop=30, step=1)
        elif b == "лютого":
            a = random.randrange(start=1, stop=28, step=1)
        e1 = random.choice(em)
        em.remove(e1)
        e2 = random.choice(em)
        em.remove(e2)
        e3 = random.choice(em)
        em.remove(e3)
        await ctx.send(f"Перемога буде {a}-го {b}. {e1}{e2}{e3}")

@bot.command(pass_context=True)
async def зрада(ctx):
    await ctx.send(f"Не разгоняй тут зраду!")

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        guild = bot.get_guild(1135569796184948766)
        if guild:
            member = guild.get_member(message.author.id)
            if member:
                if isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
                    if name in message.content:
                        content_without_name = message.content.replace(name, "")
                        await message.reply(content_without_name)
                    elif about_c in message.content:
                        content_without_name = ("**Для сервера:**\n"
                                  "!жалоба (Имя) причина (Причина) - пожаловаться на участника.\n"
                                  "!рандом (Минимальное значение) (Максимальное значение) - написать рандомное число.\n"
                                  "!перемога - пишет рандомную дату. Посмакуємо перемогу!\n"
                                  "!мут (Имя) (Время) (Причина)- позволяет замутить участника. **Доступно только Бобрам!**\n"
                                  "!размут (Имя) - позволяет разамутить участника раньше заданного времени. **Доступно только"
                                  " Бобрам!**\n"
                                  "!чистка (Количество) - удаляет сообщения в текстовом канале. **Доступно только Бобрам!**\n"
                                  "**Для ЛС с ботом:**\n"
                                  "!о\_сервере - краткая информация про сервер.\n"
                                  "!про\_админов - краткая информация про Админов.\n"
                                  "!про\_тебя - краткая информация про бота.\n"
                                  "!про\_меня - краткая информация про тебя.\n"
                                  "!сделай\_чаю - сделать себе чай.\n"
                                  "!команды - показать этот список.\n")
                        await message.reply(content_without_name)
                    elif about_s in message.content:
                        content_without_name = ("Сервер был создан в **Августе 2023** года группой подростков "
                                                                 "энтузиастов. Сервер был раньше расчитан для друзей, но после "
                                                                 "было решено создать сервер для общего пользования. Ты мог "
                                                                 "заметить тут множество разделов с названием разных игр, не так "
                                                                 "ли? Это для того чтобы большое количество участников не "
                                                                 "скучковалось в одном месте, содавая балаган. Для этого у нас "
                                                                 "есть **балакальная**, как в текстовом формате, так и в голосовом. "
                                                                 "Надеемся что тебе понравится с нами!")
                        await message.reply(content_without_name)
                    elif about_a in message.content:
                        content_without_name = ("**mal0mArka**(Вениамин) - Главный Админ, основные руки и ноги сервера. В основном "
                                                "**организовывает различные мероприятия и события**. Очень любит свой сервер и всячески"
                                                " сопобствует его развитию. *Ибо нехер*\n"
                                                "**Dasifor**(Дамир) - Один из Админов, главный Пацюк на этом сервере. Он выделяется"
                                                " своей **крайней вежливостью** к различным учатсникам своего сервера, особенно к "
                                                "<@1033579050209398814>. Обычно ему на все наплевать, потому что он не чистокровный "
                                                "фрич(по его словам). *Дідько*\n"
                                                "**Misha-K**(Михаил) -  Один из Админов, светлая душа с благими намерениями. Крайне "
                                                "общителен и очень позитивный человек. **Готов оказать помощь в (почти)любом деле**, "
                                                "не обладает запасом токсикона, правда если не **появится какое-то гамно ослиное**..."
                                                " Не злите его - вот вам мой совет. *Маломарин*")
                        await message.reply(content_without_name)
                    elif about_b in message.content:
                        content_without_name = ("Я Артемий Шнур, главный бот сервера Gaмеrsы. Могу ответить на несколько "
                                                "твоих вопросов, которые тебя интересуют. Меня создали <@738391322926252154> "
                                                "и <@683720215959437313>. Классные ребята. ")
                        await message.reply(content_without_name)
                    elif about_m in message.content:
                        content_without_name = (f"Ты <@{message.author.id}>, участник сервера Gaмеrsы. Пока что это все, что могу сказать о тебе.")
                        await message.reply(content_without_name)
                    elif cup_of_tea in message.content:
                        content_without_name = ("Да, сейчас...")
                        await message.reply(content_without_name)
                        sleep(5)
                        content_without_name = ("Вот, держите.")
                        await message.reply(content_without_name)
                        cup1 = random.choice(cup)
                        content_without_name = (cup1)
                        await message.reply(content_without_name)
                    elif any(word in message.content for word in thx[10:12]):
                        content_without_name = "Нема за що!"
                        await message.reply(content_without_name)
                    elif any(word in message.content for word in thx[12:14]):
                        content_without_name = "J,hfofqntcm!"
                        await message.reply(content_without_name)
                    elif any(word in message.content for word in thx[0:9]):
                        content_without_name = "Обращайтесь!"
                        await message.reply(content_without_name)
                    elif any(word in message.content for word in sigma[0:4]):
                        content_without_name = "https://tenor.com/view/%D1%81%D0%B8%D0%B3%D0%BC%D0%B0-gif-3883804279153061520"
                        await message.reply(content_without_name)
                    elif any(word in message.content for word in gword[0:4]):
                        content_without_name = "Сам"
                        await message.reply(content_without_name)
                    elif artem in message.content:
                        content_without_name = "Не важно"
                        await message.reply(content_without_name)
                    else:
                        content_without_name = "Я... Я не могу вас понять. Извините."
                        await message.reply(content_without_name)
            else:
                content_without_name = "Вы не являетесь участником сервера Gaмеrsы."
                await message.reply(content_without_name)
    await bot.process_commands(message)
bot.run(TOKEN1)
