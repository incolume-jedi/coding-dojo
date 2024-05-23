# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**API Translation**

Construir um módulo que consuma os serviços da API de tradução disponível em https://www.deepl.com/docs-api.

## Exemplos

`EXAMPLE REQUEST`
```
curl -X POST 'https://api-free.deepl.com/v2/translate' \
--header 'Authorization: DeepL-Auth-Key [yourAuthKey]' \
--data-urlencode 'text=Hello, world!' \
--data-urlencode 'target_lang=DE'
```
`EXAMPLE RESPONSE`
```
{
  "translations": [
    {
      "detected_source_language": "EN",
      "text": "Hallo, Welt!"
    }
  ]
}
```

## Artefatos

- [dojo](./__init__.py)
- [tests](./test_20240515.py)


## Referências

A [API do DeepL](https://www.deepl.com/docs-api). oferece acesso à tecnologia de tradução automática do DeepL, tornando possível introduzir recursos de tradução de alta qualidade diretamente nos seus sites e aplicativos.
- https://www.deepl.com/pt-BR/pro/select-country?cta=apiDocsHeader#developer
- https://developers.deepl.com/docs/getting-started/your-first-api-request
- https://github.com/DeepLcom/deepl-python
