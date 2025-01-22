from getgauge.python import step
from framework.actions.api.rest_actions import RestActions


@step("Validate response code <status_code>")
def validate_response_code(status_code):
    print(rest_action.status_code)
    assert rest_action.status_code==int(status_code)

@step("Get the poetry db details")
def get_the_poetry_db_details():
    global rest_action
    rest_action=RestActions()
    rest_action.get_request(url="https://poetrydb.org/title/Ozymandias/lines.json")
    print(rest_action.status_code)

@step("Validate input vs output json response")
def validate_input_vs_output_json_response():
    expected_output_json=[
    {
    "lines": [
      "I met a traveller from an antique land",
      "Who said: Two vast and trunkless legs of stone",
      "Stand in the desert...Near them, on the sand,",
      "Half sunk, a shattered visage lies, whose frown,",
      "And wrinkled lip, and sneer of cold command,",
      "Tell that its sculptor well those passions read",
      "Which yet survive, stamped on these lifeless things,",
      "The hand that mocked them, and the heart that fed:",
      "And on the pedestal these words appear:",
      "'My name is Ozymandias, king of kings:",
      "Look on my works, ye Mighty, and despair!'",
      "Nothing beside remains. Round the decay",
      "Of that colossal wreck, boundless and bare",
      "The lone and level sands stretch far away."
    ]
     }
    ]
    actual_json=rest_action.ret_json
    assert expected_output_json==actual_json
