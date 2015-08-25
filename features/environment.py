# -*- coding: utf-8 -*-


def before_all(context):
    """
    Setting up the values for use in the scenarios.
    :param context:
    """
    context.conf = {
        'client_id': context.config.userdata.get('client_id', 1),
        'client_name': context.config.userdata.get(
            'client_name', 'New Customer')
    }
