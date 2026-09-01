# Checklist de Refatoração - Eleventy

Use este checklist para refatorar gradualmente suas páginas HTML para o novo sistema Eleventy com componentes reutilizáveis.

## ✅ Fase 1: Setup (Concluído)
- [x] Eleventy instalado
- [x] Estrutura de pastas criada
- [x] Layout base criado
- [x] Header e footer como componentes reutilizáveis
- [x] Build testado com sucesso

## 📋 Fase 2: Refatoração de Páginas

### Páginas Principais (Prioridade Alta)
- [ ] `index.html` → `index.md` (homepage é crítica)
- [ ] `quem-somos.html` → `quem-somos.md`
- [ ] `projetos.html` → `projetos.md`
- [ ] `blog.html` → `blog.md`

### Páginas de Projetos (Prioridade Média)
- [ ] `projeto-saude-para-todos.html` → `projeto-saude-para-todos.md`
- [ ] `projeto-potencia-feminina.html` → `projeto-potencia-feminina.md`
- [ ] `projeto-florescer.html` → `projeto-florescer.md`
- [ ] `projeto-agrofloresta-viva.html` → `projeto-agrofloresta-viva.md`
- [ ] `projeto-curio-look-lab.html` → `projeto-curio-look-lab.md`
- [ ] `projeto-tecnologia-ia.html` → `projeto-tecnologia-ia.md`

### Blog Posts (Prioridade Média)
- [ ] `blog.html` → `blog.md`
- [ ] `blog-cop30.html` → `blog/cop30.md`
- [ ] `blog-imposto-de-renda.html` → `blog/imposto-de-renda.md`
- [ ] `blog-moda-sustentavel.html` → `blog/moda-sustentavel.md`
- [ ] `blog-realidade-virtual-educacao.html` → `blog/realidade-virtual-educacao.md`

### Páginas Institucionais (Prioridade Baixa)
- [ ] `contato.html` → `contato.md` (já existe exemplo: contato-novo.md)
- [ ] `como-ajudar.html` → `como-ajudar.md`
- [ ] `voluntarios.html` → `voluntarios.md`
- [ ] `empresas.html` → `empresas.md`
- [ ] `parceiros.html` → `parceiros.md`
- [ ] `historico.html` → `historico.md`
- [ ] `transparencia.html` → `transparencia.md`

## 🔧 Processo de Refatoração para Cada Página

### Exemplo Completo: `contato.html` → `contato.md`

**Antes (contato.html):**
```html
<!doctype html>
<html lang="pt-BR">
    <head>
        <meta charset="utf-8" />
        <title>Contato | Instituto Themis Furigo</title>
        <!-- ... 30+ linhas de head -->
    </head>
    <body>
        <header class="site-header">
            <!-- Header completo aqui (90+ linhas) -->
        </header>
        
        <section class="hero">
            <h1>Contato</h1>
        </section>
        
        <footer class="site-footer">
            <!-- Footer completo aqui (80+ linhas) -->
        </footer>
    </body>
</html>
```

**Depois (contato.md):**
```markdown
---
layout: base.html
title: Contato
description: Entre em contato com o Instituto Themis Furigo
---

<section class="hero">
    <h1>Contato</h1>
</section>
```

### Passo-a-Passo:

1. **Duplicar o arquivo**
   ```bash
   cp src/contato.html src/contato.md
   ```

2. **Adicionar Frontmatter YAML no topo**
   ```markdown
   ---
   layout: base.html
   title: Título da Página
   description: Descrição curta (50-160 caracteres)
   ---
   ```

3. **Remover do conteúdo:**
   - `<!DOCTYPE html>`
   - `<html>`
   - Tudo dentro de `<head>`
   - O `<header>` completo
   - O `<footer>` completo
   - Tags `</html>` e `</body>`
   - Scripts de year do footer (já incluído no layout)

4. **Manter apenas:**
   - Conteúdo entre `<header>` e `<footer>`
   - As seções, artigos, divs etc

5. **Testar**
   ```bash
   npm run dev
   # Abra http://localhost:8080/contato/
   # Verifique se parece igual ao original
   ```

6. **Comparar com original**
   - Layout igual? ✅
   - Cores iguais? ✅
   - Tipografia igual? ✅
   - Links funcionam? ✅

7. **Deletar versão antiga**
   ```bash
   rm src/contato.html
   ```

8. **Fazer build final**
   ```bash
   npm run build
   # Verifique _output/contato/index.html
   ```

## 📊 Progresso

```
Total de páginas: 23
Refatoradas: 1 (contato-novo)
Pendentes: 22
```

**Tempo estimado:** 2-3 horas (1-2 minutos por página)

## 🎯 Validação Pós-Refatoração

Para cada página refatorada:
- [ ] Build sem erros: `npm run build`
- [ ] Página acessa em `http://localhost:8080/...`
- [ ] Visual idêntico ao original
- [ ] Links internos funcionam
- [ ] Links externos funcionam
- [ ] Formulários funcionam
- [ ] Imagens carregam corretamente

## 📝 Notas

- Você pode refatorar gradualmente - páginas velhas e novas coexistem
- Quando todos estiverem em Markdown, limpe a pasta de `.html`
- Considere criar um redirector 301 no servidor para URLs antigas

## 🚀 Próxima Fase: Componentes Reutilizáveis

Depois de refatorar todas as páginas, você pode:

1. Criar `src/_includes/hero.html` - reutilizar hero sections
2. Criar `src/_includes/button.html` - botões padronizados
3. Criar `src/_includes/project-card.html` - cards de projeto
4. Criar `src/_data/projects.json` - lista centralizada de projetos

Isso reduzirá ainda mais a repetição!
