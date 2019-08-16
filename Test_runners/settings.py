#############Don't touch!####
test_string = 'Hello World!'
howmany_test = 0
howcomplete_test = 0
result_flag = 0
work_id = 0
work_login = ''
work_address = ''
work_pass = ''
work_name = ''
key = 'all'
debug_toggle = True
close_browser = True
############################Should touch!############
file_str = "string_temp.txt"

hand_test_run = "src\\AutoTests\\Test_runners\\testrun_4.json"
hand_test = True
restart_toggle = False

testrun_id = 1

test_suite = [
    {
        "enable_flag":  True,
        "host_login": 'https://10.100.10.248',
        "host_agent_address": 1,
        "login_name": "admin",
        "login_pass": "Passw0rd12"
    },
    {
        "enable_flag":  False,
        "host_login": 'https://10.100.10.248',
        "host_agent_address": 13,
        "login_name": "admin",
        "login_pass": "Passw0rd12"
    },
    {
        "enable_flag":  False,
        "host_login": 'https://10.100.10.240',
        "host_agent_address": 1,
        "login_name": "adminSept",
        "login_pass": "123qwe"
    }
]

