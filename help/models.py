from django.db import models


class Model_Name(models.Model):
    var_name_text = models.CharField(max_length=200)
    var_name_date = models.DateTimeField('date')


class Model_Name(models.Model):
    var_name_key = models.ForeignKey(Question, on_delete=models.CASCADE)
    var_name_int = models.IntegerField(default=0)
    
    def model_function(self):
        return result 
