# Claude Code 서드파티 API 설정 튜토리얼 (중국 직결)

> 중국에서 Claude Code에 서드파티 API Key를 설정하는 완전 가이드: VPN 불필요, 저지연, Claude Opus 5 / Sonnet 5 지원. 5분 완성.

> 👉 **API Key 발급**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=claude-code-guide&utm_campaign=docs-funnel) (가입 즉시 체험 크레딧 지급, 알리페이/위챗페이 충전 가능)

## Claude Code란?

Claude Code는 Anthropic에서 공식 출시한 AI 프로그래밍 어시스턴트로, 터미널에서 직접 사용할 수 있으며 코드 생성, 리팩토링, 버그 수정, 테스트 작성 등을 지원합니다.

## 설정 단계

### 1. Claude Code 설치

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 환경 변수 설정

```bash
# ~/.bash_profile 또는 ~/.zshrc에 추가
export ANTHROPIC_AUTH_TOKEN="당신의 Levogat API Key"
export ANTHROPIC_BASE_URL="https://api.levogat.com/v1"

# 적용
source ~/.bash_profile
```

### 3. 사용 시작

```bash
cd your-project
claude
```

## 추천 그룹

| 그룹 | 배율 | 적합한 상황 |
|------|------|---------|
| 기본(Azure+MJ) | 1.0x | 일상 사용, 가성비 좋음 |
| CC 전용 | 2.4x | Claude Code 전용 최적화, 안정성 최고 |
| anti/kiro | 1.2x | 가성비 선택 |

## 자주 묻는 질문

### Q: Claude Code에서 "authentication failed" 오류가 발생합니다

환경 변수가 올바르게 설정되었는지 확인하세요:
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### Q: 응답 속도가 느립니다

그룹을 전환해 보세요. CC 전용 그룹은 Claude Code에 최적화되어 있어 속도가 더 빠릅니다.

### Q: Claude Opus 4.8을 지원하나요?

지원합니다. Claude Code에서 `/model`을 입력하면 모델을 전환할 수 있습니다.

## 관련 링크

- [Levogat AI 공식 웹사이트](https://api.levogat.com)
- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code)
- [API 문서](https://levogat.apifox.cn/)
