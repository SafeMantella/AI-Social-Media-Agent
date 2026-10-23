# Prompt para cópias que já estão em uso

Envie o bloco abaixo para o agente de cada cliente, com a pasta deles aberta. Ele serve para quem baixou o zip e para quem clonou. Não peça um pull request do repo deles.

Quando este template estiver no `main`, um pedido curto também funciona: leia `.claude/commands/reportar-evolucao.md` em `https://github.com/SafeMantella/AI-Social-Media-Agent` e siga o arquivo. O bloco abaixo não depende disso.

```
Compare esta pasta com o template https://github.com/SafeMantella/AI-Social-Media-Agent e prepare um relato para o repositório original. Não faça push. Não abra issue. Não abra pull request. Não copie arquivo nenhum por cima desta pasta até eu aprovar o texto exato ou o caminho exato.

Clone raso do template em /tmp/ai-social-template-snapshot. Se o clone falhar, pare e me diga. Apague essa pasta temporária antes de terminar, inclusive se parar no meio. Compare os arquivos no disco com esse snapshot. Não use git diff contra o origin. Zip e clone passam pelo mesmo caminho.

Compare só o sistema: AGENTS.md, CLAUDE.md, README.md, README.pt-BR.md, .gitignore, .claude/, onboarding/, ferramentas/ sem venv, .venv, __pycache__, node_modules, downloads, transcripts, output, logs, cookies, sessões e sem os clones Pytho-inator, last30days-skill e fontastic-text-image-generator, as notas de pipeline e de ferramenta em memory/, e os guias estrategia/03 até estrategia/10.

Não leia para o relato: memory/config.md, identidade visual, handles, voz, automação de DM, edição observada, estrategia/00, estrategia/01, estrategia/02, estrategia/marca/, conteudo/, referencia/, freebies/ fora do README, gravações/, books/, site/, .git/, .env, e arquivo com cookie, token, secret ou credential no nome.

Antes de chamar uma diferença de mudança de sistema, mapeie os dois lados pelas linhas de onboarding/language_paths.py. Pasta renomeada e prosa traduzida não são mudança. Compare o arquivo com o arquivo no caminho mapeado. Um trecho que é só tradução não entra em upstream nem em trazer.

Separe duas listas. Upstream: o que esta cópia tem e o template não tem, e que serve para qualquer criador. Trazer: o que o template tem e esta cópia não tem. Se os dois lados mudaram as mesmas linhas, não copie. Mostre os dois e pergunte. Ignore preenchimento de onboarding, valor de config, handle, bio e nome de marca. Não leia memory/ambiente-maquina.md. Não proponha git pull --allow-unrelated-histories numa cópia que já passou pelo comando de idioma. A atualização dessa cópia é .claude/commands/atualizar-do-git.md.

Escreva memory/relato-evolucao.md e mostre o mesmo texto aqui. Três partes. Upstream: caminho, o que o sistema faz diferente, a regra em palavras gerais, e um diff curto só se cada linha for segura. Trazer: caminhos para copiar e conflitos para eu decidir. Ficar local: uma linha dizendo que marca, conteúdo, pesquisa e credencial ficaram de fora. Não resuma isso.

Antes de eu ver o rascunho, apague nomes, handles, bios, nicho, audiência, promessa, legendas, transcrições, URLs de perfil, e-mails, telefones, caminhos de home e de sessão. Apague linha com chave, token, cookie, senha, api_key, secret, BEGIN PRIVATE, sk- ou xoxb-. Se a lição só funciona com esse detalhe, descreva o mecanismo e derrube o exemplo. Se não sobrar nada generalizável, diga isso numa linha.

Pare. Eu digo o que pode ser enviado e o que pode ser copiado para cá.

Um sim para um item de upstream ainda não envia. Reescreva o corpo da issue só com o que eu aprovei, mostre de novo, e espere um segundo sim. A issue vai para SafeMantella/AI-Social-Media-Agent, nunca para um fork e nunca para o remote desta pasta. Título com prefixo [sistema]. Use gh issue create --repo SafeMantella/AI-Social-Media-Agent. Se o gh não existir ou não estiver logado, me entregue título, corpo e o link https://github.com/SafeMantella/AI-Social-Media-Agent/issues/new?template=sistema.md . Não abra pull request desta cópia.

Um sim para trazer nomeia caminhos. Copie só esses caminhos do snapshot. Não dê git merge nem git pull.

Quando eu responder, grave last_report com a data de hoje em memory/evolucao-template.md, sem colar o relato. Se eu não responder, não grave last_report.

Se eu aprovar a instalação, deixe a rotina mensal nesta pasta. O procedimento é o desta mensagem. due_days: 30. Na abertura, se started estiver vazio, grave a data de hoje e não avise. O relato vence quando last_report está vazio e started tem mais de 30 dias, ou quando last_report tem mais de 30 dias. Avise antes de outra pergunta, no máximo uma vez por dia. Um agora não não publica e não conta como relato. Uma data adia. Nada é enviado sem eu aprovar o texto exato. Não crie memory/evolucao-template.local.md.
```
