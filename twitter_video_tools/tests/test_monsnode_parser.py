# pylint: disable=redefined-outer-name
import pytest
import requests

from ..monsnode_parser import MonsnodeParser


def test_is_target_reachable(monsnode_parser: MonsnodeParser) -> None:
    # given
    expected_target_reachable = False
    try:
        requests.get(monsnode_parser.TARGET_URL, timeout=monsnode_parser.timeout)
        expected_target_reachable = True
    except requests.exceptions.ConnectionError:
        expected_target_reachable = False

    # when
    actual_target_reachable = monsnode_parser.is_target_reachable()

    # then
    assert actual_target_reachable == expected_target_reachable


@pytest.mark.skipif(not MonsnodeParser().is_target_reachable(), reason='Monsnode is currently not reachable')
def test_get_video_name(monsnode_parser: MonsnodeParser) -> None:
    # given
    target_video_link = 'https://monsnode.com/v1506575871309589251'

    # when
    video_name, video_link = monsnode_parser.get_video(target_video_link)

    # then
    assert video_name == 'ウォーター(@waterpokepwpr) - 剣盾ずっとやってきたけど、こんな経験初めて。 https:__t.co_LT6dHwYitY.mp4'
    assert video_link == 'https://monsnode.com/redirect.php?v=13768280'


@pytest.fixture
def monsnode_parser() -> MonsnodeParser:
    return MonsnodeParser()
