from django.db import migrations


def create_subjects(apps):
    Subject = apps.get_model('classroom', 'Especialidad')
    Subject.objects.create(name='Computacion', color='#007bff')
    Subject.objects.create(name='Matematicas', color='#28a745')
    Subject.objects.create(name='Software', color='#17a2b8')


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]