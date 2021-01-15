# Generated by Django 2.0 on 2021-01-15 20:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='El formato debe ser 8 digitos y una letra mayuscula.', regex='^\\d{8}[A-Z]{1}$')], verbose_name='NIF')),
                ('sexo', models.CharField(choices=[('Man', 'Man'), ('Woman', 'Woman')], default='Woman', max_length=6, verbose_name='Gender')),
                ('titulo', models.CharField(choices=[('Software', 'Software'), ('Computer Technology', 'Computer Technology'), ('Information Technology', 'Information Technology'), ('Health', 'Health')], default='Software', max_length=22, verbose_name='Grade')),
                ('curso', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth'), ('Master', 'Master')], default='First', max_length=7, verbose_name='Year')),
                ('edad', models.PositiveIntegerField(default=18, validators=[django.core.validators.MinValueValidator(17), django.core.validators.MaxValueValidator(100)], verbose_name='age')),
                ('candidatura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voting.Candidatura', verbose_name='Candidature')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
