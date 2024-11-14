"""dojo module."""

artefatos: list[str] = [
    r'https://www.python.org/static/community_logos/python-powered-h-50x65.png',
    r'https://www.python.org/static/community_logos/python-powered-h.svg',
    r'https://www.python.org/static/community_logos/python-logo-master-v3-TM.psd',
    r'https://www.gov.br/ana/pt-br/todos-os-documentos-do-portal/doc-modelo.pdf/@@download/file/doc-modelo.pdf',
    r'https://portal.ead.senasp.gov.br/noticias/ciclos/resultado-preliminar-2013-selecao-de-tutores-ajap-va-1/modelo-de-declaracao.docx/@@download/file/MODELO%20DE%20DECLARA%C3%87%C3%83O.docx',
]


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
