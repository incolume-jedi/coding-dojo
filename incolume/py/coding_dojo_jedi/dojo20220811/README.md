# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**TDD UnitTest**

Baseado no exercício [TDD para Unittest ](https://bitbucket.org/incolume-dev/calculadora_unittest)

```python
# tests.py
import unittest
import re
import sys
import requests
from dojo import calculadora


def check_connectivity(url: str = 'https://google.com'):
    try:
        req = requests.get(url)
        if req.status_code != 200:
            raise ConnectionError('Not connected')
        return True
    except ConnectionError:
        return False


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Pré-configuração da classe
        ...

    def setUp(self) -> None:
        # Preconfiguração para métodos
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        # Método chamado imediatamente após concluir o método de teste
        pass

    def tearDown(self) -> None:
        # Método chamado imediatamente após concluir a classe de teste
        pass

    @unittest.skip("Futuring work")
    class MySkippedTestCase(unittest.TestCase):
        def test_not_run(self):
            pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        """windows specific testing code"""
        pass

    @unittest.skipUnless(sys.platform.startswith("mac"), "requires MacOS")
    def test_mac_support(self):
        """MacOS specific testing code"""
        pass

    @unittest.skipUnless(sys.platform.startswith("lin"), "requires Linux")
    def test_linux_support(self):
        """Linux specific testing code"""
        pass

    def test_maybe_skipped(self):
        """test code that depends on the external resource"""
        if not check_connectivity():
            self.skipTest("external resource not available")
        pass

    def test_something(self):
        """Este teste nunca irá passar.

        Defina um skip com a mensagem 'Dont ran'.
        """
        self.assertEqual(True, False)

    def test_soma(self):
        self.assertEqual(calculadora('+', 3, '4'), 7)

    def test_soma_float(self):
        self.assertEqual(calculadora('+', 3, 4), 7.0)

    def test_menos(self):
        self.assertEqual(calculadora('-', '3', 4), -1)

    def test_menos_float(self):
        self.assertEqual(calculadora('-', 3.0, 4), -1.0)

    def test_mult(self):
        self.assertEqual(calculadora('*', 3, '4'), 12)

    def test_mult_float(self):
        self.assertEqual(calculadora('*', 3, '4.0'), 12.0)

    def test_dividir(self):
        self.assertEqual(calculadora('/', 3, '4'), .75)

    def test_dividir_float(self):
        self.assertEqual(calculadora('/', 4, 4.0), 1.0)
        self.assertEqual(calculadora('/', 4, 3), 1.3333333333333333)

    def test_mod(self):
        self.assertEqual(calculadora('%', 4, 3), 1)
        self.assertEqual(calculadora('%', 12, 7), 5)

    def test_pow(self):
        self.assertEqual(calculadora('**', 3, 4), 81)

    def test_dividir_except(self):
        with self.assertRaisesRegex(ValueError, r'.*y deve ser diferente de 0.*'):
            calculadora('/', 3, 0)
            calculadora('//', 3, 0)
            calculadora('//', 3, '0')

    def test_operador(self):
        with self.assertRaisesRegex(ValueError, re.escape("Operador inválido. Use: +, -, *, **, //, /, %")):
            calculadora('^', 3, 5)

    def test_numeric_values(self):
        with self.assertRaisesRegex(ValueError, "x e y devem ser valores numéricos reais."):
            calculadora('+', 'a', 'b')
            calculadora('+', '0', 'b')
            calculadora('+', 'a', '0')


if __name__ == '__main__':
    unittest.main()

```

## Exemplos

Para executar os testes desenvolvidos para TDD, rode o camando abaixo:

```bash
python -m unittest tests.py
```

## Artefatos

- [dojo](./dojo20220811.py)
- [tests](./test_20220811.py)

## Referências

https://bitbucket.org/incolume-dev/calculadora_unittest
