from behave import then

@then("the response status code should be {expected_status:d}")
def step_then_status_code(context, expected_status):
    assert context.response.status_code == expected_status, (
        f"Expected {expected_status} but got {context.response.status_code}"
    )