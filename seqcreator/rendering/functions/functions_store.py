
def linear_function(start, end):
    return {
        "linear": {
            "start": start,
            "end": end,
        }
    }


def const_function(val):
    return {
        "const_value": {
            "value": val,
        }
    }


def sin_function(sin_min, sin_max, phase, repeats):
    return {
        "sin": {
            "min": sin_min,
            "max": sin_max,
            "phase": phase,
            "repeats": repeats,
        }
    }


def steps_function(num_steps,
                   diff_per_step,
                   first_step_value):
    return {
        "steps": {
            "num_steps": num_steps,
            "diff_per_step": diff_per_step,
            "first_step_value": first_step_value,
        }
    }


def repeat_function(number_of_times, function):
    return {
        "repeat": {
            "numberOfTimes": number_of_times,
            "funcToRepeat": function,
        }
    }


def half_function(f1, f2):
    return {
        "half": {
            "f1": f1,
            "f2": f2,
        }
    }


def comb2_function(f1, amount1, f2, amount2):
    return {
        "comb2": {
            "f1": f1,
            "amount1": amount1,
            "f2": f2,
            "amount2": amount2,
        }
    }