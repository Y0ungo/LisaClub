"""
해커톤 AI 에이전트 스캐폴드 - 진입점.

Anthropic Claude API를 사용한 가장 단순한 "도구 호출 에이전트 루프"입니다.
터미널에서 대화하며 동작을 확인하는 용도이고, 주제가 정해지면 다음을 바꾸세요.

  1. agent/tools.py 에 실제 도구를 추가한다
  2. 아래 SYSTEM_PROMPT 을 에이전트의 실제 역할에 맞게 바꾼다
  3. 필요하면 대화 기록 저장, RAG, MCP 서버 연동 등을 확장한다 (CLAUDE.md 참고)

실행: python -m agent.main
"""
import anthropic

from agent.config import load_config
from agent.tools import TOOLS, TOOL_FUNCTIONS

SYSTEM_PROMPT = """당신은 (여기에 에이전트의 역할을 한두 문장으로 적으세요) 입니다.
사용자의 요청을 돕고, 필요할 때 제공된 도구를 사용해 정확한 정보를 확인한 뒤 답하세요."""


def run_agent_turn(client, model, messages):
    """메시지 목록을 Claude에 보내고, 도구 호출이 끝날 때까지 반복 실행한 뒤
    최종 응답(response)을 반환한다. messages는 그 과정에서 계속 추가된다."""
    while True:
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            return response

        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            func = TOOL_FUNCTIONS.get(block.name)
            if func is None:
                result = f"알 수 없는 도구: {block.name}"
            else:
                try:
                    result = func(**block.input)
                except Exception as e:
                    result = f"도구 실행 오류: {e}"
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": str(result),
            })
        messages.append({"role": "user", "content": tool_results})


def main():
    config = load_config()
    client = anthropic.Anthropic(api_key=config.api_key)

    print("AI 에이전트 스캐폴드입니다. 종료하려면 exit 입력 (또는 Ctrl+C).")
    messages = []
    while True:
        try:
            user_input = input("\n사용자> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        response = run_agent_turn(client, config.model, messages)

        for block in response.content:
            if block.type == "text":
                print(f"\n에이전트> {block.text}")


if __name__ == "__main__":
    main()
