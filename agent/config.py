"""환경 변수를 읽어 에이전트 설정을 만든다."""
import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


@dataclass
class Config:
    api_key: str
    model: str


def load_config() -> Config:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "ANTHROPIC_API_KEY 환경 변수가 없습니다. "
            ".env.example을 .env로 복사한 뒤 키를 넣어주세요."
        )
    model = os.environ.get("AGENT_MODEL", "claude-sonnet-5")
    return Config(api_key=api_key, model=model)
