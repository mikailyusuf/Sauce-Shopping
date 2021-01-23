# Generated by Django 3.1.5 on 2021-01-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_photo',
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(to='products.Image'),
        ),
    ]
