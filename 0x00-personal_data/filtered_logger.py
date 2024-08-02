#!/usr/bin/env python3
"""
Filter model
"""
import re


def filter_datum(fields, redaction, message, separator):
    pat = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pat, lambda match: f"{match.group(1)}={redaction}", message)
