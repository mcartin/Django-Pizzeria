# Generated by Django 5.0.2 on 2024-02-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0002_remove_pizza_price_alter_pizza_crust_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='pizza_size',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='title',
        ),
        migrations.AddField(
            model_name='pizza',
            name='cheese',
            field=models.CharField(choices=[('mozzarella', 'Mozzarella'), ('vegan', 'Vegan'), ('low_fat', 'Low Fat')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='crust',
            field=models.CharField(choices=[('normal', 'Normal'), ('thin', 'Thin'), ('thick', 'Thick'), ('gluten_free', 'Gluten Free')], default='normal', max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.CharField(choices=[('tomato', 'Tomato'), ('bbq', 'BBQ')], max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizzaapp.topping'),
        ),
    ]
