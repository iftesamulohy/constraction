from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from globalapp2.models import Beneficaries

# Create your models here.
class LoanBeneficaries(Beneficaries):
    pass
class LoanTransactions(models.Model):
    giver_id = models.ForeignKey(LoanBeneficaries,on_delete=models.CASCADE,related_name='given_loans')
    taker_id = models.ForeignKey(LoanBeneficaries,on_delete=models.CASCADE,related_name='taken_loans')
    amount = models.FloatField(validators=[MinValueValidator(1)])
    OPTION_a = 'Fixed'
    OPTION_b = 'Percentage'
    CHOICES = (
        (OPTION_a, 'Fixed'),
        (OPTION_b, 'Percentage'),
    )
    
    return_type = models.CharField(max_length=50, choices=CHOICES,blank=True,null=True)
    interest = models.FloatField()
    instalment = models.IntegerField(validators=[MinValueValidator(1)])
    interested_amount = models.FloatField(blank=True,null=True)
    return_amount = models.FloatField(blank=True,null=True)
    current_amount = models.FloatField(blank=True,null=True)
    status = models.BooleanField(default=True)
    last_payed  = models.DateField(blank=True,null=True)
    created_at = models.DateField(default=timezone.now())
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.return_type == 'Percentage':
            self.interested_amount = (self.amount*self.interest)/100
            self.return_amount=self.amount+self.interested_amount
        else:
            self.return_amount = self.amount+self.interest
        is_first_time = not self.pk
        if is_first_time:
            self.current_amount=self.return_amount
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.giver_id}"

