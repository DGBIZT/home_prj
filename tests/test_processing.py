import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
    ],
)
def test_filter_by_state(state, expected):
    sample_data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    result = filter_by_state(sample_data, state)
    assert result == expected

    #     [
    #         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    #         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     ]
    # ) == filter_by_state_EXECUTED
    with pytest.raises(NameError):
        filter_by_state([])


def test_sort_by_date(sort_by_date_False):
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
        == sort_by_date_False
    )


def test_sort_by_date_same(sort_by_date_same):
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ]
        )
        == sort_by_date_same
    )


def test_sort_by_date_True(sort_by_date_True):
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            True,
        )
        == sort_by_date_True
    )

    with pytest.raises(UnboundLocalError):
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "19-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    with pytest.raises(UnboundLocalError):
        sort_by_date([])
    with pytest.raises(SyntaxError):
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": 20190703183529512364}])
    with pytest.raises(UnboundLocalError):
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "19-07-03T18:35:29.512364"}])
