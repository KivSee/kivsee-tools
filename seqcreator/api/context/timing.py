import typing
from opentelemetry import context

class KivseeTimeFrame:

    def __init__(self, start_time_ms: int, end_time_ms: int, total_units: typing.Optional[float] = None):
        """
        Args:
            start_time_ms: start time in milliseconds in the current trigger
            end_time_ms: end time in milliseconds in the current trigger
            total_units: total units in the time frame. 
                Unit is the measure of the time frame cycles which can be overlayed on top of the time frame.
                For example, if the time frame represents a song, the unit can be a beat.
                Another example, if the time frame represents a soundless animation, the unit can be a second.
                total_units will usually be integer number for most structured sequences, but it is allowed to be float.
                It can also by None, to indicate this frame has no consistent time unit and thus is not allowed to have cycles.
                By setting this property specifically, the user can correctly set integer numbers
        """
        self.start_time_ms = int(start_time_ms)
        self.end_time_ms = int(end_time_ms)
        self.total_units = total_units

class KivseeTimeFrameCycle:

    def __init__(self, units_in_cycle: float, cycle_start_rel: typing.Optional[float] = None, cycle_end_rel: typing.Optional[float] = None):
        """
        Args:
            units_in_cycle: number of units in a cycle, at same units of the time frame.
                This number corresponds to the number of units in time frame.
                For example, if current time frame is 32 beats, and units_in_cycle is 4, 
                then the cycle is 4 beats and there are 8 cycles in the time frame.
            cycle_start_rel: number in range [0.0, 1.0] indicating the relative start of the current frame in each cycle.
            cycle_end_rel: number in range [0.0, 1.0] indicating the relative end of the current frame in each cycle.
        """
        self.units_in_cycle = units_in_cycle
        self.cycle_start_rel = cycle_start_rel
        self.cycle_end_rel = cycle_end_rel

timing_key = context.create_key('kivsee.timing')
cycle_key = context.create_key('kivsee.timing.cycle')

def set_timing(time_frame: KivseeTimeFrame):
    """
    set the current time frame.
    set timing data will remain in effect until overwriten by some other timing.

    Args:
        time_frame: KivseeTimeFrmae
    """
    delete_cycle()
    c = context.set_value(timing_key, time_frame, context.get_current())
    return context.attach(c)

def get_timing() -> KivseeTimeFrame:
    """
    return the current time frame as set to this scope by the user.

    Returns:
        the current time frame
    """
    return context.get_value(timing_key)

def set_cycle(cycle: KivseeTimeFrameCycle):
    """
    set the current cycle.
    set cycle data will remain in effect until overwriten by some other cycle or when timeframe changes.

    Args:
        cycle: KivseeTimeFrameCycle
    """
    c = context.set_value(cycle_key, cycle, context.get_current())
    return context.attach(c)

def get_cycle() -> KivseeTimeFrameCycle:
    """
    return the current cycle as set to this scope by the user.

    Returns:
        the current cycle
    """
    return context.get_value(cycle_key)

def delete_cycle():
    """
    delete the current cycle.
    """
    return set_cycle(None)


