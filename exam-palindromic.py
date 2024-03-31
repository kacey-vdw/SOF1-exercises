def longest_palindromic_numbers(number):
    """
        Returns set of longest palindromic numbers within number

        Args:
            number: string of nums to find palindromes in

        Returns:
            Returns set of palindromic nums

        """
    palindromes = set()

    if number != "0" and len(number) > 1:  # if begins with 0s and not 0,remove
        if number[0] == "0":
            number = str(int(number))

    if number == "".join((reversed(number))):  # if palindrome, return
        palindromes.add(number)
    else:
        if len(number) > 2:  # repeat for sublists, minus 1st and last char
            palindromes = \
                (palindromes.union(longest_palindromic_numbers(number[1:])))
            palindromes = \
                (palindromes.union(longest_palindromic_numbers(number[0:-1])))
        elif len(number) == 2:  # repeat for sublists, separate 2 chars
            palindromes = \
                (palindromes.union(longest_palindromic_numbers(number[0])))
            palindromes = \
                (palindromes.union(longest_palindromic_numbers(number[1])))

    to_remove = []
    for item1 in palindromes:  # finds all lesser palindromes
        for item2 in palindromes:
            if item1 == item2:
                continue
            else:  # removes sub-palindromes or smaller palindromes
                if item1 in item2 or len(item1) < len(item2):
                    to_remove.append(item1)
                elif item2 in item1 or len(item2) < len(item1):
                    to_remove.append(item2)

    for item in to_remove:  # removes all lesser palindromes
        palindromes.discard(item)

    return palindromes
