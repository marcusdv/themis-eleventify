# Themis Furigo - Eleventy Setup

## Estrutura do Projeto

```
themis-elev/
├── src/                    # Pasta de código-fonte
│   ├── _layouts/          # Layouts reutilizáveis (templates)
│   ├── _includes/         # Componentes reutilizáveis
│   ├── _data/             # Dados JSON para templates
│   ├── assets/            # CSS, JS, imagens
│   └── *.html             # Páginas do site
├── _output/               # Pasta gerada (build output)
├── .eleventy.js           # Configuração do Eleventy
├── package.json           # Dependências
└── README.md
```

## Comandos Disponíveis

```bash
# Build para produção
npm run build

# Desenvolvimento com hot-reload
npm run dev

# Watch mode (rebuild ao alterar arquivos)
npm run watch
```

## Como Usar

1. **Editar páginas**: Modifique os arquivos `.html` em `src/`
2. **Adicionar componentes reutilizáveis**: Crie em `src/_includes/`
3. **Criar layouts**: Adicione em `src/_layouts/`
4. **Adicionar dados**: Use JSON em `src/_data/`

## Próximos Passos

1. Extrair **header** comum para `src/_includes/header.html`
2. Extrair **footer** comum para `src/_includes/footer.html`
3. Criar **layout base** em `src/_layouts/base.html`
4. Converter páginas para usar frontmatter YAML
5. Refatorar CSS e JavaScript para modularização

## Deploy em LocalWeb

Após fazer `npm run build`, upload a pasta `_output/` para LocalWeb.
