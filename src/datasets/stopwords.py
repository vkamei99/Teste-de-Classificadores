stop_words = ['a', 'adeus', 'agora', 'ai', 'ainda', 'alem', 'algo', 'alguem',
              'algum', 'alguma', 'algumas', 'alguns', 'ali', 'ampla', 'amplas', 'amplo', 'amplos', 'ano',
              'anos', 'ante', 'antes', 'ao', 'aos', 'apenas', 'apoio', 'apos', 'aquela', 'aquelas',
              'aquele', 'aqueles', 'aqui', 'aquilo', 'area', 'as', 'as', 'assim', 'ate', 'atras',
              'atraves', 'b', 'baixo', 'bastante', 'bem', 'boa', 'boas', 'bom', 'bons', 'breve', 'c', 'ca', 'cada',
              'catorze', 'cedo', 'cento', 'certamente', 'certeza', 'cima', 'cinco', 'coisa', 'coisas',
              'com', 'como', 'conselho', 'contra', 'contudo', 'custa', 'd', 'da', 'da', 'dao', 'daquela',
              'daquelas', 'daquele', 'daqueles', 'dar', 'das', 'de', 'debaixo', 'dela', 'delas', 'dele',
              'deles', 'demais', 'dentro', 'depois', 'desde', 'dessa', 'dessas', 'desse', 'desses',
              'desta', 'destas', 'deste', 'destes', 'deve', 'devem', 'devendo', 'dever', 'devera',
              'deverao', 'deveria', 'deveriam', 'devia', 'deviam', 'dez', 'dezanove', 'dezasseis',
              'dezassete', 'dezoito', 'dia', 'diante', 'disse', 'disso', 'disto', 'dito', 'diz', 'dizem',
              'dizer', 'do', 'dois', 'dos', 'doze', 'duas', 'duvida', 'e', 'ela', 'elas', 'ele',
              'eles', 'em', 'embora', 'enquanto', 'entre', 'era', 'eram', 'eramos', 'es', 'essa', 'essas',
              'esse', 'esses', 'esta', 'esta', 'estamos', 'estao', 'estar', 'estas', 'estas', 'estava',
              'estavam', 'estavamos', 'este', 'esteja', 'estejam', 'estejamos', 'estes', 'esteve',
              'estive', 'estivemos', 'estiver', 'estivera', 'estiveram', 'estiveramos', 'estiverem',
              'estivermos', 'estivesse', 'estivessem', 'estivessemos', 'estiveste', 'estivestes', 'estou',
              'etc', 'eu', 'exemplo', 'f', 'faco', 'falta', 'favor', 'faz', 'fazeis', 'fazem', 'fazemos',
              'fazendo', 'fazer', 'fazes', 'feita', 'feitas', 'feito', 'feitos', 'fez', 'fim', 'final',
              'foi', 'fomos', 'for', 'fora', 'foram', 'foramos', 'forem', 'forma', 'formos', 'fosse',
              'fossem', 'fossemos', 'foste', 'fostes', 'fui', 'g', 'geral', 'grande', 'grandes', 'grupo', 'h',
              'ha', 'haja', 'hajam', 'hajamos', 'hao', 'havemos', 'havia', 'hei', 'hoje', 'hora', 'horas',
              'houve', 'houvemos', 'houver', 'houvera', 'houvera', 'houveram', 'houveramos', 'houverao',
              'houverei', 'houverem', 'houveremos', 'houveria', 'houveriam', 'houveriamos', 'houvermos',
              'houvesse', 'houvessem', 'houvessemos', 'i', 'isso', 'isto', 'j', 'ja', 'l', 'la', 'la', 'lado',
              'lhe', 'lhes', 'lo', 'local', 'logo', 'longe', 'lugar', 'm', 'maior', 'maioria', 'mais', 'mal', 'mas',
              'maximo', 'me', 'meio', 'menor', 'menos', 'mes', 'meses', 'mesma', 'mesmas', 'mesmo',
              'mesmos', 'meu', 'meus', 'mil', 'minha', 'minhas', 'momento', 'muita', 'muitas', 'muito',
              'muitos', 'n', 'na', 'nada', 'nao', 'naquela', 'naquelas', 'naquele', 'naqueles', 'nas', 'nem',
              'nenhum', 'nenhuma', 'nessa', 'nessas', 'nesse', 'nesses', 'nesta', 'nestas', 'neste',
              'nestes', 'ninguem', 'nivel', 'no', 'noite', 'nome', 'nos', 'nos', 'nossa', 'nossas',
              'nosso', 'nossos', 'nova', 'novas', 'nove', 'novo', 'novos', 'num', 'numa', 'numero',
              'nunca', 'o', 'obra', 'obrigada', 'obrigado', 'oitava', 'oitavo', 'oito', 'onde', 'ontem',
              'onze', 'os', 'ou', 'outra', 'outras', 'outro', 'outros', 'p', 'para', 'parece', 'parte',
              'partir', 'paucas', 'pela', 'pelas', 'pelo', 'pelos', 'pequena', 'pequenas', 'pequeno',
              'pequenos', 'per', 'perante', 'perto', 'pode', 'pude', 'pode', 'podem', 'podendo', 'poder',
              'poderia', 'poderiam', 'podia', 'podiam', 'poe', 'poem', 'pois', 'ponto', 'pontos', 'por',
              'porem', 'porque', 'porque', 'posicao', 'possivel', 'possivelmente', 'posso', 'pouca',
              'poucas', 'pouco', 'poucos', 'primeira', 'primeiras', 'primeiro', 'primeiros', 'propria',
              'proprias', 'proprio', 'proprios', 'proxima', 'proximas', 'proximo', 'proximos', 'pude',
              'puderam', 'q', 'quais', 'quais', 'qual', 'quando', 'quanto', 'quantos', 'quarta', 'quarto',
              'quatro', 'que', 'que', 'quem', 'quer', 'quereis', 'querem', 'queremas', 'queres', 'quero',
              'questao', 'quinta', 'quinto', 'quinze', 'r', 'relacao', 's', 'sabe', 'sabem', 'sao', 'se', 'segunda',
              'segundo', 'sei', 'seis', 'seja', 'sejam', 'sejamos', 'sem', 'sempre', 'sendo', 'ser',
              'sera', 'serao', 'serei', 'seremos', 'seria', 'seriam', 'seriamos', 'sete', 'setima',
              'setimo', 'seu', 'seus', 'sexta', 'sexto', 'si', 'sido', 'sim', 'sistema', 'so', 'sob',
              'sobre', 'sois', 'somos', 'sou', 'sua', 'suas', 't', 'tal', 'talvez', 'tambem', 'tampouco',
              'tanta', 'tantas', 'tanto', 'tao', 'tarde', 'te', 'tem', 'tem', 'tem', 'temos', 'tendes',
              'tendo', 'tenha', 'tenham', 'tenhamos', 'tenho', 'tens', 'ter', 'tera', 'terao', 'terceira',
              'terceiro', 'terei', 'teremos', 'teria', 'teriam', 'teriamos', 'teu', 'teus', 'teve', 'ti',
              'tido', 'tinha', 'tinham', 'tinhamos', 'tive', 'tivemos', 'tiver', 'tivera', 'tiveram',
              'tiveramos', 'tiverem', 'tivermos', 'tivesse', 'tivessem', 'tivessemos', 'tiveste',
              'tivestes', 'toda', 'todas', 'todavia', 'todo', 'todos', 'trabalho', 'tres', 'treze', 'tu',
              'tua', 'tuas', 'tudo', 'ultima', 'ultimas', 'ultimo', 'ultimos', 'um', 'uma', 'umas',
              'u', 'uns', 'vai', 'vais', 'vao', 'varios', 'v', 'vem', 'vem', 'vendo', 'vens', 'ver', 'vez',
              'vezes', 'viagem', 'vindo', 'vinte', 'vir', 'voce', 'voces', 'vos', 'vos', 'vossa', 'vossas',
              'vosso', 'vossos', 'z', 'zero', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']
