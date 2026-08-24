from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0015_toolsession_verbal_breakout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeatureRequest',
        ),
        migrations.DeleteModel(
            name='WaitingListEntry',
        ),
    ]
