def shrink(signal, element):
    """
    Shrinks the foreground of a binary 1d signal using element

    Args:
        signal: a list of 1s and 0s
        element: a list of 1s and 0s

    Returns:
        shrunken signal

    #Raises:
        #ValueError: If size is less than or equal to 2

    """
    if len(signal) <= 2:
        raise ValueError

    shrunken = []

    for index in range(0, len(signal)):
        el_len = len(element)

        while index+el_len > len(signal):  # prevent out of range error
            el_len -= 1
        if signal[index:index+el_len] == element:
            shrunken.append(1)
        elif index == len(signal) - 1:  # if last index matches element
            if signal[index] == element[0]:
                shrunken.append(1)
        else:
            shrunken.append(0)

    return shrunken


def expand(signal, element):
    """
    Expands the foreground of a binary 1d signal using element

    Args:
        signal: a list of 1s and 0s
        element: a list of 1s and 0s

    Returns:
        shrunken signal

    #Raises:
        #ValueError: If size is less than or equal to 2

    """
    if len(signal) <= 2:
        raise ValueError

    expanded = []
    for index in range(0, len(signal)):
        if index == len(signal) - 1:  # if last index matches element
            if signal[index] == element[0]:
                expanded.append(1)

        else:
            el_len = len(element)
            while index + el_len > len(signal):  # prevent out of range error
                el_len -= 1

            sublist = signal[index:index+el_len]  # sublist of chars to compare

            if sublist == element:
                expanded.append(1)
            else:  # check if any chars match
                for x in range(0, len(sublist)):
                    if sublist[x] == element[x]:
                        expanded.append(1)
                        break  # break loop if any chars match
                    else:  # if last char, append 0
                        if x == len(sublist) - 1:
                            expanded.append(0)

    return expanded


def denoise(signal, element):
    """
    Shrinks then expands the foreground of a binary 1d signal using element

    Args:
        signal: a list of 1s and 0s
        element: a list of 1s and 0s

    Returns:
        denoised signal

    """
    signal = shrink(signal, element)
    signal = expand(signal, element)
    return signal
