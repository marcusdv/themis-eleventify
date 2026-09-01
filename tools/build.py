#!/usr/bin/env python3
"""
Gerador estático do site do Instituto Themis Furigo.

Como funciona:
- tools/partials/header.html e footer.html guardam o cabeçalho e rodapé únicos do site.
- tools/pages/*.html guardam SOMENTE o conteúdo de cada página (sem <html>/<head>/header/footer).
- Este script junta tudo e grava o HTML final na raiz do repositório.

Para editar um texto do menu ou do rodapé: edite tools/partials/header.html ou footer.html
e rode `python3 tools/build.py` novamente para atualizar todas as páginas de uma vez.

Para editar o conteúdo de uma página: edite o arquivo correspondente em tools/pages/
e rode o build novamente.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTIALS = ROOT / "tools" / "partials"
PAGES = ROOT / "tools" / "pages"

HEADER = (PARTIALS / "header.html").read_text(encoding="utf-8")
FOOTER = (PARTIALS / "footer.html").read_text(encoding="utf-8")

DOC = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="data:image/svg+xml,{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
</head>
<body>
{header}
{content}
{footer}
<script src="assets/js/main.js"></script>
</body>
</html>
"""

FAVICON = "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%230B2545'/%3E%3Ctext x='50' y='66' font-size='48' font-family='Arial' font-weight='800' fill='%23F2622E' text-anchor='middle'%3ETF%3C/text%3E%3C/svg%3E"

