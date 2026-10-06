# Consultório da Marina: como começar

Este é o mesmo gerenciador de pacientes da Duda, numa versão só sua: sem dados de outra pessoa e sem plataformas pré-cadastradas. Os seus dados ficam criptografados com a **sua** senha.

## Opção A: na sua conta do claude.ai (iPad, celular e computador, com sincronização)

1. Entre em **claude.ai/code** com a sua conta. É o Claude Code na web, que precisa de um plano pago.
2. Comece uma sessão nova e **anexe o arquivo `publicar-no-claude.html`**.
3. Envie esta mensagem:

   > Publique o arquivo anexado como uma página (Artifact) privada, sem alterar o conteúdo, declarando as capacidades `db`, `user` e `downloads` (`capabilities: {"db": {}, "user": {}, "downloads": true}`). É um app pronto.

4. O Claude devolve um link `claude.ai/artifact/...`. Abra no Safari e salve nos favoritos, ou use Compartilhar → **Adicionar à Tela de Início**.
5. Na primeira vez, crie a sua senha. Se aparecer **"☁︎ sincronizado"** no topo, os dados já estão salvos na sua conta e abrem em qualquer aparelho com a mesma senha.

## Opção B: só no computador, sem conta

Dê dois cliques no `index.html`. Ele abre no navegador e guarda os dados **só naquele computador**. Faça backups em Configurações.

## Primeiros passos no app

- **Configurações:** preencha o nome, a profissão (aparece nos recibos), o registro profissional (CRP), a cidade e o valor padrão da sessão.
- **Plataformas:** se você atende por alguma plataforma que cobra repasse, cadastre-a em **Financeiro → Plataformas e repasses → + Plataforma**. A regra pode ser um valor fixo, um percentual ou faixas por valor da sessão.
- **Atenção:** **não há como recuperar a senha.** Faça um backup de vez em quando em Configurações → *Baixar backup criptografado*.
