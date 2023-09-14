# from .models import LoanLog,LoanBeneficaries

# def log_action(giver_id,taker_id,loan_id,author_id,activity):
#     LoanLog.objects.create(
#         giver_id=giver_id,
#         author_id = author_id,
#         loan_id= loan_id,
#         taker_id = taker_id,
#         activity = activity
#         )


# from django.db.models.signals import post_save, pre_delete
# from django.dispatch import receiver

# @receiver(post_save, sender=LoanBeneficaries)
# def log_create_update_action(sender, instance, created, **kwargs):
#     activity = "Created" if created else "Updated"
#     print("working")
#     data = f"{sender.__name__} object: {instance}"
#     print()
#     #log_action(author_id=user, activity=activity)

# # @receiver(pre_delete, sender=LoanBeneficaries)
# # def log_delete_action(sender, instance, **kwargs):
# #     action = "Deleted"
# #     data = f"{sender.__name__} object: {instance}"
# #     log_action(user=instance.user, action=action, data=data)



