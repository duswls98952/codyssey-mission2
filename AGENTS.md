# Agent Instructions

<!-- loom:controlling-agent:start -->
## Loom 통제 에이전트

이 workspace의 작업은 Loom의 통제를 받습니다.

1. 계획하거나 행동하기 전에 `loom agent instructions --json`을 실행합니다.
2. `startup_notice`를 한 번 고지하고 반환된 필수 시작 명령을 실행합니다.
3. workflow 변경은 Loom 명령으로 수행하며 `.loom/` metadata를 직접 수정하지 않습니다.

정본 동작 계약은 `loom contract list`, `loom contract show <id>`, `loom contract path <id>`로 확인하며 `.loom/agent-rules.md`는 사람이 읽는 사본입니다.
<!-- loom:controlling-agent:end -->
