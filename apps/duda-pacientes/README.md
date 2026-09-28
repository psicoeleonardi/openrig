# Consultório — Gerenciador de Pacientes

Aplicativo para organizar o consultório de psicologia: pacientes, responsáveis, agenda, pagamentos, notas fiscais, contatos com responsáveis, prontuário, estudo de caso e plano de tratamento.

É **um único arquivo** (`index.html`). Não precisa instalar nada nem ter internet: basta abrir o arquivo no navegador (Chrome, Edge, Firefox ou Safari).

## Como usar

1. Baixe o arquivo `index.html` e salve numa pasta fixa do computador (ex.: `Documentos/Consultorio/`).
2. Dê dois cliques nele para abrir no navegador. Se quiser, adicione aos favoritos.
3. Na primeira vez, crie uma **senha**. Ela protege os dados com criptografia.
4. Em **Configurações**, preencha nome, CRP, CPF, cidade e valor padrão da sessão. Esses dados aparecem nos recibos e documentos.

> **Importante:** os dados ficam guardados **só naquele navegador, naquele computador**. Abra sempre o mesmo arquivo, no mesmo navegador. Faça **backups** com frequência (Configurações → *Baixar backup criptografado*) e guarde-os num pendrive ou na nuvem. **Não há como recuperar a senha.** Se ela for esquecida, os dados não abrem mais.

## O que tem

| # | Pedido | Onde fica |
|---|--------|-----------|
| 1 | Lista de pacientes | **Pacientes**: busca por nome, CPF, telefone ou responsável; filtro por situação e por menores de idade; próxima sessão e saldo de cada um |
| 2 | Dados dos pacientes e dos responsáveis (menores) | Aba **Dados** do paciente. Menores de 18 anos são detectados pela data de nascimento. Cada responsável tem parentesco e CPF, e pode ser marcado como responsável financeiro (quem recebe a NF) ou como quem tem a guarda |
| 3 | Atendimentos, cancelamentos, faltas e reagendamentos | Aba **Atendimentos** e tela **Agenda**. A sessão pode ser marcada como *realizada*, *falta* (com ou sem cobrança), *cancelada* (quem cancelou, motivo, cobrar ou não) ou *reagendada* (a original fica no histórico ligada à nova). Dá para agendar sessões semanais recorrentes e ver contadores por período |
| 4 | Datas e formas de pagamento | Aba **Pagamentos e NF** e tela **Financeiro**. Formas: Pix, dinheiro, cartão, transferência, boleto e convênio. O saldo é calculado automaticamente (sessões cobráveis − pagamentos), com sugestão de valor e referência. Recibo com valor por extenso, pronto para imprimir ou salvar em PDF |
| 5 | Emissão de nota fiscal | Cria a nota com tomador (responsável financeiro, se o paciente for menor), descrição, competência e pagamentos incluídos. **Copiar dados p/ emissor** leva tudo para o portal de NFS-e; depois é só registrar o número em **Marcar emitida**. Lista pagamentos ainda sem nota |
| 6 | Contato mensal com responsáveis (menores) | Tela **Contatos** e aba **Contatos c/ responsáveis**. O próximo contato é calculado 1 mês após o último. Os atrasados e os dos próximos 7 dias aparecem na tela inicial. Link direto para o WhatsApp do responsável |
| 7 | Prontuário | Aba **Prontuário**: registros com data, tipo e sessão vinculada. Avisa quais sessões realizadas ainda não têm evolução. Pode ser impresso ou salvo em PDF |
| 8 | Estudo de caso | Aba **Estudo de caso**: queixa, histórias, dinâmica familiar, hipóteses, formulação, fatores de risco e proteção, supervisão etc. Salva sozinho e pode ser impresso ou salvo em PDF |
| 9 | Plano de tratamento | Aba **Plano de tratamento**: abordagem, frequência, objetivos, estratégias, participação da família, encaminhamentos, critérios de alta, data de revisão e **metas** com situação. Pode ser impresso ou salvo em PDF |

A tela **Início** reúne o dia a dia: sessões dos próximos 7 dias, sessões passadas que ainda precisam de atualização, contatos com responsáveis vencidos, saldos em aberto, notas a emitir e planos a revisar.

## Sobre a nota fiscal

A NFS-e é emitida no sistema da prefeitura ou no **Emissor Nacional** (https://www.nfse.gov.br/EmissorNacional), que exige o login da profissional. Por isso o app **prepara** a nota (dados do tomador, valor, descrição e competência), copia os dados para colar no emissor e registra o número e o link depois da emissão. O link do emissor pode ser trocado em Configurações para o da sua prefeitura.

## Segurança e sigilo

- Os dados ficam criptografados no navegador (AES-GCM de 256 bits, chave derivada da senha com PBKDF2). Nada é enviado para a internet.
- Bloqueio automático após 15 minutos sem uso, além do botão **Bloquear**.
- O backup criptografado só abre com a senha. A exportação "dados abertos" não tem criptografia: use apenas se precisar e guarde em local seguro.
- Os documentos impressos levam a nota de sigilo. A Resolução CFP nº 01/2009 pede que o registro documental seja guardado por no mínimo 5 anos.

## Levar para outro computador

1. No computador antigo: Configurações → *Baixar backup criptografado*.
2. No novo: abra o `index.html` e, na tela inicial, clique em *Restaurar backup*. Escolha o arquivo, digite a senha do backup e crie a senha do novo computador.
