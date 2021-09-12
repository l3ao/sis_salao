from utils import carregar_json
from django.conf import settings
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from tabelasbasicas.models import Categoria, UnidMedida, TipoPagamento
from produtos.models import Produto


def import_db():
    # tabelas de pessoas (cliente e fornecedor)
    try:
        clientes = carregar_json(settings.BASE_DIR / 'importacao/json/clientes.json')
        for cliente in clientes:
            exists_cli = Cliente.objects.filter(nome=cliente['nome']).exists()
            if not exists_cli:
                Cliente.objects.create(
                    nome = cliente['nome'],
                    data_nasc = cliente['data_nasc'] if cliente['data_nasc'] != "None" else None,
                    telefone = cliente['telefone'],
                    endereco = cliente['endereco'],
                )
        print('Clientes cadastrados..')

        fornecedores = carregar_json(settings.BASE_DIR / 'importacao/json/fornecedores.json')
        for fornecedor in fornecedores:
            exists_fornec = Fornecedor.objects.filter(nome=fornecedor['nome']).exists()
            if not exists_fornec:
                Fornecedor.objects.create(
                    nome = fornecedor['nome'],
                    rsocial = fornecedor['rsocial'],
                    ie = fornecedor['ie'],
                    cnpj = fornecedor['cnpj'],
                    cep = fornecedor['cep'],
                    endereco = fornecedor['endereco'],
                    bairro = fornecedor['bairro'],
                    fone = fornecedor['fone'],
                    cel = fornecedor['cel'],
                    email = fornecedor['email'],
                    endnumero = fornecedor['endnumero'],
                    cidade = fornecedor['cidade'],
                    estado = fornecedor['estado']
                )
        print('Fornecedores cadastrados..')

        # tabelas básicas (categorias, unidades de medidas, tipos de pagamento)
        categorias = carregar_json(settings.BASE_DIR / 'importacao/json/categoria.json')
        for categoria in categorias:
            exists_categ = Categoria.objects.filter(descricao=categoria['descricao'])
            if not exists_categ:
                Categoria.objects.create(
                    sigla=categoria['sigla'],
                    descricao=categoria['descricao'],
                )
        print('Categorias cadastradas..')

        unidmedidas = carregar_json(settings.BASE_DIR / 'importacao/json/unidmedida.json')
        for unidade in unidmedidas:
            exists_unid = UnidMedida.objects.filter(descricao=unidade['descricao'])
            if not exists_unid:
                UnidMedida.objects.create(
                    sigla=unidade['sigla'],
                    descricao=unidade['descricao'],
                )
        print('Unidade de medidas cadastradas..')

        tipospagamento = carregar_json(settings.BASE_DIR / 'importacao/json/tipopagamento.json')
        for pagamento in tipospagamento:
            exists_pagamento = TipoPagamento.objects.filter(descricao=pagamento['descricao'])
            if not exists_pagamento:
                TipoPagamento.objects.create(
                    sigla=pagamento['sigla'],
                    descricao=pagamento['descricao'],
                )
        print('Tipos de pagamento cadastrados..')

        # produtos
        produtos = carregar_json(settings.BASE_DIR / 'importacao/json/produtos.json')
        for produto in produtos:
            exists_prod = Produto.objects.filter(desc_nf=produto['descricao'])
            if not exists_prod:
                id_categoria = Categoria.objects.get(descricao=produto['categoria']).id
                id_und_medida = UnidMedida.objects.get(descricao=produto['und_medida']).id
                Produto.objects.create(
                    descricao = 'DESCRIÇÃO DA VENDA',
                    desc_nf = produto['descricao'],
                    valorpago = produto['valorpago'],
                    valorvenda = produto['valorvenda'],
                    # estoque = 0,
                    categoria_id = id_categoria,
                    und_medida_id = id_und_medida,
                )
        print('Produtos cadastrados..')
        print('Importação finalizada.')
    except Exception as e:
        print(e)
        raise Exception(e)