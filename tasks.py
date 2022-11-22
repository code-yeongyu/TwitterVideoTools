# pyright: reportUnknownMemberType=false

import toml
from colorama import Fore
from colorama import init as init_colorama
from invoke import Context, task
from invoke.exceptions import UnexpectedExit

import monkey_patch_invoke as _


@task
def check_code_style(context: Context) -> None:
    """Runs static analysis."""
    PROJECT_PATH = 'twitter_video_tools'
    init_colorama()

    print(f'{Fore.MAGENTA}==========Check Code Styles with `yapf`=========={Fore.RESET}')
    context.run(f'yapf --diff --recursive --parallel {PROJECT_PATH}', pty=True)
    print(f'{Fore.GREEN}Yapf: Success{Fore.RESET}')

    print(f'\n{Fore.MAGENTA}==========Check Code Styles with `pylint`=========={Fore.GREEN}')
    context.run(f'pylint {PROJECT_PATH}', pty=True)


@task
def check_types(context: Context) -> None:
    """Runs static analysis."""
    PROJECT_PATH = 'twitter_video_tools'
    init_colorama()

    print(f'{Fore.CYAN}==========Check typings with `pyright`=========={Fore.RESET}')
    context.run(f'pyright {PROJECT_PATH}', pty=True)

    print(f'\n{Fore.CYAN}==========Check typings with `mypy`=========={Fore.RESET}')
    context.run(f'mypy {PROJECT_PATH}', pty=True)


@task
def test(context: Context) -> None:
    """Run tests."""
    context.run('pytest . --cov=. --cov-report=xml', pty=True)


@task
def release(context: Context, version: str) -> None:
    """Build & Publish to PyPI."""

    # load pyproject
    pyproject_path = 'pyproject.toml'
    pyproject_string = ''
    with open(pyproject_path, 'r', encoding='utf-8') as pyproject_file:
        pyproject_string = pyproject_file.read()
    pyproject = toml.loads(pyproject_string)
    # change version to today datetime
    pyproject['tool']['poetry']['version'] = version
    with open(pyproject_path, 'w', encoding='utf-8') as pyproject_file:
        toml.dump(pyproject, pyproject_file)

    # build & publish
    try:
        context.run(
            '''
                poetry build --no-interaction
                poetry publish --no-interaction
            ''',
            pty=True,
        )
    except UnexpectedExit as exception:
        with open(pyproject_path, 'w', encoding='utf-8') as pyproject_file:
            pyproject_file.write(pyproject_string)
        raise exception from exception

    # recover to original
    with open(pyproject_path, 'w', encoding='utf-8') as pyproject_file:
        pyproject_file.write(pyproject_string)
