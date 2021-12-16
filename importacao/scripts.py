from utils import carregar_json
from django.conf import settings
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from tabelasbasicas.models import Categoria, UnidMedida, TipoPagamento
from produtos.models import Produto
from vendas.models import Venda, ItemDaVenda, NegociacaoParcela, ParcelaVenda
from compras.models import ParcelaCompra, ItemCompra, Compra


def clear_tables():
    # vendas
    NegociacaoParcela.objects.all().delete()
    ParcelaVenda.objects.all().delete()
    ItemDaVenda.objects.all().delete()
    Venda.objects.all().delete()

    # compras
    ParcelaCompra.objects.all().delete()
    ItemCompra.objects.all().delete()
    Compra.objects.all().delete()

    # tabelas básicas e de cadastro
    Cliente.objects.all().delete()
    Fornecedor.objects.all().delete()
    Produto.objects.all().delete()
    Categoria.objects.all().delete()
    UnidMedida.objects.all().delete()
    TipoPagamento.objects.all().delete()


def importar_all():
    importar_tabelasbasicas()
    importar_produtos()
    importar_pessoas()


def importar_tabelasbasicas():
    # tabelas básicas (categorias, unidades de medidas, tipos de pagamento)
    try:
        unidmedidas = carregar_json(settings.BASE_DIR / 'importacao/json/unidmedida.json')
        for unidade in unidmedidas:
            exists_unid = UnidMedida.objects.filter(descricao=unidade['descricao'])
            if not exists_unid:
                UnidMedida.objects.create(
                    sigla=unidade['sigla'],
                    descricao=unidade['descricao'],
                )
        print('Unidade de medidas cadastradas..')
    except Exception as e:
        raise Exception(e)

    try:
        tipospagamento = carregar_json(settings.BASE_DIR / 'importacao/json/tipopagamento.json')
        for pagamento in tipospagamento:
            exists_pagamento = TipoPagamento.objects.filter(descricao=pagamento['descricao'])
            if not exists_pagamento:
                TipoPagamento.objects.create(
                    sigla=pagamento['sigla'],
                    descricao=pagamento['descricao'],
                )
        print('Tipos de pagamento cadastrados..')
    except Exception as e:
        raise Exception(e)

    try:
        categorias = carregar_json(settings.BASE_DIR / 'importacao/json/categoria.json')
        for categoria in categorias:
            exists_categ = Categoria.objects.filter(descricao=categoria['descricao'])
            if not exists_categ:
                Categoria.objects.create(
                    sigla=categoria['sigla'],
                    descricao=categoria['descricao'],
                )
        print('Categorias cadastradas..')
    except Exception as e:
        raise Exception(e)


def importar_produtos():
    # produtosfrom importacao.scripts import importar_all
    try:
        produtos = carregar_json(settings.BASE_DIR / 'importacao/json/produtos.json')
        for produto in produtos:
            exists_prod = Produto.objects.filter(descricao=produto['descricao'])
            if not exists_prod:
                id_categoria = Categoria.objects.get(descricao=produto['categoria']).id
                id_und_medida = UnidMedida.objects.get(descricao=produto['und_medida']).id
                Produto.objects.create(
                    descricao = str(produto['descricao']).upper(),
                    valorpago = produto['valorpago'],
                    valorvenda = produto['valorvenda'],
                    # estoque = 0,
                    categoria_id = id_categoria,
                    und_medida_id = id_und_medida,
                )
        print('Produtos cadastrados..')
    except Exception as e:
        raise Exception(e)


def importar_pessoas():
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
    except Exception as e:
        print(e)
        raise Exception(e)

    try:
        fornecedores = carregar_json(settings.BASE_DIR / 'importacao/json/fornecedores.json')
        for fornecedor in fornecedores:
            exists_fornec = Fornecedor.objects.filter(nome=fornecedor['nome']).exists()
            if not exists_fornec:
                razaosocial = str(fornecedor['rsocial']).replace('.', '').replace('/', '').replace('-', '')
                Fornecedor.objects.create(
                    nome = fornecedor['nome'],
                    rsocial = razaosocial,
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
    except Exception as e:
        print(e)
        raise Exception(e)