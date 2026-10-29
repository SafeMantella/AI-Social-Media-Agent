# Agente de rede social

Um toolkit que deixa um agente de código ajudar um criador a planejar, escrever, editar e publicar conteúdo de rede social. A pasta vem vazia. Você abre com o seu agente, responde a uma entrevista, e ela vira o seu sistema: sua marca, suas plataformas, suas ferramentas, o seu jeito de trabalhar.

English: [README.md](README.md)

`AGENTS.md` é o arquivo de entrada que todo agente lê. `CLAUDE.md` aponta para ele. O Claude Code é o agente com que este toolkit é feito e testado.

## O que você recebe

- **Uma entrevista de onboarding** que grava nicho, público, promessa, pilares, voz, identidade visual, plataformas e handles em arquivos. Se você já publica, ela lê seus perfis primeiro e propõe só o que viu.
- **Pipelines** com ordem fixa (entrevista, pesquisa, escrita, aprovação, produção) para roteiros, hooks, carrosséis, edição de vídeo, pesquisa, transcrição e revisão antes de publicar.
- **Integração com o que você já usa.** O onboarding pergunta quais ferramentas você tem (Notion, editor, agendador) e se conecta a elas. Não troca nenhuma.
- **Claude in Chrome**, para o agente trabalhar dentro do seu navegador, já logado. Veja abaixo.
- **Ferramentas locais**, uma pasta cada em `ferramentas/` (transcrição, corte de silêncio, contact sheets, mineração de palavras-chave, uploads e mais). Uma skill gerada, `catalogo-ferramentas`, lista cada ferramenta e o que ela faz, para o agente achar a certa. As ferramentas próprias ficam em repositórios públicos que continuam atualizáveis.
- **Pytho-inator**, que transforma qualquer tarefa repetida em um comando Python local. É assim que o toolkit cresce com você.
- **Uma rotina de atualização.** `/update-toolkit` confere este template e cada repositório de ferramenta e registra quando conferiu.

## Instalação, passo a passo

1. **Pegue a pasta.** Clone o repositório, ou baixe o zip na página dele (Code, depois Download ZIP) e descompacte num lugar onde ela vai ficar.
   ```bash
   git clone https://github.com/SafeMantella/AI-Social-Media-Agent.git "minhas-redes"
   ```
   Com o clone, o `/update-toolkit` funciona com o histórico completo. O zip também funciona: a primeira atualização liga a pasta ao template.
