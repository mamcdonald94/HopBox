# Generated by Django 2.2 on 2021-08-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopbox_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='submited_by',
            new_name='submitted_by',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='pw_hash',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscribeded_user',
        ),
        migrations.AddField(
            model_name='user',
            name='subscribed_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_subscribed', to='hopbox_app.Subscription'),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image_for_review',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_image', to='hopbox_app.Review'),
        ),
    ]
