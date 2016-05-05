from fabric.api import *

env.colorize_errors = True


def speak(msg, wait=False):
    local('echo "%s" | say%s'%(msg, wait and ' ' or ' &'))


def delete_pyc():
    local("find . -name '*.pyc' -delete")

def coverage_run():
    local("coverage run --include='./*' --branch manage.py test")

    
def coverage_display():
    local('coverage html')

    local('open htmlcov/index.html')


def run_tests():

    delete_pyc()

    if not coverage_run():
        speak("Test succeeded.")
        coverage_display()