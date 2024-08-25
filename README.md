Código postado tem a finalidade de atender os requisitos solicitados Desvendando o Código Secreto da Polkadot;

O código em pyton se inicia solicitando um numero ao usuario (função solicita_numero()) dentro da função verifico se o usuario solicitou um numero valido se não for valido repito a solicitação. O segundo momento
solicito o segundo numero ao usuario utilizando a mesma função solicita_numero() fazendo a mesma validação do número;
Na sequencia a função "intervalo_valido" é chamada nela garanto que o primeiro numero seja menor ou igual ao segundo numero informado pelo usuario;
Se intervalo informado pelo usuario atende o esperado chamo a função percorrer_numeros, nessa função percorro atraves de um for do primeiro numero informado ate
o segundo numero informado pelo usuario. A cada numero dentro do for verifico se ele é multiplo de 
3 e 5 simultaneamente quando isso ocorre ignoro, quando o numero é multiplo de 3 eu somo ao total,
quando é multiplo de 5 subtraio do total, ao final a funcao percorrer_numeros me retorna um numero que é resultado final;
Ao final eu informo o codigo Secreto da Polkadot que foi calculado se caso aparecer a mensagem 
"O Código Secreto da Polkadot não foi possível ser encontrado" é porque o intervalo digitado pelo usuario
foi invalido.
