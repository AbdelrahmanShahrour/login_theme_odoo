# -*- coding: utf-8 -*-
{
    'name': "Login Page Theme Fullscreen",
    'summary': """
    Website portal login page fullscreen""",
    'version': '1.0.0',
    'category': 'Website',
    'description': """
    - Website portal login page
    - fullscreen background
    """,
    'author': "Abdalrahman Shahrour",
    'website': "https://www.linkedin.com/in/shahrour/",
    'license': 'LGPL-3',
    'images': ['images/loginscreen.png'],
    'depends': ['website'],
    'data': [
        'templates/website_login_page.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'login_page/static/src/css/login.css',
        ],
    },
    'installable': True,
    'application': False,
}
