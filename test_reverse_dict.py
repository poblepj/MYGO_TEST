import reverse_dict

input_value = {
    'hired': {
        'be': {
            'to': {
                'deserve': 'I'
            }
        }
    }
}


def test_01_spread_dict_val_to_list():
    record_list = []
    reverse_dict.spread_dict_val_to_list(input_value, record_list)
    spread_dict_should_be = ['hired', 'be', 'to', 'deserve', 'I']
    assert record_list == spread_dict_should_be


def test_02_list_to_nested_dict():
    spread_dict = ['hired', 'be', 'to', 'deserve', 'I']
    reverse_obj = reverse_dict.list_to_nested_dict(spread_dict)
    reverse_obj_should_be = {'I': {'deserve': {'to': {'be': {'be': 'hired'}}}}}
    assert reverse_obj == reverse_obj_should_be


def test_03_reverse_dict():
    reverse_input_dict_should_be = {'I': {'deserve': {'to': {'be': {'be': 'hired'}}}}}
    reverse_input_dict = reverse_dict.reverse_input_dict(input_value)
    assert reverse_input_dict ==  reverse_input_dict_should_be

    

