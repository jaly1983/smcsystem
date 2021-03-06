# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='程序名称')),
                ('code_name', models.CharField(max_length=32, verbose_name='程序功能名称')),
                ('path', models.CharField(blank=True, max_length=32, null=True, verbose_name='程序路径')),
                ('start', models.CharField(blank=True, max_length=128, null=True, verbose_name='启动方法')),
                ('port', models.CharField(blank=True, max_length=128, null=True, verbose_name='端口号')),
                ('mapping', models.CharField(blank=True, max_length=128, null=True, verbose_name='外网映射')),
                ('www', models.CharField(blank=True, max_length=128, null=True, verbose_name='域名')),
                ('log', models.CharField(blank=True, max_length=128, null=True, verbose_name='日志路径')),
                ('user', models.CharField(blank=True, max_length=32, null=True, verbose_name='负责人')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='负责人电话')),
                ('qq', models.CharField(blank=True, max_length=32, null=True, verbose_name='qq')),
                ('email', models.EmailField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('note', models.TextField(blank=True, null=True, verbose_name='注释')),
            ],
            options={
                'verbose_name_plural': '所有程序信息',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='业务线名称')),
                ('user', models.CharField(blank=True, max_length=32, null=True, verbose_name='总负责人')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='电话')),
                ('qq', models.CharField(blank=True, max_length=32, null=True, verbose_name='qq')),
                ('email', models.EmailField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('note', models.TextField(blank=True, null=True, verbose_name='注释')),
                ('to_code', models.ManyToManyField(blank=True, null=True, to='filing.Code', verbose_name='所属程序')),
            ],
            options={
                'verbose_name_plural': '业务信息',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=32, unique=True, verbose_name='ip地址')),
                ('hostname', models.CharField(blank=True, max_length=32, null=True, verbose_name='主机名')),
                ('cpu_num', models.CharField(blank=True, max_length=32, null=True, verbose_name='cpu数')),
                ('cpu_model', models.CharField(blank=True, max_length=64, null=True, verbose_name='cpu型号')),
                ('disk_num', models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘个数')),
                ('disk_capacity', models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘总量')),
                ('disk_use', models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘已用')),
                ('mem', models.CharField(blank=True, max_length=32, null=True, verbose_name='内存大小')),
                ('mem_use', models.CharField(blank=True, max_length=32, null=True, verbose_name='内存已用')),
                ('brand', models.CharField(blank=True, max_length=32, null=True, verbose_name='品牌')),
                ('type', models.CharField(blank=True, choices=[('1', '物理机'), ('2', '虚拟机'), ('3', '交换机'), ('4', '路由器'), ('5', '防火墙'), ('6', 'windows'), ('7', 'VMware')], default='1', max_length=32, null=True, verbose_name='主机性质')),
                ('sn', models.CharField(blank=True, max_length=32, null=True, verbose_name='sn号')),
                ('system', models.CharField(blank=True, max_length=32, null=True, verbose_name='系统版本')),
                ('kernel', models.CharField(blank=True, max_length=32, null=True, verbose_name='系统内核')),
                ('status', models.CharField(choices=[('1', '在线'), ('2', '下线')], default='1', max_length=32, verbose_name='状态')),
                ('c_room', models.CharField(blank=True, choices=[('1', '西山机房'), ('2', '国防科技园')], max_length=32, null=True, verbose_name='机房')),
                ('position', models.CharField(blank=True, max_length=32, null=True, verbose_name='机柜位置')),
                ('note', models.TextField(blank=True, max_length=256, null=True, verbose_name='注释')),
                ('to_code', models.ManyToManyField(blank=True, null=True, to='filing.Code', verbose_name='程序')),
                ('to_group', models.ManyToManyField(blank=True, null=True, to='filing.Group', verbose_name='所属项目')),
            ],
            options={
                'verbose_name_plural': '主机信息',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('level', models.CharField(max_length=32, verbose_name='级别')),
                ('message', models.CharField(max_length=128, verbose_name='日志内容')),
                ('host_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filing.Host', verbose_name='ip地址')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, verbose_name='用户名')),
                ('passwd', models.CharField(max_length=32, verbose_name='密码')),
                ('admin', models.CharField(choices=[('1', 'admin'), ('2', 'user')], default='2', max_length=32, verbose_name='状态')),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
        ),
    ]
