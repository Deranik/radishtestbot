import disnake
from disnake.ext import commands
from config import *
from disnake.ui import Button, View


class Send1(disnake.Embed):
    def __init__(self):
        super().__init__(
            description=(
                ''
            ),
            color=disnake.Color.from_rgb(47, 49, 54),
        )
 
        
class Send2(disnake.Embed):
    def __init__(self):
        super().__init__(
            description=(
                f'{TEXT}'
            ),
            color=disnake.Color.from_rgb(47, 49, 54),
        )


class ModalsView(disnake.ui.Modal):
    def __init__(self, one):
        self.one = one
        components = [
            disnake.ui.TextInput(
                label=f"{Q1}", 
                placeholder=f"{O1}", 
                custom_id="qq1", 
                max_length=100,
            ),
            disnake.ui.TextInput(
                label=f"{Q2}", 
                placeholder=F"{O2}", 
                custom_id="qq2", 
                max_length=100,
            ),
            disnake.ui.TextInput(
                label=f"{Q3}", 
                placeholder=F"{O3}", 
                custom_id="qq3", 
                style=disnake.TextInputStyle.paragraph,
                max_length=100,
            ),
            disnake.ui.TextInput(
                label=F"{Q4}", 
                placeholder=F"{O4}", 
                custom_id="qq4", 
                max_length=100,
            ),
            disnake.ui.TextInput(
                label=F"{Q5}", 
                placeholder=F"{O5}", 
                custom_id="qq5" ,
                style=disnake.TextInputStyle.paragraph,
                max_length=100,
            ),
        ]
        super().__init__(title=f"Заявка на {one}", components=components)

    async def callback(self, interaction) -> None:
        embed = disnake.Embed(description="> Ваша заявка отправлена", color=0x2f3136)
        if self.one == 'Coder':
            
            channel_id = CODER_NABOR
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                view = buttons()
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one), view=view)
                await interaction.response.send_message(embed=embed, ephemeral=True)

            else:
                await interaction.response.send_message('Ошибка', ephemeral=True)
                


class SelectSends(disnake.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @disnake.ui.select(
        custom_id='send',
        min_values=1,
        max_values=1,
        placeholder='Выберите должность',
        options=[
            disnake.SelectOption(
                label='Coder',
                description='Подать заявку на Coder',
                value='coder'
            ),
            
        ]
    )
    async def select_callback(self, select: disnake.ui.Select, inter):
       await inter.response.send_modal(modal=ModalsView('Coder'))
 



class SetsEmbed(disnake.Embed):
    def __init__(self, interaction, two):
        super().__init__(
            title=f"Пользователь подал заявку на роль {two}",
            description=f"ID: **{interaction.author.id}**\nПользователь: **{interaction.author.name}**\n",
            color=disnake.Color.from_rgb(47, 49, 54),
        )
        self.add_field(name=F"{Q1}", value=f"{interaction.text_values['qq1']}")
        self.add_field(name=F"{Q2}", value=f"{interaction.text_values['qq2']}", inline=False)
        self.add_field(name=f"{Q3}", value=f"{interaction.text_values['qq3']}", inline=False)
        self.add_field(name=F"{Q4}", value=f"{interaction.text_values['qq4']}", inline=False)
        self.add_field(name=F"{Q5}", value=f"{interaction.text_values['qq5']}", inline=False)



class buttons(View):
    def __init__(self):
        super().__init__()


    @disnake.ui.button(label="Принять", style=disnake.ButtonStyle.green, custom_id="пр")
    async def yes_button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        role = disnake.utils.get(interaction.guild.roles, id=SOBES_ROLE_ID)
        await interaction.response.send_message("Вы приняли заявку, теперь напишите пользователю о проведении собеседования. Роль была выдана", ephemeral=True)
        await interaction.author.add_roles(role)
        embed = disnake.Embed(description="Ваша заявка **принята**, ожидайте **ответа** когда вам назначат собеседование", color=disnake.Color.from_rgb(47, 49, 54))
        embed.set_thumbnail(url=interaction.author.avatar.url)
        embed.set_author(name="Заявка", icon_url=IMAGE)
        await interaction.author.send(embed=embed)

    @disnake.ui.button(label="Отклонить", style=disnake.ButtonStyle.red, custom_id="от")
    async def no_button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.message.delete()

    @disnake.ui.button(label="На рассмотрении", style=disnake.ButtonStyle.gray, custom_id="на")
    async def yzr_button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
    
            embed = disnake.Embed(description="Ваша заявка **рассматривается**, ожидайте **ответа**, если ответ не **поступит** - вас **не** приняли", color=disnake.Color.from_rgb(47, 49, 54))
            embed.set_thumbnail(url=interaction.author.avatar.url)
            embed.set_author(name="Заявка", icon_url=IMAGE)
            await interaction.author.send(embed=embed)
            await interaction.send("Отправлено")
