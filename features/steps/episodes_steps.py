from behave import given, when, then
import requests

API_BASE_URL = "https://api.jikan.moe/v4"


import time

@given("the Episodes API is available")
def step_given_episodes_api_available(context):
    response = requests.get(f"{API_BASE_URL}/anime/966/episodes")
    assert response.status_code == 200
    time.sleep(1)  # evita rate limiting

@when("I request episodes with anime ID {anime_id:d}")
def step_when_request_episodes(context, anime_id):
    time.sleep(0.5)
    context.response = requests.get(f"{API_BASE_URL}/anime/{anime_id}/episodes")

@when("I request episode 1")
def step_when_request_episode_1(context):
    time.sleep(0.5)
    context.response = requests.get(f"{API_BASE_URL}/anime/966/episodes/1")

@then("the episode fields should match:")
def step_then_episode_fields(context):
    data = context.response.json()["data"]
    for row in context.table:
        field = row["fields"]
        expected = row["value"]
        actual_value = data.get(field)
        assert str(actual_value) == str(expected), (
            f"Field '{field}': expected '{expected}' but got '{actual_value}'"
        )


@then("the episode should not be filler")
def step_then_episode_not_filler(context):
    data = context.response.json()["data"]
    assert data["filler"] == False, "Expected episode to not be filler"