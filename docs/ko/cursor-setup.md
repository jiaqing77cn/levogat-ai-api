# Cursor API 설정 튜토리얼 (중계 API로 Claude/GPT 연결)

> Cursor에 중계 API를 설정하는 완전 가이드: Claude Opus 5, GPT-6, DeepSeek V4 지원, 중국 직결.

> 👉 **API Key 발급**: [api.levogat.com](https://api.levogat.com/register?utm_source=github&utm_medium=cursor-setup&utm_campaign=docs-funnel) (가입 즉시 체험 크레딧 지급, 알리페이/위챗페이 충전 가능)

## 설정 단계

### 1. Cursor 설정 열기

`Cmd/Ctrl + ,` -> "OpenAI" 검색 -> "OpenAI API Key" 찾기

### 2. 설정 입력

- **API Key**: 당신의 Levogat API Key
- **Base URL**: `https://api.levogat.com/v1`

### 3. ~/.cursor/settings.json 수정

```json
{
  "openai.apiKey": "당신의 Levogat API Key",
  "openai.baseUrl": "https://api.levogat.com/v1",
  "openai.model": "gpt-5.6-sol"
}
```

### 4. Claude 모델 사용

Cursor의 모델 선택에서 커스텀 모델 이름을 입력하세요:
- `claude-sonnet-4-6` - 일상 코딩
- `claude-opus-4-8` - 복잡한 작업
- `gpt-5.6-sol` - GPT 프로그래밍

## 추천 설정

| 용도 | 모델 | 그룹 |
|------|------|------|
| 코드 자동완성 | gpt-5.6-luna | Codex 전용 (0.8x) |
| 대화 | claude-sonnet-4-6 | 기본 (1.0x) |
| 복잡한 리팩토링 | claude-opus-4-8 | CC 전용 (2.4x) |
