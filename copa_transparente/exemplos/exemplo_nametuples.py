# *-* coding:utf-8 *-*
import os
from collections import namedtuple

ExecucaoFinanceira namedtuple('ExecucaoFinanceira', 
    [
    'IdExecucaoFinanceira',
    'IdEmpreendimento',
    'IdInstituicaoContratado',
    'IdPessoaFisicaContratado',
    'IdLicitacao',
    'ValContrato',
    'ValTotal',
    'DatAssinatura',
    'DatInicioVigencia',
    'DatFinalVigencia',
    ])

execucao = ExecucaoFinanceira(
    '1',
    '2',
    '132',
    '-1',
    '76',
    '696648466.09',
    '0',
    '19/03/2010',
    '23/03/2010',
    '05/10/2013',
    )

print( execucao.ValContrato )
print( execucao )