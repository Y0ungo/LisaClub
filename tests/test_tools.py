"""도구 함수 단위 테스트 예시. 실행: pytest

주제가 정해져서 agent/tools.py에 도구를 추가하면,
이 파일에도 같은 패턴으로 테스트를 추가하세요.
"""
from datetime import datetime

from agent.tools import get_current_time


def test_get_current_time_returns_iso_format():
    result = get_current_time()
    # ISO 8601 형식이 아니면 여기서 예외가 발생해 테스트가 실패한다
    datetime.fromisoformat(result)
