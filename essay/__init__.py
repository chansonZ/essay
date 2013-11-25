from fabric.state import env

env.GIT_SERVER = '10.10.51.78'
env.DEPLOY_HOST = '10.13.83.204'
env.DEPLOY_USER = 'moon'
env.DEPLOY_PATH = '/opt/deploy/'
env.PROJECT_OWNER = 'clan'
env.DEFAULT_BRANCH = 'master'
env.PYPI_INDEX = 'http://10.13.83.194:9791/simple/'
