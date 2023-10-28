# Generated by Django 4.2.6 on 2023-10-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_status_tags_delete_student_delete_tagss_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='subgoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subgoals_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='subgoals',
        ),
        migrations.AddField(
            model_name='snippet',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='snippet',
            name='on_hold',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='subgoals',
            name='subgoals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.snippet'),
        ),
    ]
