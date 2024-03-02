from getgauge.python import step
from framework.actions.api.rest_actions import RestActions

rest_action=None

@step("Get the weather")
def get_the_weather():
    global rest_action
    rest_action=RestActions()
    rest_action.get_request(url="https://reqres.in/api/users?page=2")
    print(rest_action.status_code)
   # print(rest_action.ret_json)
    all_data=rest_action.ret_json['data']
    test_id={}
    for data in all_data:
        print(data)
        test_id.(data.get('id'),data.get('email'))
    print(test_id)

@step("Validate response code <status_code>")
def validate_response_code(status_code):
    print(rest_action.status_code)
    assert rest_action.status_code==int(status_code)
