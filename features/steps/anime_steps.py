from behave import given, when, then
import requests

API_BASE_URL = "https://api.jikan.moe/v4"


@given("the Shinchan API is available")
def step_given_api_available(context):
    response = requests.get(f"{API_BASE_URL}/anime/966")
    assert response.status_code == 200


@when("I request the anime with ID {anime_id:d}")
def step_when_request_anime(context, anime_id):
    context.response = requests.get(f"{API_BASE_URL}/anime/{anime_id}/full")


@then("the response should contain the fields:")
def step_then_contains_fields(context):
    data = context.response.json()["data"]
    for row in context.table:
        field = row["field"]
        assert field in data, f"Field '{field}' not found"


@then('the genres should contain "{expected_genre}"')
def step_then_genres_contain(context, expected_genre):
    data = context.response.json()["data"]
    genre_names = [g["name"] for g in data["genres"]]
    assert expected_genre in genre_names, (
        f"Expected '{expected_genre}' in {genre_names}"
    )


@then('the studios should contain "{expected_studio}"')
def step_then_studios_contain(context, expected_studio):
    data = context.response.json()["data"]
    studio_names = [s["name"] for s in data["studios"]]
    assert expected_studio in studio_names, (
        f"Expected '{expected_studio}' in {studio_names}"
    )