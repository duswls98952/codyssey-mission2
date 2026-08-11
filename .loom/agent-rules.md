# Loom 통제 에이전트 계약

Contract version: `1`

## 필수 세션 시작 고지

이 workspace의 작업은 Loom의 통제를 받습니다. 작업 제안, 실행 경계, 결정과 결과는 Loom을 통해 기록되며 중요한 변경은 사용자의 통제 아래 진행됩니다.

## 제품 원칙

```text
Agent proposes.
User controls.
Loom preserves.
```

## 필수 행동 규칙

1. workspace 세션을 시작할 때 작업이 Loom의 통제를 받는다는 사실을 사용자에게 한 번 고지합니다.
2. 계획하거나 행동하기 전에 Loom 명령으로 현재 상태를 확인합니다.
3. Job, Task, 제안, 승인, 실행, lifecycle 변경은 Loom 명령을 사용하며 .loom metadata를 직접 수정하지 않습니다.
4. workflow를 변경하기 전에 사용자 입력의 성격을 분류하며 모든 생각을 Task로 만들지 않습니다.
5. 사용자 Memory 제안 흐름을 따릅니다. 의미 있는 후보만 발췌해 사용자에게 제시하고 선택된 내용만 반영합니다.
6. 사용자가 현재 에이전트에게 Task를 지금 직접 실행하라고 명령한 경우에만 foreground task 실행을 사용할 수 있습니다.
7. Task 작업을 시작하기 전에 반드시 `loom task run <task-id>`로 세션을 먼저 엽니다. run 이전에는 파일 수정, 코드 실행, 커밋을 하지 않습니다.
8. 실행은 승인됐지만 현재 에이전트에게 직접 맡기지 않았다면 Task를 Queue에 등록하고 Worker가 실행하게 합니다.
9. 사용자가 실행을 승인하지 않았다면 계약 작성과 보완만 수행하며 Task를 실행하거나 Queue에 등록하지 않습니다.
10. 완료된 Task는 재실행하지 않습니다. 완료된 Job의 후속 작업이 같은 Job 목표 안에 있으면 새 Task로 추가하고, 목표가 다르면 새 Job을 제안합니다.
11. 에이전트가 자신의 권한 요청을 승인하거나 거절된 정책을 우회하지 않습니다.
12. 사용자의 결정, 승인, 수락을 위조하지 않습니다. Proposal을 에이전트가 대신 accept/reject/materialize하지 않고, `--user-decision` 등에 사용자 결정을 지어내 넣지 않으며, 채팅에서 사용자가 실제로 준 승인만으로 행동합니다.
13. 각 Task는 run -> 작업 -> 검증 -> 커밋 -> finish 순서를 정확히 따릅니다. 이 순서를 바꾸거나 건너뛰지 않습니다.
14. 새로 발견한 작업을 현재 Task에 몰래 확장하지 않고 후속 Proposal로 분리합니다.
15. 작업 중 유의미한 원칙, 판단, 후속 작업을 발견하면 workflow 상태로 몰래 확정하지 않고 Memory Proposal 후보로 사용자에게 제안합니다.
16. Task 커밋에는 코드 변경과 함께 .loom workflow 메타데이터를 스테이징해 포함하고, `loom task finish` 후 생성된 .loom 변경도 커밋해 workflow 기록을 미커밋 상태로 남기지 않습니다.
17. 작업 종료 전 metadata를 검증하고 결과, 검증, 남은 위험, 새 제안과 다음 행동을 보고합니다.

## 에이전트 표면 안내

- Codex 또는 Claude Code 등 어떤 에이전트 표면이든 workflow 상태를 바꾸기 전에 Loom 계약을 읽고 Loom 명령을 사용해야 합니다.
- Loom Task는 context pack이 큰 편이므로 복잡한 작업에는 상위 모델과 높은 추론 수준을 권장합니다.
- Implemented process adapters: `local`, `codex`, `codex:<model>`, `codex:<model>:<reasoning>`, `claude`, `claude:<model>`, `claude:<model>:<effort>`
- Planned process adapters: 
- Claude Code는 foreground 통제 에이전트와 Loom Task/Background Worker process adapter로 모두 지원하며 Codex와 동일한 context 및 산출물 계약을 따릅니다.

## Planning Agent 안내

### Task 생성 전 검토
- Task를 만들기 전에 기존 Job과 완료 Job 중 같은 목표의 후속 작업을 받을 수 있는 Job이 있는지 확인합니다.
- Job 경계는 사용자 목표, 기능 영역, workflow 표면, 최근 작업 내역의 연속성을 기준으로 판단합니다.
- 같은 흐름의 검증, 문서화, 정리, UI polish라는 이유만으로 새 Job을 만들지 않습니다.
- 산출물, ownership 경계, 제품 표면, 운영 관심사가 실제로 달라질 때만 새 Job을 제안합니다.

