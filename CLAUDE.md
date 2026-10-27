# Instituto Themis Furigo — site (Eleventy)

Site estático gerado com Eleventy (11ty), Liquid templates, sem framework JS. Código-fonte em `src/`, build gerado em `_output/` (ignorado no git do projeto principal, mas `_output/` tem seu próprio repositório git separado — ver abaixo).

## Comandos de build

```bash
npm run build          # build normal — para Vercel (site na raiz do domínio)
npm run build:staging  # build para staging — para FileZilla/FTP (site em /statico/)
npm run dev             # servidor local com hot-reload
npm run watch           # apenas watch, sem servidor
```

### Por que existem dois comandos de build

Todos os assets (CSS, JS, imagens, vídeos) são referenciados no código-fonte através do filtro `url` do Eleventy:

```liquid
<link rel="stylesheet" href="{{ '/assets/css/style.css' | url }}" />
```

Esse filtro aplica automaticamente o `pathPrefix` configurado no momento do build:

- **Vercel**: o site fica na raiz do domínio → `npm run build` (sem prefixo) → gera `/assets/css/style.css`.
- **Staging** (`http://staging.institutotf.ong.br/statico/`): o site fica hospedado dentro da subpasta `/statico/`, não na raiz → `npm run build:staging` (roda `eleventy --pathprefix=/statico/`) → gera `/statico/assets/css/style.css`.

**Nunca** use caminhos absolutos hardcoded (`href="/assets/..."`) direto no HTML — sempre use `{{ '/assets/...' | url }}`. Se um caminho hardcoded for commitado, ele volta a quebrar no staging (CSS/JS somem, só o HTML aparece, porque o navegador tenta buscar o asset na raiz do domínio em vez de dentro de `/statico/`).

### Deploy para staging (manual via FileZilla)

1. `npm run build:staging`
2. Enviar o **conteúdo** da pasta `_output/` (não a pasta em si) para dentro de `/statico/` no servidor.
3. Conferir em `http://staging.institutotf.ong.br/statico/`.

Os dois comandos de build escrevem no mesmo `_output/` — sempre rodar o comando certo logo antes do deploy correspondente (não reaproveitar um `_output` gerado para o outro destino).

### `_output/` tem repositório git próprio

A pasta `_output/` contém um repositório git **separado** do repositório principal do código-fonte, apontando para `github.com/marcusdv/instituto.git` (diferente do repo do código-fonte, `github.com/marcusdv/themis-eleventify.git`). Isso é intencional — não é um erro de configuração.
