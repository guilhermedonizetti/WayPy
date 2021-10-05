from setuptools import setup, version

setup(
    name = 'RoutePy',
    version = '0.1.0',
    author = 'Guilherme Donizetti and Luiz Fernando Rodrigues',
    author_email = 'guilhermetecnologias@gmail.com',
    packages = ['routepy'],
    description = 'Um pacote para gerar gráficos simples.',
    long_description = 'O pacote apenas transforma duas listas de valores em um gráfico.'
                     + 'from grafico.main import Grafico '
                     + 'gf = Grafico() '
                     + 'gf.generate_chart(datas_x, datas_y, type_chart, view, label_x, label_y, title) '
                     + ' '
                     + 'datas_x = é uma lista de valores para o eixo X.'
                     + 'datas_y = é uma lista de valores para o eixo Y.'
                     + 'type_chart = Opcional. Se refere ao tipo de gráfico que pode ser bar, plotou scatter. Por padrão é plot.'
                     + 'view = Opcional. Se for True o gráfico vai abrir assimque executar, se for falso ele apenas salva a imagem. Por padrão é True.'
                     + 'label_x = Opcional. Texto a ser exibido no eixo X.'
                     + 'datas_y = Opcional. Texto a ser exibido no eixo Y.'
                     + 'title = Opcional. Título do gráfico.',
    url = 'https://github.com/guilhermedonizetti/Grafico',
    project_urls = {
        'Código fonte': 'https://github.com/guilhermedonizetti/Grafico'
    },
    license = 'MIT',
    keywords = 'gerar gráfico',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent'
    ]
)