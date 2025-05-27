# Mock vulnerability rules for demo purposes
MOCK_RULES = [
    {
        'name': 'Hardcoded Secret',
        'pattern': 'SECRET_KEY=',
        'desc': 'Possible hardcoded secret detected.'
    },
    {
        'name': 'Insecure Function',
        'pattern': 'eval(',
        'desc': 'Use of insecure eval() function.'
    },
    {
        'name': 'Weak Hash',
        'pattern': 'md5(',
        'desc': 'Use of weak hash function md5.'
    },
]
