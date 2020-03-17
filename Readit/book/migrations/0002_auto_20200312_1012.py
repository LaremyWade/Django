# Generated by Django 3.0.4 on 2020-03-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use pen name, not real name', max_length=70, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='is_favourite',
            field=models.BooleanField(default=False, verbose_name='Favourite?'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='book.Author'),
        ),
    ]
