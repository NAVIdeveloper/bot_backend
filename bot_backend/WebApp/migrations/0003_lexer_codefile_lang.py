# Generated by Django 4.0.1 on 2023-04-17 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_codefile_is_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lexer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lang', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='codefile',
            name='lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WebApp.lexer'),
        ),
    ]
