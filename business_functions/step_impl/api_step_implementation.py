from getgauge.python import step
from framework.actions.api.rest_actions import RestActions

rest_action=None

@step("Get the personal detail")
def get_the_personal_detail():
    global rest_action
    rest_action=RestActions()
    rest_action.get_request(url="https://reqres.in/api/users?page=2")
    print(rest_action.status_code)
    all_data=rest_action.ret_json['data']
    new_employee_list=[]
    for data in all_data:
        print(data)
        emp_id=data.get('id')
        email=data.get('email')
        if emp_id is not None and email is not None:
            employee_tuple=(emp_id,email)
        else:
            print("Missing id or email---",data)
        
        new_employee_list.append(employee_tuple)
    print(new_employee_list)

    

@step("Validate response code <status_code>")
def validate_response_code(status_code):
    print(rest_action.status_code)
    assert rest_action.status_code==int(status_code)
