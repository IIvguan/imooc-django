#!/usr/bin/env python3.7.1
# -*- coding: utf-8 -*-
__author__ = 'Timothy'
import datetime
from .models import UserProfile


def user_to_payload(user):
    exp = datetime.datetime.now() + datetime.timedelta(seconds=3600 * 7)
    return {
        'user_id': str(user.id),
        'exp': exp
    }


def payload_to_user(payload):
    if not payload:
        return None
    user_id = payload.get('user_id')
    user = UserProfile.objects.get(user_id)
    return user
