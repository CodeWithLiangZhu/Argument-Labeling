from itertools import combinations


# Setting variables
arguments = set()
framework = {}
relations = set()
argumentslabelling = dict(zip(arguments, ''))
argumentslabel = dict(zip(arguments, ''))


# Determining whether arg is the attacker
def is_attacker(arg):
    for x in relations:
        if x[0] == arg:
            return True
    return False


# Determining whether arg is the attacked
def is_attacked(arg):
    for x in relations:
        if x[1] == arg:
            return True
    return False


# Return all attackers that attacked arg
def get_arg_attackers(arg):
    attackers = []
    for i in relations:
        if i[1] == arg:
            attackers.append(i[0])
    return(set(attackers))


# Return all attackees attacked by arg
# def get_arg_attackeds(arg):
#     return list(framework[arg])


# Determining whether arg is labeled 'in'
def is_in(arg):

    # If arg is not attacked, it is labeled 'in'
    if is_attacked(arg) == False:
        return True

    # If all attackers attacking arg are labeled 'out', arg is labeled 'in'
    attackers = list(get_arg_attackers(arg))
    for i in attackers:
        if argumentslabelling[i] != 'out':
            return False
    return True


# Determining whether arg is labeled 'out'
def is_out(arg):
    # If one of the attackers attacking arg is labeled "in", arg is labeled "out"
    attackers = list(get_arg_attackers(arg))
    for i in attackers:
        if argumentslabelling[i] == 'in':
            return True
    return False


# Determining whether arg is labeled 'undec'
def is_undec(arg):
    # If none attackers attacking arg are labeled 'in',
    # If one of the attackers attacking arg is not labeled "out",
    # then arg is labeled 'undec'.
    attackers = list(get_arg_attackers(arg))
    x = 0
    for i in attackers:
        if argumentslabelling[i] == 'in':
            x = 1
            return False
    if x != 1:
        for i in attackers:
            if argumentslabelling[i] != 'out':
                return True
        return False


def powerset(args):
    # Get a list of all possible combinations of args
    base_list = list(args)
    combo_list = [combinations(base_list, r) for r in range(len(args)+1)]

    # Transform data types to set
    powerset = set([])
    for l in combo_list:
        set_of_combo_list = map(frozenset, l)
        powerset = powerset.union(set_of_combo_list)
    return powerset


def generateLabelling(args):
    # Generating label sets
    output = []
    for ina in powerset(args):
        for outa in powerset(args-ina):
            output.append([ina, outa, (args-ina)-outa])
    return output


def labelling():
    output = []
    # Algorithm extensions
    for [ina, outa, undeca] in generateLabelling(arguments):
        i = 0
        # Initialising label sets
        for x in ina:
            argumentslabelling[x] = 'in'
        for x in outa:
            argumentslabelling[x] = 'out'
        for x in undeca:
            argumentslabelling[x] = 'undec'
        # Determine if a label in the label set 'in' is establish,
        # if true then labeled 'in', if false then break
        for x in ina:
            if is_in(x) == False:
                i = 1
                break
            else:
                argumentslabel[x] = 'in'
        # Continue to judge
        if i == 1:
            continue
        # Determine if a label in the label set 'out' is establish,
        # if true then labeled 'out', if false then break
        for x in outa:
            if is_out(x) == False:
                i = 1
                break
            else:
                argumentslabel[x] = 'out'
        # Continue to judge
        if i == 1:
            continue
        # Determine if a label in the label set 'undec' is establish,
        # if true then labeled 'undec', if false then break
        for x in undeca:
            if is_undec(x) == False:
                i = 1
                break
            else:
                argumentslabel[x] = 'undec'
        # Get the set of label that match the algorithm extensions
        if i == 0:
            output.append([ina, outa, undeca])
    return output


def compute_completed_labelling():
    completed = []

    # Get all the label sets containing labeled 'in' or 'undec'
    for x in labelling():
        if len(x[0]) != 0 or len(x[2]) != 0:
            completed.append(x)
    return completed


def compute_grounded_labelling():
    grounded = []

    # Get the label sets that containing the most labeled 'undec'
    maxundec = len(labelling()[0][2])
    for x in labelling():
        if maxundec <= len(x[2]):
            maxundec = len(x[2])
    for x in labelling():
        if len(x[2]) == maxundec:
            grounded.append(x)
    return grounded


def compute_preferred_labelling():
    preferred = []

    # Sort all label sets by label 'in', from most to least
    sort = [labelling()[0]]
    for x in labelling()[1::]:
        for y in range(len(sort)):
            if len(x[0]) >= len(sort[y][0]):
                sort.insert(y, x)
                break
            elif len(x[0]) < len(sort[len(sort)-y-1][0]):
                sort.insert(len(sort)-y, x)
                break

    # Get all the label sets containing the maximum labeled 'in'
    inlabel = set()
    if sort[0][0] == set():
        preferred.append(sort[0])
    else:
        for x in sort:
            difference = x[0]
            difference -= inlabel
            if difference != set():
                preferred.append(x)
                inlabel.update(x[0])
    return preferred


def compute_stable_labelling():
    stable = []

    # Get all label sets that do not containing labeled 'undec'
    for x in labelling():
        if len(x[2]) == 0:
            stable.append(x)
    return stable


def compute_semistable_labelling():
    semistable = []

    # Get all label sets containing the minimum labeled "undec"
    minundec = len(labelling()[0][2])
    for x in labelling():
        if minundec >= len(x[2]):
            minundec = len(x[2])
    for x in labelling():
        if len(x[2]) <= minundec:
            semistable.append(x)
    return semistable
