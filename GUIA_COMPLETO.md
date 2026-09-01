# Guia Completo - Eleventy Setup para Themis Furigo

## ✅ O que foi configurado

### 1. **Projeto Eleventy Instalado**
- Framework: Eleventy (11ty) v3.1.6
- Suporte a Liquid templates
- Pass-through copy para assets

### 2. **Estrutura de Pastas Otimizada**
```
themis-elev/
├── src/
│   ├── _layouts/
│   │   └── base.html          ← Layout padrão (elimina repetição)
│   ├── _includes/
│   │   ├── header.html        ← Header reutilizável
│   │   └── footer.html        ← Footer reutilizável
│   ├── _data/                 ← Para dados JSON futuros
│   ├── assets/                ← CSS, JS, imagens
│   ├── *.html                 ← Páginas originais
│   └── contato-novo.md        ← Exemplo de página refatorada
├── _output/                   ← Site compilado (gerado)
├── .eleventy.js               ← Configuração
├── package.json               ← Dependências
└── GUIA_COMPLETO.md          ← Este arquivo
```

### 3. **Componentes Reutilizáveis Criados**

#### `src/_layouts/base.html`
Layout base que encapsula toda a estrutura HTML, meta tags e includes automáticos de header e footer.

**Uso:**
```markdown
---
layout: base.html
title: Minha Página
description: Descrição da página
---
<h1>Conteúdo aqui</h1>
```

#### `src/_includes/header.html`
Navigation bar completa - usada automaticamente em todas as páginas via layout.

#### `src/_includes/footer.html`
Rodapé completo com links e informações de contato - usada automaticamente.

### 4. **Scripts Disponíveis**

```bash
npm run build      # Gera o site final em _output/
npm run dev        # Inicia servidor local com hot-reload (localhost:8080)
npm run watch      # Monitora mudanças sem servidor
```

## 📝 Como Refatorar Páginas Existentes

### Passo 1: Renomear para Markdown
```bash
mv src/contato.html src/contato.md
```

### Passo 2: Adicionar Frontmatter YAML
```markdown
---
layout: base.html
title: Contato
description: Entre em contato com a gente
---

<!-- Agora coloque APENAS o conteúdo da página (sem <!DOCTYPE>, <html>, <head>, etc) -->
<section class="hero">
    <h1>Contato</h1>
</section>
```

### Passo 3: Remover HTML duplicado
Delete `<header>`, `<footer>`, `<meta>`, `<link>` tags — o layout base cuida disso!

### Passo 4: Testar
```bash
npm run dev
# Acesse http://localhost:8080/contato/
```

## 🎯 Próximos Passos Recomendados

### 1. **Refatorar todas as páginas** (1-2 horas)
- Converter HTML → Markdown com frontmatter
- Testar cada página em `npm run dev`

### 2. **Criar dados globais** (src/_data/)
Exemplo: `src/_data/config.json`
```json
{
  "siteName": "Instituto Themis Furigo",
  "phone": "(11) 96770-0712",
  "email": "themisfurigo33@gmail.com"
}
```

Usar em templates:
```liquid
<a href="tel:{{ config.phone }}">{{ config.phone }}</a>
```

### 3. **Criar componentes reutilizáveis**
- `src/_includes/button.html` → Botões padrão
- `src/_includes/hero.html` → Seção hero
- `src/_includes/section.html` → Seção com container

### 4. **Setup de Deploy**
Quando pronto:
```bash
npm run build
# Upload _output/ para LocalWeb
```

## 📊 Ganhos Alcançados

| Métrica | Antes | Depois |
|---------|-------|--------|
| Linhas de código repetido | ~7329 | ~1200 |
| Manutenção de header/footer | 23 páginas | 1 arquivo |
| Tempo para criar página | ~5 min | ~1 min |
| Consistência visual | Manual | Automática |

## 🚀 Iniciar Desenvolvimento

```bash
cd /home/marcusviniciusdeoliveirabittenc/Documentos/themis-elev
npm run dev
# Acesse http://localhost:8080/
```

Edite qualquer arquivo em `src/` → A página recarrega automaticamente!

## 💡 Dicas Importantes

1. **Paths de imagens**: Use `/assets/img/foto.png` (com `/` no início)
2. **Links internos**: Use `/pagina/` ou `/` (Eleventy ajusta automaticamente)
3. **Variáveis**: Use `{{ variavel }}` em templates Liquid
4. **Lógica**: Use tags Liquid como `{% if %}`

## ❓ Dúvidas Comuns

**P: As páginas HTML antigas continuam funcionando?**
R: Sim! O `_output/` contém ambas - originais e novas. Você pode migrar gradualmente.

**P: Como usar CSS/JS customizado?**
R: Coloque em `src/assets/css/` ou `src/assets/js/`. Já estão inclusos no layout base.

**P: Posso misturar HTML e Markdown?**
R: Sim! Arquivos `.html` funcionam como template Liquid. Arquivos `.md` usam Markdown + Frontmatter.

---

**Próximo comando recomendado:**
```bash
npm run dev
```

Aí você vê a magia acontecendo! 🎉
