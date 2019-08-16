from testrail import *
import json

client = APIClient('http://10.100.10.245/TestRail/')
client.user = 'sild225@mail.ru'
client.password = '123qwe'

project = '1'
run = '1'
#json_data=open('./testsuite.json').read()
#data = json.loads(json_data)

json_data = open('./testrun.json').read()
data = json.loads(json_data)

def add_testsuite(project_id):
    client.send_post('add_suite/' + project_id, data)
def update_run(run_id):
    client.send_post('update_run/'+run_id, data)

def add_resault(run_id):
    client.send_post('add_results_for_cases/'+run_id, data)
#add_testsuite(project)
add_resault(run)
