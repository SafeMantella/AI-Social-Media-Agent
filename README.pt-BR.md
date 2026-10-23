# Agente de rede social

Um sistema vazio para um criador. Cole o prompt abaixo no agente de código que você quiser, com esta pasta aberta. Isso é a configuração. Ele roda o onboarding e preenche a marca, as redes e as ferramentas.

English: [README.md](README.md)

`AGENTS.md` é o arquivo de entrada. `CLAUDE.md` aponta para ele. A primeira resposta define o idioma. A entrevista segue nesse idioma. A troca das pastas acontece uma vez, depois da releitura, e só vale quando a checagem de caminhos passa.

## Cole isto

Um prompt só. Copie o bloco e envie como primeira mensagem.

```
Configure esta pasta como o meu sistema de rede social. Esta mensagem é a configuração. Não existe um passo de instalação separado.

Se ferramentas/Pytho-inator não existir, clone https://github.com/SafeMantella/Pytho-inator.git em ferramentas/Pytho-inator e deixe ferramentas/Pytho-inator/pytho-inator executável. Não edite esse clone. Leia AGENTS.md e siga o arquivo. Leia memory/config.md. Se status não for ready, siga onboarding/interview.md e não faça outro trabalho. Não sugira automação durante o onboarding. A primeira pergunta é o idioma do sistema inteiro. Depois que eu responder, faça o resto nesse idioma e grave as respostas nele. Não renomeie pastas no meio da entrevista. Depois da releitura, siga .claude/commands/aplicar-idioma.md uma vez. Isso reescreve os markdown, renomeia as pastas que eu leio, e só grava files_language quando onboarding/language_paths.py check imprimir ok. Uma pergunta por vez. Grave cada resposta no arquivo que a entrevista indicar, na hora. Se eu já publico, abra esses perfis e termine a leitura deles antes de perguntar nicho, voz ou visual. Copie a primeira linha na tela de cada vídeo para o swipe file. Antes de eu escolher continuar a edição antiga, diga o que segura um estranho e o que o perde nos primeiros segundos. Proponha só a partir do que você de fato viu. Rode a checagem de instalação de cada ferramenta que eu marcar como sim. Checagem que falha não termina. Não marque status como ready enquanto faltar resposta obrigatória ou checagem.

Se status já for ready, não me entreviste de novo. Leia memory/project_social_media_status.md e espere uma tarefa. Depois que status for ready, no fim de cada tarefa que criou ou editou arquivos, rode ferramentas/Pytho-inator/pytho-inator glance nesses arquivos. Se não imprimir nada, não fale de automação. Se imprimir um achado, mostre no máximo três linhas e pergunte se eu quero construir esse CLI em Python. Não construa sem um sim meu.

A memória do projeto fica só em memory/ dentro desta pasta, no nome de pasta que a passagem de idioma tiver deixado. Não publique, não monte no Canva e não renderize em resolução final sem um sim explícito meu.

Em toda abertura, inclusive durante a configuração, leia memory/revisao-armazenamento.md. Se a revisão de armazenamento estiver vencida, me avise e pergunte antes de qualquer outra pergunta. Medir, mover ou apagar espera um sim, e um sim para a análise não é um sim para um caminho.

Em toda abertura, inclusive durante a configuração, leia memory/atualizacao-git.md. Se started estiver vazio, grave a data de hoje e não pergunte. Se a atualização semanal do git estiver vencida, e você não tiver feito a pergunta de armazenamento neste turno, me avise e pergunte. Um sim puxa o main de https://github.com/SafeMantella/AI-Social-Media-Agent.git e adequa os arquivos de sistema. Um arquivo de marca já preenchido fica como eu escrevi. Não faça push.

Em toda abertura, inclusive durante a configuração, leia memory/evolucao-template.md. Se started estiver vazio, grave a data de hoje e não pergunte. Se o relato mensal de evolução estiver vencido, e você não tiver feito a pergunta de armazenamento nem a de git neste turno, me avise e pergunte. Não faça push e não abra issue nem pull request até eu aprovar o texto exato. Pule isto num checkout cujo memory/evolucao-template.local.md diga role: upstream.
```

