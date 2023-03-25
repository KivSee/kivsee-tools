import random
from opentelemetry import context
from contextlib import contextmanager

energy_key = context.create_key('kivsee.energy')

def _verify_energy_value(value: float):
    if value < 0 or value > 1.0:
        raise ValueError(f'energy level should be in range [0.0, 1.0], got {value}')

def _create_energy_context(value: float):
    _verify_energy_value(value)
    return context.set_value(energy_key, value, context.get_current())

def set_energy(energy_value: float):
    """
    set the current energy for code executed after this call.
    set energy will remain in effect until overwriten by some other energy.

    Example:
        set_energy(0.5)
        print(get_energy()) # 0.5
        set_energy(0.25)
        print(get_energy()) # 0.25

    Args:
        energy_value: value in range [0.0, 1.0] where 0.0 means no energy and 1.0 means max energy.
            components can examine the current energy to configure visualizations
    """
    return context.attach(_create_energy_context(energy_value))

def get_energy(value_if_missing: float = random.random()) -> float:
    """
    return the current energy as set to this scope by the user.

    Example:
        set_energy(0.5)
        print(get_energy()) # 0.5
        set_energy(0.25)
        print(get_energy()) # 0.25

    Args:
        value_if_missing: value to return if there is no active energy set.
            if not supplied, defaults to random

    Returns:
        the current energy, param value if missing, or random.
        function is guarentted to return valid energy value

    """
    energy = context.get_value(energy_key)
    if energy is not None:
        return energy
    else:
        _verify_energy_value(value_if_missing)
        return value_if_missing

@contextmanager
def use_energy(energy_value: float):
    """
    set the current energy in a "with" scope, 
    and restore the value when scope ends

    Example:
        set_energy(0.75)
        print(get_energy()) # 0.75
        with use_energy(0.25):
            print(get_energy()) # 0.25
        print(get_energy()) # 0.75

    Args:
        energy_value: value in range [0.0, 1.0] where 0.0 means no energy and 1.0 means max energy.
            components can examine the current energy to configure visualizations
    """
    token = set_energy(energy_value)
    try:
        yield
    finally:
        context.detach(token)