from fabric.api import *
from fabric.contrib.files import *

def deploy():
    run('uname -s')
    with cd('~/'+env.project_name):
        run('ls -al')
        run('git pull origin master')
        sed('lists/settings.py', 'database_name', env.db_name)
        sed('lists/settings.py', 'database_user', env.user)
        sed('lists/settings.py', 'database_password', env.password)
        run('dos2unix public/django.fcgi')
        run('chmod +x public/django.fcgi')