import random

class GameMaster():

    def __init__(self, players, jobs):
        # 役割の配布
        for i, player in enumerate(players):
            random.shuffle(jobs)
            player.Ibecome(jobs.pop(-1))

        self.players = players
        self.jobs = jobs

        # for seer
        self.nouse_display = ' '.join([
            job.getDisplayName() for job in self.jobs if not job.usingSomeone()
        ])

        # for werewolf
        self.werewolfs_list = [player for player in self.players if player.Iam().amIWerewolf()]

        # for thief
        self.thief_exchange_actor = None
        self.thief_exchange_target = None
