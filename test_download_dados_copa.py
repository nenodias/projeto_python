# *-* coding:utf-8 *-*
import unittest
from unittest import mock
from download_dados_copa import download_length, download, BUFF_SIZE

class DownloadTest(unittest.TestCase):

    def teste_download_with_know_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect=['Data']*2)

        output = mock.MagicMock()

        download_length(response, output, 1025)

        # Terei duas chamadas recebendo o parâmetro BUFF_SIZE
        chamadas = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]

        response.read.assert_has_calls(chamadas)
        # Irá executar o método e verificar as chamadas se são iguais (ordem e parâmetros)

        # Terei duas chamadas recebendo o parâmetro 'Data'
        chamadas = [mock.call('Data'), mock.call('Data')]

        output.write.assert_has_calls(chamadas)
        # Irá executar o método e verificar as chamadas se são iguais (ordem e parâmetros)

    def teste_download_with_no_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect = ['data', 'more data', ''])

        output = mock.MagicMock()
        output.write = mock.MagicMock()

        download(response, output)

        # 3 items do side effect
        chamadas = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]
        response.read.assert_has_calls(chamadas)

        # 2 itens, pois o vazio para a leitura do response
        chamadas = [mock.call('data'), mock.call('more data')]
        output.write.assert_has_calls(chamadas)
