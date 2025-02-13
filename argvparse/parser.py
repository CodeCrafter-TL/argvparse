def parse(argv: list[str]) -> dict[str, str | bool]:
    """
    ### Parse argv

    * #### Examples:
    ```
    >>> argv = ["-a", "-b", "-c"]
    >>> print(parse_argv(argv))
    {'-a': True, '-b': True, '-c': True}

    >>> argv = ["-a", "a", "-b", "b"]
    >>> print(parse_argv(argv))
    {'-a': 'a', '-b': 'b'}

    >>> argv = ["-a", "-b", "c", "-d", "d"]
    >>> print(parse_argv(argv))
    {'-a': True, '-b': 'c', '-d': 'd'}
    ```
    """
    output_argv = {}
    temp_key = True
    temp_value = True

    for arg in argv[1:]:
        if arg.startswith("-"):
            if temp_key:
                output_argv[temp_key] = temp_value
            temp_key = arg
            temp_value = True
        else:
            temp_value = arg

            if temp_key:
                output_argv[temp_key] = temp_value
                temp_key = True
            else:
                output_argv[temp_value] = True

    if temp_key:
        output_argv[temp_key] = temp_value

    return output_argv