# (arquivo de conteúdo, título da aba, descrição, item ativo do menu, arquivo de saída)
PAGES_MAP = [
    ("index.html", "Instituto Themis Furigo | Transformando vidas através da educação, saúde, tecnologia e sustentabilidade", "ONG que atua em saúde, empreendedorismo feminino, agricultura familiar, moda sustentável e tecnologia/IA para gerar oportunidades reais de transformação social.", "home", "index.html"),
    ("quem-somos.html", "Quem Somos | Instituto Themis Furigo", "História, missão, visão, valores e compromisso do Instituto Themis Furigo com os Objetivos de Desenvolvimento Sustentável da ONU.", "quem-somos", "quem-somos.html"),
    ("projetos.html", "Projetos | Instituto Themis Furigo", "Conheça os projetos do Instituto Themis Furigo em saúde, empreendedorismo feminino, infância, agricultura familiar, moda sustentável e tecnologia.", "projetos", "projetos.html"),
    ("projeto-saude-para-todos.html", "Saúde para Todos | Instituto Themis Furigo", "Consultas, exames e procedimentos gratuitos para quem não tem acesso à saúde de qualidade.", "projetos", "projeto-saude-para-todos.html"),
    ("projeto-potencia-feminina.html", "Potência Feminina | Instituto Themis Furigo", "Capacitação gratuita de mulheres em empregabilidade, empreendedorismo e programação, em parceria com Google e Rede Mulher Empreendedora.", "projetos", "projeto-potencia-feminina.html"),
    ("projeto-florescer.html", "Florescer | Instituto Themis Furigo", "Atendimento terapêutico e psicológico para promover o bem-estar emocional de crianças e famílias em vulnerabilidade.", "projetos", "projeto-florescer.html"),
    ("projeto-agrofloresta-viva.html", "Agrofloresta Viva | Instituto Themis Furigo", "Agricultura familiar regenerativa e segurança alimentar para comunidades em vulnerabilidade.", "projetos", "projeto-agrofloresta-viva.html"),
    ("projeto-curio-look-lab.html", "Curió Look Lab | Instituto Themis Furigo", "Costura sustentável e economia circular: renda para mulheres através da moda consciente.", "projetos", "projeto-curio-look-lab.html"),
    ("projeto-tecnologia-ia.html", "Educação do Futuro: IA e Realidade Virtual | Instituto Themis Furigo", "Capacitação profissional de jovens em programação, Inteligência Artificial e Realidade Virtual.", "projetos", "projeto-tecnologia-ia.html"),
    ("historico.html", "Histórico de Projetos | Instituto Themis Furigo", "Conheça os grandes projetos já realizados pelo Instituto Themis Furigo, como o Heróis Usam Máscaras e o Hortifruti Solidário.", "historico", "historico.html"),
    ("blog.html", "Blog e Notícias | Instituto Themis Furigo", "Portal de notícias, histórias reais e conteúdo sobre saúde, mulheres, agricultura familiar, tecnologia, ESG e muito mais.", "blog", "blog.html"),
    ("blog-cop30.html", "O que a COP30 significa para as ONGs brasileiras | Blog ITF", "Como a COP30, em Belém, impacta o financiamento climático e as organizações sociais brasileiras.", "blog", "blog-cop30.html"),
    ("blog-realidade-virtual-educacao.html", "O impacto da realidade virtual na educação profissional | Blog ITF", "Como óculos de realidade virtual estão sendo usados para capacitar jovens no Instituto Themis Furigo.", "blog", "blog-realidade-virtual-educacao.html"),
    ("blog-moda-sustentavel.html", "Moda sustentável gera renda para mulheres | Blog ITF", "Como o projeto Curió Look Lab transforma retalhos e tempo ocioso em renda e autonomia.", "blog", "blog-moda-sustentavel.html"),
    ("blog-imposto-de-renda.html", "Como doar parte do Imposto de Renda para projetos sociais | Blog ITF", "Passo a passo para destinar parte do seu IR devido a organizações da sociedade civil.", "blog", "blog-imposto-de-renda.html"),
    ("transparencia.html", "Transparência | Instituto Themis Furigo", "Estatuto, certificados, prestação de contas, relatórios e governança do Instituto Themis Furigo.", "transparencia", "transparencia.html"),
    ("empresas.html", "Para Empresas | Instituto Themis Furigo", "Patrocínio, leis de incentivo fiscal, ESG e projetos personalizados para empresas parceiras.", "empresas", "empresas.html"),
    ("voluntarios.html", "Seja Voluntário | Instituto Themis Furigo", "Ofereça seu tempo e talento para transformar vidas junto ao Instituto Themis Furigo.", "voluntarios", "voluntarios.html"),
    ("parceiros.html", "Parceiros | Instituto Themis Furigo", "Empresas, institutos e órgãos públicos que apoiam os projetos do Instituto Themis Furigo.", "parceiros", "parceiros.html"),
    ("como-ajudar.html", "Como Ajudar | Instituto Themis Furigo", "Seja voluntário, seja parceiro, compre na Curió Look ou contribua financeiramente com os projetos do Instituto Themis Furigo.", "como-ajudar", "como-ajudar.html"),
    ("contato.html", "Contato | Instituto Themis Furigo", "Fale com o Instituto Themis Furigo: endereço, telefone, e-mail e redes sociais.", "contato", "contato.html"),
]


def build():
    for content_file, title, description, active, out_file in PAGES_MAP:
        content_path = PAGES / content_file
        if not content_path.exists():
            print(f"[AVISO] Conteúdo ausente, pulando: {content_file}")
            continue
        content = content_path.read_text(encoding="utf-8")
        header = inject_active(HEADER, active)
        html = DOC.format(
            title=title,
            description=description,
            favicon=FAVICON,
            header=header,
            content=content,
            footer=FOOTER,
        )
        (ROOT / out_file).write_text(html, encoding="utf-8")
        print(f"[OK] {out_file}")


def inject_active(header, active):
    def repl(match):
        classes = match.group(1)
        key = match.group(2)
        if key == active:
            if "active" not in classes:
                classes = (classes + " active").strip()
        else:
            classes = re.sub(r"\bactive\b", "", classes).strip()
        return f'class="{classes}" data-nav="{key}"'

    return re.sub(r'class="([^"]*)"\s+data-nav="([^"]+)"', repl, header)


if __name__ == "__main__":
    build()
