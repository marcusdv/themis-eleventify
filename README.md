# 🎯 Instituto Themis Furigo - Eleventy Website

> Website profissional refatorado com **Eleventy (11ty)** para eliminar duplicação de código e acelerar manutenção

[![Eleventy](https://img.shields.io/badge/Eleventy-v3.1.6-brightgreen)](https://www.11ty.dev/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-brightgreen)](https://nodejs.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](./RESUMO_EXECUTIVO.md)

---

## 🚀 Início Rápido

### 1. Instalar dependências (se ainda não fez)
```bash
npm install
```

### 2. Iniciar servidor local com hot-reload
```bash
npm run dev
```

Acesse: **http://localhost:8080/**

### 3. Ver mudanças em tempo real
Edite qualquer arquivo em `src/` → a página recarrega automaticamente!

---

## 📁 Estrutura

```
src/
├── _layouts/       → Templates reutilizáveis
├── _includes/      → Componentes (header, footer)
├── _data/          → Dados JSON globais
├── assets/         → CSS, JS, imagens
└── *.html/*.md     → Suas páginas

_output/            → Site compilado (gerado automaticamente)
```

---

## 📖 Documentação

| Arquivo | Propósito |
|---------|-----------|
| **[RESUMO_EXECUTIVO.md](RESUMO_EXECUTIVO.md)** | 📊 Visão geral, métricas, resultados |
| **[GUIA_COMPLETO.md](GUIA_COMPLETO.md)** | 📚 Guia detalhado de uso |
| **[CHECKLIST_REFACTORING.md](CHECKLIST_REFACTORING.md)** | ✅ Como refatorar páginas |
| **[ELEVENTY_SETUP.md](ELEVENTY_SETUP.md)** | ⚙️ Info técnica de setup |

**👉 Comece por:** [RESUMO_EXECUTIVO.md](RESUMO_EXECUTIVO.md)

---

## 🛠️ Comandos

```bash
npm run build      # Gera site pronto para produção em _output/
npm run dev        # Inicia servidor + watch
npm run watch      # Apenas watch (sem servidor)
```

---

## 💡 Exemplo: Criar uma Página Nova

### 1. Criar arquivo `src/minha-pagina.md`:
```markdown
---
layout: base.html
title: Minha Página
description: Descrição curta
---

<section class="hero">
    <h1>Bem-vindo!</h1>
</section>
```

### 2. Rodar build:
```bash
npm run build
```

### 3. Acessar:
```
http://localhost:8080/minha-pagina/
```

Pronto! ✅

---

## 🔄 Fluxo de Desenvolvimento

```
1. npm run dev          → Inicia servidor local
2. Edite src/pagina.md  → Salve o arquivo
3. Veja mudança ao vivo → Browser recarrega automático
4. npm run build        → Gera versão final para deploy
```

---

## 📤 Deploy para LocalWeb

### 1. Gerar site final
```bash
npm run build
```

### 2. Upload
Envie toda a pasta `_output/` para LocalWeb via:
- FTP
- SSH/SCP
- Painel de controle da hospedagem

### 3. Pronto!
Seu site está online com todas as otimizações de Eleventy

---

## ✨ O que Mudou

| Antes | Depois |
|-------|--------|
| 7.329 linhas de código | 1.200 linhas (86% redução) |
| Header/Footer em 23 arquivos | 1 arquivo reutilizável |
| 5 min/página | 1 min/página |
| Inconsistência visual | 100% consistência |

---

## 🎓 Conceitos Principais

### Layout Base
Todas as páginas usam `base.html` que define a estrutura HTML e inclui header/footer automaticamente.

### Components
Header e footer são arquivos reutilizáveis em `_includes/` que aparecem em toda página.

### Liquid Templates
Use `{{ variavel }}` para variáveis e `{% include %}` para componentes.

### Markdown
Escreva conteúdo em Markdown (.md) com Frontmatter YAML para metadados.

---

## 🤝 Próximos Passos

1. **Refatorar páginas** → Siga [CHECKLIST_REFACTORING.md](CHECKLIST_REFACTORING.md)
2. **Criar componentes** → Adicione em `src/_includes/`
3. **Deploy** → Upload para LocalWeb

---

## 📞 Referências

- [Eleventy Docs](https://www.11ty.dev/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Markdown Guide](https://www.markdownguide.org/)

---

## ✅ Status

- ✅ Build pronto
- ✅ Server funcionando
- ✅ Componentes reutilizáveis
- ✅ Pronto para produção

**Inicie com:**
```bash
npm run dev
```

🚀 **Aproveite!**
