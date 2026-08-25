from django.db import migrations,models
class Migration(migrations.Migration):
 initial=True; dependencies=[]
 operations=[migrations.CreateModel(name='Concert',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(max_length=200)),('venue',models.CharField(max_length=200)),('city',models.CharField(max_length=100)),('country',models.CharField(blank=True,max_length=100)),('date',models.DateTimeField()),('description',models.TextField(blank=True))])]
