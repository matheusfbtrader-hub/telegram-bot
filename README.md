# 🤖 Bot de Automação para Telegram

Projeto desenvolvido para automatizar o atendimento e o direcionamento de usuários em uma comunidade relacionada ao mercado financeiro.

O bot foi criado a partir de uma necessidade real: organizar o fluxo de entrada de usuários e direcioná-los automaticamente de acordo com suas escolhas, reduzindo etapas manuais no atendimento.

## 🚀 Funcionalidades

- Interação automática através do comando `/start`
- Menu com botões interativos
- Direcionamento de usuários conforme a opção selecionada
- Fluxos condicionais de atendimento
- Redirecionamento para páginas externas
- Liberação e direcionamento para canal no Telegram

## 🛠️ Tecnologias utilizadas

- Python
- Telegram Bot API
- python-telegram-bot
- Programação assíncrona
- Lógica de programação
- Variáveis de ambiente para proteção de credenciais
## 🔐 Segurança

As credenciais utilizadas pelo bot não são armazenadas diretamente no código-fonte. O token da API é carregado através de variável de ambiente.

Exemplo:

```python
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
 ```
## 💡 Sobre o projeto

Este projeto surgiu antes do início da minha graduação em Análise e Desenvolvimento de Sistemas e representa uma das minhas primeiras experiências práticas com automação e programação aplicada a uma necessidade real.

Atualmente, continuo aprimorando meus conhecimentos em desenvolvimento de software, Python, Java, HTML, algoritmos e lógica de programação.

## 👨‍💻 Autor

Matheus Henrique
Estudante de Análise e Desenvolvimento de Sistemas — UNISUAM

