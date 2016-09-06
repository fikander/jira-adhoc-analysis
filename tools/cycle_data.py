import getpass
from jira import JIRA
from jira_cycle_extract import cycletime, config

def get_jira_client(connection, verbose=False):
    url = connection['domain']

    token = connection['token']
    if token:
        username, password = base64.b64decode(token).decode('utf-8').split(':')
    else:
        username = connection['username']
        password = connection['password']

    if verbose:
        print("Connecting to {url} as {username}".format(url=url, username=username))

    if username and username != '__none__':
        return JIRA({'server': url}, basic_auth=(username, password))
    else:
        return JIRA({'server': url})


def calc_cycle_data(config_yaml, verbose=False):
    # Parse options
    options = config.config_to_options(config_yaml)

    # Connect to JIRA
    # Get domain and credentials if not specified via environemnt variables (would have been picked by config_to_options)
    connection = options['connection']
    if not connection.get('domain', None):
        print("JIRA domain (e.g. http://mycompany.atlassian.net)")
        connection['domain'] = input()
    if not connection.get('token'):
        if not connection.get('username', None):
            print('JIRA username:')
            connection['username'] = input()
        if not connection.get('password', None):
            print('JIRA password:')
            connection['password'] = getpass.getpass()
    jira = get_jira_client(connection, verbose=verbose)

    # Fetch issues and calculate cycle data as a Pandas DataFrame
    q = cycletime.CycleTimeQueries(jira, **options['settings'])
    cycle_data = q.cycle_data(verbose=verbose)
    return q, cycle_data
