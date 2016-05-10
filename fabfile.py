from fabric.api import *
from fabric.colors import red
from fabric.contrib.console import confirm
from fabric.operations import prompt
import platform


# Give beautiful display of errors
env.colorize_errors = True

# Example: https://hooks.slack.services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
WEBHOOK_URL = 'Your custom assigned webhook url from slack api.'

# Example: #general
CHANNEL = 'Desired channel to post to.'


def slacker(msg):
    """
    Slack integration.

    *msg* -> Message to be written to channel board and commit.
    """
    msg_info = '(git) Blog App :point_up::cloud: on \
                <https://github.com/nickatnight/tivix-assignment|GitHub>.\n\n'+msg

    # Check if the user entered a message and exit the routine since we do not
    # want to commit an empty message -__ -;
    if not msg:
        print red('No message specified.')
        return False

    # Escape the string since slack is very picky on payload format.
    escaped_text = msg_info.replace('"', '\\"').replace("'", "\\'")

    # Format the json payload
    json = "{\"channel\": \""+CHANNEL+"\", \"text\": \""+escaped_text+"\",\
            \"username\": \"freebot\", \"icon_emoji\": \":octocat:\"}"

    # Post the payload
    local('curl -d "payload='+json+'" '+WEBHOOK_URL)


def git_sum(msg):
    # Textbook git commands
    local('git add .')
    local('git commit -m "'+msg+'"')
    local('git push origin master')

    # Uncomment following line if slack api info defined
    # slacker(msg)


def speak(msg, wait=False):
    """
    Text-to-speech integration for users on Mac/Linux.

    *msg*  -> Message to be spoken
    *wait* -> Fork a new process or wait for speech to finish
    """
    if 'Darwin' in platform.system():
        local('echo "%s" | say%s' % (msg, wait and ' ' or ' &'))
    elif 'Linux' in platform.system():
        local('echo "%s" | espeak%s' % (msg, wait and ' ' or ' &'))
    else:
        print red('Unable to use this function.')


def delete_pyc():
    """
    Check for local .pyc files and give them the boot
    """
    local("find . -name '*.pyc' -delete")


def coverage_run():
    """
    Run coverage package and include branch tag to make sure every code branch
    is taken.
    """
    local("coverage run --include='./*' --branch manage.py test")


def coverage_display():
    """
    Get the results of our coverage execution in html format and open a new
    browser window displaying the summary.
    """
    local('coverage html')

    # local('open htmlcov/index.html')


def run_tests():
    """
    Run unit tests and only display the results if the tests succeed.
    """
    if not coverage_run():
        speak("Test succeeded.")
        coverage_display()


def deploy_local():
    """
    Delete .pyc files and start the dev server.
    """
    run_tests()
    delete_pyc()
    if confirm("Would you like to push to GitHub?"):
        msg = prompt("Enter commit message: ")
        git_sum(msg)
    local('python manage.py runserver')
