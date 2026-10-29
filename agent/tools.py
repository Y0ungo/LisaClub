"""
에이전트가 사용할 도구(tool) 정의.

도구를 추가하는 법 (3단계):
1. 아래처럼 파이썬 함수를 작성한다.
   - 입력은 전부 키워드 인자로 받는다 (Claude가 JSON으로 넘겨준 값이 그대로 매핑됨)
   - 반환값은 문자열(또는 str()로 변환 가능한 값)이어야 한다
2. TOOLS 리스트에 Claude API 형식의 스키마를 추가한다.
   - "name"은 아래 함수 이름과 정확히 같아야 한다
   - "description"은 "언제 이 도구를 쓰는지"를 모델이 판단할 수 있게 구체적으로 적는다
3. TOOL_FUNCTIONS 딕셔너리에 "이름": 함수 를 등록한다.

예시로 들어있는 get_current_time 도구는 주제가 정해지면 지우고
실제로 필요한 도구(검색, DB 조회, 외부 API 호출 등)로 교체하세요.
"""
from datetime import datetime, timezone


def get_current_time() -> str:
    """현재 UTC 시간을 ISO 8601 문자열로 반환한다."""
    return datetime.now(timezone.utc).isoformat()


TOOLS = [
    {
        "name": "get_current_time",
        "description": (
            "현재 UTC 날짜/시간을 ISO 8601 형식 문자열로 반환한다. "
            "사용자가 지금 몇 시인지, 오늘 날짜가 언제인지 물을 때 사용한다."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    # 여기에 실제 도구 스키마를 추가하세요.
]

TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    # 여기에 "도구이름": 함수 를 등록하세요.
}
