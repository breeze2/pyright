# This sample tests type var matching for constrained type vars.

import pathlib
import shutil
from typing import AnyStr, Sequence, TypeVar, Union


class Foo:
    pass


class Bar(Foo):
    pass


T1 = TypeVar("T1", Foo, str)
T2 = TypeVar("T2", bound=Foo)


def test1(x: T1) -> T1:
    return x


def test2(x: T2) -> T2:
    return x


# This should generate an error because test1(Bar())
# should evaluate to type Foo, not Bar.
aa1: Bar = test1(Bar())

aa2: Foo = test1(Bar())

bb1: Bar = test2(Bar())

bb2: Foo = test2(Bar())


# The call to rmtree should not generate any errors.
data_dir = pathlib.Path("/tmp")
archive_path = data_dir / "hello"
shutil.rmtree(archive_path)


def func1(a: AnyStr, b: AnyStr) -> None:
    ...


def func2(a: Union[str, bytes], b: Union[str, bytes]):
    # This should generate two errors
    func1(a, b)


class A:
    ...


class B:
    ...


class C:
    ...


class D:
    ...


T3 = TypeVar("T3", A, B, Union[C, D])


def do_something(value: T3) -> T3:
    ...


def func10(value: Union[C, D]):
    value1 = do_something(value)


def func11(value: D):
    value1 = do_something(value)


def func12(value: Union[A, B]):
    # This should generate an error because A and B
    # map to different constraints.
    value1 = do_something(value)


def func13(value: Union[A, D]):
    # This should generate an error because A and D
    # map to different constraints.
    value1 = do_something(value)
