from job.Job import Job

class Villager(Job):

    def __init__(self):
        super().__init__()
        super().setName('villager')
        super().setDisplayName('**村人**')
        super().IamWerewolf(False)
