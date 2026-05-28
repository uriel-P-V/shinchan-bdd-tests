# shinchan-bdd-tests
 
![CI](https://github.com/uriel-P-V/shinchan-bdd-tests/actions/workflows/tests.yml/badge.svg)
 
A BDD-based test suite for the Jikan API (MyAnimeList) —
demonstrates multi-feature Gherkin organization using Crayon Shin-chan data,
including anime metadata validation, character field validation,
episode filler detection, and rate-limit-aware mock strategy.
 
---
 
## Project Structure
 
```
shinchan-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml                  ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   ├── common_steps.py            ← Shared status code step
│   │   ├── anime_steps.py             ← Anime metadata steps
│   │   ├── characters_steps.py        ← Character list and detail steps
│   │   └── episodes_steps.py          ← Episode field and filler steps
│   ├── environment.py                 ← Hooks and unified mock
│   ├── anime.feature                  ← Anime metadata validation
│   ├── characters.feature             ← Character list and Shinnosuke fields
│   └── episodes.feature               ← Episode fields and filler check
└── requirements.txt
```
 
---
 
## Features
 
- **Anime metadata validation** — score, status, genres list, studios list
- **List membership** — verifies genre and studio names from nested object lists
- **Character count validation** — verifies list has more than 10 characters
- **Nested field validation** — name, favorites, nicknames from character detail
- **Episode filler detection** — verifies `filler: false` on episode 1
- **Rate-limit-aware** — `time.sleep` between requests to respect Jikan 3 req/s limit
- **Single mock** — one `patch("requests.get")` dispatching by URL
- **Tag-driven execution** — `@smoke` hits real API, `@regression` fully mocked
---
 
## BDD Scenarios
 
```gherkin
Feature: Shinchan Anime API
 
  @smoke
  Scenario: GET anime by ID
    When I request the anime with ID 966
    Then the response status code should be 200
 
  @regression
  Scenario: Validate that genres contain Comedy
    When I request the anime with ID 966
    Then the genres should contain "Comedy"
 
Feature: Shinchan Episodes API
 
  @regression
  Scenario: Validate that the first episode is not a filler
    When I request episodes with anime ID 966
    And I request episode 1
    Then the episode should not be filler
```
 
---
 
## Mock Strategy
 
Single `patch("requests.get")` dispatching by URL — covers health checks,
anime full details, character list, character detail, episode list and episode detail.
 
```python
def unified_mock_get(url, **kwargs):
    if url == f"{API_BASE_URL}/anime/966/full":
        mock.json.return_value = {"data": MOCK_ANIME}
    elif url == f"{API_BASE_URL}/anime/966/characters":
        mock.json.return_value = {"data": MOCK_CHARACTERS}
    elif url == f"{API_BASE_URL}/characters/2951/full":
        mock.json.return_value = {"data": MOCK_CHARACTER}
    elif url == f"{API_BASE_URL}/anime/966/episodes/1":
        mock.json.return_value = {"data": MOCK_EPISODE_1}
```
 
---
 
## Setup
 
```bash
git clone https://github.com/uriel-P-V/shinchan-bdd-tests.git
cd shinchan-bdd-tests
pip install -r requirements.txt
behave
```
 
---
 
## Running Tests
 
```bash
# All scenarios
behave
 
# Smoke only — hits real Jikan API (rate limited)
behave --tags=smoke
 
# Regression only — fully mocked, no internet required
behave --tags=regression
```
 
> **Note:** Jikan API enforces a rate limit of 3 requests/second.
> Smoke tests include `time.sleep` delays to avoid 429 errors.
 
---
 
## CI/CD Pipeline
 
Two dependent jobs run on every push and pull request to `main`:
 
```
push / PR → smoke (3 scenarios) → regression (7 scenarios)
```
 
If `smoke` fails, `regression` is skipped automatically.
 
---
 
## Tech Stack
 
- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — patch, MagicMock, side_effect
- **GitHub Actions** — CI/CD pipeline
---
 
## Author
 
**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)
 