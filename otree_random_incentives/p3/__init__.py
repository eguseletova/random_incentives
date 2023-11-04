from otree.api import *
import random


doc = """
Random Incentives Game
"""


class Constants(BaseConstants):
    name_in_url = 'p3'
    players_per_group = None
    num_rounds = 1
    incentive_chance = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    random_number = models.IntegerField()

    choice = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Have you ever been to the UK?'
    )


def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            participant.random_number = random.randint(1,100)
            player.random_number = participant.random_number


# PAGES
class no_incentives(Page):
    form_model = 'player'
    form_fields = ['random_number']

    @staticmethod
    def is_displayed(player: Player):
        return player.random_number > Constants.incentive_chance


class incentives(Page):
    form_model = 'player'
    form_fields = ['random_number']

    @staticmethod
    def is_displayed(player: Player):
        return player.random_number <= Constants.incentive_chance


class choice(Page):
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def is_displayed(player: Player):
        return player.random_number <= Constants.incentive_chance


page_sequence = [no_incentives, incentives, choice]