Responda todas as perguntas. O onboarding termina quando `memory/config.md` diz `status: ready`. Se você já publica, o agente lê esses perfis antes do resto da entrevista.

## O que tem aqui

| Caminho | Função |
|---|---|
| `AGENTS.md` | Regras. Lidas em toda abertura. |
| `onboarding/interview.md` | A entrevista da primeira vez. |
| `memory/` | Decisões, pipelines e a marca depois que o onboarding preenche. Comece por `memory/project_social_media_status.md`. |
| `estrategia/` | Docs de estratégia. Os guias longos são o método. Os arquivos de marca ficam em branco até o onboarding. |
| `.claude/skills/` | SOPs que o agente carrega. |
| `.claude/commands/` | Fluxos. Peça ao agente para ler o arquivo e seguir. |
| `ferramentas/` | Ferramentas locais. |
| `conteudo/` | Peças canônicas quando o armazenamento é markdown. |
| `referencia/pesquisas/` | Saída de pesquisa. |
| `referencia/perfil-atual/` | O que o onboarding leu dos perfis que você já publica. |
| `freebies/` | Uma pasta por isca, a partir do molde em `freebies/README.md`. |
| `gravações/` | Vídeo local de entrada. Fora do git. Vazia no modelo. |

Notion e Canva são opcionais. O onboarding registra qual você usa. Markdown em `conteudo/` é a reserva.

## Requisitos

Os scripts foram escritos no macOS. A base é Python 3.10+, ffmpeg, git e Node.

```bash
brew install python@3.13 node ffmpeg git
```

Whisper só é necessário se o onboarding escolher transcrição local. ElevenLabs só é necessário se o onboarding escolher esse motor. O segredo fica no ambiente, como `ELEVENLABS_API_KEY`.

Edição de vídeo espera uma skill local que transcreva, corte e renderize, instalada onde o seu agente carrega skills. O pipeline chama essa skill de `local-video-use`.

## Contas e custo

| Item | Quando | Custo |
|---|---|---|
| O seu agente de código | Sempre | Depende do produto |
| Conta Adobe | Passo de limpeza de áudio | Existe plano grátis. Os limites não foram reconferidos aqui |
| Conta Reddit | Se Reddit for manual ou auto | Grátis. Auto viola os termos do Reddit e pode limitar a conta |
| ElevenLabs | Se a transcrição for elevenlabs | Cobrado pela ElevenLabs |
| xAI | Se a geração de imagem com Grok for sim | Cobrado por imagem |
| Notion | Se o armazenamento for notion | O plano deles |
| Canva | Se o carrossel for canva | O plano deles. Grave o id do template mestre |
| PilotDM | Se a automação de DM do Instagram for sim | Existe plano grátis |
| GitHub | Para publicar ou compartilhar uma ferramenta | O plano deles |

## Ferramentas locais

Cada ferramenta tem um README na pasta dela. Clones de terceiros ficam fora do git. Clone de novo quando quiser essa ferramenta:

```bash
cd ferramentas
git clone https://github.com/mvanhorn/last30days-skill.git
git clone https://github.com/SafeMantella/Pytho-inator.git
chmod +x Pytho-inator/pytho-inator
```

O Pytho-inator mapeia uma tarefa repetida para um CLI Python local. Depois do onboarding, o agente sugere esse CLI no fim da tarefa. Nada é construído até um sim.

Arquivos de sessão e exportações do navegador ficam fora do git. Veja `.gitignore`.

O onboarding roda a checagem de instalação de cada ferramenta marcada como sim. Checagem que falha não termina o onboarding.

## Regras para qualquer agente

- Não publique, não monte no Canva e não renderize um vídeo em resolução final sem um sim explícito.
- Não guarde memória do projeto fora de `memory/`.
- Não troque Notion ou Canva porque um login falhou. Pare e pergunte.
- Correção que é preferência reaproveitável entra em `memory/` na hora.

## Checagem rápida

```bash
python3 onboarding/test_leak_check.py
python3 onboarding/leak_check.py . --wordlist /path/to/wordlist.txt
```

O segundo comando precisa de uma wordlist que não faz parte deste repositório. Sem wordlist, ele ainda procura caminhos de home, e-mails e URLs ao vivo de Notion ou Canva.
