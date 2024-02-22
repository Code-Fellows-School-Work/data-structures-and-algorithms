import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example_1():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_example_2():
    synonyms = {
        "quick": "fast",
        "slow": "lethargic",
        "happy": "joyful",
        "sad": "sorrowful",
        "bright": "luminous",
    }
    antonyms = {
        "quick": "slow",
        "slow": "quick",
        "happy": "sad",
        "sad": "happy",
        "sharp": "dull",
    }

    expected = [
        ["quick", "fast", "slow"],
        ["slow", "lethargic", "quick"],
        ["happy", "joyful", "sad"],
        ["sad", "sorrowful", "happy"],
        ["bright", "luminous", None],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_example_3():
    synonyms = {
        "clear": "transparent",
        "obscure": "unclear",
        "rich": "wealthy",
        "poor": "impoverished",
        "simple": "uncomplicated",
    }
    antonyms = {

    }

    expected = [
        ["clear", "transparent", None],
        ["obscure", "unclear", None],
        ["rich", "wealthy", None],
        ["poor", "impoverished", None],
        ["simple", "uncomplicated", None],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
