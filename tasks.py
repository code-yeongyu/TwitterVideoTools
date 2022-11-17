from invoke import Context, task

import monkey_patch_invoke as _


@task
def test(context: Context) -> None:
    """Run tests."""
    context.run('pytest . ', pty=True)


@task
def publish(context: Context) -> None:
    """Publish to PyPI."""
    context.run('poetry publish --build', pty=True)
