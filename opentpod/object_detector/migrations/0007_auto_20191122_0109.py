# Generated by Django 2.2.3 on 2019-11-22 01:09

from django.db import migrations, models
import opentpod.object_detector.models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0021_auto_20190826_1827'),
        ('object_detector', '0006_auto_20191120_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detector',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='trainset',
            name='videos',
        ),
        migrations.AddField(
            model_name='trainset',
            name='tasks',
            field=models.ManyToManyField(to='engine.Task'),
        ),
        migrations.AlterField(
            model_name='detector',
            name='dnn_type',
            field=models.CharField(choices=[('tensorflow_faster_rcnn_resnet101', 'Tensorflow Faster-RCNN ResNet 101'), ('tensorflow_faster_rcnn_resnet50', 'Tensorflow Faster-RCNN ResNet 50'), ('tensorflow_ssd_mobilenet_v2', 'Tensorflow SSD MobileNet V2')], max_length=32),
        ),
        migrations.AlterField(
            model_name='detector',
            name='status',
            field=models.CharField(choices=[('created', 'CREATED'), ('training', 'TRAINING'), ('trained', 'TRAINED'), ('error', 'ERROR')], default=opentpod.object_detector.models.Status('created'), max_length=32),
        ),
    ]