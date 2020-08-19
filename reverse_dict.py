def spread_dict_val_to_list(input_dict: dict, record_list: list) -> None:
    """

    :param input_dict: the dictionary you want to spread
    :param record_list: an empty list to record all values
    :return: None
    """
    dict_key = [*input_dict]
    for item in dict_key:
        record_list.append(item)
        is_item_type_dict = type(input_dict[item]) == dict
        if is_item_type_dict:
            spread_dict_val_to_list(input_dict[item], record_list)
        else:
            record_list.append(input_dict[item])


def list_to_nested_dict(input_list: list) -> dict:
    """

    :param input_list: contains the all keys and values in dictionary
    :return: an nested dictionary
    """
    return_dict = {}

    for index, item in enumerate(input_list):

        if index == 0:
            return_dict[input_list[1]] = item
        else:

            return_dict = {
                item: return_dict
            }
    return return_dict


def reverse_input_dict(input_dict: dict) -> dict:
    """

    :param input_dict: the input_dict you want to reverse
    :return: the reversed dict
    """
    record_list = []
    spread_dict_val_to_list(input_dict, record_list)
    reverse_obj = list_to_nested_dict(record_list)
    return reverse_obj


if __name__ == '__main__':
    input_value = {
        'hired': {
            'be': {
                'to': {
                    'deserve': 'I'
                }
            }
        }
    }
    print(reverse_input_dict(input_value))

