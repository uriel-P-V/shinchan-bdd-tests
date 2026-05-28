from behave import given, when, then
import requests

API_BASE_URL = "https://api.jikan.moe/v4"


@given("the Characters API is available")
def step_given_characters_api_available(context):
    response = requests.get(f"{API_BASE_URL}/anime/966/characters")
    assert response.status_code == 200


@when("I request characters with anime ID {anime_id:d}")
def step_when_request_characters(context, anime_id):
    context.response = requests.get(f"{API_BASE_URL}/anime/{anime_id}/characters")


@then("the list of characters should contain more than 10 items")
def step_then_list_characters(context):
    data = context.response.json()["data"]
    assert len(data) > 10, f"Expected more than 10 characters but got {len(data)}"


@when("I request the character with ID {character_id:d}")
def step_when_request_character(context, character_id):
    context.response = requests.get(f"{API_BASE_URL}/characters/{character_id}/full")


@then("the character fields should match:")
def step_then_character_fields(context):
    data = context.response.json()["data"]
    for row in context.table:
        field = row["fields"]
        expected = row["value"]
        actual_value = data.get(field)
        if field == "nicknames":
            assert expected in actual_value, (
                f"Expected '{expected}' in nicknames {actual_value}"
            )
        else:
            assert str(actual_value) == str(expected), (
                f"Field '{field}': expected '{expected}' but got '{actual_value}'"
            )