import pytest

from utils import MonsnodeParser


class TestMonsodeParser:    # pylint: disable=too-few-public-methods
    monsnode_parser = MonsnodeParser()

    @pytest.mark.skipif(not monsnode_parser.is_target_reachable(), reason='Monsnode is currently not reachable')
    def test_get_video_name(self) -> None:
        # given
        target_video_link = 'https://monsnode.com/v1506575871309589251'

        # when
        video_name, video_link = self.monsnode_parser.get_video(target_video_link)

        # then
        assert video_name == 'ウォーター(@waterpokepwpr) - 剣盾ずっとやってきたけど、こんな経験初めて。 https:__t.co_LT6dHwYitY.mp4'
        assert video_link == 'https://monsnode.com/redirect.php?v=13768280'
