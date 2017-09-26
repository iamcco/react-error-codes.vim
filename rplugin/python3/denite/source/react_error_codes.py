# ============================================================================
# FILE: react_error_codes.py
# AUTHOR: 年糕小豆汤 <ooiss@qq.com>
# License: MIT license
# codes: https://github.com/facebook/react/blob/master/scripts/error-codes/codes.json
# code 22 document: https://facebook.github.io/react/docs/error-decoder.html?invariant=22
# ============================================================================

import os

import webbrowser

from ..kind.base import Base as BaseKind

from .base import Base

# 脚本所在目录绝对路径
CURRENT_SCRIPT_PATH_DIRNAME = os.path.dirname(os.path.abspath(__file__))

# react error code 的文档路径
CODE_DOCUMENT_URI = 'https://facebook.github.io/react/docs/error-decoder.html?invariant=%s'

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'react_error_codes'
        self.matchers = ['matcher_regexp']
        self.sorters = []
        self.kind = Kind(vim)

    def on_init(self, context):
        context['codes'] = [{'word': line.strip(),
                            'source__code': line.split(':')[0]}
                for line in open(os.path.join(CURRENT_SCRIPT_PATH_DIRNAME, 'codes.dat'), 'r')]

    def gather_candidates(self, context):
        return context['codes']

class Kind(BaseKind):
    def __init__(self, vim):
        super().__init__(vim)

        self.default_action = 'open'
        self.persist_actions += ['open']
        self.redraw_actions += ['open']
        self.name = 'react_error_codes'

    def action_open(self, context):
        webbrowser.open(CODE_DOCUMENT_URI % context['targets'][0]['source__code'])
