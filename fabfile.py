from fabric.api import *
from fabric.contrib.files import *
from fabric.colors import _wrap_with

green_bg = _wrap_with('42')
red_bg = _wrap_with('41')
# Set the list of apps to test
env.test_apps = "lists_app"


def deploy():
    with cd('~/' + env.project_name):
        run('git pull origin master')
        sed('lists/settings.py', 'database_name', env.db_name)
        sed('lists/settings.py', 'database_user', env.user)
        sed('lists/settings.py', 'database_password', env.password)
        run('dos2unix public/django.fcgi')
        run('chmod +x public/django.fcgi')


def test():
    with settings(warn_only=True):
        result = local('./.env/bin/python ./manage.py test %(test_apps)s -v 2 --failfast' % env, capture=False)
    if result.failed:
        print red_bg("Some tests failed")
    else:
        print
        print green_bg("All tests passed - have a banana!")