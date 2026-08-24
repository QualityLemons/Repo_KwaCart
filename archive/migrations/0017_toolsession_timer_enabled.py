from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0016_remove_engagement_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolsession',
            name='timer_enabled',
            field=models.BooleanField(
                default=True,
                help_text=(
                    'When false, the session timer is hidden for everyone and the room '
                    'runs at its own pace. Hosts can toggle this during an open session.'
                ),
            ),
        ),
    ]
