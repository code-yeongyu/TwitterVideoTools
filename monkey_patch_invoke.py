# type: ignore
# pylint: disable=unused-argument
import inspect
import types
from typing import Callable, Union

from invoke.tasks import NO_DEFAULT, Task


def monkey_patch_invoke() -> None:

    def patched_argspec(self: Task, body: Callable) -> tuple[list[str], dict[str, object]]:
        """
        A monkey patching code for supporting python3
        from: https://github.com/pyinvoke/invoke/issues/357#issuecomment-1250744013
        """
        func: Union[Callable,
                    types.MethodWrapperType] = body if isinstance(body, types.FunctionType) else body.__call__
        sig = inspect.signature(func)
        arg_names = [k for k, _ in sig.parameters.items()]
        spec_dict: dict[str, object] = {}
        for key, value in sig.parameters.items():
            value = value.default if not value.default == sig.empty else NO_DEFAULT
            spec_dict.update({key: value})
        # Pop context argument
        try:
            context_arg = arg_names.pop(0)
        except IndexError as error:
            raise TypeError('Tasks must have an initial Context argument!') from error
        del spec_dict[context_arg]
        return arg_names, spec_dict

    Task.argspec = types.MethodType(patched_argspec, Task)


monkey_patch_invoke()
