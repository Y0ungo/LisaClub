# LisaClub — 해커톤 AI 에이전트 (스캐폴드)

주제가 아직 정해지지 않은 상태에서 바로 시작할 수 있도록 만든 최소 골격입니다.
자세한 가이드(구조 설명, 확장 방법, 체크리스트)는 [CLAUDE.md](CLAUDE.md)를 보세요.

## 빠른 시작

```bash
python -m venv .venv
source .venv/bin/activate   # Windows는 .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # 복사 후 ANTHROPIC_API_KEY 입력
python -m agent.main
```

## 구조

| 경로 | 역할 |
|---|---|
| `agent/main.py` | 에이전트 실행 루프 (입력 → Claude 호출 → 도구 실행 → 응답) |
| `agent/tools.py` | 도구(함수) 정의 — 주제에 맞는 도구를 여기에 추가 |
| `agent/config.py` | 환경 변수 로딩 |
| `tests/` | 도구 단위 테스트 (`pytest`로 실행) |

## 테스트

```bash
pytest
```
