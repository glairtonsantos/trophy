from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.registers.models import CollectedCoin, KilledMonster, Death
from .models import Trophy, TrophyUser

def register_trophy_user(user, instance_queryset, attribute):
    amount = instance_queryset.count()

    finder_trophy = Trophy.objects.filter(
        level__amount=amount, 
        level__register_class=attribute
    ).first()
    
    if finder_trophy:
        TrophyUser.objects.create(
            trophy=finder_trophy,
            user=user
        )

@receiver(post_save, sender=CollectedCoin)
def verify_if_win_trophy_coin(sender, instance, **kwargs):
    register_trophy_user(
        instance.user, 
        instance.user.coins.all(), 
        'coins'
    )

@receiver(post_save, sender=KilledMonster)
def verify_if_win_trophy_killed_monster(sender, instance, **kwargs):
    queryset = instance.user.dead_monsters.filter(
        monster__name=instance.monster.name
    )
    register_trophy_user(
        instance.user, 
        queryset, 
        'monsters'
    )

@receiver(post_save, sender=Death)
def verify_if_win_trophy_death(sender, instance, **kwargs):
    register_trophy_user(
        instance.user, 
        instance.user.deaths.all(), 
        'deaths'
    )