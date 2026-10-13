import { test, expect } from 'claude-code/testing'

test('arquivo inexistente passa direto (falha aberta)', async ($, on) => {
  on('tool.call', { tool: 'Read' }, () => ({ result: 'ok' }) as never) // stand-in do engine
  const r = await $.tool.call({ tool: 'Read', file_path: '/nao/existe.png' })
  expect(r.deny).toBeUndefined()
})

test('notion-fetch repetido: 2ª chamada recusada, 3ª passa', async ($, on) => {
  on('tool.call', { tool: 'mcp__claude_ai_Notion__notion-fetch' }, () => ({ result: 'ok' }) as never)
  const call = () => $.tool.call({ tool: 'mcp__claude_ai_Notion__notion-fetch', id: 'abc' } as never)
  expect((await call()).deny).toBeUndefined()
  expect((await call()).deny).toBeDefined()
  expect((await call()).deny).toBeUndefined()
})

test('cat pequeno ou com pipe passa', async ($, on) => {
  on('tool.call', { tool: 'Bash' }, () => ({ result: 'ok' }) as never)
  expect(((await $.tool.call({ tool: 'Bash', command: 'cat /nao/existe | head' })) as { deny?: string }).deny).toBeUndefined()
})