### Task 계약
- Task 제목은 추상 카테고리가 아니라 실제 수행할 일을 드러내야 합니다.
- 모든 Task에는 description, expected output, done condition, validation hint, scope가 있어야 합니다.
- 사용자가 작업 묶음을 Task로 넣으라고 하면 기본적으로 설계 고정 -> 구현 -> 검증 순서가 이어지게 구성합니다.
- 단일 후속 Task를 추가할 때는 대상 Job의 goal과 최근 Task history를 기준으로 적절한 계약과 위치를 정합니다.

## Memory Proposal 후보 안내

### 제안해야 할 때
- 새로운 장기 workflow 규칙이 발견됐을 때
- 사용자가 한 방향을 선택하고 다른 대안을 포기했을 때
- 반복 가능한 실패 패턴, 복구 방법, runbook이 생겼을 때
- 유용하지만 현재 Task 경계 밖인 후속 작업이 보였을 때

### 제안 방식
- 의미 있는 후보만 요약하고 모든 생각을 저장하지 않습니다.
- 후보를 실제 Memory, Job, Task로 반영하기 전 사용자 선택을 받습니다.
- .loom 파일을 직접 수정하지 않고 Loom memory proposal 명령 또는 Web Proposal Inbox를 사용합니다.
- 후보가 Job, Task, Active Memory가 되면 provenance link를 남기고 proposal을 consume합니다.

## Loom 내부 문서

- `.loom/agent-rules.md`: Loom init이 생성하는 통제 에이전트 계약 문서입니다.
- `.loom/project.md`: workspace 프로젝트 메모리 루트이며 loom analyze-repo로 보강됩니다.
- `.loom/memory/profile.json`: 언어, 문서 경로, memory bucket을 정의하는 workflow memory profile입니다.

## Loom 코드 계약

- `agent-session`: 통제 에이전트가 세션 시작부터 종료까지 따라야 하는 최상위 행동 계약입니다. Command: `loom contract show agent-session`. Source: `loom/core/agent_rules.py`, `AGENTS.md`, `CLAUDE.md`
- `task-execution`: Task 실행 전 prompt/context/previous-results에 들어가는 입력 경계입니다. Command: `loom contract show task-execution`. Source: `loom/application/context_pack.py`, `loom/application/team_policy.py`
- `codex-adapter`: Codex CLI process adapter가 받아야 하는 입력과 반환해야 하는 JSON 결과 계약입니다. Command: `loom contract show codex-adapter`. Source: `loom/adapters/agents/codex_cli.py`, `loom/ports/agents.py`
- `claude-adapter`: Claude Code CLI process adapter가 받아야 하는 입력과 반환해야 하는 JSON 결과 계약입니다. Command: `loom contract show claude-adapter`. Source: `loom/adapters/agents/claude_code.py`, `loom/adapters/agents/claude_events.py`, `loom/ports/agents.py`
- `workflow-memory`: 사용자 생각을 Proposal Inbox, Active Memory, Archive/Audit로 나누는 저장 계약입니다. Command: `loom contract show workflow-memory`. Source: `loom/core/store.py`, `loom/application/services.py`, `loom/adapters/agents/advisor_router.py`, `loom/adapters/agents/proposal_suggester.py`, `loom/adapters/agents/claude_advisors.py`
- `workflow-advisor`: 레포 기반 질문에 대해 추천/대안/근거를 제안하는 Advisor 계약입니다. Command: `loom contract show workflow-advisor`. Source: `loom/application/advisor.py`, `loom/adapters/agents/advisor_router.py`, `loom/adapters/agents/workflow_advisor.py`, `loom/adapters/agents/claude_advisors.py`
- `proposal-placement`: Accepted Proposal을 기존 Job/새 Job/Task로 배치할 때 쓰는 판단 계약입니다. Command: `loom contract show proposal-placement`. Source: `loom/application/proposal_placement.py`, `loom/adapters/agents/advisor_router.py`, `loom/adapters/agents/proposal_task_advisor.py`, `loom/adapters/agents/claude_advisors.py`
- `import-history`: git/docs/submodule evidence를 Job/Task workflow memory로 복원하는 단계형 계약입니다. Command: `loom contract show import-history`. Source: `loom/application/services.py`
- `control-plane-worker`: Control-plane command를 로컬 worker가 claim/heartbeat/complete하는 경계입니다. Command: `loom contract show control-plane-worker`. Source: `loom/runtime/control_plane_worker.py`, `loom/adapters/control_plane/client.py`
- `done-guardrail`: Task를 DONE으로 인정하기 전에 필요한 산출물과 상태 전이를 검증하는 계약입니다. Command: `loom contract show done-guardrail`. Source: `loom/application/services.py`

## 실행 경로 선택

- **Foreground Task 실행**: 사용자가 현재 통제 에이전트에게 해당 Task를 지금 직접 실행하라고 명시했습니다.
- **Queue / Worker 실행**: 사용자가 실행을 승인했지만 현재 에이전트에게 foreground 실행을 직접 맡기지 않았습니다.
- **실행하지 않음**: 사용자가 Task 실행을 승인하지 않았습니다.

## 필수 세션 시작 절차

- `loom status --json`
- `loom resume --json`
- `loom validate --strict`

## 필수 작업 종료 절차

- `loom validate --strict`
- `loom resume --json`
