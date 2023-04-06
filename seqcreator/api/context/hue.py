import random
from opentelemetry import context
from contextlib import contextmanager
from typing import Tuple

primary_hue_key = context.create_key('kivsee.primary_hue')
secondary_hue_key = context.create_key('kivsee.secondary_hue')

def set_hues(primary_hue: float, secondary_hue: float):
    """
    set both primary and secondary hues for code executed after this call.
    set hues will remain in effect until overwriten by some other hues.

    Example:
        set_hues(0.5, 0.6)

    Args:
        primary_hue: any float value that represents the primary hue to use in effects
        secondary_hue: any float value that represents the secondary hue to use in effects
    """
    primary_hue_context = context.set_value(primary_hue_key, primary_hue)
    both_hues_context = context.set_value(secondary_hue_key, secondary_hue, primary_hue_context)
    print(both_hues_context)
    return context.attach(both_hues_context)

def set_primary_hue(primary_hue: float):
    """
    set primary hue for code executed after this call.
    set primary hue will remain in effect until overwriten by some other primary hue.
    secondary hue is not affected

    Example:
        set_primary_hue(0.33)

    Args:
        primary_hue: any float value that represents the primary hue to use in effects
    """
    return context.attach(context.set_value(primary_hue_key, primary_hue))

def set_secondary_hue(secondary_hue: float):
    """
    set secondary hue for code executed after this call.
    set secondary hue will remain in effect until overwriten by some other secondary hue.
    primary hue is not affected

    Example:
        set_secondary_hue(0.66)

    Args:
        secondary_hue: any float value that represents the secondary hue to use in effects
    """
    return context.attach(context.set_value(secondary_hue_key, secondary_hue))

def get_hues(primary_if_missing: float = None, secondary_if_missing: float = None) -> Tuple[float]:
    """
    return the current primary and secondary hues as set to this scope by the user.

    Example:
        set_hues(0.5, 0.6)
        print(get_hues()) # [0.5, 0.6]
        set_primary_hue(0.25)
        print(get_hues()) # [0.25, 0.6]

    Args:
        primary_if_missing: value to return for primary hue if there is no active primary hue set.
        secondary_if_missing: value to return for secondary hue if there is no active secondary hue set.

    Returns:
        the current secondary hue, or param value if missing.
        function returns None if secondary hue is not set in context or as default

    Returns:
        a list with 2 elements: primary hue in index 0 and secondary hue in index 1
        any of those numbers might be None to indicate they were not set as context and no fallback supplied

    """
    primary_hue = context.get_value(primary_hue_key)
    primary_hue = primary_hue if primary_hue is not None else primary_if_missing

    secondary_hue = context.get_value(secondary_hue_key)
    secondary_hue = secondary_hue if secondary_hue is not None else secondary_if_missing

    return (primary_hue, secondary_hue)

def get_primary_hue(value_if_missing: float = random.random()) -> float:
    """
    return the current primary hue as set to this scope by the user.

    Example:
        set_primary_hue(0.5)
        print(get_primary_hue()) # 0.5
        set_hues(0.25, 0.75)
        print(get_primary_hue()) # 0.25

    Args:
        value_if_missing: value to return if there is no active primary hue set.

    Returns:
        the current primary hue, or param value if missing.
        function returns None if primary hue is not set in context or as default

    """
    primary_hue = context.get_value(primary_hue_key)
    if primary_hue is not None:
        return primary_hue
    else:
        return value_if_missing

def get_secondary_hue(value_if_missing: float) -> float:
    """
    return the current secondary hue as set to this scope by the user.

    Example:
        set_secondary_hue(0.5)
        print(get_secondary_hue()) # 0.5
        set_hues(0.25, 0.75)
        print(get_secondary_hue()) # 0.75

    Args:
        value_if_missing: value to return if there is no active secondary hue set.

    Returns:
        the current secondary hue, or param value if missing.
        function returns None if secondary hue is not set in context or as default

    """
    secondary_hue = context.get_value(secondary_hue_key)
    if secondary_hue is not None:
        return secondary_hue
    else:
        return value_if_missing

@contextmanager
def use_hues(primary_hue_value: float, secondary_hue_value: float):
    """
    set both the primary and secondary hues in a "with" scope, 
    and restore the values when scope ends

    Example:
        set_hues(0.1, 0.2)
        print(get_hues()) # [0.1, 0.2]
        with use_hues(0.3, 0.4):
            print(get_hues()) # [0.3, 0.4]
        print(get_hues()) # [0.1, 0.2]

    Args:
        primary_hue_value: primary hue for effects started in this scope
        secondary_hue_value: secondary hue for effects started in this scope
    """
    token = set_hues(primary_hue_value, secondary_hue_value)
    try:
        yield
    finally:
        context.detach(token)

@contextmanager
def use_primary_hue(primary_hue_value: float):
    """
    set the current primary hue in a "with" scope, 
    and restore the value when scope ends

    Example:
        set_primary_hue(0.75)
        print(get_primary_hue()) # 0.75
        with use_primary_hue(0.25):
            print(get_primary_hue()) # 0.25
        print(get_primary_hue()) # 0.75

    Args:
        primary_hue_value: primary hue for effects started in this scope
    """
    token = set_primary_hue(primary_hue_value)
    try:
        yield
    finally:
        context.detach(token)

@contextmanager
def use_secondary_hue(secondary_hue_value: float):
    """
    set the current secondary hue in a "with" scope, 
    and restore the value when scope ends

    Example:
        set_secondary_hue(0.75)
        print(get_secondary_hue()) # 0.75
        with use_primary_hue(0.25):
            print(get_secondary_hue()) # 0.25
        print(get_secondary_hue()) # 0.75

    Args:
        secondary_hue_value: secondary hue for effects started in this scope
    """
    token = set_secondary_hue(secondary_hue_value)
    try:
        yield
    finally:
        context.detach(token)