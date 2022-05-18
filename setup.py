from setuptools import setup, find_packages

setup(
    name='gitlab_ticket_maker',
    packages=find_packages(),
    description='A simple command line tool to create new Gitlab Issues',
    version='0.1.0',
    url='https://github.com/maximestevenot/gitlab-ticket-maker.git',
    author='Maxime Stevenot',
    python_requires='>=3.8.0,<4.0.0',
    author_email='maxime.stevenot@soprabanking.com',
    keywords=['gitlab', 'ticket', 'issue'],
    entry_points={
        'console_scripts': [
            'tkt = gitlab_ticket_maker.main:cli'
        ]
    }
)
