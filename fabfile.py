import os

from fabric.context_managers import cd, prefix, lcd
from fabric.decorators import task, roles, parallel, runs_once
from fabric.operations import run, put, local
from fabric.state import env
from fabric.tasks import execute

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env.use_ssh_config = True
env.hosts = [
    # STAGING
    'zoo-staging-web1'
]
env.roledefs = {
    'zoo-staging': ['zoo-staging-web1'],
    'zoo-staging-db-control': ['zoo-staging-web1']
    }

# TODO: remove servers from the load balancer
@task(default=True)
@roles('zoo-staging')
def deploy_staging(skip_pip=False):
    deploy_env('develop', 'zoo-staging-db-control', skip_pip)
    # only clear the cache when we're on the last host
    if env.host_string == env.all_hosts[-1]:
        #clear_views_templates_cache()
        # need to send the mail only once
        #send_deploy_changes_mail()
        # delete the log file after deployment mail command is run successfully
        #delete_latest_log_file()
        pass

def deploy_env(branch, db_control_hosts, skip_pip=False):
    # only log the changes when we're on the last host
    if env.host_string == env.all_hosts[-1]:
        git_fetch(branch)
        git_log(branch)
    git_pull(branch)
    if not skip_pip:
        update_requirements()
    db_hosts = env.roledefs[db_control_hosts]
    if env.host_string in db_hosts:
    	pass
    cycle_uwsgi()


def git_log(branch):
    with cd('/web/zoo'):
        log_command = "git log HEAD..origin/{0} --no-merges --pretty=format:\'%H %s\' >> new_changes.log".format(branch)
        run('sudo -u ubuntu sh -c "' + log_command + '"')


def git_fetch(branch):
    with cd('/web/zoo'):
        run('sudo -u ubuntu git fetch origin {0}:refs/remotes/origin/{0}'.format(branch))


def git_pull(branch):
    with cd('/web/zoo'):
        run('sudo -u ubuntu git pull origin {0}'.format(branch))


def update_requirements():
    with cd('/web/zoo'):
        with prefix('workon zoo'):
            run('pip install -U -r requirements.txt -r requirements-ec2.txt')

def cycle_uwsgi():
    run('sudo supervisorctl restart uwsgi')

@task
def delete_latest_log_file():
    with cd('/web/zoo'):
        run('sudo -u ubuntu rm new_changes.log')

