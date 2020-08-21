from PyInquirer import prompt, style_from_dict, Token, Separator
from pprint import pprint
from main import init

styling = style_from_dict({
    Token.Pointer: '#673ab7 bold',
    Token.Selected: '#54cc7a bold',
    Token.QuestionMark: '#ebd234 ',
    Token.Question: '#673ab7 bold',
    Token.Separator: '#cc5454 bold',
    Token.Instruction: ''
})

def get_options():

    deployment_options = [{
        'type': 'checkbox',
        'name': 'modules',
        'message': 'Select Deployment Modules',
        'choices': [
            Separator("=== Infra ==="),
            {
                'key': 'n',
                'name': 'NGINX',
                'value': 'nginx'
            },
            {
                'key': 'd',
                'name': 'Database',
                'value': 'db',
                'disabled': 'Currently not supported'
            },
            Separator("=== Applications ==="),
            {
                'key': 'B',
                'name': 'Backend Application',
                'value': 'backend'
            }
        ],
    }]
    answers = prompt(deployment_options, style=styling)
    return answers


def get_update_conf(answers):

    if answers.get("modules") is None:
        print("No modules has been seleted !!")
        return

    for module in answers.get("modules"):
        if module == 'nginx':
            nginx_options = [
                {
                    'type': 'input',
                    'name': 'PWD',
                    'message': 'Set the working directory of NGINX docker',
                    'default': '/usr/share/nginx/html'

                }
            ]
            ans = prompt(nginx_options, style=styling)
            init.config['NGINX']['PWD'] = ans.get('PWD')

        elif module == 'backend':
            backend_opt = [
                {
                    'type': 'input',
                    'name': 'Address',
                    'message': 'Backend App IP Address / Domain',
                    'default': 'localhost'

                },
                {
                    'type': 'input',
                    'name': 'Port',
                    'message': 'Backend App Port',
                    'default': '9000'
                },
                {
                    'type': 'input',
                    'name': 'DB',
                    'message': 'Backend App Database URL',
                    'default': 'mysql://192.168.2.1:3306/ngh_access_gateway'
                },
                {
                    'type': 'input',
                    'name': 'DBuser',
                    'message': 'Backend App Database Username',
                },
                {
                    'type': 'password',
                    'name': 'DBpass',
                    'message': 'Backend App Database Password',
                }
            ]
            ans = prompt(backend_opt, style=styling)
            init.config['APP']['ADDRESS'] = ans.get('Address')
            init.config['APP']['PORT'] = ans.get('Port')



