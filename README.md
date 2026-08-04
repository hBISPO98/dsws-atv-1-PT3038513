# Projeto Flask - Atividade Prática 🚀

Projeto desenvolvido com o framework **Flask** para estudo de rotas, requisições, códigos de status, cookies, redirecionamentos e tratamento de erros.

## 🌐 Endpoints / Rotas Disponíveis

Você pode testar cada uma das rotas abaixo adicionando o caminho ao final da URL principal do projeto:

* **Página Inicial:** `https://hiandra.pythonanywhere.com/`
  * Retorna uma saudação de boas-vindas.

* **Saudação Personalizada (Link dinâmico):** `https://hiandra.pythonanywhere.com/user/hBISPO98`
  * 💡 *Nota para quem for testar:* Você deve alterar `<hBISPO98>` para qualquer palavra ou nome que desejar na URL (Exemplo: `/user/Radia Perlman` ou `/user/Tim Berners`).
  * Retorna uma saudação personalizada com o nome informado.

* **Contexto da Requisição:** `https://hiandra.pythonanywhere.com/contextorequisicao`
  * Exibe informações sobre o navegador (User-Agent) de quem fez a requisição.

* **Código de Status Diferente:** `https://teixeif.pythonanywhere.com/codigostatusdiferente`
  * Retorna a mensagem "Bad request" acompanhada do código de status HTTP `400`.

* **Objeto de Resposta com Cookie:** `https://hiandra.pythonanywhere.com/objetoresposta`
  * Retorna um documento e define um cookie (`language, pt-BR`, verificável ao inspecionar a página) no navegador.

* **Redirecionamento:** `https://hiandra.pythonanywhere.com/ifsp`
  * Redireciona automaticamente o navegador para o site oficial do IFSP (Pirituba).

* **Cancelar Requisição:** `https://hiandra.pythonanywhere.com/cancelar`
)`
  * Interrompe a requisição gerando um erro HTTP `404 Not Found`.
