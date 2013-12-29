from fabric.state import env

env.GIT_SERVER = 'https://github.com/'
env.DEPLOY_USER = 'noroot'
env.DEPLOY_PATH = '/opt/deploy/'
env.PROJECT_OWNER = 'SohuTech'
env.DEFAULT_BRANCH = 'master'
env.PYPI_INDEX = 'http://pypi.douban.com/simple/'
