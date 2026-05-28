from unittest.mock import patch, MagicMock

API_BASE_URL = "https://api.jikan.moe/v4"

MOCK_ANIME = {
    "mal_id": 966,
    "title": "Crayon Shin-chan",
    "score": 7.84,
    "status": "Currently Airing",
    "genres": [
        {"name": "Comedy"},
        {"name": "Ecchi"}
    ],
    "studios": [
        {"name": "Shin-Ei Animation"}
    ]
}

MOCK_CHARACTERS = [
    {
        "character": {
            "mal_id": 2951,
            "name": "Shinnosuke Nohara"
        }
    }
    for _ in range(15)
]

MOCK_CHARACTER = {
    "mal_id": 2951,
    "name": "Shinnosuke Nohara",
    "favorites": 1165,
    "nicknames": ["Shin-chan"]
}

MOCK_EPISODES = [
    {
        "mal_id": 1,
        "title": "Running an Errand / Mom's Mornings are Busy / Drawing",
        "filler": False,
        "score": 4.07
    }
]

MOCK_EPISODE_1 = {
    "mal_id": 1,
    "title": "Running an Errand / Mom's Mornings are Busy / Drawing",
    "filler": False,
    "score": 4.07
}


def unified_mock_get(url, **kwargs):
    mock = MagicMock()

    # Health check — anime available
    if url == f"{API_BASE_URL}/anime/966":
        mock.status_code = 200
        mock.json.return_value = {"data": MOCK_ANIME}

    # Anime full details
    elif url == f"{API_BASE_URL}/anime/966/full":
        mock.status_code = 200
        mock.json.return_value = {"data": MOCK_ANIME}

    # Characters list — health check and list request
    elif url == f"{API_BASE_URL}/anime/966/characters":
        mock.status_code = 200
        mock.json.return_value = {"data": MOCK_CHARACTERS}

    # Single character full
    elif url == f"{API_BASE_URL}/characters/2951/full":
        mock.status_code = 200
        mock.json.return_value = {"data": MOCK_CHARACTER}

    # Episodes list — health check and list request
    elif url == f"{API_BASE_URL}/anime/966/episodes":
        mock.status_code = 200
        mock.json.return_value = {"data": MOCK_EPISODES}

    # Episode 1 individual
    elif url == f"{API_BASE_URL}/anime/966/episodes/1":
        mock.status_code = 200
        mock.json.return_value = {"data": MOCK_EPISODE_1}

    else:
        mock.status_code = 404
        mock.json.return_value = {"error": "Not found"}

    return mock


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    if "regression" in scenario.tags:
        context.mock_get = patch(
            "requests.get",
            side_effect=unified_mock_get
        )
        context.mock_get.start()


def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name} - Status: {scenario.status}")
    if "regression" in scenario.tags:
        context.mock_get.stop()