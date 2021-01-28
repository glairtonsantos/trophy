from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.registers.models import CollectedCoin
from .models import Trophy, TrophyUser


@receiver(post_save, sender=CollectedCoin)
def verify_if_win_trophy_coin(sender, instance, **kwargs):
    amountCoin = instance.user.coins.all().count()

    finder_trophy = Trophy.objects.filter(
        level__amount=amountCoin, 
        level__register_class='coins'
    ).first()
    
    if finder_trophy:
        TrophyUser.objects.create(
            trophy=finder_trophy,
            user=instance.user
        )