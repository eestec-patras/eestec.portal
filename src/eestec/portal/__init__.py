# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('eestec.portal')

LC_MEMBERS_GROUP_SUFFIX = '-members'
LC_BOARD_GROUP_SUFFIX = '-board'
LC_NOTIFICATIONS_GROUP_SUFFIX = '-notifications'


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
