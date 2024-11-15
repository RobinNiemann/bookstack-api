def get_filter_str(filter):

    operator_str = ''

    if len(filter.get_operator()) > 0:
        operator_str = ':' + filter.get_operator()

    filter_str = 'filter' + '[' + filter.get_key() + operator_str + ']=' + filter.get_value()

    return filter_str


def create_url_parameters_string(count=0, offset=0, sort=None, filters=[]):

    parameter_list=[]

    if count > 0:
        count_str = 'count=' + str(count)
        parameter_list.append(count_str)
    if offset > 0:
        offset_str = 'offset=' + str(offset)
        parameter_list.append(offset_str)
    if sort is not None:
        sort_str = 'sort=' + str(sort)
        parameter_list.append(sort_str)
    if len(filters) > 0:
        for el in filters:
            filter_str = get_filter_str(el)
            parameter_list.append(filter_str)

    parameter_str = ''

    if len(parameter_list) >= 1:
        parameter_str = parameter_list[0]
    if len(parameter_list) > 1:
        for el in parameter_list[1:]:
            parameter_str += '&' + el
    
    return parameter_str
    