2. **Instale as ferramentas de base.** macOS é para onde os scripts foram escritos. Veja Requisitos abaixo (`brew install python@3.13 node ffmpeg git`).
3. **Instale o [Claude Code](https://claude.com/claude-code)** e entre na sua conta.
4. **Abra a pasta no Claude Code.** No terminal: `cd minhas-redes && claude`. No app desktop ou numa extensão de IDE, abra a pasta como projeto.
5. **Digite `/onboarding` dentro do Claude Code.** Esse comando é toda a configuração. Ele clona o que faltar e depois faz uma pergunta por vez, gravando cada resposta nos seus arquivos. Não há mais nada para colar ou instalar antes.
6. **Responda a entrevista.** A primeira pergunta é o idioma do sistema inteiro. Depois vêm a marca, se você já publica (nesse caso, os links de três posts que você escolhe), nicho, voz, visual, plataformas e handles. Ele também oferece o Claude in Chrome e pergunta quais ferramentas você já usa. Pede sua permissão antes de instalar qualquer coisa. Você escolhe **expresso** (só o núcleo: marca, referências, voz, visual; integrações depois com `/ativar-ferramenta`) ou **completo**. Antes da leitura do perfil ele roda o `/doctor` e conserta o que a máquina não tem, sem pedir sua senha.
7. **Terminou quando `memory/config.md` diz `status: ready`.** Rode `/doctor` para checar a máquina e `/iniciar` para começar a trabalhar. Se a conversa parar no meio, abra a pasta de novo e digite `/onboarding`: ele retoma na primeira pergunta sem resposta.

Se você pular o passo 5 e só disser olá, o agente vê a configuração vazia e começa a entrevista do mesmo jeito.

As pastas são renomeadas uma vez, depois da releitura, para o idioma que você escolheu, e só quando `python3 onboarding/language_paths.py check` imprime `ok`. As checagens de início de sessão (revisão de armazenamento, atualização do toolkit, relato ao template) estão escritas no `AGENTS.md`.

## Claude in Chrome

O Claude in Chrome é uma extensão que deixa o agente trabalhar no seu próprio Chrome, com os seus logins. Para este toolkit, ele cobre o que não tem API: ler um perfil que exige login, pesquisar atrás de login, conferir se um post está no ar e clicar no Notion quando não há conector. Sem ele, o agente só lê páginas públicas e pede arquivos de sessão.

A pergunta 1a do onboarding explica, pede sua permissão, instala com você e testa:

1. Instale o Chrome se não tiver.
2. Instale a extensão "Claude in Chrome" pela Chrome Web Store e entre com a mesma conta Claude do agente.
3. No Claude Code, rode `/chrome` para conectar (ou inicie o Claude Code com `claude --chrome`).
4. O agente abre uma aba numa URL pública e lê o título. Só um teste que passa grava `claude_in_chrome: yes`.

Ele é opcional para o `ready`, e você pode dizer não. O agente nunca instala sem o seu sim, e nunca publica, paga ou envia nada por ele sem o seu sim. A política de navegador (rota mais barata primeiro, screenshot por último): `memory/regras-execucao-robusta.md`.

## Como funciona no dia a dia

1. `/iniciar` lembra o que está pendente, em cinco linhas.
2. Você nomeia uma peça. O agente lê o pipeline daquela tarefa e segue a ordem.
3. A pesquisa usa só as ferramentas que você ligou. Ferramenta em `no` vira uma lacuna registrada, não um pulo silencioso.
4. A escrita vai para o armazenamento canônico (Notion ou `conteudo/`). Você aprova. Depois o agente produz.
5. Nada é publicado, exportado como carrossel ou renderizado em resolução final sem um sim explícito.
6. No fim de uma tarefa que criou arquivos, o Pytho-inator pode oferecer um CLI local para o trabalho repetido. Nada é construído sem o seu sim.

## Comandos

Digite no Claude Code, ou peça a qualquer outro agente que leia o arquivo e siga. `COMANDOS.md` é o manual gerado (`/comandos`).

| Comando | O que faz |
|---|---|
| `/onboarding` | Toda a configuração. Digite uma vez depois de abrir a pasta |
| `/doctor` | Confere a máquina contra a sua config e diz o que falta |
| `/ativar-ferramenta` | Liga uma integração opcional depois, com instalação e teste |
| `/learn-from-edit` | Cole a sua versão de um rascunho e o sistema aprende suas regras pela diferença |
| `/exportar-sessao` | Salva esta conversa em Markdown (dados pessoais mascarados), só quando você pedir |
| `/iniciar` | Abre a sessão: o que está pendente, em cinco linhas |
| `/carousel` | Monta um carrossel: entrevista, pesquisa, plano, aprovação e depois a produção com as ferramentas de design do Claude ou o HyperFrames |
| `/pesquisar` | Pesquisa um assunto, perfil ou peça com as ferramentas ligadas |
| `/update-toolkit` | Confere o template e cada repositório de ferramenta, atualiza o que estiver atrás e registra as datas |
| `/atualizar-ferramentas` | Só os repositórios de ferramentas |
| `/atualizar-do-git` | Só o template |
| `/revisar-armazenamento` | Mede a pasta e propõe o que mover. Nada se move sem a sua aprovação |
| `/reportar-evolucao` | Rascunha um relato sem dados pessoais do que você mudou, para o template. Não publica nada até você aprovar o texto |
| `/revisar-video`, `/edicao`, `/avaliar-edicao`, `/refinar-overlay` | Revisão e ciclo de edição de vídeo |
| `/sugerir-conteudo` | Ideias de conteúdo a partir do trabalho da sessão |
| `/registrar-bastidores` | Série de bastidores, só quando você ligou |
| `/atualizar-memoria` | Salva em `memory/` as decisões e correções da sessão |
| `/map-automation-opportunities`, `/check-skills` | Onde o Pytho-inator pode encolher um fluxo para um comando |
| `/aplicar-idioma` | Roda uma vez, depois do onboarding |
| `/comandos` | Regenera e mostra o manual |

## O que tem aqui

| Caminho | Papel |
|---|---|
| `AGENTS.md` | Regras. Lido em toda abertura |
| `onboarding/` | A entrevista, a checagem de caminhos de idioma e a checagem de vazamento |
| `memory/` | Config, decisões, pipelines e a marca depois que o onboarding preenche. Comece em `memory/INDEX.md` |
| `estrategia/` | Guias de estratégia (o método). Os arquivos de marca ficam em branco até o onboarding |
| `.claude/commands/`, `.claude/skills/` | Fluxos e SOPs, compartilhados por todo agente |
| `ferramentas/` | Ferramentas locais |
| `conteudo/` | Peças canônicas quando o armazenamento é markdown |
| `referencia/pesquisas/` | Saída das pesquisas |
| `referencia/perfil-atual/` | O que o onboarding leu dos perfis em que você já publica |
| `freebies/` | Uma pasta por isca digital |
| `gravações/` | Entrada de vídeo local. Fora do git |
| `COMANDOS.md` | Manual gerado de comandos e skills |

Os nomes de pasta são os do template. A passagem de idioma renomeia as que você vê (por exemplo `estrategia` vira `strategy` se você escolher inglês), e os caminhos nos arquivos acompanham.

## Ferramentas

Cada ferramenta é uma pasta com um README. O agente lê o catálogo gerado (`.claude/skills/catalogo-ferramentas/SKILL.md`), que o `ferramentas/manual-comandos/gerar` reescreve sempre que você adiciona, remove ou renomeia uma pasta de ferramenta. As ferramentas próprias são symlinks para seis repositórios públicos clonados em `ferramentas/_repos/`. O código não é rastreado aqui, então atualizar uma ferramenta nunca suja a sua cópia. Detalhes e comandos de clone: `memory/ferramentas-repos.md`.

| Repositório | Ferramentas |
|---|---|
| [token-kit](https://github.com/SafeMantella/token-kit) | `prep-frames`, `prep-texto`, `token-saver`: ler vídeo ou arquivo grande sem gastar tokens |
| [video-cut-pipeline](https://github.com/SafeMantella/video-cut-pipeline) | `corte-silencio`, `evals`, `evals-edicao`: corte de silêncio e retake, e a revisão manual do corte |
| [transcrever-ptbr](https://github.com/SafeMantella/transcrever-ptbr) | `transcrever`: transcrição local com dois motores e checagem de fala perdida |
| [video-tools](https://github.com/SafeMantella/video-tools) | `video-camadas`, `slides-pdf`: texto atrás da pessoa, slides HTML para PDF |
| [social-toolbox](https://github.com/SafeMantella/social-toolbox) | `keyword-mining`, `minerar-hooks`, `pdf-to-markdown`, `grokbot`, `links`, `extrair-audio`, `grok-imagem` |
| [sau-tools](https://github.com/SafeMantella/sau-tools) | `sau-yt`, `sau-tiktok`: upload para YouTube (privado por padrão) e TikTok, só com o seu sim |

Outros clones ficam direto em `ferramentas/`, fora do git: [Pytho-inator](https://github.com/SafeMantella/Pytho-inator), [Adobe Podcast for Claude Code](https://github.com/SafeMantella/Adobe-Podcast-for-Claude-Code), [Fontastic](https://github.com/SafeMantella/Fontastic-Text-Image-Generator) e ferramentas de terceiros ([last30days-skill](https://github.com/mvanhorn/last30days-skill), [social-auto-upload](https://github.com/dreammis/social-auto-upload), [ln](https://github.com/fogleman/ln)). Wrappers pequenos rastreados aqui: `adobe-enhance`, `reddit-answers`, `instagram-transcript`, `buscar-imagens`, `montar-lista`, `looks-take`, `faixa-legenda`, `manual-comandos`, `atualizar-ferramentas`, `verificar-ambiente`, `checar-legenda`, `detectar-sessao`, `audio-do-reel`, `exportar-sessao` e os wrappers de `minet` e `scrapling` (os virtualenvs são locais). `editonny` é um recorte de uma skill de motion. `separar-voz` é só um virtualenv.

Clone os soltos quando o onboarding pedir, ou à mão:

```bash
cd ferramentas
git clone https://github.com/mvanhorn/last30days-skill.git
git clone https://github.com/SafeMantella/Pytho-inator.git && chmod +x Pytho-inator/pytho-inator
git clone https://github.com/SafeMantella/Fontastic-Text-Image-Generator.git fontastic-text-image-generator
git clone https://github.com/SafeMantella/Adobe-Podcast-for-Claude-Code.git adobe-podcast
git clone https://github.com/dreammis/social-auto-upload.git
git clone https://github.com/fogleman/ln.git
```

Arquivos de sessão, cookies, `.env` e perfis de navegador ficam fora do git. Veja o `.gitignore`.

## Pytho-inator

O [Pytho-inator](https://github.com/SafeMantella/Pytho-inator) mapeia uma tarefa que você repete para um comando Python local, então o agente roda uma linha e lê a última linha da saída em vez de reexplicar os passos toda vez. É assim que você adiciona ferramentas a este toolkit.

- O onboarding pergunta quais trabalhos você repete toda semana e registra em `memory/ferramentas-existentes.md`.
- Depois do onboarding, no fim de uma tarefa que criou arquivos, ele pode oferecer um CLI em no máximo três linhas. Você diz sim ou ignora.
- Um sim constrói com a skill ponytail em `ultra`, `uv` no lugar do Python do sistema e dependências gratuitas e abertas. API paga ou o primeiro teste precisam do seu sim.
- No Claude Code, um mod opcional mostra a oferta debaixo da resposta. O onboarding pergunta antes de instalar.
- `/map-automation-opportunities` ranqueia o que vale automatizar. `/check-skills` mostra quais skills podem encolher.

## Mantendo atualizado

No começo de toda sessão o agente lê `memory/toolkit-updates.md`. Esse arquivo só registra quando o template e cada repositório de ferramenta foram conferidos pela última vez. Se algo estiver vazio ou com mais de sete dias, o agente avisa e pergunta se pode rodar `/update-toolkit`. Um sim busca, avança o que estiver atrás e grava as datas. Nunca faz push, e um arquivo de marca que você preencheu fica como você escreveu.

Mais duas rotinas funcionam do mesmo jeito e perguntam antes de agir: uma revisão semanal de armazenamento (`memory/revisao-armazenamento.md`) e um relato mensal do que você mudou no sistema, enviado ao template só depois que você aprova o texto exato (`memory/evolucao-template.md`).

## Requisitos

macOS é para onde os scripts foram escritos. Python 3.10+, ffmpeg, git e Node são a base.

```bash
brew install python@3.13 node ffmpeg git
```

Whisper só é necessário se o onboarding escolheu transcrição local. ElevenLabs só se escolheu essa, e a chave fica no ambiente como `ELEVENLABS_API_KEY`. Edição de vídeo espera uma skill local de vídeo que transcreve, corta e renderiza, instalada onde o seu agente carrega skills (o pipeline a chama de `local-video-use`).

## Contas e custo

| Item | Quando | Custo |
|---|---|---|
| Seu agente de código | Sempre | Depende do produto |
| Claude in Chrome | Se você ligar | Exige um plano Claude que o inclua. Confira na página da extensão |
| Conta Adobe | Etapa de limpeza de áudio | Existe plano grátis. Limites não reverificados aqui |
| Conta Reddit | Se Reddit for manual ou auto | Grátis. Auto vai contra os termos do Reddit e pode limitar a conta |
| ElevenLabs | Se a transcrição for elevenlabs | Cobrado pela ElevenLabs |
| xAI | Se a imagem via Grok for sim | Cobrado por imagem |
| Notion | Se o armazenamento for notion | Plano deles |
| HyperFrames | Se o carrossel for hyperframes, e para overlays de vídeo | Instalar é escolha sua. Veja o custo na página dele |
| Canva | Só em cópia antiga com carrossel canva | Plano deles |
| PilotDM | Se a automação de DM do Instagram for sim | Existe plano grátis |
| GitHub | Para publicar ou compartilhar uma ferramenta | Plano deles |

## Regras para todo agente

- Não publique, não exporte carrossel e não renderize vídeo em resolução final sem um sim explícito.
- Não instale nada na máquina do criador sem o sim dele.
- Não guarde memória do projeto fora de `memory/`.
- Não desligue o Notion porque um login falhou. Pare e pergunte.
- Correções que são preferências reutilizáveis vão para `memory/` na hora.
- Leia a tarefa inteira, mantenha a ordem dos passos e mostre evidência antes de dizer "pronto" (`memory/regras-execucao-robusta.md`).

## Cheque vazamentos antes de compartilhar

```bash
python3 onboarding/test_leak_check.py
python3 onboarding/leak_check.py . --wordlist /path/to/wordlist.txt
```

O segundo comando precisa de uma lista de palavras que não faz parte deste repositório. Sem ela, ainda checa caminhos de home, e-mails e URLs ativas de Notion ou Canva.
