# ============================================================================
# FILE: react_error_codes.py
# AUTHOR: 年糕小豆汤 <ooiss@qq.com>
# License: MIT license
# codes: https://github.com/facebook/react/blob/master/scripts/error-codes/codes.json
# code 22 document: https://facebook.github.io/react/docs/error-decoder.html?invariant=22
# ============================================================================

import os

from .base import Base

CURRENT_SCRIPT_PATH_DIRNAME = os.path.dirname(os.path.abspath(__file__))


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'react_error_codes'
        self.kind = 'file'
        self.matchers = ['matcher_regexp']
        self.sorters = []

    def on_init(self, context):
        context['codes'] = [{'word': line.strip()}
                for line in open(os.path.join(CURRENT_SCRIPT_PATH_DIRNAME, 'codes.dat'), 'r')]

    def gather_candidates(self, context):
        return context['codes']
